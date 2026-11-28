# PYTHON ....
# Telegram : @yy_100k - @zizfif
# instagram : ****
# Codeder : ابن بابل

#ركز 👇 

# هذه الاداة مجانية وليست للبيع الرجاء عدم بيعها ..
# عدم ازالة الحقوق تقديرا لتعبنا وجعلنا نستمر في تقديم مثل هكذا (ادوات او بوتات)..
# نحن مصدر الاساسي لبرمجه : @yy_100k
#==========================#

import requests
import random
import threading
import time
import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

DEV = '@zizfif'
CHANNEL = '@yy_100k'

hit = 0
bad = 0
insta_good = 0
check = 0
lock = threading.Lock()
stop_flag = False

VALID_VIP_CODES = ["VIP-lNS-XXX"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    logo = f"""
{Fore.CYAN}{Style.BRIGHT}
╔══════════════════════════════════════╗
║     INSTAGRAM + hi2.in CHECKER       ║
║          Advanced Edition             ║
╚══════════════════════════════════════╝
{Fore.YELLOW}
    ██╗███╗   ██╗███████╗████████╗ █████╗ 
    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗
    ██║██╔██╗ ██║███████╗   ██║   ███████║
    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║
    ██║██║ ╚████║███████║   ██║   ██║  ██║
    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
{Style.RESET_ALL}
{Fore.GREEN}Developer: {DEV} | Channel: {CHANNEL}{Style.RESET_ALL}
"""
    print(logo)

def show_disclaimer():
    clear_screen()
    print_logo()
    print(f"{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}⚠️  سياسة الاستخدام والموافقة ⚠️{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}")
    print("1. هذا البرنامج مخصص للأغراض التعليمية فقط.")
    print("2. يمنع استخدامه في البيع أو إعادة التوزيع بدون إذن.")
    print("3. انتهاك حقوق النشر محظور تمامًا.")
    print("4. استخدامك لهذا البرنامج يعني موافقتك على هذه الشروط.")
    print("5. المطور غير مسؤول عن أي استخدام غير قانوني.")
    print(f"{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}")
    choice = input(f"{Fore.CYAN}هل توافق على الشروط؟ (اكتب 'نعم' للمتابعة): {Style.RESET_ALL}").strip()
    if choice.lower() not in ['نعم', 'yes', 'y']:
        print(f"{Fore.RED}تم رفض الشروط. الخروج...{Style.RESET_ALL}")
        sys.exit(0)

def verify_vip_code():
   
    clear_screen()
    print_logo()
    print(f"{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🔑 الدخول مقتصر على حاملي كود VIP 🔑{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}")
    code = input(f"{Fore.GREEN}الرجاء إدخال الكود : {Style.RESET_ALL}").strip()
    if code in VALID_VIP_CODES:
        print(f"{Fore.GREEN}✅ الكود صحيح جارِ التحميل...{Style.RESET_ALL}")
        time.sleep(1)
        return True
    else:
        print(f"{Fore.RED}❌ الكود غير صحيح لا يمكنك الدخول.{Style.RESET_ALL}")
        return False

def get_credentials():
    global tok, id
    print(f"{Fore.YELLOW}الرجاء إدخال بيانات المطلوبه:{Style.RESET_ALL}")
    tok = input(f"{Fore.GREEN}توكن البوت: {Style.RESET_ALL}").strip()
    id = input(f"{Fore.GREEN}ايدي حسابك : {Style.RESET_ALL}").strip()
    if not tok or not id:
        print(f"{Fore.RED}البيانات غير صحيحة الخروج...{Style.RESET_ALL}")
        sys.exit(1)

def solve_recaptcha():
    try:
        anchor_url = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct&co=aHR0cHM6Ly9oaTIuaW46NDQz&hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&size=invisible"
        params = anchor_url.split('?')[1]
        r = requests.get(f'https://www.google.com/recaptcha/enterprise/anchor?{params}', timeout=10)
        token = r.text.split('recaptcha-token" value="')[1].split('"')[0]
        payload = (
            f"v={params.split('v=')[1].split('&')[0]}"
            f"&reason=q&c={token}"
            f"&k=6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct"
            f"&co=aHR0cHM6Ly9oaTIuaW46NDQz&hl=en&size=invisible"
        )
        headers = {
            "User-Agent": generate_user_agent(),
            "Referer": f"https://www.google.com/recaptcha/enterprise/anchor?{params}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        resp = requests.post(
            'https://www.google.com/recaptcha/enterprise/reload',
            data=payload,
            headers=headers,
            timeout=10
        )
        return resp.text.split('resp","')[1].split('"')[0]
    except Exception:
        return None

def generate_user_agent():
    return random.choice([
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
    ])

def check_hi2(email_prefix):
    solve = solve_recaptcha()
    if not solve:
        return None
    data = {
        'domain': "@hi2.in",
        'prefix': email_prefix,
        'recaptcha': solve,
    }
    headers = {
        'User-Agent': generate_user_agent(),
        'Accept': "application/json, text/plain, */*",
        'authorization': "Basic bnVsbA==",
    }
    try:
        response = requests.post("https://hi2.in/api/custom", data=data, headers=headers, timeout=10)
        result = response.json()
        if "error" in result:
            return False
        else:
            return True
    except Exception:
        return None

def check_instagram(email):
    url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
    headers = {
        'user-agent': generate_user_agent(),
        'x-csrftoken': 'PI-elia_elia',
    }
    data = {'email': email}
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        text = response.text
        if 'email_is_taken' in text:
            return True
        else:
            return False
    except Exception:
        return None

def send_telegram(email):
    try:
        msg = f"""
{Fore.CYAN}════════════════════════════{Style.RESET_ALL}
{Fore.GREEN}✅ HIT INSTAGRAM ✅{Style.RESET_ALL}
{Fore.CYAN}════════════════════════════{Style.RESET_ALL}

{Fore.YELLOW}📧 EMAIL:{Style.RESET_ALL} {email}

{Fore.MAGENTA}👨‍💻 DEV : {DEV}{Style.RESET_ALL}
{Fore.BLUE}📢 CHANNEL : {CHANNEL}{Style.RESET_ALL}
{Fore.CYAN}════════════════════════════{Style.RESET_ALL}
"""
        clean_msg = msg.replace(Fore.GREEN, '').replace(Fore.CYAN, '').replace(Fore.YELLOW, '').replace(Fore.MAGENTA, '').replace(Fore.BLUE, '').replace(Style.RESET_ALL, '')
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={clean_msg}", timeout=5)
    except:
        pass

def generate_username():
    return ''.join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=5))

