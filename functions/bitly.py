import os
import bitlyshortener
from dotenv import load_dotenv
load_dotenv()


def bitly():
    print('Shorten your URL by BITLY')

    api_key_bitly = [f"{os.environ.get('API_KEY_BITLY')}"]
    shortener = bitlyshortener.Shortener(tokens=api_key_bitly)

    numbers_urls = int(input('How many urls do you want to shorten? '))
    long_urls = []
    for i in range(numbers_urls):
        url = input('Add url: ')
        long_urls.append(url)

    long_urls = shortener.shorten_urls(long_urls)

    print(f'Shortened url: {long_urls}')
