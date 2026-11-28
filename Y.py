#!/usr/bin/env python3
# PYTHON ....
# Telegram : @yy_100k - @zizfif
# Codeder : ابن بابل
# CHECKER VIP - launcher
#==========================#

import json
import os
import sys
import time

import importlib
import subprocess


def ensure_package(module_name, pip_name=None):
    pip_name = pip_name or module_name
    try:
        return importlib.import_module(module_name)
    except ImportError:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", pip_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except Exception:
            print(f"pip install {pip_name}")
            sys.exit(1)
        try:
            return importlib.import_module(module_name)
        except ImportError:
            print(f"pip install {pip_name}")
            sys.exit(1)


requests = ensure_package("requests")


API_BASE = "http://185.77.96.1:5000"
CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".gg_hotmail_config.json")


class C:
    RST = "\033[0m"
    B = "\033[1m"
    RED = "\033[91m"
    GRN = "\033[92m"
    YEL = "\033[93m"
    CYN = "\033[96m"
    WHT = "\033[97m"
    GRY = "\033[90m"
    GOLD = "\033[38;5;220m"
    GOLD_HI = "\033[38;5;226m"


def cp(text=""):
    sys.stdout.write(str(text) + "\n")
    sys.stdout.flush()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def load_config():
    try:
        with open(CONFIG_PATH, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def save_config(**updates):
    cfg = load_config()
    cfg.update(updates)
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as fh:
            json.dump(cfg, fh, ensure_ascii=False, indent=2)
    except Exception:
        pass


def _json(resp):
    try:
        return resp.json()
    except Exception:
        return {}


def check_status(uid):
    try:
        r = requests.get(f"{API_BASE}/api/status", headers={"X-User-ID": uid}, timeout=15)
    except requests.RequestException:
        return "network", {}
    data = _json(r)
    if r.status_code != 200:
        return "invalid", data
    if data.get("is_banned"):
        return "banned", data
    if data.get("expired"):
        return "expired", data
    return "ok", data


def activate(code):
    try:
        r = requests.post(f"{API_BASE}/api/activate", json={"code": code}, timeout=20)
    except requests.RequestException:
        return "network", {}
    return r.status_code, _json(r)


def fetch_ui(uid):
    try:
        r = requests.get(f"{API_BASE}/api/client",
                         headers={"X-User-ID": uid}, timeout=30)
    except requests.RequestException:
        return "network", ""
    if r.status_code == 200 and r.text.strip():
        return "ok", r.text
    return "denied", ""


def connection_gate():
    cp(f"  {C.RED}❌ تعذر الاتصال بالسيرفر / Cannot reach the server{C.RST}")
    cp(f"  {C.YEL}1{C.RST} {C.CYN}◀{C.RST} {C.WHT}إعادة المحاولة{C.RST}")
    cp(f"  {C.YEL}2{C.RST} {C.CYN}◀{C.RST} {C.WHT}خروج{C.RST}")
    ch = input(f"  {C.CYN}➤{C.RST} ").strip()
    return ch != "2"


def activation_flow():
    cp()
    cp(f"  {C.GOLD_HI}{C.B}CHECKER VIP{C.RST}")
    cp(f"  {C.GRY}{'─' * 30}{C.RST}")
    cp(f"  {C.WHT}أدخل كود الاشتراك / Enter subscription code{C.RST}")
    for _ in range(20):
        code = input(f"  {C.GOLD}➤{C.RST} ").strip()
        if not code:
            continue
        sc, data = activate(code)
        if sc == "network":
            if not connection_gate():
                return None
            continue
        if sc == 200 and data.get("user_id"):
            save_config(user_id=data["user_id"])
            end = str(data.get("end") or data.get("end_date") or "")[:10]
            cp(f"  {C.GRN}✔ تم التفعيل / Activated{C.RST} {C.GRY}{end}{C.RST}")
            return data["user_id"]
        cp(f"  {C.RED}✘ {data.get('error', 'كود غير صالح / Invalid code')}{C.RST}")
    return None


def main():
    uid = load_config().get("user_id") or None

    if uid:
        state, data = check_status(uid)
        if state == "banned":
            cp(f"  {C.RED}🚫 حسابك محظور: {data.get('ban_reason') or ''}{C.RST}")
            return
        if state == "network":
            if not connection_gate():
                return
            return main()
        if state != "ok":
            uid = None

    if not uid:
        uid = activation_flow()
        if not uid:
            return

    for _ in range(3):
        state, ui = fetch_ui(uid)
        if state == "ok":
            break
        if state == "network":
            if not connection_gate():
                return
            continue
        cp(f"  {C.RED}✘ الاشتراك غير صالح أو منتهي / Subscription invalid or expired{C.RST}")
        uid = activation_flow()
        if not uid:
            return
    else:
        return

    try:
        code = compile(ui, "<checker-vip>", "exec")
    except SyntaxError:
        cp(f"  {C.RED}✘ تعذر عرض الأداة يرجى مراسلة الدعم الفني @zizfif{C.RST}")
        return

    env = {"__name__": "__main__", "BOOTSTRAP_API": API_BASE}
    exec(code, env)


if __name__ == "__main__":
    try:
        clear_screen()
        main()
    except KeyboardInterrupt:
        cp()
        cp(f"  {C.GRY}تم الإيقاف / Stopped{C.RST}")
