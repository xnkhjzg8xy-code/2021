import webbrowser
webbrowser.open('https://t.me/pytho2n')
import os, sys, re, json, string, random, hashlib, uuid, time, gzip, secrets, asyncio, urllib3
import requests, aiohttp
from datetime import datetime
from threading import Thread
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange, randint, choices
from colorama import Fore, Style, init
from secrets import token_hex
import cfonts
from cfonts import render, say
from bs4 import BeautifulSoup
import cloudscraper
from urllib.parse import urlencode
import yt_dlp
from concurrent.futures import ThreadPoolExecutor

os.system("pip install --upgrade aras1")
import aras1


try:
    from MedoSigner import Argus, Gorgon, md5, Ladon
    import binascii
except:
    os.system("pip install requests uuid MedoSigner pycryptodome 2>/dev/null")
    from MedoSigner import Argus, Gorgon, md5, Ladon
    import binascii

os.system('cls' if os.name == 'nt' else 'clear')


G1 = '\x1b[38;5;22m'
G2 = '\x1b[38;5;28m'
G3 = '\x1b[38;5;34m'
G4 = '\x1b[38;5;40m'
G5 = '\x1b[38;5;46m'
G6 = '\x1b[38;5;76m'
G7 = '\x1b[38;5;82m'
G8 = '\x1b[38;5;118m'
G9 = '\x1b[38;5;154m'
G10 = '\x1b[38;5;190m'
G11 = '\x1b[38;5;48m'
G12 = '\x1b[38;5;83m'
G13 = '\x1b[38;5;84m'
G14 = '\x1b[38;5;85m'
G15 = '\x1b[1;32m'
reset = "\033[0m"
a50 = '\x1b[38;5;196m'
J = G10   
a1 = G2
a2 = G3
a3 = G4
a4 = G5
a5 = G6
a6 = G8
a7 = G9
a8 = G2
a9 = G10
a10 = G3
a11 = G1
a12 = G12
a13 = G11
a14 = G13
a15 = G3
a16 = G7
a17 = G8
a18 = G2
a19 = G4
a20 = G10
a21 = G9
a22 = G12
a23 = G5
a24 = G3
a25 = G2
a26 = G11
a27 = G13
a28 = G1
a29 = G14
a30 = G15
a31 = G4
a32 = G8
a33 = G6
a34 = G12
a35 = G10
a36 = G5
a37 = G7
a38 = G3
a39 = G9
a40 = G11

aras1.arasTik()
TOKEN = input(f' {G6} ​𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧  {G6}: ' + str(G5))
ID = input(f' {G6} ​𝐄𝐧𝐭𝐞𝐫 𝐈𝐃  {G6} :  ' + str(G5))
webbrowser.open('https://t.me/pytho2n')
os.system('cls' if os.name == 'nt' else 'clear')



