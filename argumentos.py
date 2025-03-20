
def exibir_produto(nome_produto, preco): # * na fentre dos argumantos, se tortna mandatário ao invocar a função
    print(f'{nome_produto} está no valor de: R$ {preco}')


#Argumento posicionais
exibir_produto(nome_produto= 'Iphone', preco= 5000)

# Mandatório => Quando se coloca * na frente dos argumentos na função ao chamar a função essas argumento precisa passar os nomes
exibir_produto(nome_produto= 'Iphone', preco= 5000)

# Argumentos nomeados
exibir_produto(preco= 5000, nome_produto= 'Iphone')