"""
    Use a operação  necessária (brack ou  continue) para que a seguinte condição aconteça
    Ao chegar ao estilo "Rock" a execução deve ser interrompida.
"""

estilos = ['Hip-hop', 'Rock', 'Rap', 'Pop']

for estilo in estilos:
    if estilo == 'Rock':
        break
    print(f'Estilo musical {estilo}')