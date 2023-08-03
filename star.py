import discord
from discord.ext import commands
import sqlite3

intents = discord.Intents.all()
intents.members = True  # enable the Members intent
intents.message_content = True  # v2

TOKEN = 'bot_token'
PREFIX = '$'

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

conn = sqlite3.connect('starboard_counter.db')
db = conn.cursor()

# Create the table if it doesn't exist
db.execute("CREATE TABLE IF NOT EXISTS messages(message_id INTEGER PRIMARY KEY, star_count INTEGER)")

@bot.event
async def on_ready():
    print('Bot is online')


@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == '⭐':
        message_id = payload.message_id
        db.execute("SELECT star_count FROM messages WHERE message_id = ?", (message_id,))
        result = db.fetchone()
        if result is not None:
            star_count = result[0] + 1
            db.execute("UPDATE messages SET star_count = ? WHERE message_id = ?", (star_count, message_id))
        else:
            star_count = 1
            db.execute("INSERT INTO messages (message_id, star_count) VALUES (?, ?)", (message_id, star_count))

        conn.commit()

        channel = await bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(message_id)
        starboard_channel = discord.utils.get(channel.guild.channels, name='starboard')
        if starboard_channel is None:
            overwrites = {
                channel.guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=False),
                bot.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }
            starboard_channel = await channel.guild.create_text_channel(name='starboard', overwrites=overwrites)

        if star_count == 2:
            embed = discord.Embed(color=discord.Color.random())
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
            if len(message.content) > 0:
                embed.description = message.content
            for attachment in message.attachments:
                if attachment.content_type.startswith('image'):
                    embed.set_image(url=attachment.url)
                else:
                    embed.add_field(name='Attachment', value=f'[Download]({attachment.url})')
            embed.add_field(name='Source', value=f'[Jump!]({message.jump_url})\n{message.created_at.date()} {message.created_at.time()}')
            embed.set_footer(text=f'Message ID: {message_id} • ⭐{star_count}')
            await starboard_channel.send(embed=embed)
        else:
            async for starboard_message in starboard_channel.history():
                if starboard_message.embeds and str(starboard_message.embeds[0].footer.text).startswith(f'Message ID: {message_id}'):
                    starboard_embed = starboard_message.embeds[0]
                    starboard_embed.set_footer(text=f'Message ID: {message_id} • ⭐{star_count}')
                    await starboard_message.edit(embed=starboard_embed)

@bot.event
async def on_raw_reaction_remove(payload):
    if str(payload.emoji) == '⭐':
        message_id = payload.message_id
        db.execute("SELECT star_count FROM messages WHERE message_id = ?", (message_id,))
        result = db.fetchone()
        if result is not None:
            star_count = result[0] - 1
            if star_count <= 0:
                # If star_count becomes 0 or negative, delete the row from the database
                db.execute("DELETE FROM messages WHERE message_id = ?", (message_id,))
            else:
                db.execute("UPDATE messages SET star_count = ? WHERE message_id = ?", (star_count, message_id))
            conn.commit()

            channel = await bot.fetch_channel(payload.channel_id)
            starboard_channel = discord.utils.get(channel.guild.channels, name='starboard')
            async for starboard_message in starboard_channel.history():
                if starboard_message.embeds and str(starboard_message.embeds[0].footer.text).startswith(f'Message ID: {message_id}'):
                    if star_count < 2:
                        await starboard_message.delete()
                    else:
                        starboard_embed = starboard_message.embeds[0]
                        starboard_embed.set_footer(text=f'Message ID: {message_id} • ⭐{star_count}')
                        await starboard_message.edit(embed=starboard_embed)

bot.run(TOKEN)
