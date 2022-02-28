import os
import bitlyshortener
from dotenv import load_dotenv
load_dotenv()


def bitly():
    print('Shorten your URL by BITLY')

    api_key_bitly = [f"{os.environ.get('API_KEY_BITLY')}"]
    shortener = bitlyshortener.Shortener(tokens=api_key_bitly)

    numbers_urls = str(
        input('How many urls do you want to shorten? [1] ')).strip()
    if numbers_urls == '':
        numbers_urls = '1'

    print()

    if numbers_urls == 'exit':
        exit()
    elif numbers_urls.isdigit():
        numbers_urls = int(numbers_urls)

        long_urls = []
        name_urls = []
        id_urls = []

        urls_info = {}

        for i in range(numbers_urls):
            print(f'{i + 1}º url')
            name = input('-->> Add a url name: ')
            url = input('-->> Add url: ')

            long_urls = shortener.shorten_urls([url])

            urls_info[i] = [{'name': name, 'url': long_urls[0]}]

            long_urls.clear()
            print()

        for id_dict, id_content in urls_info.items():
            for infos in id_content:
                for name_url, link in infos.items():
                    print(f'{name_url}: {link}')
