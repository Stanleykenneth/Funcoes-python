"""
    Imprima na tela a marca + versões de todos celulares, usando as informações abaixo

    celulrares = ['Asus', 'Sansung', 'Sony', 'Iphone']
    versões = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']
"""


celulares = ['Asus', 'Sansung', 'Sony', 'Iphone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'Celular {celular} na versão {versao}')