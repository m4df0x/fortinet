import requests
import xml.etree.ElementTree as ET

def check_multiple_firmwares(url: str, current_versions: dict):    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der URL: {e}")
        return

    try:
        root = ET.fromstring(response.content)
    except ET.ParseError as e:
        print(f"Fehler beim Parsen des XML: {e}")
        return

    # Alle Titel aus dem Feed
    titles = [
        item.find('title').text.strip()
        for item in root.findall('./channel/item')
        if item.find('title') is not None
    ]

    # Vergleich pro Produkt
    for product, current_version in current_versions.items():
        # Alle Einträge zu diesem Produkt
        product_versions = [t for t in titles if product in t]

        if not product_versions:
            print(f"{product}: Keine Einträge im Feed gefunden.")
            continue

        if any(current_version in t for t in product_versions):
            print(f"{product}: Alles OK – {current_version} ist aktuell.")
        else:
            print(f"{product}: Neues Update vorhanden!")
            print(f"  Deine Version: {current_version}")
            print("  Verfügbare neuere Versionen:")
            for v in product_versions:
                print(f"   - {v}")

if __name__ == "__main__":
    rss_url = "https://support.fortinet.com/rss/firmware.xml"

    aktuelle_versionen = {
        #"FortiOS": "FortiOS 7.4.3",
        "FortiAnalyzer": "FortiAnalyzer 7.4.2",
        "FortiManager": "FortiManager 7.4.2",
        #"FortiWeb": "FortiWeb 7.4.4",
        #"FortiProxy": "FortiProxy 7.4.4",
        #"FortiMail" : "FortiMail 7.4.3",
        #"FortiAP" : "FortiAP 7.4.4",
        #"FortiExtender" : "FortiExtender 7.4.4",
        #"FortiSwitch" : "FortiSwitch 7.4.4",
        #"FortiAuthenticator" : "FortiAuthenticator 6.6.2",
    }

    check_multiple_firmwares(rss_url, aktuelle_versionen)
