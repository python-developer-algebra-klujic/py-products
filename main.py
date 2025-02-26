'''
Kreirati aplikaciju koja omogucava korisniku neogranicen unos proizvoda
te ih pohranjuje ih u datoteku (naizv datoteke po izboru, ali ucitan iz app_config.ini).

Svaki proizvod treba biti u zasebnoj liniji u datoteci.
SVaki proizvod treba imati
ID - redni broj od 1
Naziv
Sifru
Cijenu - valutu NE cuvate u datoteci
Oznaku valute - ucitajte iz app_config.ini datoteke

Kreirajte sve potrebne funkcije za unos, pohranu i ispis proizvoda te izbornik
'''
import os


products = []
product_id = 1
product = {
    'id': 1,
    'title': 'Printer',
    'code': 'PRN',
    'price': 250.99,
    'currency_symbol': 'EUR'
}


while True:

    os.system('cls')

    print()
    print('Py Products')
    print()
    product = input('Upisite proizvod kojeg zelite dodati u sustav: ')
    products.append(product)

    print(products)

    next_product = input('Zelite li dodati jos jedan proizvod? (da/ne): ')
    if next_product.lower() != 'da':
        break