def aras12(mail):
    try:
        url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
        headers = {
            'X-Csrftoken': secrets.token_hex(16),
            'User-Agent': generate_user_agent(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/accounts/signup/email/',
        }
        data = {'email': mail}
        res = requests.post(url, headers=headers, data=data, timeout=10).text
        return "email_is_taken" in res
    except:
        return False

def aras13(fr):
    try:
        url = "https://www.instagram.com/async/wbloks/fetch/"
        def ua(): return generate_user_agent()
        params = {
            'appid': "com.bloks.www.caa.ar.search.async",
            'type': "action",
            '__bkv': "cc4d2103131ee3bbc02c20a86f633b7fb7a031cbf515d12d81e0c8ae7af305dd"
        }
        payload = {
            '__d': "www", '__user': "0", '__a': "1", '__req': "9",
            '__hs': "20475.HYP:instagram_web_pkg.2.1...0", 'dpr': "3",
            '__ccg': "GOOD", '__rev': "1032300900", '__s': "nrgu8k:vm015z:oanvx6",
            '__hsi': "7598106668658828571", '__dyn': "7xeUjG1mxu1syUbFp41twpUnwgU29zEdEc8co2qwJw5ux609vCwjE1EE2Cw8G1Qw5Mx62G3i1ywOwv89k2C1Fwc60D82Ixe0EUjwGzEaE2iwNwmE2eUlwhEe87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK1sAwHxW1owLwHwGwa6byohw5yweu",
            '__csr': "gLff3k5T92cDYAyT4Wkxh5bGhjehqjDVuhUCUya8u889hp8ydihrghXG9yGxGm2m9Gu59rxd0KAzy29oKbyUqxyfxOm7VEWfxDKiGgS4Uf98iJ0zGcKEqz89U5G4ry88bxqfzE9UeEGfw34U01oL8dHK0cvN00pOwywQV9o1uO00LYwcjw7Tgvg6Je1rwko2xDg19o68wgwGoaUiw7to66UjgmRw3MXw0yqw0sO8092U0myw",
            '__hsdp': "n0I43m1iQhGIiFckEKrBZvIj2SKUl8FeSE9Q08xyoC0x80sAw1TK0GU3xU1jE31w9y095waN04Uw",
            '__hblp': "0dO0Coco1ME884u9wcC2t0lUbo22wzx61mDw5Pw4OwsoboK0sm0FE620cizU5W0bAz8W0wEGuq08Owc60C80xu2S0H40jy1dwDzo2Ow61w",
            '__sjsp': "n0I43m1iQhGIiFckEKrBZvIRh4rHK5iaqSE0AG9yo",
            '__comet_req': "7", 'lsd': "AdJv3Nfv2cg", 'jazoest': "2958",
            '__spin_r': "1032300900", '__spin_b': "trunk", '__spin_t': "1769072066",
            '__crn': "comet.igweb.PolarisWebBloksAccountRecoveryRoute",
            'params': "{\"params\":\"{\\\"server_params\\\":{\\\"event_request_id\\\":\\\"3a359125-0214-4c12-9516-8779938e6188\\\",\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"INTERNAL__latency_qpl_instance_id\\\":\\\"47361890900104\\\",\\\"device_id\\\":\\\"\\\",\\\"family_device_id\\\":null,\\\"waterfall_id\\\":\\\"69517426-942a-45d2-8ac7-e4f11a60412a\\\",\\\"offline_experiment_group\\\":null,\\\"layered_homepage_experiment_group\\\":null,\\\"is_platform_login\\\":0,\\\"is_from_logged_in_switcher\\\":0,\\\"is_from_logged_out\\\":0,\\\"access_flow_version\\\":\\\"pre_mt_behavior\\\",\\\"context_data\\\":\\\"Ac_RWrril-QBHwJ5esJkO0r_7Q6DijxM0ntnpV72Xwb9pwsT_1irnjiemlrD4UrE8SZUidlwtGeIAdKnN9x0Yt2xwljNTR9nNNdvl5IBdQTVzfy-m4keAoyj2DJC0XaijIwHZoblRGk2SZCZqPZ2356akgjRVowNkYgDbwOOxTdeBRyLAz7akj7KXpnBIRKbYdGn7zGOhcNzNlMwLmfvjOpjevZSZ-fPAgKvYAqbbU1igFi7kJW7Lmz8ltK5l-jl6iabxQzMgtEi-Nll6Apb4I-H_6OqU1x7ckCuv-pKy_oPMRzNgvz2omC1ELg5fb6FearpkUsZyWEjsFgUGhmkz-WLIA8CNBXJ10VAC1ypksrM6RXfzZKJqtz569eaxG-dw9FLpDJX0-_wgFqzqYKWtJIdB_GZXwpLD2VLOd-aXfHN0SWjWSI|arm\\\"},\\\"client_input_params\\\":{\\\"zero_balance_state\\\":null,\\\"search_query\\\":\\\"f{1453}\\\",\\\"fetched_email_list\\\":[],\\\"fetched_email_token_list\\\":{},\\\"sso_accounts_auth_data\\\":[],\\\"sfdid\\\":\\\"\\\",\\\"text_input_id\\\":\\\"7tzaot:101\\\",\\\"encrypted_msisdn\\\":\\\"\\\",\\\"headers_infra_flow_id\\\":\\\"\\\",\\\"was_headers_prefill_available\\\":0,\\\"was_headers_prefill_used\\\":0,\\\"ig_oauth_token\\\":[],\\\"android_build_type\\\":\\\"\\\",\\\"is_whatsapp_installed\\\":0,\\\"device_network_info\\\":null,\\\"accounts_list\\\":[],\\\"is_oauth_without_permission\\\":0,\\\"search_screen_type\\\":\\\"email_or_username\\\",\\\"ig_vetted_device_nonce\\\":\\\"\\\",\\\"gms_incoming_call_retriever_eligibility\\\":\\\"client_not_supported\\\",\\\"auth_secure_device_id\\\":\\\"\\\",\\\"network_bssid\\\":null,\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\"},\\\"aac\\\":\\\"\\\"}}\"}"
        }
        headers = {
            'User-Agent': ua(), 'Accept-Encoding': "gzip, deflate, br, zstd",
            'origin': "https://www.instagram.com", 'referer': "https://www.instagram.com/accounts/password/reset/",
            'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7", 'priority': "u=1, i",
            'Cookie': "ig_did=886A3671-95EB-4016-9618-6504E3C60311; mid=aV938wABAAGNLqQD0prSU56ivhek; csrftoken=3xQbJVCm8wRdlSXKaXxztd; datr=HXhfaRa1lVxxpoC1K89YyZiA; ig_nrcb=1; wd=406x766"
        }
        fff = payload["params"]
        fff = fff.replace("f{1453}", fr)
        payload["params"] = fff
        response = requests.post(url, params=params, data=payload, headers=headers, timeout=15)
        data = response.content
        try: data = gzip.decompress(data)
        except: pass
        try: data = brotli.decompress(data)
        except: pass
        r = data.decode("utf-8", errors="ignore")
        if response.status_code == 200:
            return "No"
        else:
            return "Yes"
    except:
        return "Error"

aras5 = 0
aras6 = 0
aras7 = 0
aras8 = 0
aras9 = 0
aras10 = {}
aras11 = '@gmail.com'

def aras14():
    os.system('clear')
    output = f"""
{a36}══════˛ 𝗜𝗡𝗦𝗧𝗔 .══════ 
{a3}True : {a4}{aras6} 
{Z}Not : {a5}{aras7} 
{X}False : {a6}{aras8} 
\033[1;32mGood : {a7}{aras9} 
{a40}Dev : @W4_M4
{a36}══════˛ 𝗜𝗡𝗦𝗧𝗔 .══════ 
"""
    sys.stdout.write(output)
    sys.stdout.flush()



def aras15(pool, mn, mx):
    try:
        if mx < mn:
            mn, mx = mx, mn
        if mn < 1:
            mn = 1
            mx = max(mx, 1)
        length = randint(mn, mx)
        return ''.join(choice(pool) for _ in range(length))
    except:
        return ''.join(choice(pool) for _ in range(5))

def aras16():
    try:
        _n1 = aras15(string.ascii_lowercase, 6, 9)
        _n2 = aras15(string.ascii_lowercase, 3, 9)
        _host = aras15(string.ascii_lowercase, 15, 30)
        _h1 = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'User-Agent': str(generate_user_agent()),
        }
        _url1 = 'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB'
        _r1 = requests.get(_url1, headers=_h1, timeout=15)
        _tok = re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', _r1.text).group(2)
        _h2 = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'User-Agent': generate_user_agent(),
        }
        _payload = {
            'f.req': f'["{_tok}","{_n1}","{_n2}","{_n1}","{_n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        _res = requests.post('https://accounts.google.com/_/signup/validatepersonaldetails', cookies={'__Host-GAPS': _host}, headers=_h2, data=_payload, timeout=15)
        _tl = str(_res.text).split('",null,"')[1].split('"')[0]
        _gaps = _res.cookies.get_dict()['__Host-GAPS']
        with open('InstaTool Token File.txt', 'w') as _f:
            _f.write(f"{_tl}//{_gaps}\n")
        return True
    except Exception as e:
        with open('InstaTool Token File.txt', 'w') as _f:
            _f.write("dummy_token//dummy_gaps")
        return False

def aras17():
    try:
        aras16()
    except Exception as e:
        with open('InstaTool Token File.txt', 'w') as f:
            f.write("dummy_token//dummy_gaps")



def aras18():
    with open('InstaTool Token File.txt', 'r') as _f:
        _raw = _f.read().splitlines()[0]
    return _raw.split('//')

def aras19(tl):
    return {
        'authority': 'accounts.google.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com', 'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}',
        'User-Agent': generate_user_agent(),
    }

def aras20(tl, username):
    return (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
            f"&f.req=%5B%22TL%3A{tl}%22%2C%22{username}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
            f"&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
            f"&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
            f"%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
            f"&gmscoreversion=undefined&flowName=GlifWebSignIn&")

def aras21(email):
    global aras8, aras6
    try:
        _user = email.split('@')[0] if '@' in email else email
        _tl, _host = aras18()
        _res = pp('https://accounts.google.com/_/signup/usernameavailability', params={'TL': _tl}, cookies={'__Host-GAPS': _host}, headers=aras19(_tl), data=aras20(_tl, _user))
        if '"gf.uar",1' in _res.text:
            aras6 += 1
            aras14()
            _full = _user + '@gmail.com'
            _uname, _domain = _full.split('@')
            aras25(_uname, _domain)
        else:
            aras8 += 1
            aras14()
    except:
        pass

def aras22(email):
    global aras9, aras7
    try:
        email_exists = aras12(email)
        if email_exists:
            if aras11 in email:
                aras21(email)
            aras9 += 1
            aras14()
        else:
            aras7 += 1
            aras14()
    except:
        aras7 += 1
        aras14()

def aras23(user):
    try:
        reset_info = aras13(user)
        return reset_info
    except:
        return f"Reset Error"

_ID_YEAR_MAP = {1279000:2010, 17750000:2011, 279760000:2012, 900990000:2013, 1629010000:2014, 2500000000:2015, 3713668786:2016, 5699785217:2017, 8597939245:2018, 21254029834:2019}

def aras24(hy):
    try:
        for upper, year in _ID_YEAR_MAP.items():
            if hy <= upper:
                return year
        return 2023
    except:
        pass

def aras25(username, domain):
    global aras5
    account_info = aras10.get(username, {})
    user_id = account_info.get('pk')
    full_name = account_info.get('full_name')
    followers = account_info.get('follower_count')
    following = account_info.get('following_count')
    posts = account_info.get('media_count')
    bio = account_info.get('biography')
    aras5 += 1
    info_text = f"""
{a36}═══════˛ 𝗜𝗡𝗦𝗧𝗔 .═══════
☀ Hit      : {aras5}
☀ Name     : {full_name}
☀ Uid      : {user_id}
☀ Username : @{username}
☀ Email    : {username}@{domain}
☀ Followers: {followers}
☀ Following: {following}
☀ Posts    : {posts}
☀ Bio      : {bio}
☀ Url      : instagram.com/{username}
☀ Dev      : @W4_M4 ¦ 𝐀𝐑𝐀𝐒
☀ Ch       : https://t.me/pytho2n
{a36}═══════˛ 𝗜𝗡𝗦𝗧𝗔 .═══════
"""
    with open('instahitsaras.txt', 'a') as f:
        f.write(info_text + "\n")
    try: 
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except: 
        pass



def arasss3():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    _ml_session = input(f' {a4}({a4}•{a4}) {a4}  𝐒𝐞𝐬𝐬𝐢𝐨𝐧  {a4}:   ' + str(a4)).strip()
    _ml_user = input(f' {a4}({a4}•{a4}) {a4}  𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞  {a4}:   ' + str(a4)).strip()
    _ml_cookies = {
        'mid': 'aDO-KQABAAExyfJ_qx07dh6O4k0L', 'datr': 'Kb4zaOZ4X1pBLmcZTU-5XMeg',
        'ig_did': 'F54D16DB-ADB8-4706-B125-DE0F2FCD949D', 'ig_nrcb': '1', 'ps_l': '1', 'ps_n': '1',
        'csrftoken': 'bkfRYesAUiJNlKfj9U6xyyIQ9Q6S5oyX', 'dpr': '3.0585973262786865',
        'sessionid': _ml_session, 'ds_user_id': '75453355788', 'wd': '640x1264',
        'rur': '"FRC\\05475453355788\\0541787174994:01fea41f10db60ac91874e964688de28b728888a4076c25a1af2302d649716bc66bf3fae"',
    }
    _ml_headers = {
        'authority': 'www.instagram.com', 'accept': '*/*', 'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': f'https://www.instagram.com/{_ml_user}/following/', 'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"', 'user-agent': str(generate_user_agent()),
        'x-asbd-id': '359341', 'x-csrftoken': 'bkfRYesAUiJNlKfj9U6xyyIQ9Q6S5oyX', 'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2fqLtpbV0Fzp95nkqXZannApZA7qf8vodtOH7vbV4MdrrF', 'x-requested-with': 'XMLHttpRequest',
        'x-web-session-id': '66x9a9:61wlcg:hcs4or',
    }
    try:
        _ml_res = requests.get('https://www.instagram.com/api/v1/users/web_profile_info/', params={'username': _ml_user}, cookies=_ml_cookies, headers=_ml_headers).json()
        _ml_id = _ml_res['data']['user']['id']
        _ml_total = _ml_res['data']['user']['edge_followed_by']['count']
        print(f'\n{a12} Total Following : {a20}{_ml_total}{a12}\n')
    except:
        print(f'{a1} Error user{reset}')
        return
    _ml_done = 0
    _ml_index = 0
    def _ml_fetch(cursor):
        nonlocal _ml_done, _ml_index
        _ml_data = requests.get(f'https://www.instagram.com/api/v1/friendships/{_ml_id}/following/', params={'count': '12', 'max_id': cursor}, cookies=_ml_cookies, headers=_ml_headers).json()
        while True:
            try:
                _ml_done += 1
                _ml_index += 1
                _uname = _ml_data['users'][_ml_index]['username']
                sys.stdout.write(f'\r {a12}{_ml_done}  –  {a20}{_uname}   ')
                sys.stdout.flush()
                with open('lsta_aras.txt', 'a') as _f:
                    _f.write(f'{_uname}\n')
            except:
                _ml_index = 0
                cursor += 12
                _ml_fetch(cursor)
                if _ml_done == _ml_total:
                    return
    _ml_fetch(cursor=0)

def arasss4():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    _mlr_asa, _mlr_tt = [], 0
    print(f'\n{a12} Save : aras.txt\n')
    async def _mlr_g():
        nonlocal _mlr_tt
        async with aiohttp.ClientSession() as _s:
            while True:
                _kw = ''.join(random.choice(random.choice(['abcdefghijklmnopqrstuvwxyz', 'אבגדהוזחטיכלמנסعפצקרשת', 'αβγδεζηθικλμνξοπρστυφχψω', 'あいうえおかきくけこ', 'กขฃคฅฆงจฉชซ'])) for _ in range(random.randint(4, 8)))
                _h = {'user-agent': generate_user_agent(), 'x-csrftoken': 'mf3zd6qWxnKgh9BaNRI5Ldpms2NrH62X', 'referer': 'https://www.instagram.com/'}
                _d = {'variables': '{"data":{"context":"blended","query":"' + _kw + '","search_surface":"web_top_search"},"hasQuery":true}', 'doc_id': '7935512656557707'}
                try:
                    async with _s.post('https://www.instagram.com/graphql/query', headers=_h, data=_d) as _r:
                        _res = await _r.json()
                        for _i in _res['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']:
                            _u = _i['user']['username']
                            if _u not in _mlr_asa:
                                _mlr_tt += 1
                                _mlr_asa.append(_u)
                                sys.stdout.write(f'\r{a12} {_mlr_tt} - • - {a20}{_u}\x1b[K')
                                sys.stdout.flush()
                                open('aras.txt', 'a').write(_u + '\n')
                except:
                    await asyncio.sleep(0.1)
    async def _mlr_main():
        await asyncio.gather(*[_mlr_g() for _ in range(50)])
    asyncio.run(_mlr_main())

def arasss5():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    def check_user(u):
        try:
            r = requests.get(f'https://www.youtube.com/@{u}', headers={'User-Agent': generate_user_agent()}, timeout=10)
            if r.status_code == 404:
                print(f'{a4}[Hit] @{u}{reset}')
                msg = f"┉┉┉┉┉┉┉ ˛ 𝖠𝖱𝖠𝖲 ˛ ┉┉┉┉┉┉┉\n⌁ 𝐔𝐬𝐞𝐫 : @{u}\n⌁ 𝐏𝐥𝐚𝐭𝐟𝐨𝐫𝐦 : 𝐘𝐨𝐮𝐓𝐮𝐛𝐞\n𝐁𝐲 : @W4_M4 ¦ ArAs\n𝐂𝐡 : @pytho2n\n┉┉┉┉┉┉┉ ˛ 𝖠𝖱𝖠𝖲 ˛ ┉┉┉┉┉┉┉"
                requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': ID, 'text': msg})
            else:
                print(f'{a50}[Bad] @{u}{reset}')
        except:
            pass
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    with ThreadPoolExecutor(max_workers=20) as executor:
        while True:
            u = random.choice(chars[:26]) + ''.join(random.choice(chars) for _ in range(3))
            executor.submit(check_user, u)
            time.sleep(0.01)

def arasss6():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    u = input(f' {G6}({G6}•{G6}) {G5}𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞{G6}: {G4}').strip()
    if not u: return
    h = u if u.startswith('@') else f'@{u}'
    opts = {'quiet': True, 'no_warnings': True, 'extract_flat': True}
    try:
        with yt_dlp.YoutubeDL(opts) as y:
            info = y.extract_info(f"https://www.youtube.com/{h}", download=False)
            name = info.get('channel', 'None')
            subs = info.get('channel_follower_count', 'None')
            videos = info.get('video_count', 'None')
            bio = info.get('description', 'None').split('\n')[0]
            print(f"""
{a36}═══════˛ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 .═══════{reset}
{a4}⌁ 𝐍𝐚𝐦𝐞       : {name}{reset}
{a4}⌁ 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞𝐫𝐬 : {subs}{reset}
{a4}⌁ 𝐋𝐢𝐧𝐤       : https://www.youtube.com/{h}{reset}
{a4}⌁ 𝐕𝐢𝐝𝐞𝐨𝐬      : {videos}{reset}
{a4}⌁ 𝐁𝐢𝐨        : {bio[:50]}{reset}
{a4}⌁ 𝐁𝐲        : @W4_M4 ¦ ArAs
{a4}⌁ 𝐂𝐡        : @pytho2n
{a36}═══════˛ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 .═══════{reset}
""")
    except:
        print(f"\n{a2}- مشكله في جلب المعلومات .{reset}")

def arasss7():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    link = input(f' {G6}({G6}•{G6}) {G5}𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐋𝐢𝐧𝐤{G6}: {G4}').strip()
    if not link: return
    opts = {'format': 'bestvideo', 'outtmpl': '%(title)s.%(ext)s', 'quiet': True, 'no_warnings': True, 'noprogress': True}
    try:
        with yt_dlp.YoutubeDL(opts) as y:
            y.download([link])
        print(f"\n{a4}- تـم تـحـميـل المقطع .{reset}")
    except:
        print(f"\n{a2}- مشكله اثناء التحميل .{reset}")

def arasss8():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    print(f"""
{G10}[{G5}1{G10}] {G12}#_#_#
{G10}[{G5}2{G10}] {G12}#_##
{G10}[{G5}3{G10}] {G12}###_#
""")
    opt = input(f' {G6}({G6}•{G6}) {G6}𝐂𝐡𝐨𝐨𝐬𝐞{G6}:   ' + str(G5)).strip()
    def TikTok(u):
        try:
            h = {"User-Agent": "Mozilla/5.0"}
            res = requests.get(f'https://www.tiktok.com/@{u}', headers=h).text
            if 'webapp.user-detail"' in res:
                print(f"{G2}Bad: {u}")
            else:
                raise Exception
        except:
            print(f"{G5}- Good: {u}")
            msg = f"- {u}\nDev: @W4_M4\nhttps://t.me/pytho2n"
            requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': ID, 'text': msg})
    def gen():
        chars = '1234567890qwertyuiopasdfghjklzxcvbnm'
        while 1:
            c = lambda: random.choice(chars)
            if opt == '1':
                u = f"{c()}_{c()}_{c()}"
            elif opt == '2':
                u = f"{c()}_{c()}{c()}"
            else:
                u = f"{c()}{c()}{c()}_{c()}"
            TikTok(u)
    for _ in range(5):
        Thread(target=gen).start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

def arasss9():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    username = input(f' {G6}({G6}•{G6}) {G5}𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞{G6}: {G4}').replace("@", "").strip()
    def TikTokInfo(user):
        try:
            s = cloudscraper.create_scraper()
            res = s.get(f"https://www.tiktok.com/@{user}", headers={"User-Agent": "Mozilla/5.0"})
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                script = soup.find('script', id='__UNIVERSAL_DATA_FOR_REHYDRATION__')
                if not script:
                    return None
                d = json.loads(script.text)['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
                u, st = d['user'], d['stats']
                hit = st.get('heartCount', 0)
                name = u.get('nickname', 'No Name')
                user_id = u.get('id', 'No ID')
                followers = st.get('followerCount', 0)
                following = st.get('followingCount', 0)
                posts = st.get('videoCount', 0)
                bio = u.get('signature', 'No Bio')
                url = f"tiktok.com/@{user}"
                return f"""
{a36}═══════˛ 𝗧𝗶𝗸𝗧𝗼𝗸 .═══════
☀ Hit      : {hit:,}
☀ Name     : {name}
☀ Uid      : {user_id}
☀ Username : @{user}
☀ Email    : {user}@tiktok.com
☀ Followers: {followers:,}
☀ Following: {following:,}
☀ Posts    : {posts:,}
☀ Bio      : {bio}
☀ Url      : {url}
☀ Dev      : @W4_M4 ¦ 𝐀𝐑𝐀𝐒
☀ Ch       : https://t.me/pytho2n
{a36}═══════˛ 𝗧𝗶𝗸𝗧𝗼𝗸 .═══════"""
        except:
            return None
    info = TikTokInfo(username)
    if info:
        print(info)
    else:
        print(f"\n{G2}- Error .{reset}")

def arasss10():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    link = input(f' {G6}({G6}•{G6}) {G5}𝐓𝐢𝐤𝐓𝐨𝐤 𝐋𝐢𝐧𝐤{G6}: {G4}').strip()
    if not link: return
    try:
        data = requests.get(f'https://tikwm.com/api/?url={link}').json()['data']
        with open(f"tiktok_video_{int(time.time())}.mp4", 'wb') as f:
            f.write(requests.get(data['play']).content)
        print(f"\n{a4}- تـم تـحـميـل المقطع .{reset}")
    except:
        print(f"\n{a2}- مشكله اثناء التحميل .{reset}")

def arasss11():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    bad = 0
    ok = 0
    def sign(params, payload=None, sec_device_id="", cookie=None, aid=1233, license_id=1611921764, sdk_version_str="2.3.1.i18n", sdk_version=2, platform=19, unix=None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload else None
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon": Ladon.encrypt(unix, license_id, aid),"x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)}
    def Info():
        try:
            link = input(f' {G6}({G6}•{G6}) {G5}VIDEO LINK{G6}: {G4}')
            response = requests.get("https://api16-normal-c-alisg.ttapis.com/tiktok/linker/target/get/v1/", params={'url': link, 'iid': str(random.randint(1014, 1016)), 'device_id': str(random.randint(1014, 1016)), 'channel': 'googleplay', 'aid': '1233', 'app_name': 'musical_ly', 'version_code': '310503', 'version_name': '31.5.3', 'device_platform': 'android', 'device_type': 'SM-T505N', 'os_version': '12'}, headers={'User-Agent': 'com.zhiliaoapp.musically/2023105030 (Linux; U; Android 12; ar_EG; SM-T505N; Build/SP1A.210812.016; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)'})
            Video = response.json()['landing_url']
            Username = Video.split("https://www.tiktok.com/@")[1].split("/video")[0]
            idVd = Video.split("/video/")[1].split("?")[0]
            patre = {"Host": "www.tiktok.com", "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8", "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7"}
            tikinfo = requests.get(f'https://www.tiktok.com/@{Username}', headers=patre).text
            getting = tikinfo.split('webapp.user-detail"')[1].split('"RecommendUserList"')[0]
            UserId = getting.split('id":"')[1].split('",')[0]
            return idVd, UserId
        except:
            print(f" {G2}- VPN أو رابط خطأ {reset}")
            return None, None
    idVd, UserId = Info()
    if not idVd:
        return
    def report_thread():
        nonlocal ok, bad
        while True:
            try:
                secret = secrets.token_hex(16)
                cookies = {"passport_csrf_token": secret, "passport_csrf_token_default": secret}
                params = {'report_type': "video", 'object_id': str(idVd), 'owner_id': str(UserId), 'enter_from': "homepage_hot", 'extra_log_params': "{\"last_from_group_id\":\""+str(idVd)+"\",\"is_ecom\":\"0\"}", 'aweme_type': "0", 'group_id': str(idVd), 'is_with_series_anchor': "0", 'is_with_series_bottom_bar': "0", 'is_collection_item': "0", 'collection_id': "0", 'is_intro': "0", 'preview_status': "0", 'play_video_type': "null", 'is_purchased': "0", 'series_category': "0", 'is_series_continuation_play': "0", 'series_enter_entrance': "", 'is_ad': "0", 'is_from_sdp': "0", 'source_author_id': "", 'source_group_id': "", 'series_anchor_type': "", 'source_video_id': "", 'isFirst': "1", 'no_hw': "1", 'report_desc': "", 'uri': "", 'reason': "90087", 'category': "porn", 'request_tag_from': "h5", 'device_platform': "android", 'os': "android", 'ssmix': "a", '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632", 'cdid': str(uuid.uuid4()), 'channel': "googleplay", 'aid': "1233", 'app_name': "musical_ly", 'version_code': "370805", 'version_name': "37.8.5", 'manifest_version_code': "2023708050", 'update_version_code': "2023708050", 'ab_version': "37.8.5", 'resolution': "1080*2220", 'dpi': "440", 'device_type': "Redmi Note 8 Pro", 'device_brand': "Redmi", 'language': "ar", 'os_api': "30", 'os_version': "11", 'ac': "mobile", 'is_pad': "0", 'current_region': "YE", 'app_type': "normal", 'sys_region': "EG", 'last_install_time': "1734850426", 'mcc_mnc': "42103", 'timezone_name': "Asia/Aden", 'residence': "YE", 'app_language': "ar", 'carrier_region': "YE", 'timezone_offset': "10800", 'host_abi': "arm64-v8a", 'locale': "ar", 'ac2': "lte", 'uoo': "1", 'op_region': "YE", 'build_number': "37.8.5", 'region': "EG", 'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1), 'iid': str(random.randint(1, 10**19)), 'device_id': str(random.randint(1, 10**19)), 'openudid': str(binascii.hexlify(os.urandom(8)).decode())}
                m = sign(params=urlencode(params), payload="", cookie=urlencode(cookies))
                headers = {'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 11; ar; Redmi Note 8 Pro; Build/RP1A.200720.011; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)", 'x-tt-referer': "https://www.tiktok.com/falcon/communitysafety/page/reasons/index.html", 'Accept': "application/json, text/plain, */*", 'x-tt-passport-csrf-token': secret, 'content-type': "application/x-www-form-urlencoded", 'x-argus': m["x-argus"], 'x-gorgon': m["x-gorgon"], 'x-khronos': m["x-khronos"], 'x-ladon': m["x-ladon"]}
                response = requests.get(f"https://api16-normal-c-alisg.ttapis.com/aweme/v2/aweme/feedback/?{urlencode(params)}", headers=headers, cookies=cookies).text
                if '"status_code":0' in response:
                    ok += 1
                else:
                    bad += 1
                print(f"\r{G12}OK:{G6}{ok}{G12} | BAD:{G6}{bad}    ", end="")
                time.sleep(random.uniform(3, 7))
            except:
                bad += 1
                print(f"\r{G12}OK:{G6}{ok}{G12} | BAD:{G6}{bad}    ", end="")
                time.sleep(random.uniform(3, 7))
    for _ in range(3):
        Thread(target=report_thread).start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{G12}OK : {G6}{ok}")
        print(f"{G12}BAD : {G6}{bad}")

def arasss12():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    email = input(f' {G6}({G6}•{G6}) {G5}𝐄𝐍𝐓𝐄𝐑 𝐄𝐌𝐀𝐈𝐋{G6}: {G4}')
    url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/"
    params = {
        'passport-sdk-version': "19", 'iid': "7372613882915211014", 'device_id': "7372613015445308933",
        'ac': "wifi", 'channel': "googleplay", 'aid': "1233", 'app_name': "musical_ly", 'version_code': "310503",
        'version_name': "31.5.3", 'device_platform': "android", 'os': "android", 'ab_version': "31.5.3",
        'ssmix': "a", 'device_type': "ART-L29N", 'device_brand': "HUAWEI", 'language': "ar", 'os_api': "29",
        'os_version': "10", 'openudid': "47b07f1a42f3d962", 'manifest_version_code': "2023105030",
        'resolution': "720*1491", 'dpi': "320", 'update_version_code': "2023105030", '_rticket': "1716570582691",
        'is_pad': "0", 'app_type': "normal", 'sys_region': "YE", 'mcc_mnc': "42102", 'timezone_name': "Asia/Aden",
        'carrier_region_v2': "421", 'app_language': "ar", 'carrier_region': "YE", 'ac2': "wifi", 'uoo': "1",
        'op_region': "YE", 'timezone_offset': "10800", 'build_number': "31.5.3", 'host_abi': "arm64-v8a",
        'locale': "ar", 'region': "YE", 'ts': "1716570584", 'cdid': "10f6e4d6-16f9-4a03-a021-4375a1c072c8",
        'support_webview': "1", 'reg_store_region': "ye", 'cronet_version': "2fdb62f9_2023-09-06",
        'ttnet_version': "4.2.152.11-tiktok", 'use_store_region_cookie': "1"
    }
    payload = f"rules_version=v2&account_sdk_source=app&multi_login=1&type=31&email={email}&mix_mode=1"
    headers = {
        'User-Agent': "com.zhiliaoapp.musically/2023105030 (Linux; U; Android 10; ar_YE; ART-L29N; Build/HUAWEIART-L29N; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)",
        'Content-Type': "application/x-www-form-urlencoded", 'sdk-version': "2", 'x-ss-req-ticket': "1716570582694",
        'x-tt-passport-csrf-token': "24a8c5234188c87c654cf17f2ee2dc70", 'passport-sdk-version': "19",
        'x-tt-dm-status': "login=0;ct=1;rt=6", 'x-tt-bypass-dp': "1", 'x-vc-bdturing-sdk-version': "2.3.3.i18n",
        'x-ss-stub': "8CC81EE0FB32631749A8267BEB4F3249", 'x-tt-trace-id': "00-ab947041106650c879cc0a06053304d1-ab947041106650c8-01",
        'x-argus': "43ezL+yAGAg/ntTuU/ujVA8I1E6tQEh2+Ay9fZ8xSJzIxShzJLdOIp1oZSMcTmTd79DKgYvYG3Y6EJHQw0hRl3ptm+MgzlmjKohIZsPGftz0AudftXdILG3SqIRh7R4+Kzs+vcYKR/dal+lnAhKgTRRfxYDDBVHNB7kpiQEOkH915AYJ1uF8qGO3uZTHfElq8kc94HsCZBDWv5ZZ6vOB3hPbgc/dLzjxLir837B5Jpe4OllaKgN3L5v3WC+2JJn/VTMk81UwfNSH8l7p7NnIbXJd6m59h9IFWgomPpqEpOhlu+ROhJuWmJ5FS3lZJrPBK0h3mlYhNJbKxRgIaeylVZkljvuFZ8fwPxvog2U6obOSEXQATIjZMhT+BoSTcvpdGn/P55O9J3IR/0hlDwzx3Sp3/xqsfp8l/QmArv4ha70TG1by0QDdvXAfBzs/JJZQ9qku/JAZnYfgXoPfrhQbdwjJf2Gmj8XphbcKIp/oEUzSOs5Fjc3pbRgfLVBPbTf/0yEVGlwv4VblaBxOsAaqJuRY",
        'x-gorgon': "84040039000073c5d5fa441990245151415451f12ba24072b6e4", 'x-khronos': "1716570578",
        'x-ladon': "DOCmYT1SFgBtXIky8cBH+g/ymcAe+237nMdEAu2IPa2oUq7O",
    }
    session = requests.Session()
    try:
        response = session.post(url, params=params, data=payload, headers=headers)
        if '"status_code":0' in response.text:
            print(f"\n{G5}- Code Sent{reset}")
        else:
            print(f"\n{G2}-  Failed{reset}")
    except:
        print(f"\n{G2}-  Error{reset}")

def arasss13():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    print(f"""
{J}[{a20}𝟏{J}]  {a12}####     
{J}[{a20}𝟐{J}]  {a12}###_     
{J}[{a20}𝟑{J}]  {a12}##_#     
{J}[{a20}𝟒{J}]  {a12}#_##     
{J}[{a20}𝟓{J}]  {a12}_###     
{J}[{a20}𝟔{J}]  {a12}##.##    
{J}[{a20}𝟕{J}]  {a12}###.     
{J}[{a20}𝟖{J}]  {a12}#.#.#    
{J}[{a20}𝟗{J}]  {a12}##_##    
{J}[{a20}𝟏𝟎{J}] {a12}#_#_#    
{J}[{a20}𝟏𝟏{J}] {a12}.####    
{J}[{a20}𝟏𝟐{J}] {a12}####.    
{J}[{a20}𝟏𝟑{J}] {a12}#_#_     
{J}[{a20}𝟏𝟒{J}] {a12}_#_#     
{J}[{a20}𝟏𝟓{J}] {a12}##..#    
{J}[{a20}𝟏𝟔{J}] {a12}#..##    
{J}[{a20}𝟏𝟕{J}] {a12}#_._#    
{J}[{a20}𝟏𝟖{J}] {a12}#.##     
{J}[{a20}𝟏𝟗{J}] {a12}##.#     
{J}[{a20}𝟐𝟎{J}] {a12}#.##_    
""")
    _ui_choice = input(f' {a5}({a5}•{a5}) {a5}𝐂𝐡𝐨𝐨𝐬𝐞{a5}:   ' + str(a4)).strip()
    _ui_hits, _ui_bad = 0, 0
    _ui_chars, _ui_und, _ui_dot = 'abcdefghijklmnopqrstuvwxyz1234567890', '_', '.'
    def _ui_run():
        nonlocal _ui_hits, _ui_bad
        while True:
            c = lambda: random.choice(_ui_chars)
            _pts = {
                '1': f"{c()}{c()}{c()}{c()}", '2': f"{c()}{c()}{c()}{_ui_und}", '3': f"{c()}{c()}{_ui_und}{c()}",
                '4': f"{c()}{_ui_und}{c()}{c()}", '5': f"{_ui_und}{c()}{c()}{c()}", '6': f"{c()}{c()}{_ui_dot}{c()}{c()}",
                '7': f"{c()}{c()}{c()}{_ui_dot}", '8': f"{c()}{_ui_dot}{c()}{_ui_dot}{c()}", '9': f"{c()}{c()}{_ui_und}{c()}{c()}",
                '10': f"{c()}{_ui_und}{c()}{_ui_und}{c()}", '11': f"{_ui_dot}{c()}{c()}{c()}{c()}", '12': f"{c()}{c()}{c()}{c()}{_ui_dot}",
                '13': f"{c()}{_ui_und}{c()}{_ui_und}", '14': f"{_ui_und}{c()}{_ui_und}{c()}", '15': f"{c()}{c()}{_ui_dot}{_ui_dot}{c()}",
                '16': f"{c()}{_ui_dot}{_ui_dot}{c()}{c()}", '17': f"{c()}{_ui_und}{_ui_dot}{_ui_und}{c()}", '18': f"{c()}{_ui_dot}{c()}{c()}",
                '19': f"{c()}{c()}{_ui_dot}{c()}", '20': f"{c()}{_ui_dot}{c()}{c()}{_ui_und}",
            }
            _uname = _pts.get(_ui_choice, f"{c()}{c()}{c()}{c()}")
            try:
                r = requests.get(f"https://www.instagram.com/{_uname}/?__a=1&__d=1", headers={"User-Agent": generate_user_agent()})
                if r.status_code == 200 and 'username' in r.text:
                    _ui_hits += 1
                    msg = f"• ━━━ 𝗜𝗡𝗦𝗧𝗔 𝗨𝗦𝗘𝗥 ━━━ •\n\n-  User → {_uname}\n\n• ━━━━━━━━━━━━━━━ •\nDev : @W4_M4\nch : https://t.me/pytho2n"
                    try:
                        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={msg}")
                    except:
                        pass
                else:
                    _ui_bad += 1
            except:
                _ui_bad += 1
            print(f'\r{a12} Hits: {a20}{_ui_hits} {a12}Bad: {a20}{_ui_bad}', end='')
    for _ in range(20):
        Thread(target=_ui_run).start()

def arasss14():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    u = input(f' {G6}({G6}•{G6}) {G5}𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞{G6}: {G4}').replace("@", "").strip()
    if not u: return
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={u}"
    h = {"user-agent": "Mozilla/5.0", "x-ig-app-id": "936619743392459"}
    try:
        r = requests.get(url, headers=h)
        if r.status_code == 200:
            data = r.json()["data"]["user"]
            n = data["full_name"] if data["full_name"] else data["username"]
            s = data["edge_followed_by"]["count"]
            v = data["edge_owner_to_timeline_media"]["count"]
            b = data["biography"].split('\n')[0] if data["biography"] else "None"
            print(f"""
{a36}═══════˛ 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 .═══════{reset}
{a4}⌁ 𝐍𝐚𝐦𝐞       : {n}{reset}
{a4}⌁ 𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {s:,}{reset}
{a4}⌁ 𝐋𝐢𝐧𝐤       : https://www.instagram.com/{u}{reset}
{a4}⌁ 𝐏𝐨𝐬𝐭𝐬      : {v:,}{reset}
{a4}⌁ 𝐁𝐢𝐨        : {b[:50]}{reset}
{a4}⌁ 𝐁𝐲        : @W4_M4 ¦ ArAs
{a4}⌁ 𝐂𝐡        : @pytho2n
{a36}═══════˛ 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 .═══════{reset}
""")
        else:
            print(f"\n{a2}- مشكله في جلب المعلومات .{reset}")
    except:
        print(f"\n{a2}- مشكله في جلب المعلومات .{reset}")

def arasss15():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    link = input(f' {G6}({G6}•{G6}) {G5}𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐋𝐢𝐧𝐤{G6}: {G4}').strip()
    if not link: return
    opts = {'quiet': True, 'no_warnings': True, 'noprogress': True, 'format': 'best', 'outtmpl': 'insta_video_%(id)s.%(ext)s'}
    try:
        with yt_dlp.YoutubeDL(opts) as y:
            y.download([link])
        print(f"\n{a4}- تـم تـحـميـل المقطع .{reset}")
    except:
        print(f"\n{a2}- مشكله اثناء التحميل .{reset}")

def arasss16():
    urllib3.disable_warnings()
    def _srv_run(end, ext={}):
        try:
            res = requests.get(f'https://leofame.com/ar/{end}').cookies.get_dict()
            url = input(f'\n {a5}({a5}•{a5}) {a4}  Enter {end.split("-")[-1]} Link  {a5}:   ' + str(a4))
            if url:
                data = {'token': res['token'], 'timezone_offset': 'Asia/Baghdad', 'free_link': url, **ext}
                req = requests.post(f'https://leofame.com/ar/{end}?api=1', cookies=res, headers={'user-agent': str(generate_user_agent())}, data=data, verify=False)
                if 'success' in req.text:
                    print(f'\n {a3}[+] Done\n')
                else:
                    print(f'\n {a1}[-] Failed\n')
        except:
            pass
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        aras1.arasTik()
        print(f"""
{J}[{a20}𝟏{J}] {a12}𝐕𝐢𝐞𝐰𝐬     
{J}[{a20}𝟐{J}] {a12}𝐒𝐭𝐨𝐫𝐲 𝐕𝐢𝐞𝐰    
{J}[{a20}𝟑{J}] {a12}𝐒𝐡𝐚𝐫𝐞𝐬    
""")
        _srv_ch = input(f' {a5}({a5}•{a5}) {a5}𝐂𝐡𝐨𝐨𝐬𝐞{a5}:   ' + str(a4)).strip()
        if   _srv_ch == '1': _srv_run('free-instagram-views',       {'quantity': '200', 'speed': '5'})
        elif _srv_ch == '2': _srv_run('free-instagram-story-views')
        elif _srv_ch == '3': _srv_run('free-instagram-shares',      {'quantity': '98',  'speed': '5'})

def arasss17():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    _rp_user = input(f' {a5}({a5}•{a5}) {a4}  𝐔𝐬𝐞𝐫  {a5}:   ' + str(a4)).strip()
    _rp_session = input(f' {a5}({a5}•{a5}) {a4}  𝐒𝐞𝐬𝐬𝐢𝐨𝐧  {a5}:   ' + str(a4)).strip()
    _rp_csrf = token_hex(16)
    _rp_gg = 0
    _rp_bb = 0
    try:
        r = requests.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={_rp_user}", headers={"User-Agent": generate_user_agent(), "x-ig-app-id": "936619743392459"})
        if r.status_code == 200:
            _rp_id = r.json()["data"]["user"]["id"]
        else:
            print(f'{a1}-  Error.{reset}')
            return
        def _rp_get_ua():
            _v = random.choice(['28/9', '29/10'])
            return f'Instagram 16{random.randint(5,8)}.0.0 Android ({_v}; google; Pixel 5)'
        _rp_h = {'authority': 'www.instagram.com', 'content-type': 'application/x-www-form-urlencoded', 'user-agent': _rp_get_ua(), 'x-csrftoken': _rp_csrf, 'x-ig-app-id': '1217981644879628'}
        _rp_k = {'container_module': 'profilePage', 'entry_point': '1', 'location': '2', 'object_id': _rp_id, 'object_type': '5'}
        try:
            _rp_ctx = requests.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', cookies={'sessionid': _rp_session}, headers=_rp_h, data={**_rp_k, 'frx_prompt_request_type': '1'}).json()['response']['context']
        except:
            _rp_ctx = None
            print(f'{a1} Session Error{reset}')
            return
        if _rp_ctx:
            _rp_d = {**_rp_k, 'context': _rp_ctx, 'selected_tag_types': '["prostitution"]', 'action_type': '2', 'frx_prompt_request_type': '2'}
            while True:
                time.sleep(7)
                try:
                    _rp_r = requests.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/', cookies={'sessionid': _rp_session}, headers=_rp_h, data=_rp_d).text
                    if '"status":"ok"' in _rp_r:
                        _rp_gg += 1
                    else:
                        _rp_bb += 1
                    print(f'\r{a12} Done: {a20}{_rp_gg} {a12}| Bad: {a20}{_rp_bb}', end='')
                except:
                    break
    except:
        print(f'{a1}- Error .{reset}')

def arasss18():
    os.system('cls' if os.name == 'nt' else 'clear')
    aras1.arasTik()
    _gs_u = input(f' {a5}({a5}•{a5}) {a4}  𝐔𝐬𝐞𝐫  {a5}:   ' + str(a4)).strip()
    _gs_p = input(f' {a5}({a5}•{a5}) {a4}  𝐏𝐚𝐬𝐬  {a5}:   ' + str(a4)).strip()
    _gs_ua = "Instagram 155.0.0.37.107 Android (24/7.0; 480dpi; 720x1280; Xiaomi; Mi-4c; qcom; en_US)"
    _gs_did = 'android-' + hashlib.md5(_gs_u.encode()).hexdigest()[:16]
    _gs_data = {'guid': '83f2000a-4b95-4811-bc8d-0f3539ef07cf', 'enc_password': f"#PWD_INSTAGRAM:0:{int(time.time())}:{_gs_p}", 'username': _gs_u, 'device_id': _gs_did}
    try:
        _gs_res = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers={'User-Agent': _gs_ua}, data=_gs_data)
        if "two_factor_required" in _gs_res.text:
            _gs_code = input(f' {a5}({a5}•{a5}) {a4}  𝟐𝐅𝐀 𝐂𝐨𝐝𝐞  {a5}:   ' + str(a4)).strip()
            _gs_data.update({'verification_code': _gs_code, 'two_factor_identifier': _gs_res.json()['two_factor_info']['two_factor_identifier']})
            _gs_res = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers={'User-Agent': _gs_ua}, data=_gs_data)
        if "logged_in_user" in _gs_res.text:
            _gs_sid = _gs_res.cookies.get("sessionid")
            print(f'\n{a12} Session : {a20}{_gs_sid}\n')
            with open("session_aras.txt", "a") as _f:
                _f.write(f"{_gs_u}:{_gs_sid}\n")
        else:
            print(f'\n{a1}- Login Erorr .\n')
    except:
        pass


