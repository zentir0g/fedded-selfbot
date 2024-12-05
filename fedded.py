import sys
sys.path.insert(0, 'discord.py-self')
import discord
import threading
import requests
import requests
import asyncio
import json
import re
import datetime
import urllib
import pickle
import os
import instaloader
import aiohttp
import datetime
from dateutil import parser
from discord.ext import commands, tasks
from datetime import datetime, timezone
from datetime import datetime
from datetime import datetime, timedelta

with open('config/config.json') as f:
    config = json.load(f)
    token = config['token']
    prefix = config['prefix']
    BOT_TOKEN = config['token']
    MAIN_TOKEN = config['token']
    ALT_TOKEN = config['token']
    WEBHOOK_URL = config['sniper_webhook']
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')

statuses = []
current_status = 0
afk_users = {}
afk_reason = None
SPECIFIC_USER_ID = 333014456399560705
status_changing = False
spamming = False
vc_join_tasks = {}
spam_task = None
greeting_settings = {}
fonts_folder = "fonts"
fonts = {}
usedcodes = []
auto_react_enabled = True
status_file = "trash/status_lines.txt"
nitro_sniper = True
onalt = False
sound_notification = False
webhooknotification = True
changing_time = 10
status_tag = discord.Status.online

def NitroInfo(elapsed, code):
    print(f"Elapsed Time: {elapsed} seconds\nNitro Code: {code}")

