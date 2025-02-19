# This example requires the 'message_content' privileged intent to function.

import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

        if message.content.startswith("!howareyou?"):
            await message.reply("Pretty Good!", mention_author=True)

        if message.content.startswith("!goodbye"):
            await message.reply("Goodbye!", mention_author=True)

    async def on_message(self, message):
        if message.content.startswith('!deleteme'):
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()

            # this also works
            await message.channel.send('Goodbye in 3 seconds...', delete_after=3.0)

    async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)
    async def on_message(self, message):
        if message.content.startswith('!editme'):
            msg = await message.channel.send("Arros")
            await asyncio.sleep(3.0)
            await msg.edit(content='Arroz')

    async def on_message_edit(self, before, after):
        msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
        await before.channel.send(msg)   

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("Token va aqui")