def print_status():
    status = f"""
{Fore.CYAN}╔{'═'*50}╗{Style.RESET_ALL}
{Fore.CYAN}║{Style.RESET_ALL} {Fore.WHITE}الحالة الحالية:{Style.RESET_ALL}                               {Fore.CYAN}║{Style.RESET_ALL}
{Fore.CYAN}║{Style.RESET_ALL} {Fore.GREEN}✅ HIT:{Style.RESET_ALL} {hit}                                      {Fore.CYAN}║{Style.RESET_ALL}
{Fore.CYAN}║{Style.RESET_ALL} {Fore.YELLOW}📸 INSTA_GOOD:{Style.RESET_ALL} {insta_good}                             {Fore.CYAN}║{Style.RESET_ALL}
{Fore.CYAN}║{Style.RESET_ALL} {Fore.RED}❌ BAD:{Style.RESET_ALL} {bad}                                       {Fore.CYAN}║{Style.RESET_ALL}
{Fore.CYAN}║{Style.RESET_ALL} {Fore.BLUE}🔄 CHECK:{Style.RESET_ALL} {check}                                    {Fore.CYAN}║{Style.RESET_ALL}
{Fore.CYAN}║{Style.RESET_ALL} {Fore.MAGENTA}👨‍💻 DEV: {DEV}{Style.RESET_ALL}                          {Fore.CYAN}║{Style.RESET_ALL}
{Fore.CYAN}╚{'═'*50}╝{Style.RESET_ALL}
"""
    sys.stdout.write("\033[K")
    sys.stdout.write(status)
    sys.stdout.flush()

def worker():
    global hit, bad, insta_good, check, stop_flag
    while not stop_flag:
        username = generate_username()
        email = username + "@hi2.in"
        
        with lock:
            check += 1
        
        insta_result = check_instagram(email)
        
        if insta_result is None:
            with lock:
                bad += 1
            if not stop_flag:
                print(f"\n{Fore.RED}⚠️  يرجى تفعيل VPN (تم اكتشاف حظر محتمل){Style.RESET_ALL}")
                time.sleep(2)
        elif insta_result:
            with lock:
                insta_good += 1
            
            hi2_result = check_hi2(username)
            
            if hi2_result is None:
                with lock:
                    bad += 1
            elif hi2_result:
                with lock:
                    hit += 1
                print(f"\n{Fore.GREEN}✅ HIT: {email}{Style.RESET_ALL}")
                with open("vip_Hits.txt", "a") as f:
                    f.write(f"{email}\n")
                send_telegram(email)
        else:
            with lock:
                bad += 1
        
        with lock:
            print_status()

def main():
    global stop_flag
    show_disclaimer()
    
   
    if not verify_vip_code():
        input(f"{Fore.RED}اضغط Enter للخروج...{Style.RESET_ALL}")
        sys.exit(1)
    
    get_credentials()
    
    clear_screen()
    print_logo()
    print(f"{Fore.GREEN}بدء الفحص... اضغط Ctrl+C للإيقاف.{Style.RESET_ALL}\n")
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_flag = True
        print(f"\n\n{Fore.YELLOW}جارِ الإيقاف...{Style.RESET_ALL}")
        time.sleep(1)
        clear_screen()
        print_logo()
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}النتائج النهائية:{Style.RESET_ALL}")
        print_status()
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}شكراً لاستخدامك الأداة!{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    main()
