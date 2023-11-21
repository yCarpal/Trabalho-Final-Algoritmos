def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

def relatorio(nome_arquivo, conteudo):# dois parametros 1 nome do arquivo e o outro é o meu conteudo
    with open(nome_arquivo, "a") as arquivo: #"a" ele escreve e adiciona elementos no final do arquivo
        arquivo.write(conteudo) #escreve o conteudo no arquivo

def contar_orgaos_do_distrito(distrito):
    contador = 0
    with open("aquaviario.csv", "r") as distritos:
        linhas = distritos.readlines() # ler todo o meu arquivo csv
        for linha in linhas[1:]: #para todo elemento na linha ignorando a primeiro, então a partir da segunda
            campos = linha.strip().split(',') # remover os espaçoes vazios e colocar no lugar deles uma "," 
            if int(campos[0]) == int(distrito): # se a coluna 0  é equivalente a distrito ele ira adicionar a aumentar de 1 em 1 a qnt de orgãos 
                contador += 1
    resultado = f'O Número total de órgãos no Distrito {distrito} é de {contador}\n'
    relatorio("distritos.txt", resultado)
    return contador # voltar o contador

def listar_orgaos_do_distrito(distrito):
    with open("aquaviario.csv", "r") as distritos:# ler o arquivo
        linhas = distritos.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',')
            if campos[0] == distrito:
                resultado = f'O Distrito {distrito} possui o orgão {campos[1]}, na região de {campos[2]}\n'# O distrito " selecionado" posssui orgão da 1 coluna, na regiao de(coluna 2), ou seja ele ira mostrar cada orgão daquele distrito e sua região em sequencia
                relatorio("distritos.txt", resultado)
                print(resultado) # mostrar

# Código principal "Meu menu de interação"
while True:
    Traco("Nome: Leonardo Cutrim de Oliveira \n")
    Traco("Turma: BSI 23 \n")
    Traco("Professor: Rafael Speroni \n")
    Traco("Menu de opções:")
    Traco("1. Contar órgãos do distrito")
    Traco("2. Listar órgãos do distrito") 
    Traco("3. Sair do Sistema")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        distrito = input('Digite o número do distrito (de 1 a 9) para contar os órgãos do aquaviário: ')
        if distrito not in map(str, range(1, 10)): #  a função map() fornece uma maneira de aplicar uma função a todos os itens em um iterável. 
                                                   # uma vez que ela está aplicando a função apenas a um item de cada vez, em vez de fazer cópias dos itens em outro iterável. E se o distrito não tiver entre o 1 e 10 ele irá para o else
            print('Número de distrito não está no arquivo')
        else: # se não
            contador = contar_orgaos_do_distrito(distrito) #aplicar a função de contagem no parametro distrito
            print(f'O Número total de órgãos no Distrito {distrito} é de {contador}')
    elif opcao == "2":
        distrito = input('Digite o número do distrito (de 1 a 9) para listar os órgãos do aquaviário: ')
        if distrito not in map(str, range(1, 10)):
            print('Número de distrito não está no arquivo')
        else:
            listar_orgaos_do_distrito(distrito) #função listar
    elif opcao == "3":
        print("Saindo do programa, Muito obrigado!!! ")
        break
    else:
        print("não existe esta opção, selecione uma existente")
