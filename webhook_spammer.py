import requests
import time
from colorama import Fore
import utils


def run_webhook_spammer():
    utils.clear_screen()
    print(Fore.RED + utils.logo)
    print(Fore.RED + utils.creator.center(utils.largeur))
    print(Fore.RED + "WEBHOOK SPAMMER\n")
    url = input("URL du Webhook : ")
    message = input("Message : ")
    name = input("Nom du Webhook : ")
    try:
        count = int(input("Nombre de messages à envoyer : "))
    except:
        count = 10

    print("\nMode d'envoi :")
    print("1. Normal (délai configurable)")
    print("2. Turbo (0.5s)")
    print("3. Ultra (0.2s)")
    print("4. Lightning (0.1s)")
    print("5. Tornado (0.05s)")
    mode = input("Choisissez le mode (1-5) [défaut 5] : ") or "5"

    if mode == "1":
        delay = float(input("Délai entre chaque message (en secondes) : "))
    elif mode == "2":
        delay = 0.5
    elif mode == "3":
        delay = 0.2
    elif mode == "4":
        delay = 0.01
    elif mode == "5":
        delay = 0.05
    else:
        delay = 0.05

    print("\nAffichage :")
    print("1. Temps réel")
    print("2. Silencieux")
    display_mode = input("Choisissez l'affichage (1-2) [défaut 2] : ") or "2"

    payload = {"content": message, "username": name}
    headers = {"Content-Type": "application/json"}

    success_count = 0
    failed_count = 0
    session = requests.Session()
    start_time = time.perf_counter()

    for i in range(1, count + 1):
        try:
            r = session.post(url, json=payload, headers=headers, timeout=5)
            if r.status_code == 429:
                retry_after = float(r.headers.get("Retry-After", 1000)) / 1000
                print(f"⚠️ Rate limit ! Attente {retry_after:.2f}s")
                time.sleep(retry_after)
                continue
            if r.status_code < 400:
                success_count += 1
                if display_mode == "1":
                    print(f"✅ Message {i}")
            else:
                failed_count += 1
        except Exception as e:
            failed_count += 1
            if display_mode == "1":
                print(f"❌ Message {i} failed: {e}")
        time.sleep(delay)

    end_time = time.perf_counter()
    print(f"\n✅ Succès: {success_count} | ❌ Échecs: {failed_count}")
    print(f"⏱️ Temps total: {end_time - start_time:.2f}s")
    input("Appuyez sur Entrée pour retourner au menu...")

if __name__ == "__main__":
    run_webhook_spammer()
