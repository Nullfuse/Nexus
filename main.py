import requests
from io import BytesIO

from PIL import Image

import os
os.system("install-pkg tesseract-ocr")
import pytesseract

import discord

from keep_alive import keep_alive

pytesseract.pytesseract.tesseract_cmd = "tesseract"
os.environ["TESSDATA_PREFIX"] = "/home/runner/.apt/usr/share/tesseract-ocr/4.00/tessdata/"

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if (message.author.bot == False):
    attachment = message.attachments
    if(len(attachment) > 0):
        url = attachment[0]
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(image)
        await message.channel.send(text)

keep_alive()

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client.run(TOKEN)