def mainHeader():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US',
        'Content-Type': 'application/json',
        'authorization': token,
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'Content-Type': 'application/json',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'America/Chicago',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJwdGIiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4xMDcyIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDQiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjEwNzIgQ2hyb21lLzEyMC4wLjYwOTkuMjkxIEVsZWN0cm9uLzI4LjIuMTAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjI4LjIuMTAiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTM5NTksIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ3Njk3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9'
    }
    return headers

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
@bot.event
async def on_message(message):
    # Only add reactions if the auto_react_enabled variable is True
    if message.author == bot.user and auto_react_enabled:
        reactions = {
            'hii': '👋',
            'happy': '😄',
            'sad': '😢',
            'fix': '🛠️',
            'bruh': '🗿',
            'oof': '🙃',
            'listen': '👂',
            'nvm': '☝️',
            'sahi': '👌',
            'hmm': '🤔',
            'let me check': '✔️',
            'welcome': '🙏',
            'wlc': '🙏',
            'fool': '🤪',
            'nice' : '✨',
            'cool' : '😎',
            'great' : '✨',
            'wait' : '⌛',
            'wtf' : '🖕',
            'ik' : '️☝️',
            'i know' : '☝️',
            'win it' : '🎉',
            'fuck off' : '🖕',
            'nice': '✨',
            'good': '👍',
            'great': '👌',
            'awesome': '🤩',
            'amazing': '👏',
            'excellent': '👌',
            'fantastic': '🌟',
            'superb': '👌',
            'wonderful': '👏',
            'brilliant': '👍',
            'impressive': '👏',
            'outstanding': '🌟',
            'phenomenal': '👌',
            'splendid': '🌟',
            'terrific': '👍',
            'top-notch': '👏',
            'stellar': '⭐',
            'flawless': '👌',
            'exceptional': '🌟',
            'remarkable': '👏',
            'super': '👍',
            'first-rate': '👌',
            'incredible': '👏',
            'marvelous': '🌟',
            'perfect': '💯',
            'no': '❌',
            'nah': '❌',
            'not': '❌',
            'never': '❌',
            'negative': '❌',
            'don\'t': '❌',
            'do not': '❌',
            'cannot': '❌',
            'can\'t': '❌',
            'won\'t': '❌',
            'refuse': '❌',
            'decline': '❌',
            'reject': '❌',
            'denied': '❌',
            'negative': '❌',
            'thanks': '🙏',
            'thank you': '🙏',
            'thx': '🙏',
            'ty': '🙏',
            'appreciate': '🙏',
            'grateful': '🙏',
            'thankful': '🙏',
            'cheers': '🙏',
            'much obliged': '🙏',
            'many thanks': '🙏',
            'thanks a lot': '🙏',
            'thank you very much': '🙏',
            'thank you so much': '🙏',
            'welcome': '🙏',
            'wlc': '🙏',
            'welc': '🙏',
            'hi': '👋',
            'hello': '👋',
            'hey': '👋',
            'greetings': '👋',
            'salutations': '👋',
            'howdy': '👋',
            'hola': '👋',
            'bonjour': '👋',
            'ciao': '👋',
            'namaste': '👋',
            'welcome back': '👋',
            'good to see you': '👋',
            'ok': '👌',
            'yes': '✅',
            'yeah': '👍',
            'yep': '👍',
            'yup': '👍',
            'sure': '👍',
            'absolutely': '👍',
            'definitely': '👍',
            'certainly': '👍',
            'agreed': '👍',
            'nice': '👌',
            'fine': '👌',
            'cool': '😎',
            'love it': '❤️',
            'thumbs up': '👍',
            'clap': '👏',
            'congrats': '🎉',
            'celebrate': '🎉',
            'cheers': '🥂',
            'high five': '🖐️',
            'bye': '👋',
            'goodbye': '👋',
            'farewell': '👋',
            'see you': '👋',
            'see ya': '👋',
            'see you later': '👋',
            'see you soon': '👋',
            'catch you later': '👋',
            'talk to you later': '👋',
            'till next time': '👋',
            'until we meet again': '👋',
            'take care': '👋',
            'have a good one': '👋',
            'have a great day': '👋',
            'have a nice day': '👋',
            'have a wonderful day': '👋',
            'have a fantastic day': '👋',
            'have a lovely day': '👋',
            'have a pleasant day': '👋',
            'goodnight': '🌙',
            'sweet dreams': '🌙💤',
            'adios': '👋',
            'cheerio': '👋',
            'take it easy': '👋',
            'peace out': '✌️',
            'later': '👋',
            'ttyl': '👋',
            'talk to you soon': '👋',
            'until later': '👋',
            'until next time': '👋',
            'so long': '👋',
            'fare thee well': '👋',
            'be well': '👋',
            'lol': '🤣',
            'lmao': '🤣',
            'lmfao': '🤣',
            'haha': '😄',
            'hehe': '🤭',
            'rofl': '🤣',
            'hahaha': '😄',
            'lolol': '🤣',
            'lolz': '🤣',
            'lmfao': '🤣',
            'lmfaoo': '🤣',
            'bahaha': '😄',
            'bwahaha': '😄',
            'hahah': '😄',
            'hahahaha': '😄',
            'hahahah': '😄',
            'hehehe': '🤭',
            'hehehehe': '🤭',
            'roflmao': '🤣',
            'roflmaoo': '🤣',
            'rotfl': '🤣',
            'teehee': '😄',
            'ha': '😄',
            'haha': '😄',
            'hah': '😄',
            'heheh': '🤭',
            'heheheh': '🤭',
            'ahah': '😄',
            'ahahaha': '😄',
            'ahaha': '😄',
            'ahahah': '😄',
            'ahahaha': '😄',
            'maybe': '🤷',
            'perhaps': '🤷',
            'possibly': '🤷',
            'uncertain': '🤷',
            'undecided': '🤷',
            'unsure': '🤷',
            'dunno': '🤷',
            'not sure': '🤷',
            'no idea': '🤷',
            'no clue': '🤷',
            'i don\'t know': '🤷',
            'idk': '🤷',
            'i have no idea': '🤷',
            'i\'m unsure': '🤷',
            'who knows': '🤷',
            'beats me': '🤷',
            'can\'t say': '🤷',
            'hard to say': '🤷',
            'it\'s up in the air': '🤷',
            'i\'m not certain': '🤷',
            'i\'m not sure': '🤷',
            'i\'m undecided': '🤷',
            'i\'m not convinced': '🤷',
            'i\'m on the fence': '🤷',
            'how are you': '👋',
            'how\'s it going': '🤔',
            'hru': '🤷',
            'how are u': '👋',
            'how are ya': '🤷',
            'how\'s life': '🌟',
            'how have you been': '🤔',
            'what\'s up': '👋',
            'what\'s new': '🌟',
            'how\'s everything': '🌟',
            'how do you do': '👋',
            'are you okay': '🤷',
            'r u ok': '🤷',
            'how\'s your day': '🌞',
            'how\'s your day going': '🌞',
            'how\'s your day been': '🌞',
            'how\'s your day so far': '🌞',
            'how\'s your week': '📆',
            'how\'s your weekend': '🌴',
            'how are things': '🤷',
            'how\'s your health': '🌡️',
            'how\'s your mood': '😊',
            'how\'s your spirit': '✨',
            'nvm': '🙅',
            'never mind': '🙅',
            'forget it': '🙅',
            'ignore': '🙈',
            'disregard': '🙉',
            'skip': '⏭️',
            'pass': '⏭️',
            'not important': '🤷',
            'not relevant': '🤷‍',
            'not interested': '🤷‍',
            'don\'t care': '🤷‍',
            'let it go': '🧘',
            'nothing': '😐',
            'nope': '🙅‍',
            'ignore me': '🙈',
            'disregard me': '🙉',
            'not important to me': '🤷‍',
            'not relevant to me': '🤷‍',
            'I don\'t care': '🤷',
            'let me go': '🧘',
            'don\'t bother': '🙅',
            'bruh': '🗿',
            'oof': '🙃',
            'yikes': '😬',
            'facepalm': '🤦',
            'disappointed': '😞',
            'disaster': '💥',
            'fail': '👎',
            'epic fail': '🤦',
            'disaster': '😱',
            'tragic': '😢',
            'awful': '😖',
            'terrible': '😫',
            'horrible': '😣',
            'cringe': '🤢',
            'oh no': '😱',
            'disappointing': '😕',
            'regrettable': '😔',
            'shocking': '😳',
            'unexpected': '😮',
            'unbelievable': '🤯',
            'chaos': '🌪️',
            'nightmare': '🌙',
            'mess': '🧹',
            'botch': '🤪',
            'sloppy': '🤷',
            'disorganized': '🌀',
            'unprofessional': '🤦',
            
        }

        for word, emoji in reactions.items():
            if message.content.lower() == word:
                await message.add_reaction(emoji)

        if message.content.endswith('?'):
            await message.add_reaction('❓') 

    if not message.author.bot:
        if isinstance(message.channel, discord.DMChannel):
            if afk_reason is not None:
                reply_message = f"Sorry, I am currently AFK with the reason: {afk_reason}."
                await message.author.send(reply_message)
        else:
            if bot.user in message.mentions:
                if afk_reason is not None:
                    reply_message = f"Sorry, **{message.author.name}**, I am currently AFK with the reason: {afk_reason}."
                    await message.channel.send(reply_message)

    if (
        "discord.gift/" in message.content
        or "discord.com/gifts/" in message.content
        or "discordapp.com/gifts/" in message.content
    ):
        if nitro_sniper:
            start = datetime.now()
            if "discord.gift/" in message.content:
                code = re.findall(r"discord[.]gift/(\w+)", message.content)
            if "discordapp.com/gifts/" in message.content:
                code = re.findall(r"discordapp[.]com/gifts/(\w+)", message.content)
            if "discord.com/gifts/" in message.content:
                code = re.findall(r"discord[.]com/gifts/(\w+)", message.content)
            for code in code:
                if len(code) == 16 or len(code) == 24:
                    if code not in usedcodes:
                        usedcodes.append(code)
                        headers = {"Authorization": ALT_TOKEN if onalt else MAIN_TOKEN}
                        r = requests.post(
                            f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem",
                            headers=headers,
                        ).text
                        elapsed = datetime.now() - start
                        elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
                        time = datetime.now().strftime("%H:%M")
                        if "This gift has been redeemed already." in r:
                            print(f"\n{time} - Nitro is Already Redeemed")
                            NitroInfo(elapsed, code)
                        elif "subscription_plan" in r:
                            print(f"\n{time} - Nitro Successfully Claimed!")
                            NitroInfo(elapsed, code)
                            if webhooknotification:
                                message_content = (
                                    "# ??__Fedded Selfbot__??\n"
                                    "`??` **Congrats!!** your nitro GIFT LINK has been claimed.\n"
                                    "||@everyone|| ||@here||"
                                )
                                data = {
                                    "content": message_content
                                }
                                requests.post(WEBHOOK_URL, json=data)
                        elif "Unknown Gift Code" in r:
                            print(f"\n{time} - Unknown Nitro Gift Code")
                            NitroInfo(elapsed, code)

    await bot.process_commands(message)

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    with open('messages/help.txt', 'r', encoding='utf-8') as file:
        help_message = file.read()
    await ctx.send(help_message)

