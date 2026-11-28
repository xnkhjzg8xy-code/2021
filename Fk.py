#— — — — — — — — — — — — —
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#اورق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
W1 = '\x1b[1;97m'
W2 = '\x1b[38;5;120m'
W3 = '\x1b[38;5;204m'
W4 = '\x1b[38;5;150m'
W5 = '\x1b[1;33m'
W6 = '\x1b[1;31m'
W7 = "\033[1;33m"
W8 = '\x1b[2;36m'
W8 = f'\x1b[38;5;117m'
W9 = "\033[1m\033[34m"
#— — — — — — — — — — — — —
GE,BE,GI,BI=0,0,0,0
#— — — — — — — — — — — — —

print(f"""
 {X}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⠀⢀⣴⣶⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣞⣿⢠⡟⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣨⣿⣿⣼⣿⣟⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⠶⠶⣿⣿⣿⢛⣿⣿⣿⣷⡟⠏⠿⡄⠀⠀⠀⠀
⠀⣀⣠⣤⣤⣼⣿⣟⢛⠠⡀⢄⡸⠄⣿⢿⣿⣇⣼⢿⣿⣟⠣⡘⠸⢿⠀⠀⠀⠀
⣸⣿⣿⣿⣿⣿⣿⣿⡌⠱⣈⠒⡄⢣⠘⠾⠟⡠⠘⠞⡿⢋⠔⢡⠃⣿⡆⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠡⠄⢃⠌⠄⢣⠘⠤⡁⢍⠒⡐⠌⣂⠦⣉⣿⡇⠀⠀⠀
⢿⣿⣿⣿⣿⣿⣿⣿⡇⢡⠊⠔⡨⠘⢄⠊⡔⢁⠊⡔⢁⠎⣐⠺⢅⣾⡇⠀⠀⠀
⠘⣿⣿⣿⣿⣿⣿⣿⠃⡐⠌⡂⠥⢑⡈⢒⠨⠄⡃⢄⢃⢎⡱⢃⠎⣾⠇⠀⠀⠀
⠀⠈⠛⢿⣿⣿⡿⠋⡐⢀⠢⢡⠘⡠⠘⡄⢃⣜⣠⣮⡿⠷⡂⢍⢂⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠓⠶⠶⠤⢾⣄⠂⡱⣌⡜⣻⣋⣯⡕⡘⠤⡑⢪⡰⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣤⣔⣸⣨⣍⣍⣱⣬⣶⣽⣶⡿⠟⠢⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡷⠈⠙⠛⠿⠯⠽⠿⠿⠟⠛⠋⠉⣄⣇⠀⠹⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢃⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠄⠀⣹⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣾⠃⠘⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⣿⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡏⠀⠀⠀⣼⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡉⠻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣷⣤⣀⣼⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠘⠿⢿⣿⣯⣽⣻⠟⠁⠐⢤⡯⢙⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠲⢶⣄⠀⢻⡆⠀⣤⣀⠀⠀⠀⢸⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣽⡄⠀⠀⠀⠘⣿⠀⠈⠛⠃⠀⠀⢸⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠉⠛⠓⠒⠒⠻⡟⠒⠶⠦⠶⠶⠞⢿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠬⣷⣶⢶⣦⣤⣄⣷⣄⣀⣄⣀⣀⣠⣾⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⡄⡀⠙⢾⣟⢯⣿⡿⠿⠿⢿⣿⣿⡿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣤⣤⣤⣤⣼⣿⣿⡇⠈⠠⠄⠀⠙⣿⣿⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠁⠀⠀⠀⠘⠿⣭⣉⣉⣩⡵⠋⠀⠀⠀
""")

import requests
# ... بقية الإمبروتات الخاصة بك
to = input('enter your token : ') # هذا سطر تعريف المتغير to
id = input('enter your id : ')   # هذا سطر تعريف المتغير id

# ... بقية الكود الخاص بك

import webbrowser
webbrowser.open("https://t.me/Copy_122")
import webbrowser
webbrowser.open("https://t.me/Copy_122")
from requests import get, post
from random import choice, randrange
from threading import Thread
import os, sys
import http.client
import requests
import re
import time
try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent')
from random import choice, randrange
from requests import get
import urllib.parse
import binascii
import uuid
import random
import json
import secrets
from urllib.parse import urlencode
import uuid

try:
    from MedoSigner import Argus, Gorgon, md5, Ladon
except:
    os.system('pip install MedoSigner')

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
    data = payload
    if not unix: unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(
            params,
            x_ss_stub,
            unix,
            platform=platform,
            aid=aid,
            license_id=license_id,
            sec_device_id=sec_device_id,
            sdk_version=sdk_version_str,
            sdk_version_int=sdk_version
        )
    }

