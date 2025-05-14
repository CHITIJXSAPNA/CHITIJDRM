from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid 
import requests
import m3u8
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message    
from p_bar import progress_bar    
from subprocess import getstatusoutput    
from aiohttp import ClientSession    
import helper    
from logger import logging    
import time    
import asyncio    
from pyrogram.types import User, Message    
import sys    
import re    
import os 
import urllib
import urllib.parse
import tgcrypto
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode
from helper import *
from config import API_ID, API_HASH, BOT_TOKEN

bot = Client("bot",
             api_id=225877,
             api_hash="0c9262b17ad8e38f1e4d",
             bot_token="")

photo1 = 'https://envs.sh/PQ_.jpg'
getstatusoutput(f"wget {photo1} -O 'photo.jpg'")    
photo = "photo.jpg"

api_url = "http://master-api-v3.vercel.app/"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
token_cp = 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9gft'

@bot.on_message(filters.command("start"))
async def start_command(bot: Client, m: Message):
    await m.reply_text('''🎉 <b>Welcome to DRM Bot! </b>🎉
    
<b>You can download all Non-DRM+Decrypted DRM content 🔐 including:</b>
<blockquote><i>
   • 📚 Appx Zip
   • 🎓 Classplus DRM+ NDRM
   • 🧑‍🏫 PhysicsWallah DRM
   • 📚 CareerWill + PDF
   • 🎓 Khan GS
   • 🚀 APPX + APPX DEC PDF
   • 🎓 Vimeo Protection
   • 🎓 Brightcove Protection
   • 🎓 Visionias Protection
   • 🎓 Zoom Video
   • 🎓 All Non DRM+DEC DRM
   • 🎓 MPD URLs if the key is known (e.g., Mpd_url?key=key XX:XX)
</blockquote></i>
<b>🚀 The bot is open to everyone! Use /chitij to start downloading.</b>
<b>📞 For support, contact [CURSED CHITIJ](https://t.me/username)</b>''')

