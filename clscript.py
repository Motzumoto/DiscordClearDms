import discord, asyncio
from colorama import Fore, Back, Style, init
from os import system
import shutil

client = discord.Client()

token = "PUT_TOKEN_IN_THESE_QUOTES"

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns
    cpink = Style.BRIGHT + Fore.RED

    def ui():
        tyler('')

    ui()


@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        width = shutil.get_terminal_size().columns
        cpink = Style.BRIGHT + Fore.MAGENTA

        if commands[0] == 'cl':
			if len(commands) == 1:
				async for msg in channel.history(limit=9999):
					if msg.author == client.user:
						try:
							await msg.delete()
                        except Exception as x:
								pass

        if commands[0] == 'cleardms':
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                print(msg)
                        except:
                             pass
client.run(token, bot=False)
