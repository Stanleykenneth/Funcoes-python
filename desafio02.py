'''
    Crie uma função chamada "calcular_valores" que receba 2 parâmetros o primeiro de um quantidade e o segundoa parâmetros é a quantidade,
    porém a quantidade deve haver um valor padrão de 1. Sua função de exibir o resultado do quantidade, multiplicando a quantidade escolhida.

'''

def calcular_valores(preco, quantidade = 1):

    total = preco * quantidade
    print(f'O valor do produto(s) é R$ {total:.2f}')

calcular_valores(56.60, 10)    