def TikApimOh(email):
    while True:
        try:
            hash_list = [
                "cafe66f2ae8a76f077cbd626ea86df79", "9c5f3bd655c1073be5766126e5de6fd3",
                "53824e1723b4981d6cd70509b914098f", "1342c2d734388562d6459a5a9fe72792",
                "f1ff89b59a6ba357d77e98bdcf255cab", "7da0a62f4f89c6649b8dfa160d6cec8d",
                "dbf07d996eb8201596c24c09ae323267", "9cc709863127d0aaf365cd16de02c219",
                "55e806351ecd3cc6b61ef91aecc7e505", "697da55c5506fd52436c701c1e2b52f4",
                "bf0bb6f9349449bd775325522cceba25", "57169db67755173ad686ac0adbf61b2c",
                "414944c36526c4965203cdc5d6430586", "a2939903b2da2d314749d9eda608dee8",
                "42b2e8551486b0628ab16c7cc8e90ba1", "27005da3a7d772cb382c3eaac3c090af",
                "ab44c8c16bc5aaf4f3edef66b8915ef7", "2274f897b348647258efdb1b005216e0",
                "d8dffcf38a761c5e8a509b4aea7a4303", "6052a82299cb2b38874dee88c82a0d21",
                "93ab06dc14cef94ffacf9cad56314b65", "ff925b0293db2e1a647b4f615fd815e5",
                "329e7d2ca6364cf94db07ab521275673", "acaed5f00fb0910a53772ec701b9e850",
                "a4a9c45ce50f087e31d8dd90606565dc", "610a8a6ccf26c62d0849a292918eaafe",
                "41fe5fe6c60679e9ec18c5af7ba05c69", "c83a8c956921e7e35398c02d554112b5",
                "9c4254d518f4796d67825fcf1b35cfa8", "c544414665b9558f8157a55e65f7d44e",
                "d7ca96c365b263675a102a582972feea", "5bb1cd7de83db6f316b69e3b045701dc",
                "5845e1e5be9ef3bf73c22b6527bd0c8e", "37fb0b33c8e72da7130d41dbb466db86",
                "9cf1061a9235aad06d4dda19485a108c", "07849301f75b8ba5090258904cdb98f4",
                "8eae100188029eca8fd6002b2198de8f", "69ac0eea723bdfda1f1633171ba4e18f",
                "3599955114effa5ff50e494135012856", "a1593241c82c93e5c19fa180ef5b21a6",
                "a624d9823074741e1a91bf1cbcccfd63", "69be771087f3392967cf9dddf6c76935",
                "fb2253e2732428600ff8bfdaa1229adc", "594e8f0cd3bd7d7bed94161b9aee6b86",
                "68ca12e10055cf7f3e8200d82586d8d3", "e6e25d852227cc3006fdfef85dd38d81",
                "e160f93facb5c030a029c74beb2e234b"
            ]

            rticket = str(randrange(120_000_000, 160_000_000) * -1) + "4632"
            cdid = str(uuid.uuid4())
            iid = str(randrange(10**18, 10**19))
            device_id = str(randrange(10**18, 10**19))
            openudid = binascii.hexlify(os.urandom(8)).decode()
            ran = choice(hash_list)
            cookies = {'sessionid': ran}

            params = {
                '_rticket': rticket, 'ab_version': '37.8.5', 'ac': 'WIFI', 'ac2': 'wifi',
                'aid': '1233', 'app_language': 'ar', 'app_name': 'musical_ly',
                'app_type': 'normal', 'build_number': '37.8.5', 'carrier_region': 'US',
                'carrier_region_v2': '460', 'cdid': cdid, 'channel': 'googleplay',
                'cronet_version': '75b93580_2024-11-28', 'device_brand': 'rockchip',
                'device_id': device_id, 'device_platform': 'android',
                'device_type': 'rk3588s_q', 'dpi': '320', 'fixed_mix_mode': '1',
                'host_abi': 'arm64-v8a', 'iid': iid, 'is_pad': '0', 'language': 'ar',
                'last_install_time': '1745162892', 'locale': 'ar',
                'manifest_version_code': '2023708050', 'mix_mode': '1',
                'op_region': 'US', 'openudid': openudid, 'os': 'android',
                'os_api': '29', 'os_version': '10', 'region': 'IQ',
                'request_tag_from': 'h5', 'rebuyukution': '720%2A1280',
                'rrb': '%7B%7D', 'scene': '4', 'ssmix': 'a', 'support_webview': '1',
                'sys_region': 'IQ', 'timezone_name': 'Europe%2FAmsterdam',
                'timezone_offset': '3600', 'ts': '1745163105',
                'ttnet_version': '4.2.210.6-tiktok', 'uoo': '0',
                'update_version_code': '2023708050', 'use_store_region_cookie': '1',
                'version_code': '370805', 'version_name': '37.8.5',
                'app_version': '32.9.5'
            }

            user_agent = (
                f"com.zhiliaoapp.musically/{randrange(2_000_000_000, 3_000_000_000)} "
                f"(Linux; U; Android {randrange(10, 16)}; "
                f"{choice(['ar_AE', 'en_US', 'fr_FR', 'es_ES'])}; "
                f"{choice(['phone', 'tablet', 'tv'])}; "
                f"Build/UP1A.{randrange(200_000_000, 300_000_000)}; "
                f"Cronet/{randrange(10_000_000, 20_000_000)} {randrange(2023, 2026)}-"
                f"{randrange(1,13):02}-{randrange(1,29):02}; "
                f"QuicVersion:{randrange(10_000_000, 20_000_000)} {randrange(2023, 2026)}-"
                f"{randrange(1,13):02}-{randrange(1,29):02})"
            )

            m = sign(params=urlencode(params), payload="", cookie="")

            headers = {
                'User-Agent': user_agent,
                'x-tt-passport-csrf-token': 'deb4845f1062c1cf916902c6058604d1',
                'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
                'x-argus': m["x-argus"],
                'x-gorgon': m["x-gorgon"],
                'x-khronos': m["x-khronos"],
                'x-ladon': m["x-ladon"]
            }

            url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=0&app_language=en&"
            res = requests.post(url, params=params, headers=headers, data={"email": email}, cookies=cookies).text
            
            # هذا هو الشرط الذي يحدد ما إذا كان الإيميل متاحًا أم لا
            if 'Email is linked to another account. Unlink or try another email.' in res:
                return True
            else:
                return False
        except:
            pass


