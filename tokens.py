from functions.clear import clear

clear()
print('Informe os Tokens:')
print('\n')

token_cuttly = input('API KEY CUTTLY \n-->> ')
print()

token_bitly = input('API KEY BITLY \n-->> ')
print()

with open('.env', 'w') as file_env:
    file_env.write(
        f'API_KEY_CUTTLY={token_cuttly}\nAPI_KEY_BITLY={token_bitly}')

print('Arquivo .env criado com sucesso. Agora você pode usar o Your Link sem problemas')
