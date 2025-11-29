import requests
from colorama import Fore
import utils


def run_ip_lookup():
    utils.clear_screen()
    print(Fore.RED + utils.logo)
    print(Fore.RED + utils.creator.center(utils.largeur))
    print(Fore.RED + "IP LOOKUP\n")
    ip = input("Enter IP: ")
    try:
        r = requests.get(f"http://api.ipstack.com/{ip}?access_key=860c8aa4abf83b193c5a902bc056a7c5", timeout=10)
        r.raise_for_status()
        data = r.json()
        
        if 'error' in data and data['error']:
                error_info = data['error'].get('info', 'Erreur inconnue')
                print(Fore.RED + f"Erreur: {error_info}")
        else:
            print("RESULTS\n\n")
            print(Fore.RED + f"Country: {data.get('country_name', 'N/A')}")
            print(Fore.RED + f"City: {data.get('city', 'N/A')}")
            print(Fore.RED + f"Region: {data.get('region_name', 'N/A')}")
            print(Fore.RED + f"Timezone: {data.get('time_zone', {}).get('id', 'N/A')}") 
            print(Fore.RED + f"ISP: {data.get('connection', {}).get('isp', 'N/A')}")
            print(Fore.RED + f"ASN: {data.get('connection', {}).get('asn', 'N/A')}")
            print(Fore.RED + f"Latitude: {data.get('latitude', 'N/A')}")
            print(Fore.RED + f"Longitude: {data.get('longitude', 'N/A')}")
            print(Fore.RED + f"Postal Code: {data.get('zip', 'N/A')}")
            print(Fore.RED + f"Currency: {data.get('currency', {}).get('code', 'N/A')}")
    except Exception as e:
        print(Fore.RED + f"Erreur: {e}")

    input("Press enter to return...")

if __name__ == "__main__":
    run_ip_lookup()
