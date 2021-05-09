import os
import logging
import aiohttp
from io import BytesIO, StringIO
from pyrogram import Client

API_ID = os.environ.get('API_ID', 4100189)
API_HASH = os.environ.get('API_HASH', '5a05b2632ec2c6739d1ee7b3636d7097')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '1765605223:AAFfQ26dMbMAcHIlEolyp8UxTNruVBGUfyY')
TESTMODE = os.environ.get('TESTMODE')
TESTMODE = TESTMODE and TESTMODE != '0'

EVERYONE_CHATS = os.environ.get('EVERYONE_CHATS')
EVERYONE_CHATS = list(map(int, EVERYONE_CHATS.split(' '))) if EVERYONE_CHATS else [-1001378211961]
ADMIN_CHATS = os.environ.get('1830707932')
ADMIN_CHATS = list(map(int, ADMIN_CHATS.split(' '))) if ADMIN_CHATS else [441422215]
ALL_CHATS = EVERYONE_CHATS + ADMIN_CHATS

PROGRESS_UPDATE_DELAY = int(os.environ.get('PROGRESS_UPDATE_DELAY', 5))
MAGNET_TIMEOUT = int(os.environ.get('LEECH_TIMEOUT', 60))
LEECH_TIMEOUT = int(os.environ.get('LEECH_TIMEOUT', 300))

logging.basicConfig(level=logging.INFO)
app = Client('lazyleech', API_ID, API_HASH, plugins={'root': os.path.join(__package__, 'plugins')}, bot_token=BOT_TOKEN, test_mode=TESTMODE, parse_mode='html', sleep_threshold=30)
session = aiohttp.ClientSession()
help_dict = dict()
preserved_logs = []

class SendAsZipFlag:
    pass

class ForceDocumentFlag:
    pass

def memory_file(name=None, contents=None, *, bytes=True):
    if isinstance(contents, str) and bytes:
        contents = contents.encode()
    file = BytesIO() if bytes else StringIO()
    if name:
        file.name = name
    if contents:
        file.write(contents)
        file.seek(0)
    return file
