'''
DONE    Kreirati aplikaciju koja omogucava korisniku neogranicen unos proizvoda
DONE    te ih pohranjuje ih u datoteku (naziv datoteke po izboru, ali ucitan iz app_config.ini).
DONE    Svaki proizvod treba biti u zasebnoj liniji u datoteci.

DONE    SVaki proizvod treba imati
DONE    ID - redni broj od 1
DONE    Naziv
DONE    Sifru
DONE    Cijenu - valutu NE cuvate u datoteci
DONE    Oznaku valute - ucitajte iz app_config.ini datoteke

DONE        Kreirajte sve potrebne funkcije za
DONE        unos,
DONE        pohranu
DONE        i ispis proizvoda
DONE        te izbornik
'''
import os
import sys
from typing import Dict


def load_config():
    config = {}
    try:
        with open('app_config.ini', 'r') as file_reader:
            file_content_list = file_reader.readlines()
            # file_path = file_content[0] # putanja kamo cemo pohraniti nase proizvode
            # currency_symbol = file_content[1] # 'EUR'
            # product_id = file_content[2] # 1

            config['file_path'] = file_content_list[0].strip() # remove  SPACE, \n \t ...
            config['currency_symbol'] = file_content_list[1].strip()
            config['product_id'] = int(file_content_list[2]) # '1', a treba mi 1

            return config

    except Exception as ex:
        print(f'Dogodila se greska: {ex}')
        # Prekid izvrsavanja programa
        sys.exit()


def menu():
    pass


def print_product(product: Dict):
    pass


def save_product(product: Dict, file_path: str):
    try:
        with open(file_path, 'a') as file_writer:
            file_writer.write(f'{str(product)}\n')
            return 200

    except Exception as ex:
        print(f'Dogodila se greska: {ex}.')
        return 500


def create_product(product_id: int, currency_symbol: str):
    product = {}

    product_title = input('Upisite naziv proizvoda kojeg zelite dodati u sustav: ')
    # product_code = input('Upisite sifru proizvoda kojeg zelite dodati u sustav: ')
    product_price = float(input('Upisite cijenu proizvoda kojeg zelite dodati u sustav: '))

    product['id'] = product_id
    product['title'] = product_title
    # product['code'] = product_code
    # Monitior -> MON00001; Tipkovnica TIP00001
    # str.zfill(redni_broj, sirina_broja)
    product['code'] = f'{product_title[ : 3].upper()}{str.zfill(str(product_id), 5)}'
    product['price'] = product_price
    product['currency_symbol'] = currency_symbol.upper()

    return product


def main():
    # Ucitaj konfiguraciju
    config = load_config()
    current_product_id = config['product_id']

    while True:
        # TODO Pozvati funkciju za prikaz izbornika
        os.system('cls')

        print()
        print('Py Products')
        print()

        product = create_product(current_product_id, config['currency_symbol'])
        status = save_product(product, config['file_path'])
        if status == 200:
            current_product_id += 1

        next_product = input('Zelite li dodati jos jedan proizvod? (da/ne): ')
        if next_product.lower() != 'da':
            break


if __name__ == '__main__':
    main()