@bot.command()
async def autoreact(ctx, option: str):
    await ctx.message.delete()
    global auto_react_enabled
    if option.lower() == "on":
        auto_react_enabled = True
        await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Auto-reactions are now enabled.**")
    elif option.lower() == "off":
        auto_react_enabled = False
        await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Auto-reactions are now disabled.**")
    else:
        await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Invalid option. Use +autoreact on or +autoreact off.**")

@bot.command()
async def spam(ctx, amount: int, *, message: str):
    await ctx.message.delete()
    for _ in range(amount):
        await ctx.send(message)

@bot.command()
async def afk(ctx, *, reason):
    await ctx.message.delete()
    global afk_reason
    afk_reason = reason
    message = f"# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **I am now AFK with the reason: {reason}.**"
    await ctx.send(message)

@bot.command()
async def unafk(ctx):
    await ctx.message.delete()
    global afk_reason
    afk_reason = None
    message = "# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **I am no longer AFK.**"
    await ctx.send(message)
    
@bot.command(aliases=['bal', 'ltcbal'])
async def getbal(ctx, ltcaddress):
    await ctx.message.delete()
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8  
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("Failed to retrieve balance. Please check the Litecoin address.")
        return
    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("Failed to retrieve the current price of Litecoin.")
        return
    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price
    message = f"# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **LTC Address: `{ltcaddress}`**\n"
    message += f"`🔏` Current LTC: **${usd_balance:.2f} USD**\n"
    message += f"`🔏` Total LTC Received: **${usd_total_balance:.2f} USD**\n"
    message += f"`🔏` Unconfirmed LTC: **${usd_unconfirmed_balance:.2f} USD**"
    response_message = await ctx.send(message)
    await asyncio.sleep(60)
    await response_message.delete()