import threading,time
from faker import Faker

faker=Faker()
iyi=0
kotu=0

thomas='\033[0m'
yarak='\033[1m'
z='\033[92m'
b='\033[91m'
m='\033[93m'
a='\033[95m'
q='\033[96m'
#— — — — — — — — — — — — —
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#اورق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
W1 = '\x1b[1;97m'
W2 = '\x1b[38;5;120m'
W3 = '\x1b[38;5;204m'
W4 = '\x1b[38;5;150m'
W5 = '\x1b[1;33m'
W6 = '\x1b[1;31m'
W7 = "\033[1;33m"
W8 = '\x1b[2;36m'
W8 = f'\x1b[38;5;117m'
W9 = "\033[1m\033[34m"
#— — — — — — — — — — — — —
GE,BE,GI,BI=0,0,0,0
#— — — — — — — — — — — — —

escort=threading.Lock()
sex=['◐','◓','◑','◒']

print(f"{F}الحسابات اللي انصادت تنحفظ في ملف اسمه {Z}(تم الصيد.txt)")

canavaro=f"""{q}
⢦⡠⠀⠀⠀⠀⠀⠀⠀⠀⣴⢋⡄⠐⠄⠒⠻⠭⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠡⠁⣸⣦⠀⠙⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⢀⣼⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣶⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⢰⡄⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⢣⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣷⣿⣷⣦⣼⠀⢀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⢠⢉⠻⢶⣿⣿⣿⣿⡟⣭⡼⠟⠛⠛⠿⢿⢿⡿⣿⣿⡿⣿⣿⡿⢿⣿⣿⡟⣁⠀⠸⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠈⡐⢸⠖⠹⣿⣿⡏⠰⠂⢀⠀⠀⡀⠀⠀⢠⣥⠃⠈⠀⠀⡀⠀⠀⠀⠉⠐⣿⠀⢀⡈⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠰⢰⠀⣿⣿⣿⣷⣴⠾⠦⢥⠈⠀⠀⣀⣸⣿⡅⠠⣄⠀⢁⠀⠋⠀⠀⣷⠏⠀⠸⢀⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⢳⡗⠘⣿⣿⣿⣿⣿⣷⡾⠋⣠⣴⣿⣿⣿⠀⠀⠘⣆⠀⠂⢀⣠⣾⠃⠀⠀⢰⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠘⠿⠆⢹⣿⣿⣿⣿⣿⣶⣾⠟⠀⣾⣿⣿⡀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⢠⣿⣿⣿⣿⣿⣿
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣷⠀⢰⣿⣿⣿⡁⠀⠄⢻⣿⣿⣿⣿⣉⠀⣀⣾⣿⣿⣿⣿⣿⣿
⣷⠀⠐⣦⡇⠀⠀⠀⠀⣀⠈⣿⣿⣿⣿⣿⣿⢋⣼⠀⠀⠈⠁⠁⠀⠀⣼⣿⣿⣷⣿⠇⣰⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣷⣤⡀⠶⢾⡯⢰⢿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠟⣯⠀⣉⡛⠻⠿⢿⣿⣿⣿⣿
⣿⣿⡿⣿⣿⣿⣿⡼⢻⢁⣾⠸⣿⣿⣿⡿⠋⠁⣨⣤⣤⣤⣤⣤⣤⣤⣬⣿⣿⢠⡏⠀⠳⡆⢬⣑⡒⠮⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠃⣠⣾⣿⣧⠹⡟⢿⣷⣷⡟⠛⠛⠁⠰⠿⢿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠨⠘⣿⣿⣷⡝⣿⣿
⣿⣿⣿⣿⣿⠟⣡⢾⢿⣿⣿⣿⣷⣜⢦⡙⢿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⠝⠀⢀⣼⠀⠀⡄⢌⠻⣿⣿⣏⣿
⣿⣿⣿⠟⢁⣶⠏⡜⢸⣿⠈⣿⣧⢻⣦⣌⠢⣍⠻⢿⣫⣿⣿⣿⣿⡿⠟⠀⠀⣴⣾⣿⠆⢠⡇⢸⣧⣿⣿⣿⣿
⣿⡿⢁⣴⣿⡟⣸⠃⣿⣿⣦⣏⡙⢿⣿⣏⡑⠂⠉⠀⠌⣁⡀⠈⠛⠀⣀⡤⠿⣿⡿⠋⣠⣿⠀⣄⣿⣿⣿⣿⣿
⣋⣴⣿⣿⣿⢃⡟⠀⣿⠹⣿⣿⣿⣦⠙⢻⣿⣷⣶⣄⣤⣤⣉⠉⠠⢾⣤⣶⣾⣟⣡⣾⣿⣿⢰⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣾⣵⡆⢻⡇⠙⣿⣿⣿⣿⣶⣌⣹⠿⢿⣿⣿⠏⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿

كوبي https://t.me/Copy_122
"""



