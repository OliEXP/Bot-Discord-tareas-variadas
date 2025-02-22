# This example requires the 'message_content' privileged intent to function.

import discord
import random
import asyncio

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "CARA"
    else:
        return "CRUZ"
    
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
    async def on_message(self, message):
        if message.author == self.user.id:
            return  # Evita que el bot responda a sus propios mensajes

        if message.content.startswith("!password"):
            password = gen_pass(10)  # Genera una contraseña de 10 caracteres
            await message.channel.send(f"Tu contraseña aleatoria es: {password}")

    async def on_message(self, message):
        if message.author == self.user.id:
            return  # Evita que el bot responda a sus propios mensajes

        if message.content.startswith("!coin"):  # Genera una contraseña de 10 caracteres
            await message.channel.send(f"El resultado es: {flip_coin()}")   

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('PON EL TOKEN DE TU BOT AQUÍ')
