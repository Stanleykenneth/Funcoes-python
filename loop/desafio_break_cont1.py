"""
    Use a operação  necessária (brack ou  continue) para que a seguinte condição aconteça
    Ao chegar ao estilo "Rap" o mesmo não deve ser impresso na tela
"""

estilos = ['hip-hop' , 'Rock', 'Rap', 'Pop']

for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(f'Estilos musicais {estilo}')