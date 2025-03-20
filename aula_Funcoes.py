"""
    def nome_da_funcao(parametros):
    comandos

"""
# função sem parametro

""" def dar_boas_vindas():
    print('Bem-vindo')

dar_boas_vindas()
 """
# Função com parametros

""" def boas_vindas_personalizadas(nome):
    print(f'Bem-vindo(a) {nome}')

boas_vindas_personalizadas('Fulano')    
 """

# função com valor padrão. Passando argumento estático
""" def apresentar_lugar(lugar = 'nossa loja'):
    print(f'conheça {lugar}')

apresentar_lugar() """

def apresentar_lugar(horario_funcionamento, lugar = 'nossa loja'):
    print(f'Conheça a {lugar}, horário de funcionamento {horario_funcionamento}')

apresentar_lugar('08:00 as 18:00', 'Disney')