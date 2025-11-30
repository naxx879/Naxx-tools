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

def run_hwid_tool():
    utils.clear_screen()
    print(Fore.RED + utils.logo)
    print(Fore.RED + utils.creator.center(utils.largeur))
    print(Fore.RED + "Hardware ID\n")
    print(Fore.RED + "CPU SERIAL")
    print(utils.run_ps("(Get-CimInstance Win32_Processor).ProcessorId"))
    print(Fore.RED + "Disk Serial")
    print(utils.run_ps("(Get-CimInstance Win32_PhysicalMedia | Select-Object -Expand SerialNumber)"))
    print(Fore.RED + "Motherboard Serial")
    print(utils.run_ps("(Get-CimInstance Win32_BaseBoard).SerialNumber"))
    input("Press enter to return...")

if __name__ == "__main__":
    run_hwid_tool()
