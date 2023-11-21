def Traco(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

def mostrar_categorias():
    nome_arquivo = 'aquaviario.csv'
    
    valores_unicos = []

    with open(nome_arquivo, 'r') as arquivo_csv:
        linhas = arquivo_csv.readlines()
        # Encontra o índice da coluna
        cabecalho = linhas[0].strip().split(',')
        indice_coluna = cabecalho.index("DS_CATEGORIA_POR")

        for linha in linhas[1:]:
            valores_unicos.append(linha.strip().split(',')[indice_coluna])

    for valor in valores_unicos:
        print(valor)

def contar_pessoas_por_cargo(cargo):
    contador = 0
    with open("aquaviario.csv", "r") as cargos:
        linhas = cargos.readlines()
        for linha in linhas[1:]:
            campos = linha.strip().split(',')
            if campos[5] == cargo:
                contador += 1
    return contador

def Resumo(arquivo, texto):
    with open(arquivo, 'a') as arquivo_saida: # criar um arquivo resumo de tudo desta função
        arquivo_saida.write(texto + '\n')

while True:
    Traco("Nome: Leonardo Cutrim de Oliveira")
    Traco("Turma: BSI 23")
    Traco("Professor: Rafael Speroni")
    Traco("Menu de Opções:")
    Traco("1. Mostrar quantidade de pessoas por cargo")
    Traco("2. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_categorias()
        cargo = input("Digite o cargo: ")
        total_pessoas = contar_pessoas_por_cargo(cargo) #aplicar a função em cima do cargo selecionado
        print(f"Quantidade de pessoas que atuam no cargo '{cargo}': {total_pessoas}")

        resultado_opcao1 = f"Opção 1 - Cargo: {cargo} e o Total de Pessoas que o operam é de {total_pessoas}"
        Resumo('QuantidadeDePessoas.txt', resultado_opcao1)

    elif opcao == "2":
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Escolha novamente.")