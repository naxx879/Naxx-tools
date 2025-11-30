import os
import platform
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

logo = """
 ███▄    █  ▄▄▄      ▒██   ██▒   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
 ██ ▀█   █ ▒████▄    ▒▒ █ █ ▒░   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▓██  ▀█ ██▒▒██  ▀█▄  ░░  █   ░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
▓██▒  ▐▌██▒░██▄▄▄▄██  ░ █ █ ▒    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██░   ▓██░ ▓█   ▓██▒▒██▒ ▒██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒▒ ░ ░▓ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░ ░░   ░ ▒░  ▒   ▒▒ ░░░   ░▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
   ░   ░ ░   ░   ▒    ░    ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
         ░       ░  ░ ░    ░                  ░ ░      ░ ░      ░  ░      ░  
"""

creator = "Creator: Naxx / Yabyxy"

largeur = 80

def is_windows():
    return platform.system().lower().startswith("win")

def clear_screen():
    os.system("cls" if is_windows() else "clear")

def set_title(title):
    if is_windows():
        os.system(f"title {title}")
    else:
        print(f"\33]0;{title}\a", end="", flush=True)

def run_ps(ps_cmd: str) -> str:
    try:
        if is_windows():
            out = subprocess.check_output([
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy", "Bypass",
                "-Command", ps_cmd
            ], stderr=subprocess.STDOUT)
        else:
            if "Win32_Processor" in ps_cmd:
                cmd = "lscpu | grep 'Model name' | awk -F: '{print $2}'"
            elif "Win32_PhysicalMedia" in ps_cmd:
                cmd = "sudo hdparm -I /dev/sda | grep 'Serial Number' || echo 'No Serial'"
            elif "Win32_BaseBoard" in ps_cmd:
                cmd = "sudo dmidecode -s baseboard-serial-number || echo 'Unknown'"
            else:
                cmd = "uname -a"
            out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return out.decode("utf-8", errors="ignore").strip()
    except Exception as e:
        return f"Erreur: {e}"