aras1.arasTik()
print(f"""
{G10}[{G5}𝟭{G10}]  {G12}𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 𝐋𝐢𝐬𝐭 𝐈𝐧𝐬𝐭𝐚         {G10}(سحب متابعين انستا)
{G10}[{G5}𝟮{G10}]  {G12}𝐑𝐚𝐧𝐝𝐨𝐦 𝐈𝐧𝐬𝐭𝐚 𝐔𝐬𝐞𝐫𝐬           {G10}(سحب عشوائي انستا)
{G10}[{G5}𝟯{G10}]  {G12}𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐔𝐬𝐞𝐫𝐬                {G10}(صيد يوزرات يوتيوب)
{G10}[{G5}𝟰{G10}]  {G12}𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐈𝐧𝐟𝐨                 {G10}(معلومات يوتيوب)
{G10}[{G5}𝟱{G10}]  {G12}𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝             {G10}(تحميل يوتيوب)
{G10}[{G5}𝟲{G10}]  {G12}𝐓𝐢𝐤𝐓𝐨𝐤 𝐔𝐬𝐞𝐫𝐬                 {G10}(صيد تيك توك)
{G10}[{G5}𝟳{G10}]  {G12}𝐓𝐢𝐤𝐓𝐨𝐤 𝐈𝐧𝐟𝐨                  {G10}(معلومات تيك توك)
{G10}[{G5}𝟴{G10}]  {G12}𝐓𝐢𝐤𝐓𝐨𝐤 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝              {G10}(تحميل تيك توك)
{G10}[{G5}𝟵{G10}]  {G12}𝐓𝐢𝐤𝐓𝐨𝐤 𝐑𝐞𝐩𝐨𝐫𝐭𝐬              {G10}(ابلاغ تيك)
{G10}[{G5}𝟭𝟬{G10}] {G12}𝐓𝐢𝐤𝐓𝐨𝐤 𝐑𝐞𝐬𝐞𝐭                 {G10}(ريست تيك)
{G10}[{G5}𝟭𝟭{G10}] {G12}𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐔𝐬𝐞𝐫𝐬              {G10}(صيد يوزرات انستا بأنماط)
{G10}[{G5}𝟭𝟮{G10}] {G12}𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨               {G10}(معلومات انستا)
{G10}[{G5}𝟭𝟯{G10}] {G12}𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝           {G10}(تحميل انستا)
{G10}[{G5}𝟭𝟰{G10}] {G12}𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐒𝐞𝐫𝐯𝐢𝐜𝐞𝐬           {G10}(خدمات انستا)
{G10}[{G5}𝟭𝟱{G10}] {G12}𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐑𝐞𝐩𝐨𝐫𝐭𝐬            {G10}(ابلاغ انستا)
{G10}[{G5}𝟭𝟲{G10}] {G12}𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧            {G10}(سحب سيشن انستا)
""")

choice = input(f' {G6}({G6}•{G6}) {G6}𝐂𝐡𝐨𝐨𝐬𝐞{G6}:   ' + str(G5)).strip()

if choice == '1':
    arasss3()
elif choice == '2':
    arasss4()
elif choice == '3':
    arasss5()
elif choice == '4':
    arasss6()
elif choice == '5':
    arasss7()
elif choice == '6':
    arasss8()
elif choice == '7':
    arasss9()
elif choice == '8':
    arasss10()
elif choice == '9':
    arasss11()
elif choice == '10':
    arasss12()
elif choice == '11':
    arasss13()
elif choice == '12':
    arasss14()
elif choice == '13':
    arasss15()
elif choice == '14':
    arasss16()
elif choice == '15':
    arasss17()
elif choice == '16':
    arasss18()
else:
    print(f"{a1}- Erorr .")
