from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging
from config import OWNER_ID, BOT_USERNAME
from config import *
from Krishna import Krishna as app

import pyrogram
from pyrogram.errors import FloodWait


# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------


start_txt = """<b> 🥰𝗞𝗿𝗶𝘀𝗵𝗻𝗮 𝗧𝗵𝗲 𝗚𝗿𝗼𝘂𝗽 𝗣𝗿𝗼𝘁𝗲𝗰𝘁𝗼𝗿 🪈🪈 </b>

𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗞𝗿𝗶𝘀𝗵𝗻𝗮 𝗣𝗿𝗼𝘁𝗲𝗰𝘁𝗼𝗿.......🥰
𝗜'𝗺 𝗧𝗵𝗲 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝘄𝗵𝗼 𝗽𝗿𝗼𝘁𝗲𝗰𝘁 𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝗙𝗿𝗼𝗺 𝗰𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 𝗜𝗻𝗳𝗿𝗶𝗻𝗴𝗺𝗲𝗻𝘁.....😶‍🌫️
𝗠𝘆 𝗔𝗶𝗺 𝗝𝘂𝘀𝘁 𝗧𝗼 𝗣𝗿𝗼𝘁𝗲𝗰𝘁 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗙𝗿𝗼𝗺 𝗬𝗼𝘂𝗿 𝗛𝗮𝘁𝗲𝗿𝘀...😀
𝗝𝗼𝗶𝗻 -: @my_worldcs 𝗦𝘁𝗮𝗿𝘁 -: @krishnamubot

𝗜𝗳 𝘂 𝗵𝗮𝘃𝗲 𝗮𝗻𝘆 𝗤𝘂𝗲𝗿𝗿𝘆 𝗙𝗲𝗲𝗹 𝗙𝗿𝗲𝗲 𝘁𝗼 𝗿𝗲𝗽𝗼𝗿𝘁 𝗮𝘁 𝗺𝘆 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽 ||[𝗞𝗥𝗜𝗦𝗛𝗡𝗔 𝗞𝗜 𝗡𝗔𝗚𝗔𝗥𝗜](https://t.me/my_worldcs)||🥰🪈 """

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("•𝗠𝘂𝗷𝗵𝗲 𝗟𝗲 𝗖𝗵𝗮𝗹𝗼•", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• 𝗛𝗮𝗻𝗱𝗹𝗲𝗿 •", callback_data="Krishna_back")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/7f8ebddf56559ac69d31b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/my_worldcs"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("Krishna_back"))
async def Krishna_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"



@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



FORBIDDEN_KEYWORDS = ["porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
        
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 10

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")
    

# -----------------------------------------------------------------------------------


    
@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    pass 
# -------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"@{message.from_user.username} 𝗗𝗲𝗸𝗵𝗼 𝗣𝗗𝗙 𝗯𝗵𝗲𝗷𝗼𝗴𝗲 𝗧𝗼 𝗱𝗲𝗹𝘁𝗲 𝗸𝗿 𝗱𝘂𝗻𝗴𝗮 𝗔𝘂𝗿 𝗺𝗲𝗿𝗲 𝗴𝗿𝗼 𝘀𝗲 𝗱𝗼𝗼𝗿 𝗿𝗮𝗵𝗼 ,\n 𝗖𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 𝗹𝗴𝗮𝗻𝗲 𝗞𝗶 𝗞𝗼𝘀𝗵𝗶𝘀𝗵 𝗻 𝗞𝗿𝗼 \n\n 𝗗𝗲𝗹𝗲𝘁𝗲 𝗸𝗿 𝗱𝗶𝘆𝗮 𝗠𝗲𝗻𝗲 𝗮𝗮𝗯 𝗺𝘁 𝗗𝗮𝗹𝗻𝗮.\n\n 𝗺𝘆 𝗼𝘄𝗻𝗲𝗿 @chiku_pahadi 🥰."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

# ----------------------------------------
