import os, json, discord, ctypes, subprocess, datetime, asyncio
from discord.ext import commands

with open('settings.json') as f:
    config = json.load(f)

userid = config.get('discord-id')
token = config.get('bot-token')
prefix = config.get('bot-prefix')
thumbnail = 'https://cdn.discordapp.com/icons/822519367866253373/8b2422ccb9b5ee7abce83f026ae22c5b.webp'

intents = discord.Intents().all()
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")


def banner():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Made by LiteEagle262 | liteeagle.me")
    print(f"""
            ██████╗  ██████╗ ████████╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
            ██╔══██╗██╔═══██╗╚══██╔══╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
            ██████╔╝██║   ██║   ██║       ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
            ██╔══██╗██║   ██║   ██║       ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
            ██████╔╝╚██████╔╝   ██║       ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
            ╚═════╝  ╚═════╝    ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

                         https://github.com/LiteEagle262/Viridian-Trade-Bot-Manager

                Viridian Trade Bot Manager | Logged in as: {client.user.name}#{client.user.discriminator}
                                    ID: {client.user.id} | Prefix: {prefix}
        """)

def open_file():
    os.startfile("Cry.ConsoleApp.exe")
    if os.path.exists("players.txt") == True:
        os.remove("players.txt")

@client.event
async def on_connect():
    banner()
    open_file()


def close_file():
    os.system('TASKKILL /F /IM Cry.ConsoleApp.exe')


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    pn_lower = process_name.lower()
    return last_line.lower().startswith(pn_lower)


@client.command()
async def help(ctx):
    if ctx.message.author.id == int(userid):
        e = discord.Embed(title=f'**Bot Commands:**', color=0xff0000)
        e.add_field(name=f"{prefix}check", value="Checks if the bot is running", inline=True)
        e.add_field(name=f"{prefix}open", value="Opens the Trade Bot", inline=True)
        e.add_field(name=f"{prefix}stop", value="Stops The Trade Bot", inline=True)
        e.add_field(name=f"{prefix}restart", value="Restarts the Trade bot", inline=True)
        e.add_field(name=f"{prefix}config <attachedfile>", value="Replaces the current config with the config attached", inline=True)
        e.add_field(name=f"{prefix}proxy <attachedfile>", value="Replaces the current proxies with the proxies attached", inline=True)
        e.set_thumbnail(url=thumbnail)
        e.timestamp = datetime.datetime.utcnow()
        e.set_footer(text='Trade Bot Manager')
        await ctx.send(embed=e)

@client.command()
async def check(ctx):
    if ctx.message.author.id == int(userid):
        if process_exists("Cry.ConsoleApp.exe") == True:
            e = discord.Embed(title=f'**Running**', description=f"The Trade bot is currently running", color=0xff0000)
            e.set_thumbnail(url=thumbnail)
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text='Trade Bot Manager')
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title=f'**Not Running**', description=f"The trade bot is not running you may want to restart it", color=0xff0000)
            e.set_thumbnail(url=thumbnail)
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text='Trade Bot Manager')
            await ctx.send(embed=e)

@client.command()
async def stop(ctx):
    if ctx.message.author.id == int(userid):
        if process_exists("Cry.ConsoleApp.exe") == True:
            close_file()
            e = discord.Embed(title=f'**Success**', description=f"Successfully Stopped Viridian Trade Bot, to open it again do, `{prefix}open`", color=0xff0000)
            e.set_thumbnail(url=thumbnail)
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text='Trade Bot Manager')
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title=f'**Failed**', description=f"The bot isnt even running.", color=0xff0000)
            e.set_thumbnail(url=thumbnail)
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text='Trade Bot Manager')
            await ctx.send(embed=e)


@client.command()
async def open(ctx):
    if ctx.message.author.id == int(userid):
        if process_exists("Cry.ConsoleApp.exe") == False:
            open_file()
            e = discord.Embed(title=f'**Success**', description=f"Successfully Opened Viridian Trade Bot, to stop it do, `{prefix}stop`", color=0xff0000)
            e.set_thumbnail(url=thumbnail)
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text='Trade Bot Manager')
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title=f'**Failed**', description=f"The bot is already running!", color=0xff0000)
            e.set_thumbnail(url=thumbnail)
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text='Trade Bot Manager')
            await ctx.send(embed=e)


@client.command()
async def restart(ctx):
    if ctx.message.author.id == int(userid):
        close_file()
        await asyncio.sleep(2)
        open_file()
        e = discord.Embed(title=f'**Success**', description=f"Successfully Restarted The Bot", color=0xff0000)
        e.set_thumbnail(url=thumbnail)
        e.timestamp = datetime.datetime.utcnow()
        e.set_footer(text='Trade Bot Manager')
        await ctx.send(embed=e)


@client.command()
async def config(ctx):
    if ctx.message.author.id == int(userid):
        if str(ctx.message.attachments) == "[]":
            return
        else:
            split_v1 = str(ctx.message.attachments).split("filename='")[1]
            filename = str(split_v1).split("' ")[0]
            if filename == "appsettings.json":
                if os.path.exists("appsettings.json") == True:
                    os.remove("appsettings.json")
                await asyncio.sleep(2)
                await ctx.message.attachments[0].save(fp="{}".format(filename))
                e = discord.Embed(title=f'**Success**', description=f"Successfully Uploaded the config to the bot. (bot restart may be required)", color=0xff0000)
                e.set_thumbnail(url=thumbnail)
                e.timestamp = datetime.datetime.utcnow()
                e.set_footer(text='Trade Bot Manager')
                await ctx.send(embed=e)
@client.command()
async def proxy(ctx):
    if ctx.message.author.id == int(userid):
        if str(ctx.message.attachments) == "[]":
            return
        else:
            split_v1 = str(ctx.message.attachments).split("filename='")[1]
            filename = str(split_v1).split("' ")[0]
            if filename == "proxies.txt":
                if os.path.exists("proxies.txt") == True:
                    os.remove("proxies.txt")
                await asyncio.sleep(2)
                await ctx.message.attachments[0].save(fp="{}".format(filename))
                e = discord.Embed(title=f'**Success**', description=f"Successfully Uploaded the proxies to the bot. (bot restart may be required)", color=0xff0000)
                e.set_thumbnail(url=thumbnail)
                e.timestamp = datetime.datetime.utcnow()
                e.set_footer(text='Trade Bot Manager')
                await ctx.send(embed=e)                

client.run(token)
