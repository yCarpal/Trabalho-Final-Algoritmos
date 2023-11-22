def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

def mostrar_categorias():
    # Nome do arquivo CSV
    nome_arquivo = 'aquaviario.csv'
    
    # Lista para armazenar os valores únicos da coluna desejada
    valores_unicos = []

    # Lê o arquivo CSV e extrai os valores únicos da coluna desejada
    with open(nome_arquivo, 'r') as arquivo_csv:
        linhas = arquivo_csv.readlines()
        
        # Encontra o índice da coluna
        cabecalho = linhas[0].strip().split(',')
        indice_coluna = cabecalho.index("CD_CATEGORIA")

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
            campos = i.strip().split(',')
            if campos[4] == categoria:
                categoriass.append(campos[3])  # Adicione o órgão à lista
    return set(categoriass)

def mostrar_niveis_disponiveis():
    print("Níveis disponíveis: 1 a 10")

def mostrar_cargos_por_nivel(nivel):
    cargos_nivel = []
    with open("aquaviario.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas[1:]:
            campos = linha.strip().split(',')
            if campos[6] == nivel:
                cargos_nivel.append(campos[5])  # Adicione o cargo à lista
    return set(cargos_nivel)

while True:
    Traco("Nome: Leonardo Cutrim de Oliveira")
    Traco("Turma: BSI 23")
    Traco("Professor: Rafael Speroni")
    Traco("Menu de Opções:")
    Traco("1. Listar órgãos por categoria")
    Traco("2. Mostrar cargos por nível")
    Traco("3. Sair do sistema")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        mostrar_categorias()
        cat = input("Digite a categoria: \n")
        cats = listar_orgaos_por_categoria(cat)
        print(f"Órgãos na categoria {cat}:\n")
        for i in cats:
            print(i)

        # Salva os prints no arquivo "cargos.txt"
        with open("cargos.txt", "w") as arquivo:
            arquivo.write(f"Órgãos na categoria {cat}:\n")
            for i in cats:
                arquivo.write(i + "\n")
                
        print("Os dados foram salvos no arquivo cargos.txt.")
    elif opcao == "2":
        mostrar_niveis_disponiveis()
        nivel = input("Digite o nível (1 a 10): \n")
        cargos_nivel = mostrar_cargos_por_nivel(nivel)
        print(f"Cargos no nível {nivel}:\n")
        for cargo in cargos_nivel:
            print(cargo)

        # Salva os prints no arquivo "cargos.txt"
        with open("realtorioCargos.txt", "w") as arquivo:
            arquivo.write(f"Cargos no nível {nivel}:\n")
            for cargo in cargos_nivel:
                arquivo.write(cargo + "\n")
                
        print("Os dados foram salvos no arquivo relatorioCargos.txt.")
    elif opcao == "3":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("não existe esta opção, selecione uma existente")