@bot.command(aliases=['av', 'ava'])
async def avatar(ctx, user: discord.User = None):
    await ctx.message.delete()
    member = user or ctx.author

    avatar_url = member.display_avatar.url
    await ctx.send(f"# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Here is the [avatar]({avatar_url}) of {member.mention} **")

@bot.command(name='banner')
async def fetch_user_banner(ctx, user: discord.User = None):
    await ctx.message.delete()
    member = user or ctx.author
    uid = member.id
    url = f"https://discord.com/api/v8/users/{uid}"
    headers = mainHeader()

    response = requests.get(url, headers=headers)

    banner = 'https://cdn.discordapp.com/attachments/829722741288337428/834016013678673950/banner_invisible.gif'  # invisible image

    if response.status_code != 404:
        data = response.json()
        receive = data.get('banner', None)

        if receive is not None:
            format = 'png'
            if receive.startswith('a_'):
                format = 'gif'
            
            banner = f"https://cdn.discordapp.com/banners/{uid}/{receive}.{format}?size=1024"  # Adjust the size here

    await ctx.send(f"# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Here is the [banner]({banner}) of {member.mention} **")

@bot.command()
async def clear(ctx, amount: int):
    def is_bot_message(message):
        return message.author == bot.user

    messages = []
    if isinstance(ctx.channel, discord.TextChannel):
        # Collect bot messages up to the specified amount
        async for message in ctx.channel.history(limit=None):
            if is_bot_message(message):
                messages.append(message)
                if len(messages) >= amount:
                    break

        # Delete the messages and handle any errors
        for message in messages:
            try:
                await message.delete()
            except Exception as e:
                print(f"Could not delete message {message.id}: {e}")

    elif isinstance(ctx.channel, discord.DMChannel):
        # Collect bot messages up to the specified amount in a DM
        async for message in ctx.channel.history(limit=None):
            if is_bot_message(message):
                messages.append(message)
                if len(messages) >= amount:
                    break

        # Delete messages one by one (bulk delete isn't available for DMs)
        for message in messages:
            try:
                await message.delete()
            except Exception as e:
                print(f"Could not delete message {message.id}: {e}")


@bot.command()
async def hackclear(ctx):
    await ctx.send("⠀" + "\n"*1998 + "⠀")
    await ctx.message.delete()

@bot.command()
async def vcjoin(ctx, channel_id: int, mute: str, deafen: str, camera: str):
    await ctx.message.delete()

    # Convert input strings to boolean values
    mute = mute.lower() == 'y'
    deafen = deafen.lower() == 'y'
    camera = camera.lower() == 'y'

    # Get the voice channel by ID
    channel = ctx.guild.get_channel(channel_id)

    if channel is None or not isinstance(channel, discord.VoiceChannel):
        await ctx.send('# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Invalid voice channel ID.**')
        return

    # Join the voice channel
    try:
        voice_client = await channel.connect()
        await voice_client.guild.change_voice_state(
            channel=channel,
            self_mute=mute,
            self_deaf=deafen,
            self_video=camera
        )
        await ctx.send(f'# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Joined voice channel `{channel.name}` with mute={mute}, deafen={deafen}, camera={camera}.**')
    except discord.Forbidden:
        await ctx.send('# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **I do not have permission to join this voice channel.**')
    except discord.ClientException:
        await ctx.send('# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Already connected to a voice channel.**')
    except Exception as e:
        await ctx.send(f'# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **An error occurred: {e}**')

