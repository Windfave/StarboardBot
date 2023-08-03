
# Starboard Bot

This project lets you star react messages and pin them to a special channel when it receives enough said votes (default = 2).

The embed sent into said channel contains the author of the message and the message itself,
along with the reaction counter which is updated constantly (until the bot is turned off)
[That is subject to change]



## Acknowledgements

 - amateur (probably outdated) code



## Features

- Live Starboard System
- More to come in the future

Any message that gets 2 and more star reactions gets sent as an embed into a #starboard channel.
If there is no said channel, the bot will create it. (Do not rename it.)

The embed is constantly being updated (the reaction count) as long as the bot is turned on.
If it is turned off and turned on again it won't have any memory of adding said message into the channel, and therefore won't update the reaction count there. It's possible it would add the message again if the message got two more reactions.

If the message goes below 2  reactions, it gets removed from the #starboard.

![example](https://cdn.discordapp.com/attachments/675325021937205268/1076848349732413551/image.png)
## Installation

To be able to use this project you need [**python 3.11.2**.](https://www.python.org/downloads/)
Make sure you add pip to PATH. Restart your computer afterwards.
After this you will need some libraries that you can find in the requirements.txt file.
The most important one is [discord.py](https://discordpy.readthedocs.io/en/stable/)

```bash
  cd theproject
  py -3 -m pip install -U discord.py (if on Windows)
```

You can also get the library directly from PyPI:

```bash
  python3 -m pip install -U discord.py
```

After this is done, you should be ready to set up the bot.
First to make the bot even work, you need to create the Bot Application in Discord.
To do so, [you must go to the Developer Application section.](https://discord.com/developers/applications)

    
## Making the discord bot

When you access the Developer Application section, you want to go to the Applications tab.
That should be open by default. Press New Application.

![Stepone](https://cdn.discordapp.com/attachments/675325021937205268/1076844192103419964/image.png)

Now, you will see this window open. Enter the desired name of your bot and agree to the ToS and Developer Policy.

![Steptwo](https://cdn.discordapp.com/attachments/675325021937205268/1076844544752107540/image.png)

Here, you will now be redirected to your bots settings. Here, you can change the name, profile picture and even add more information about your bot in the description, which will show in the bot's about me section on it's profile. From here you want to open the bot tab.

![Stepthree](https://cdn.discordapp.com/attachments/675325021937205268/1076844915717320834/image.png)

This is what the bot tab will look like. You want to press Add Bot.

![Stepfour](https://cdn.discordapp.com/attachments/675325021937205268/1076845723003404338/image.png)

Now, you have created the bot. Now, copy the token and save it, paste it into the python file.

![Stepfive](https://cdn.discordapp.com/attachments/675325021937205268/1076845962569457684/image.png)

Replace the 'INSERTBOTTOKENHERE' with the token you just added to your clipboard.

![Stepsix](https://cdn.discordapp.com/attachments/675325021937205268/1076846189821046784/image.png)

Now you want to enable all of these intents.

![Stepseven](https://cdn.discordapp.com/attachments/675325021937205268/1076846365012930570/image.png)

After doing so, save the changes in the python file.
You will have to invite the bot to a server, [you can use this tool to generate you an invite link using your bot's application id](https://discordapi.com/permissions.html)

Select the needed permissions and invite the bot.
Now all you need to do is to turn on the bot like so:

```bash
cd thefolderwiththebot
python star.py
```

The bot should turn on and tell you that the bot is online.
