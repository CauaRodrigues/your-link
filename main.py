from functions.clear import clear
from functions.colors import colors as c, your_link
from functions.cuttly import cuttly
from functions.bitly import bitly

clear()
your_link()

print(f'Choose a shortener...\n',
      f'{c["FontRed"]}[1]{c["FontPurple"]} {c["StyleBold"]}CUTTLY {c["ResetAll"]}\n',
      f'{c["FontRed"]}[2]{c["FontPurple"]} {c["StyleBold"]}BITLY {c["ResetAll"]}(more than one URL)\n',
      f'{c["FontRed"]}[3]{c["FontPurple"]} {c["StyleBold"]}NONE {c["ResetAll"]}\n',
      )

chooseShortener = str(input(
    f'{c["FontRed"]}{c["StyleBold"]}--->>>{c["ResetAll"]} ')).strip()

if chooseShortener.isdigit():
    chooseShortenerInt = int(chooseShortener)

    if chooseShortenerInt == 1:
        cuttly()

    elif chooseShortenerInt == 2:
        bitly()

    elif chooseShortenerInt == 3:
        print(
            f'{c["FontYellow"]}{c["BgRed"]}{c["StyleBold"]} This option is under development {c["ResetAll"]}')

    else:
        print(
            f'Option "{c["FontYellow"]}{chooseShortenerInt}{c["ResetAll"]}" is not defined.')

else:
    print(f'{c["FontRed"]}ERROR!{c["ResetAll"]} \"{c["FontYellow"]} {chooseShortener} {c["ResetAll"]}\" is not defined.')
