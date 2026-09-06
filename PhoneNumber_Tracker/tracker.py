import webbrowser
import requests

def get_location(lat, lng, api_key):
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?q={lat},{lng}&key={api_key}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Vérifie si la requête a réussi
        data = response.json()
        if data.get('results'):
            return data['results'][0]['formatted']
        else:
            return "Adresse introuvable"
    except requests.exceptions.RequestException as e:
        return f"Erreur API: {e}"

def main():
    api_key = 'YOUR_API_KEY'  # Remplace par ta clé OpenCage

    try:
        current_lat = float(input("Entrez votre latitude actuelle: "))
        current_lng = float(input("Entrez votre longitude actuelle: "))
        dest_lat = float(input("Entrez la latitude de destination: "))
        dest_lng = float(input("Entrez la longitude de destination: "))
    except ValueError:
        print("⚠️ Les coordonnées doivent être des nombres valides.")
        return

    current_location = get_location(current_lat, current_lng, api_key)
    dest_location = get_location(dest_lat, dest_lng, api_key)

    print(f"📍 Votre position actuelle: {current_location}")
    print(f"🎯 Destination: {dest_location}")

    maps_url = f"https://www.google.com/maps/dir/{current_lat},{current_lng}/{dest_lat},{dest_lng}"
    print(f"🔗 Itinéraire Google Maps: {maps_url}")
    webbrowser.open(maps_url)

if __name__ == "__main__":
    main()