@bot.command()
async def stream(ctx, *, text):
    await ctx.message.delete()
    activity = discord.Streaming(name=text, url='https://www.twitch.tv/devilharisyt')
    await bot.change_presence(activity=activity)
    await ctx.send(f'# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Status Updated to streaming**\n`🔏` **Text :** {text}')

@bot.command()
async def vcleave(ctx):
    await ctx.message.delete()
    try:
        voice_client = ctx.voice_client
        if voice_client:
            await voice_client.disconnect()
            await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Successfully disconnected from VC.**")
        else:
            await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **I'm not currently in a VC.**")
    except Exception as e:
        await ctx.send(f"# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **An error occurred: {e}**")

@bot.command()
async def deleteallchannels(ctx):
    await ctx.message.delete()
    channel_ids = []

    TEMP_DIR = "trash"
    TEMP_FILE = os.path.join(TEMP_DIR, "channel_ids.pkl")

    # Create the trash folder if it doesn't exist
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    # Collect channel IDs from the server
    for guild in bot.guilds:
        if guild.id == ctx.guild.id:  # Ensure we're scraping the channels from the current server
            for channel in guild.channels:
                channel_ids.append(channel.id)
    
    # Save channel IDs to the temporary file using pickle
    with open(TEMP_FILE, 'wb') as f:
        pickle.dump(channel_ids, f)

    # Create a thread for each channel and start it
    for channel_id in channel_ids:
        thread = threading.Thread(target=delete_channel, args=(channel_id,))
        thread.start()

    await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **All channels are being deleted.**")

def delete_channel(channel_id):
    url = f"https://canary.discord.com/api/v9/channels/{channel_id}"
    
    headers = {
        "accept": "*/*",
        "accept-language": "en-US",
        "authorization": token,
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-discord-timezone": "America/Chicago",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4zNzMiLCJvc192ZXJzaW9uIjoiMTAuMC4xOTA0NCIsIm9zX2FyY2giOiJ4NjQiLCJhcHBfYXJjaCI6Ing2NCIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjM3MyBDaHJvbWUvMTI0LjAuNjM2Ny4yMDcgRWxlY3Ryb24vMzAuMC42IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIzMC4wLjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozMDA3MDcsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ4NjAyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Closed channel with ID {channel_id}")
    else:
        print(f"Failed to close channel with ID {channel_id}: {response.status_code} {response.text}")
 
@bot.command()
async def deleteallroles(ctx):
    await ctx.message.delete()
    server = ctx.guild

    if server is None:
        await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **The server does not exist.**")
        return

    roles = server.roles

    for role in roles:
        if role.name != "@everyone":  # Skip the @everyone role
            try:
                await role.delete(reason="Deleting all roles")
            except Exception as e:
                print(f"# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Failed to delete role {role.name}: {e}**")

    await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **All roles have been deleted successfully!**")
  
@bot.command()
async def clone_channels(ctx, old_server_id: int, new_server_id: int):
    await ctx.message.delete()
    old_server = bot.get_guild(old_server_id)
    new_server = bot.get_guild(new_server_id)

    if not old_server:
        await ctx.send('# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Old server not found.**')
        return
    if not new_server:
        await ctx.send('# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **New server not found.**')
        return
    category_map = {}

    clone_messages = []  # List to store clone messages

    for old_category in old_server.categories:
        new_category = await new_server.create_category_channel(name=old_category.name, overwrites=old_category.overwrites)
        category_map[old_category.id] = new_category

        for old_text_channel in old_category.text_channels:
            new_text_channel = await new_category.create_text_channel(name=old_text_channel.name, overwrites=old_text_channel.overwrites)
            clone_messages.append(f'Text channel cloned: {old_text_channel.name} -> {new_text_channel.name} in category: {old_category.name} -> {new_category.name}')

        for old_voice_channel in old_category.voice_channels:
            new_voice_channel = await new_category.create_voice_channel(name=old_voice_channel.name, overwrites=old_voice_channel.overwrites)
            clone_messages.append(f'Voice channel cloned: {old_voice_channel.name} -> {new_voice_channel.name} in category: {old_category.name} -> {new_category.name}')

    for old_channel in old_server.channels:
        if isinstance(old_channel, (discord.TextChannel, discord.VoiceChannel)) and old_channel.category is None:
            if isinstance(old_channel, discord.TextChannel):
                new_channel = await new_server.create_text_channel(name=old_channel.name, overwrites=old_channel.overwrites)
                clone_messages.append(f'Text channel cloned: {old_channel.name} (No Category) -> {new_channel.name}')
            elif isinstance(old_channel, discord.VoiceChannel):
                new_channel = await new_server.create_voice_channel(name=old_channel.name, overwrites=old_channel.overwrites)
                clone_messages.append(f'Voice channel cloned: {old_channel.name} (No Category) -> {new_channel.name}')

    # Print all clone messages in console
    for message in clone_messages:
        print(message)

    # Send one final message indicating channels are cloned
    await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Channels cloned successfully!**")

