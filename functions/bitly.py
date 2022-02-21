import os
import bitlyshortener
from dotenv import load_dotenv
load_dotenv()


def bitly():
    print('Shorten your URL by BITLY')

    api_key_bitly = [f"{os.environ.get('API_KEY_BITLY')}"]
    shortener = bitlyshortener.Shortener(tokens=api_key_bitly)

    numbers_urls = str(input('How many urls do you want to shorten? '))

    if numbers_urls == 'exit':
        exit()
    elif numbers_urls.isdigit():
        numbers_urls = int(numbers_urls)

        long_urls = []
        name_urls = []
        id_urls = []

        urls_info = {}

        for i in range(numbers_urls):
            print(i + 1, 'url')
            name = input('Add a url name: ')
            url = input('Add url: ')

            long_urls = shortener.shorten_urls([url])

            urls_info[i] = [{'name': name, 'url': long_urls[0]}]

            long_urls.clear()

            # id_urls.append(i)
            # name_urls.append(name)
            # long_urls.append(url)

            print()

        # long_urls = shortener.shorten_urls(long_urls)

        for id_dict, id_content in urls_info.items():
            for infos in id_content:
                for name_url, url_short in infos.items():
                    print(name_url, url_short)
                    # [] Mostrar o valor de uma forma mais bonitinha hahaha

            # show_id_url = id_urls[i] + 1
            # show_name_url = name_urls[i]
            # show_long_url = long_urls[i]

            # print(f'{show_id_url}) {show_name_url}: {show_long_url}')


# for x, y in thisdict.items():
#     print(x, y)
#     if x == 'year':
#         for i in y:
#             for o, p in i.items():
#                 print(p)
