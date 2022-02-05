import os
import requests
from dotenv import load_dotenv
load_dotenv()


def cuttly():
    print("Shorten your URL by CUTTLY")

    url = input("Add url: ")
    api_key_cuttly = os.environ.get('API_KEY_CUTTLY')
    api_url = f"https://cutt.ly/api/api.php?key={api_key_cuttly}&short={url}"
    data = requests.get(api_url).json()["url"]

    if data["status"] == 7:
        shortened_url = data["shortLink"]
        print("Shortened URL: ", shortened_url)
    else:
        print("[!] Error Shortening URL: ", data)