@bot.on_message(filters.command(["id"]))
async def id_command(client, message: Message):
    chat_id = message.chat.id
    await message.reply_text(
        f"🎉 **Success!**\n\n"
        f"🆔 **This Group/Channel ID:**\n`{chat_id}`\n\n"
        f"📌 **You can use /chitij directly in this chat.**"
    )

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("🚦**STOPPED**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command("chitij"))
async def account_login(bot: Client, m: Message):
    chat_id = str(m.chat.id)
    logging.info(f"Received /chitij command in chat: {chat_id}, type: {m.chat.type}")

    editable = await m.reply_text("**Please Send TXT file for download**")
    input: Message = await bot.listen(editable.chat.id)
    y = await input.download()
    file_name, ext = os.path.splitext(os.path.basename(y))

    if file_name.endswith("_helper"):
        x = decrypt_file_txt(y)
        await input.delete(True)
    else:
        x = y 

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name Or /d for default**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == '/d':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter resolution** `144` , `240` , `360` , `480` , `720` , `1080`")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080"
        else:
            res = "1280x720"
    except Exception:
        res = "UN"

    await editable.edit("**Enter A Caption For your Upload OR /d for default**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == '/d':
        MR = "CURSED CHITIJ"
    else:
        MR = raw_text3

    await editable.edit("**Enter pw token for mpd or /d for no **")
    input11: Message = await bot.listen(editable.chat.id)
    token = input11.text
    await input11.delete(True)

    await editable.edit("Enter Your Tumbnail Link or use `no` for default")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)
            elif "https://cpvod.testbook.com/" in url:
                url = url.replace("https://cpvod.testbook.com/","https://media-cdn.classplusapp.com/drm/")
                url = 'https://dragoapi.vercel.app/classplus?link=' + url
                mpd, keys = helper.get_mps_and_keys(url)
                url = mpd
                keys_string = " ".join([f"--key {key}" for key in keys])
            elif "d1d34p8vz63oiq" in url or "sec1.pw.live" in url:
                url = f"https://anonymouspwplayer-b99f57957198.herokuapp.com/pw?url={url}?token={token}"
            elif "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
            elif "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov 
            elif "classplusapp.com/drm/" in url:
                url = 'https://dragoapi.vercel.app/classplus?link=' + url
                mpd, keys = helper.get_mps_and_keys(url)
                url = mpd
                keys_string = " ".join([f"--key {key}" for key in keys])
            elif "tencdn.classplusapp" in url:
                headers = {'Host': 'api.classplusapp.com', 'x-access-token': f'{token_cp}', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
                params = (('url', f'{url}'))
                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                url = response.json()['url']
            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': f'{token_cp}'}).json()['url']
            elif 'media-cdn.classplusapp.com' in url or 'media-cdn-alisg.classplusapp.com' in url or 'media-cdn-a.classplusapp.com' in url:
                headers = {'x-access-token': f'{token_cp}', "X-CDN-Tag": "empty"}
                response = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=headers)
                url = response.json()['url']
            elif 'encrypted.m' in url:
                appxkey = url.split('*')[1]
                url = url.split('*')[0]
            elif "allenplus" in url or "player.vimeo" in url:
                if "controller/videoplay" in url:
                    url0 = "https://player.vimeo.com/video/" + url.split("videocode=")[1].split("&videohash=")[0]
                    url = f"https://master-api-v3.vercel.app/allenplus-vimeo?url={url0}&authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
                else:
                    url = f"https://master-api-v3.vercel.app/allenplus-vimeo?url={url}&authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
            elif url.startswith("https://videotest.adda247.com/"):
                if url.split("/")[3] != "demo":
                    url = f'https://videotest.adda247.com/demo/{url.split("https://videotest.adda247.com/")[1]}'
            elif 'master.mpd' in url:
                url = f"{api_url}pw-dl?url={url}&token={token}&authorization={api_token}&q={raw_text2}"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{name1[:60]} '

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'**╭━━━━━━━━━━━╮**\n**💫 𝐕ɪᴅᴇⱺ 𝐈𝐃** : **{str(count).zfill(3)}**\n**╰━━━━━━━━━━━╯**\n**📁𝐓ɪᴛʟᴇ : {name1}** **({res}) CHITIJ.mkv\n** \n<blockquote>**📚𝐂ⱺᴜʀꜱᴇ** : **{raw_text0}**\n\n**⚡Dⱺw𐓣𝗅ⱺ𝖺𝖽ed By** : **{MR}** </blockquote>'
                cc1 = f'**╭━━━━━━━━━━╮**\n**💫 𝐅ɪʟᴇ 𝐈𝐃** : **{str(count).zfill(3)}**\n**╰━━━━━━━━━━╯**\n**📁𝐓ɪᴛʟᴇ : {name1}** **CHITIJ.pdf\n** \n<blockquote>**📚�	Cⱺᴜʀꜱᴇ** : **{raw_text0}**\n\n**⚡Dⱺw𐓣𝗅ⱺ𝖺𝖽ed By** : **{MR}** </blockquote>'
                cc2 = f'**╭━━━━━━━━━━━╮**\n**💫 𝐈ᴍᴀɢᴇ 𝐈𝐃** : **{str(count).zfill(3)}**\n**╰━━━━━━━━━━━╯**\n\n**📁𝐓ɪᴛʟᴇ** : **{name1}** **CHITIJ.jpg**\n\n**📚𝐂ⱺᴜʀꜱᴇ** : **{raw_text0}**\n\n**⚡Dⱺw𐓣𝗅ⱺ𝖺𝖽ed By** : **{MR}**'
                ccyt = f'**╭── ⋆⋅☆⋅⋆ ──╮**\n✦ **{str(count).zfill(3)}** ✦\n**╰── ⋆⋅☆⋅⋆ ──╯**\n\n🎭 **Title:** `{name1} 😎 .mkv`\n🎬 **Video Link:** {url}\n🖥️ **Resolution:** [{res}]\n\n📘 **Course:** `{b_name}`\n\n🚀 **Extracted By:** `**{MR}**`'

                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id, document=ka, caption=cc1)
                        count += 1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".zip" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.zip" "{url}"'
                        download_cmd = f"{cmd} -R 50 --fragment-retries 50"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.zip', caption=cc1)
                        count += 1
                        os.remove(f'{name}.zip')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        count += 1
                        pass
                elif 'pdf*' in url:
                    pdf_key = url.split('*')[1]
                    url = url.split('*')[0]
                    pdf_enc = await helper.download_and_decrypt_pdf(url, name, pdf_key)
                    copy = await bot.send_document(chat_id=m.chat.id, document=pdf_enc, caption=cc1)
                    count += 1
                    os.remove(pdf_enc)
                    continue
                elif ".pdf" in url:
                    try:
                        if "cwmediabkt99" in url:
                            time.sleep(2)
                            cmd = f'yt-dlp -o "{name}.pdf" "https://master-api-v3.vercel.app/cw-pdf?url={url}&authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"'
                            download_cmd = f"{cmd} -R 50 --fragment-retries 50"
                            os.system(download_cmd)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1
                            os.remove(f'{name}.pdf')
                        else:
                            cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                            download_cmd = f"{cmd} -R 50 --fragment-retries 50"
                            os.system(download_cmd)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1
                            os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif any(img in url.lower() for img in ['.jpeg', '.png', '.jpg']):
                    try:
                        subprocess.run(['wget', url, '-O', f'{name}.jpg'], check=True)
                        await bot.send_photo(
                            chat_id=m.chat.id,
                            caption=cc2,
                            photo=f'{name}.jpg',
                        )
                        count += 1
                        await asyncio.sleep(1)
                        continue
                    except subprocess.CalledProcessError:
                        await message.reply("Failed to download the image. Please check the URL.")
                    except Exception as e:
                        await message.reply(f"An error occurred: {e}")
                    finally:
                        if os.path.exists(f'{name}.jpg'):
                            os.remove(f'{name}.jpg')
                elif "youtu" in url:
                    try:
                        await bot.send_photo(chat_id=m.chat.id, photo=photo, caption=ccyt)
                        count += 1
                    except Exception as e:
                        await m.reply_text(str(e))
                        await asyncio.sleep(1)
                        continue
                elif ".ws" in url and url.endswith(".ws"):
                    try:
                        await helper.pdf_download(f"{api_url}utkash-ws?url={url}&authorization={api_token}", f"{name}.html")
                        time.sleep(1)
                        await bot.send_document(chat_id=m.chat.id, document=f"{name}.html", caption=cc1)
                        os.remove(f'{name}.html')
                        count += 1
                        time.sleep(5)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                        await m.reply_text(str(e))
                        continue
                elif 'encrypted.m' in url:
                    Show = f"✈️ **ρrogrᥱss** ✈️\n\n┠ 📈 **𝖳𝗈𝗧ᥲᥣ 𝗅ιᥒ𝗄𝗌** = **{len(links)}**\n┠ 🔄 **𝗖υ𝗋𝗋ᥱᥒ𝗧ᥙ𝗻𝗀 𝗈ᥒ** = **{str(count).zfill(3)}**\n\n**🚀𝖣𝗈𝗐ᥒᥣ𝗈ᥲ𝖽ιᥒ�_g🚀**\n\n**🧚🏻‍♂️ tιtᥣᥱ** : **{name}**\n├── **📁ᥱxtᥱᥒsιoᥒ** : **{MR}**\n├── **📺 𝗥ᥱ𝗌υᥣ𝗧ᥲι𝗈ᥒ** : **{raw_text2}**\n├── **Url** : `Kya karega URL dekh ke  BSDK 👻👻`\n├──  **🖼️ thυmbᥒᥲιᥣ** : **`{input6.text}`**\n├── **bot mᥲdᥱ bყ** : **⁣CHITIJ**"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_and_decrypt_video(url, cmd, name, appxkey)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    await asyncio.sleep(1)
                    continue
                elif 'drmcdni' in url or 'drm/wv' in url:
                    Show = f"✈️ **ρrogrᥱss** ✈️\n\n┠ 📈 **𝖳𝗈𝗧ᥲᥣ 𝗅ιᥒ𝗄𝗌** = **{len(links)}**\n┠ 🔄 **𝗖υ𝗋𝗋ᥱᥒ𝗧ᥙ𝗻𝗀 𝗈ᥒ** = **{str(count).zfill(3)}**\n\n**🚀𝖣𝗈𝗐ᥒᥣ𝗈ᥲ𝖽ιᥒ𝗀🚀**\n\n**🧚🏻‍♂️ tιtᥣᥱ** : **{name}**\n├── **📁 ᥱxtᥱᥒsιoᥒ** : **{MR}**\n├── **📺 𝗥ᥱ𝗌υᥣ𝗧ᥲι𝗈ᥒ** : **{raw_text2}**\n├── **Url** : `Kya karega URL dekh ke  BSDK 👻👻`\n├──  **🖼️ thυmbᥒᥲιᥣ** : **`{input6.text}`**\n├── **bot mᥲdᥱ bყ** : **⁣CHITIJ**"
                    prog = await m.reply_text(Show)
                    res_file = await helper.decrypt_and_merge_video(mpd, keys_string, path, name, raw_text2)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    await asyncio.sleep(1)
                    continue
                else:
                    Show = f"✈️ **ρrogrᥱss** ✈️\n\n┠ 📈 **𝖳𝗈𝗧ᥲᥣ 𝗅ιᥒ𝗄𝗌** = **{len(links)}**\n┠ 🔄 **𝗖υ𝗋𝗋ᥱᥒ𝗧ᥙ𝗻𝗀 𝗈ᥒ** = **{str(count).zfill(3)}**\n\n**🚀𝖣𝗈𝗐ᥒᥣ𝗈ᥲ𝖽ιᥒ𝗀🚀**\n\n**🧚🏻‍♂️ tιtᥣᥱ** : **{name}**\n├── **📁 ᥱxtᥱᥒsιoᥒ** : **{MR}**\n├── **📺 𝗥ᥱ𝗌υᥣ𝗧ᥲι𝗈ᥒ** : **{raw_text2}**\n├── **Url** : `Kya karega URL dekh ke  BSDK 👻👻`\n├──  **🖼️ thυmbᥒᥲιᥣ** : **`{input6.text}`**\n├── **bot mᥲdᥱ bყ** : **⁣CHITIJ**"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed \**\n\n{str(e)}\n\n**Name** - {name}\n**Link** - {url}"
                )
                count += 1
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**Sᴜᴄᴄᴇsғᴜʟʟʏ Dᴏᴡɴʟᴏᴀᴅᴇᴅ Aʟʟ Lᴇᴄᴛᴜʀᴇs SIR 👿🚀**")

bot.run()
