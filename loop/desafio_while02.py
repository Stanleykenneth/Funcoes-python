"""
    Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só ira permitir o programa continuar caso ele digite a senha 'secreto'
"""

senha = ''
while senha != 'secreto':
    senha = input('Digite sua senha: ') 
    