# 5. Clone Roles
@bot.command()
async def clone_roles(ctx, old_server_id: int, new_server_id: int):
    await ctx.message.delete()
    old_server = bot.get_guild(old_server_id)
    new_server = bot.get_guild(new_server_id)

    if old_server is None:
        await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **The old server does not exist.**")
        return

    if new_server is None:
        await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **The new server does not exist.**")
        return

    old_roles = old_server.roles

    role_map = {}

    clone_messages = []  # List to store clone messages

    for role in reversed(old_roles):  # Iterate in reverse order
        new_role = await new_server.create_role(name=role.name, color=role.color, hoist=role.hoist,
                                               mentionable=role.mentionable, permissions=role.permissions,
                                               reason="Cloning roles")
        role_map[role.id] = new_role
        clone_messages.append(f'Role cloned: {role.name} -> {new_role.name}')
        print(f'Role cloned: {role.name} -> {new_role.name}')

    for member in old_server.members:
        member_roles = member.roles
        new_member = new_server.get_member(member.id)
        if new_member is not None:
            for role in reversed(member_roles):  # Iterate in reverse order
                if role.id in role_map:
                    new_role = role_map[role.id]
                    await new_member.add_roles(new_role)

    # Send one final message indicating roles are cloned
    await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Roles have been cloned successfully!**")

    # Print all clone messages in console
    for message in clone_messages:
        print(message)
  
@bot.command(aliases=["pornhubcomment", 'phc'])
async def phcomment(ctx, user: discord.Member = None, *, args=None):
    await ctx.message.delete()
    
    if user is None or args is None:
        await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Missing parameters.**")
        return
    
    encoded_args = urllib.parse.quote(args)
    
    endpoint = f"https://nekobot.xyz/api/imagegen?type=phcomment&text={encoded_args}&username={user.display_name}&image={user.avatar.url}"
    
    r = requests.get(endpoint)
    res = r.json()
    
    await ctx.send(res["message"])  # Directly send the URL

@bot.command()
async def iplookup(ctx, ip):
    await ctx.message.delete()
    api_key = 'a91c8e0d5897462581c0c923ada079e5'  
    api_url = f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}'
    
    response = requests.get(api_url)
    data = response.json()
    
    if 'country_name' in data:
        country = data['country_name']
        city = data['city']
        isp = data['isp']
        current_time_unix = data['time_zone']['current_time_unix']

        current_time_formatted = f"<t:{int(current_time_unix)}:f>"
        
        message = f"# 🎈 __Fedded Selfbot__ 🎈\n"
        message += f"`🔏` **IP Lookup Results for `{ip}`**\n"
        message += f"`🔏` **Country**: {country}\n"
        message += f"`🔏` **City**: {city}\n"
        message += f"`🔏` **ISP**: {isp}\n"
        message += f"`🔏` **Current Time**: {current_time_formatted}\n"
        
        await ctx.send(message)
    else:
        await ctx.send("Invalid IP address or an error occurred during the lookup.")
 
@bot.command()
async def math(ctx, *, expression):
    await ctx.message.delete()
    try:
        result = eval(expression)
        await ctx.send(f'# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Result: `{result}`**')
    except:
        await ctx.send('# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Invalid expression.**')
 
L = instaloader.Instaloader()

