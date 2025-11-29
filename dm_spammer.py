import discord
import asyncio
import base64
from colorama import Fore
import utils


def run_discord_dm():
    utils.clear_screen()
    print(Fore.RED + utils.logo)
    print(Fore.RED + utils.creator.center(utils.largeur))
    print(Fore.RED + "Discord DM Spammer\n")
    
    token = "MTQ0NDAyMjI4NzUzODk4MzA5Mw.G6CrST.OwVWRl9-w4cXYXYWVmZ0o738a1oK3pTlQXNe5o"
    
    try:
        bot_id_b64 = token.split(".")[0]
        bot_id_b64 += "=" * ((4 - len(bot_id_b64) % 4) % 4)
        bot_id = base64.b64decode(bot_id_b64).decode("utf-8")
        invite_url = f"https://discord.com/api/oauth2/authorize?client_id=1444022287538983093&permissions=0&scope=bot"
        print(Fore.CYAN + f"🔗 Lien d'invitation du bot : {invite_url}\n")
        print(Fore.YELLOW + "Invitez le bot sur un serveur où se trouve aussi la cible !\n")
    except Exception:
        print(Fore.YELLOW + "Impossible de générer le lien d'invitation (token invalide ?)\n")

    try:
        user_id = int(input("ID de la personne (ID): "))
        message_content = input("Message à envoyer: ")
        count = int(input("Nombre de message a envoyer: "))
        
        intents = discord.Intents.all()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            try:
                user = await client.fetch_user(user_id)
                for i in range(count):
                    await user.send(message_content)
                    print(Fore.GREEN + f"\n✅ Message envoyé à {user.name} ({user.id})")
                    await asyncio.sleep(0.4)
            except discord.Forbidden:
                print(Fore.RED + "\n❌ Impossible d'envoyer le message.")
                print(Fore.RED + "Causes possibles :")
                print(Fore.RED + "1. Le bot et l'utilisateur ne sont sur aucun serveur commun.")
                print(Fore.RED + "2. L'utilisateur a désactivé les DMs.")
                print(Fore.RED + "3. L'utilisateur a bloqué le bot.")
            except discord.NotFound:
                print(Fore.RED + "\n❌ Utilisateur introuvable")
            except Exception as e:
                print(Fore.RED + f"\n❌ Erreur: {e}")
            finally:
                await client.close()

        print(Fore.YELLOW + "\nConnexion en cours...")
        try:
            client.run(token)
        except Exception as e:
            print(Fore.RED + f"\n❌ Erreur de connexion (Token invalide ?): {e}")

    except ValueError:
        print(Fore.RED + "\n❌ ID invalide (doit être un nombre)")
    
    input("\nAppuyez sur Entrée pour retourner au menu...")

if __name__ == "__main__":
    run_discord_dm()
