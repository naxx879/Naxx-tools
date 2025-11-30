import sys
import subprocess
import os
from colorama import Fore
import utils

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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    utils.set_title("NAXTOOLS")
    utils.clear_screen()
    print(Fore.RED + utils.logo)
    print(Fore.RED + utils.creator.center(utils.largeur))
    print("\n[1] IP Lookup")
    print("[2] Webhook Spammer")
    print("[3] Show HWID")
    print("[4] Discord Dm spammer")
    print("")

    x = input("Option : ")

    if x == "1":
        subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "ip_lookup.py")])

    elif x == "2":
        subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "webhook_spammer.py")])

    elif x == "3":
        subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "hwid_tool.py")])

    elif x == "4":
        subprocess.run([sys.executable, os.path.join(SCRIPT_DIR, "dm_spammer.py")])


    else:
        utils.clear_screen()
        print(Fore.RED + "Option invalide\n")
        input("Press enter to return...")