@bot.command()
async def insta(ctx, username: str):
    await ctx.message.delete()
    try:
        # Load the Instagram profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Prepare the response with profile details in the specified format
        response = (
            "# 🎈 __Fedded Selfbot__ 🎈\n"
            f"`🔏` **Username:** {profile.username}\n"
            f"`🔏` **Full Name:** {profile.full_name}\n"
            f"`🔏` **Followers:** {profile.followers}\n"
            f"`🔏` **Following:** {profile.followees}\n"
            f"`🔏` **Number of Posts:** {profile.mediacount}\n"
            f"`🔏` **Profile Picture URL:** [Click here for link]({profile.profile_pic_url})\n"
            f"`🔏` **Bio:** {profile.biography}\n"
        )
    except instaloader.exceptions.ProfileNotExistsException:
        response = f"Profile '{username}' does not exist."
    except Exception as e:
        response = f"An error occurred: {str(e)}"

    await ctx.send(response)

@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    if response.status_code == 200:
        data = response.json()
        if data:
            cat_image_url = data[0]['url']
            await ctx.send(cat_image_url)
        else:
            await ctx.send('# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Could not retrieve a cat image.**')
    else:
        await ctx.send('# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Failed to fetch cat image.**')

def extract_promo_code(promo_link):
    return promo_link.split('/')[-1]

# Command to check the promo code status
@bot.command()
async def checkpromo(ctx, promo_link: str):
    async with aiohttp.ClientSession() as session:
        promo_code = extract_promo_code(promo_link)
        url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'
        
        async with session.get(url) as response:
            if response.status in [200, 201, 204]:
                data = await response.json()

                # Check if the promo is already claimed
                if data["uses"] == data["max_uses"]:
                    await ctx.send(f"# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Code :** `{promo_code}`\n`🔏` **Valid :** No")
                else:
                    # Extract expiration and other details
                    try:
                        now = datetime.datetime.utcnow()
                        exp_at = data["expires_at"].split(".")[0]
                        parsed = parser.parse(exp_at)
                        remaining_time = parsed - now
                        days_left = remaining_time.days
                        duration = data["subscription_plan"]["name"] if "subscription_plan" in data else "Unknown Duration"
                    except Exception as e:
                        print(e)
                        days_left = "Failed To Parse"
                        duration = "Unknown"

                    # Send the result
                    await ctx.send(f"# 🎈 __Fedded Selfbot__ 🎈\n"
                                   f"`🔏` **Code :** `{promo_code}`\n"
                                   f"`🔏` **Valid :** Yes\n"
                                   f"`🔏` **Expires in :** {days_left} days\n")
            elif response.status == 429:
                retry_after = response.headers.get("retry-after", 2)
                await ctx.send(f"Rate limited for {retry_after} seconds, please try again later.")
            else:
                await ctx.send(f"# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Code :** `{promo_code}`\n`🔏` **Valid :** No")

@bot.command()
async def rizz(ctx, user: discord.User):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as session:
        async with session.get('https://rizzapi.vercel.app/random') as response:
            if response.status == 200:
                data = await response.json()
                pickup_line = data.get("text", "Couldn't fetch a pickup line.")
                await ctx.send(f'{user.mention} {pickup_line}')
            else:
                await ctx.send(f'# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **Sorry, {ctx.author.mention}, I couldn\'t fetch a pickup line.**')

@bot.command()
async def closealldms(ctx):
    await ctx.message.delete()
    dm_user_ids = []

    TEMP_DIR = "trash"
    TEMP_FILE = os.path.join(TEMP_DIR, "dm_user_ids.pkl")  # Use .pkl extension for pickle files

    # Create the trash folder if it doesn't exist
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    # Collect user IDs from DM channels
    for dm in bot.private_channels:
        if isinstance(dm, discord.DMChannel):
            dm_user_ids.append(dm.id)
    
    # Save user IDs to the temporary file using pickle
    with open(TEMP_FILE, 'wb') as f:
        pickle.dump(dm_user_ids, f)

    # Create a thread for each DM channel and start it
    for channel_id in dm_user_ids:
        thread = threading.Thread(target=close_dm, args=(channel_id,))
        thread.start()

    await ctx.send("# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **All DMs are being closed.**")

def close_dm(channel_id):
    # URL for closing the DM channel
    url = f"https://ptb.discord.com/api/v9/channels/{channel_id}?silent=false"
    
    # Use the provided headers
    headers = mainHeader()

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Closed DM with channel ID {channel_id}")
    else:
        print(f"Failed to close DM with channel ID {channel_id}: {response.status_code} {response.text}")

def remove_friend(user_id):
    url = f"https://canary.discord.com/api/v9/users/@me/relationships/{user_id}"
    response = requests.delete(url, headers=mainHeader())
    if response.status_code == 204:
        print(f"Removed friend {user_id}")
    else:
        print(f"Failed to remove friend {user_id}, status code: {response.status_code}")