def purna(zenci_yarak,amderinligi):
    if len(zenci_yarak)>=amderinligi:return zenci_yarak[:amderinligi]
    buyuk=(amderinligi-len(zenci_yarak))//2
    kucuk=amderinligi-len(zenci_yarak)-buyuk
    return ' '*buyuk+zenci_yarak+' '*kucuk

def porno():
    global iyi,kotu
    while True:
        try:
            kullanici=faker.user_name()
            mail=f'{kullanici}@yopmail.com'
            
                  
            sonuc=TikApimOh(mail) 
            with escort:
                if sonuc: # إذا كان الإيميل متاحاً ("شغال")
                    iyi+=1
                    bosalma=f"{z}متاح{thomas}"
               
                    with open("تم الصيد.txt","a") as dosya:
                        dosya.write(mail+"\n")
         
                    # هنا نضيف السطر لإرسال الإيميل المتاح إلى البوت
                    # تأكد أن to و id معرفين كمتغيرات في بداية السكربت أو في نطاق عام
                    requests.post(f"https://api.telegram.org/bot{to}/sendMessage?chat_id={id}&text={mail}")
                else: # إذا كان الإيميل غير متاح
                    kotu+=1
                    bosalma=f"{b}خطأ{thomas}"
                    # لا يوجد سطر إرسال للبوت هنا، وبالتالي لن يرسل الإيميلات غير المتاحة

                amderinligi=70
                vajina=22

                pembe_am=''
                patlak_am=''
                beyaz_am=''
                kara_am=''
                kıllı_am=''
                sulu_am=''
                tüysüz_am=''
                kucuklam_am=''

                amciikoh=sex[(iyi+kotu)%len(sex)]

                yarambasi=(
                    f"{sulu_am} {amciikoh} {yarak}{m}تيكتوك يومب ميل{thomas}"
                    +' '*(amderinligi-len(" TikTok Yopmail Aracı ")-5)
                    +f"{sulu_am}"
                )

                amcikk=(
                    f"{sulu_am} "
                    +purna(f"{z}متاح: {iyi}{thomas}",vajina)
                    +purna(f"{b}خطأ: {kotu}{thomas}",vajina)
                    +f"{sulu_am}"
                )

                mmm="إيميل:"
                ammm=amderinligi-len(mmm)-6
                ebeninami=mail if len(mail)<=ammm else mail[:ammm-3]+"..."
                sikmek=f"{sulu_am} {mmm} {q}{ebeninami}{thomas}"+' '*(amderinligi-len(mmm)-len(ebeninami)-5)+sulu_am

                print("\033[H\033[J",end="")
                print(canavaro)
                print(f"{pembe_am}{kıllı_am*(amderinligi-2)}{patlak_am}")
                print(yarambasi)
                print(tüysüz_am+kıllı_am*(amderinligi-2)+kucuklam_am)
                print(amcikk)
                print(sikmek)
                print(f"{beyaz_am}{kıllı_am*(amderinligi-2)}{alt_kucuk}")
                
        except Exception:
            with escort:
                print(f"\n{b}{thomas}")


for _ in range(30):
    threading.Thread(target=porno,daemon=True).start()
while True:
    time.sleep(1)
