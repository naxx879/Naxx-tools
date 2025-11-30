import discord
import asyncio
import base64
from colorama import Fore
import utils
import os


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

def run_discord_dm():
    utils.set_title("NAXTOOLS")
    utils.clear_screen()
    print(Fore.RED + utils.logo)
    print(Fore.RED + utils.creator.center(utils.largeur))
    print(Fore.RED + "Discord DM Spammer\n")

    token = " " # Enter a token of your bot here

    try:
        bot_id_b64 = token.split(".")[0]
        bot_id_b64 += "=" * ((4 - len(bot_id_b64) % 4) % 4)
        bot_id = base64.b64decode(bot_id_b64).decode("utf-8")
        invite_url = f""#Enter a invite url of your bot here
        print(Fore.CYAN + f"🔗 Lien d'invitation du bot : {invite_url}\n")
        print(Fore.YELLOW + "Invitez le bot sur un serveur où se trouve aussi la cible !\n")
    except Exception:
        print(Fore.YELLOW + "Impossible de générer le lien d'invitation (token invalide ?)\n")
    
    try:
        user_id = int(input("User ID: "))
        message = input("Message: ")
        count = int(input("Count:"))
        
        intents = discord.Intents.all()
        client = discord.Client(intents=intents)

        @client.event 
        async def on_ready():
            print(f"Logged in as {client.user}")

            try:
                user = await client.fetch_user(user_id)
                for i in range(count):
                    await user.send(message)
                    print(Fore.GREEN + "Message sent successfully")
                    await asyncio.sleep(0.5)
            except discord.Forbidden:
                print(Fore.RED + "Impossible to send a message to this user")
            except discord.NotFound:
                print(Fore.RED + "User not found")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

            await client.close()

        print(Fore.YELLOW + "Connexion en cours...")
        client.run(token)

    except ValueError:
        print(Fore.RED + "Erreur: L'ID doit être un nombre.")
    except Exception as e:
        print(Fore.RED + f"Une erreur est survenue: {e}")

    input(Fore.YELLOW + "\nAppuyez sur Entrée pour retourner au menu...")

if __name__ == "__main__":
    run_discord_dm()