async def get_friends():
    relationships = await bot.http.get_relationships()
    return [relationship['id'] for relationship in relationships if relationship['type'] == 1]

@bot.command()
async def delfriends(ctx):
    await ctx.message.delete()
    
    while True:
        friend_ids = await get_friends()
        if not friend_ids:
            break

        # Save the friend IDs to a file using pickle
        with open('trash/friend_ids.pkl', 'wb') as f:
            pickle.dump(friend_ids, f)

        threads = []
        for friend_id in friend_ids:
            thread = threading.Thread(target=remove_friend, args=(friend_id,))
            threads.append(thread)

        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        time.sleep(2)  # Adding a short delay between each check

    total_friends = len(friend_ids)
    await ctx.send(f"# 🎈 __Fedded Selfbot__ 🎈\n`🔏` **All Friends Have Been Removed**")

@bot.command()
async def roast(ctx):
    # Check if the message is a reply
    if ctx.message.reference is None:
        await ctx.send("You need to reply to a message to use this command.")
        return

    # Get the message being replied to
    reply_to_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    message_content = reply_to_message.content

    # Prepare the payload for the API request
    payload = {
        "userMessage": {
            "role": "user",
            "content": message_content
        },
        "history": [
            {
                "role": "assistant",
                "content": "Hello there. I'm here to roast you."
            }
        ],
        "style": "default"
    }

    # Perform the API request
    response = requests.post(
        "https://www.roastedby.ai/api/generate",
        headers={
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "priority": "u=1, i",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        },
        json=payload
    )

    # Extract the response content
    try:
        response_data = response.json()
        roast_response = response_data.get('content', 'No response from the API.')
    except requests.exceptions.JSONDecodeError:
        roast_response = 'Failed to decode the API response.'
    except Exception as e:
        roast_response = f"Error processing the response: {str(e)}"

    # Send the response as a message
    await ctx.message.edit(roast_response)

def get_token_info(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    # API call to check the token
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

    if res.status_code == 200:
        res_json = res.json()

        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        phone_number = res_json.get('phone', 'None')
        email = res_json.get('email', 'N/A')
        mfa_enabled = res_json.get('mfa_enabled', False)
        flags = res_json.get('flags', 'N/A')
        locale = res_json.get('locale', 'N/A')
        verified = res_json.get('verified', False)

        # Calculate account creation date from user ID
        timestamp = ((int(user_id) >> 22) + 1420070400000) / 1000
        creation_date = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%d-%m-%Y %H:%M:%S UTC')

        # Get detailed payment methods info
        billing_info = []
        payment_sources = requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()

        for source in payment_sources:
            if source['type'] == 1:  # Credit Card
                brand = source['brand'].capitalize()
                last_4 = source['last_4']
                expires = f"{source['expires_month']:02d}/{source['expires_year']}"
                address = f"{source['billing_address']['line_1']}, {source['billing_address']['city']}, {source['billing_address']['postal_code']}, {source['billing_address']['country']}"
                billing_info.append(f"💳 **Credit Card**\nBrand: {brand}\nLast 4 Digits: {last_4}\nExpires: {expires}\nAddress: {address}")
            elif source['type'] == 2:  # PayPal
                billing_info.append(f"💰 **PayPal**\nEmail: {source['email']}")

        billing_info_text = "\n\n".join(billing_info) if billing_info else "No payment methods linked."

        # Return all the information in plain text format
        return (
            f"# 🎈 __Fedded Selfbot__ 🎈\n`👤` **Username**: {user_name}\n"
            f"`🆔` **User ID**: {user_id}\n"
            f"`📅` **Creation Date**: {creation_date}\n"
            f"`📱` **Phone Number**: {phone_number}\n"
            f"`✉️` **Email**: {email}\n"
            f"`🔒` **MFA Enabled**: {mfa_enabled}\n"
            f"`🏳️` **Flags**: {flags}\n"
            f"`🌐` **Locale**: {locale}\n"
            f"`✅` **Email Verified**: {verified}\n"
            f"`🛒` **Billing Info**:\n{billing_info_text}\n"
            f"`🔑` **Token**: ```{token}```"
        )
    
    elif res.status_code == 401:
        return "The token is not valid."
    
    else:
        return "An error occurred while checking the token."

# Bot command to check token
@bot.command()
async def tokencheck(ctx, token: str):
    await ctx.message.delete()
    token_info = get_token_info(token)

    # Send token information in plain text format
    await ctx.send(f"{token_info}")

bot.run(token)
