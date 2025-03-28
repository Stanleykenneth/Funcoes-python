'''
    Crie um decorator que irá pegar a função que foi passado para ele e imprimir o horário atual
    antes de executar a função e depois imprimir horário após ter finalizado a excução da função.


'''

from datetime import datetime

def monitorar_horario(funcao):
    def monitor():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return monitor

@monitorar_horario
def baixar_musica():
    print('Baixando musica')


baixar_musica()    
     