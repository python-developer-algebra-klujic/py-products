'''
DONE    Kreirati aplikaciju koja omogucava korisniku neogranicen unos proizvoda

te ih pohranjuje ih u datoteku (naizv datoteke po izboru, ali ucitan iz app_config.ini).
Svaki proizvod treba biti u zasebnoj liniji u datoteci.


DONE    SVaki proizvod treba imati
DONE    ID - redni broj od 1
DONE    Naziv
DONE    Sifru
DONE    Cijenu - valutu NE cuvate u datoteci
DONE    Oznaku valute - ucitajte iz app_config.ini datoteke


Kreirajte sve potrebne funkcije za unos, pohranu i ispis proizvoda te izbornik
'''
import os


products = []
product_id = 1
currency_symbol = 'EUR'


def create_product():
    global product_id

    product = {}

    product_title = input('Upisite naziv proizvoda kojeg zelite dodati u sustav: ')
    # product_code = input('Upisite sifru proizvoda kojeg zelite dodati u sustav: ')
    product_price = float(input('Upisite cijenu proizvoda kojeg zelite dodati u sustav: '))

    product['id'] = product_id
    product['title'] = product_title
    # product['code'] = product_code
    # Monitior -> MON00001; Tipkovnica TIP00001
    # str.zfill(redni_broj, sirina_broja)
    product['code'] = f'{product_title[0 : 3].upper()}{str.zfill(str(product_id), 5)}'
    product['price'] = product_price
    product['currency_symbol'] = currency_symbol

    product_id += 1

    return product


while True:

    os.system('cls')


    print()
    print('Py Products')
    print()

    # Unos proizvoda
    # product = create_product()
    # products.append(product)
    products.append(create_product())

    # Provjera unosa u listu
    print(products)

    next_product = input('Zelite li dodati jos jedan proizvod? (da/ne): ')
    if next_product.lower() != 'da':
        break
