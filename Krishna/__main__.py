import asyncio
import importlib
from pyrogram import idle
from Krishna import Krishna
from Krishna.modules import ALL_MODULES

LOGGER_ID = -1002099846701

loop = asyncio.get_event_loop()

async def Krishna_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Krishna.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await idle()
    print(" 𝗢𝗺 𝗡𝗮𝗺𝗮𝗵 𝗩𝗮𝘀𝘂𝗱𝗲𝘃𝗮𝘆𝗮 𝗖𝗼𝗱𝘆 𝗰𝗼𝗽𝘆 𝗺𝗮𝘁 𝗸𝗿𝗻𝗮 𝘃𝗮𝘁𝘀!!@Chiku_pahadi")
    await Krishna.send_message(LOGGER_ID, "**𝗜'𝗺 𝘄𝗶𝘁𝗵 𝘂 𝗮𝗹𝘄𝗮𝘆 𝘁𝗼 𝗽𝗿𝗼𝘁𝗲𝗰𝘁 𝘂😌 𝗡𝗼𝘄 𝗮𝗹𝗹 𝗧𝗵𝗶𝗻𝗴𝘀 𝗜𝗻 𝗺𝘆 𝗖𝗼𝗻𝘁𝗿𝗼𝗹 \n 𝗠𝘆 𝗹𝗼𝘃𝗲  [𝐂𝐇𝐈𝐊𝐔スビ](https://t.me/chiku_pahadi)**")

if __name__ == "__main__":
    loop.run_until_complete(krishna_boot())
    
