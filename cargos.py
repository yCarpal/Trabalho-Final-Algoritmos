def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

def mostrar_categorias():
    
    nome_arquivo = 'aquaviario.csv' # Nome do arquivo CSV
    
    # Lista para armazenar os valores únicos da coluna escolhida
    valores_unicos = []

    # Lê o arquivo CSV e extrai os valores únicos da coluna escolhida
    with open(nome_arquivo, 'r') as arquivo_csv:
        linhas = arquivo_csv.readlines()
        
        # Encontra o índice da coluna
        cabecalho = linhas[0].strip().split(',')
        indice_coluna = cabecalho.index("DS_CATEGORIA_POR") # pega o indice da coluna

        # Percorre as linhas do arquivo, adicionando os valores únicos ao conjunto
        for linha in linhas[1:]:
            valores_unicos.append(linha.strip().split(',')[indice_coluna])

    # Mostra os valores únicos da coluna
    for valor in valores_unicos:
        print(valor)

    
def listar_orgaos_por_categoria(categoria):
    categoriass = []
    with open("aquaviario.csv", "r") as categorias:
        linhas = categorias.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',') #
            if campos[4] == categoria:
                categoriass.append(campos[3])  # Adicione o órgão à lista
    return categoriass

while True:
    Traco("Nome: Leonardo Cutrim de Oliveira ")
    Traco("Turma: BSI 23 ")
    Traco("Professor: Rafael Speroni")
    Traco("Menu de Opções:")
    Traco("1. Listar órgãos por categoria")
    Traco("2. Sair do sistema")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        mostrar_categorias() # irá mostrar todas as categorias para o operador escolher qual ele quer.
        cat = input("Digite a categoria: \n")
        cats = listar_orgaos_por_categoria(cat)
        print(f"Órgãos na categoria {cat}:\n")
        for i in cats: # mostrar cada item em cats
            print(i)

        # Salva os prints no arquivo "cargos.txt"
        with open("cargos.txt", "w") as arquivo:
            arquivo.write(f"Órgãos na categoria {cat}:\n")
            for i in cats:
                arquivo.write(i + "\n")
                
        print("Os dados foram salvos no arquivo cargos.txt.")
    elif opcao == "2":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("não existe esta opção, selecione uma existente")
