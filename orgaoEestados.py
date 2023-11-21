
def Traco(txt, nome_arquivo=None):
    linha = '-'*30
    print(linha)
    print(txt)
    print(linha)

    if nome_arquivo:
        salvar_em_arquivo(nome_arquivo, linha + '\n' + txt + '\n' + linha + '\n')

def salvar_em_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(conteudo)

def filtrar_orgaos_por_estado(estado):
    contador = 0
    with open("aquaviario.csv", "r") as estados:
        linhas = estados.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',')
            if campos[2] == estado:
                contador += 1
    return contador

def listar_orgaos_por_estado(estado):
    orgaos = []
    with open("aquaviario.csv", "r") as estados:
        linhas = estados.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',')
            if campos[2] == estado:
                orgaos.append(campos[1])
    return orgaos

def contar_estados_no_arquivo():
    estados_distintos = set()
    with open("aquaviario.csv", "r") as estados:
        linhas = estados.readlines()
        for i in linhas[1:]:
            campos = i.strip().split(',')
            estado = campos[2]
            estados_distintos.add(estado)
    return estados_distintos

def criar_resumo():
    estados = contar_estados_no_arquivo()
    
    for estado in estados:
        total_orgaos = filtrar_orgaos_por_estado(estado)
        orgaos = listar_orgaos_por_estado(estado)

        resultado = f"Resumo para o estado {estado}:\n"
        resultado += f"Total de órgãos: {total_orgaos}\n"
        resultado += f"Órgãos no estado {estado}:\n"
        for orgao in orgaos:
            resultado += orgao + "\n"

        nome_arquivo = f"resumo_{estado}.txt"
        Traco(resultado, nome_arquivo)
        print(f"Arquivo '{nome_arquivo}' criado com sucesso.")

# Código principal
while True:
    Traco("Nome: Leonardo Cutrim de Oliveira")
    Traco("Turma: BSI 23")
    Traco("Professor: Rafael Speroni")
    Traco("Menu de Opções:")
    Traco("1. Contar órgãos por estado")
    Traco("2. Listar órgãos por estado")
    Traco("3. Contar quantidade de estados")
    Traco("4. Criar arquivo de resumo")
    Traco("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        estado = input("Digite o estado: ")
        total_orgaos = filtrar_orgaos_por_estado(estado)
        print(f"Total de órgãos no estado {estado}: {total_orgaos}")
    elif opcao == "2":
        estado = input("Digite o estado: ")
        orgaos = listar_orgaos_por_estado(estado)
        print(f"Órgãos no estado {estado}:")
        for orgao in orgaos:
            print(orgao)
    elif opcao == "3":
        total_estados = len(contar_estados_no_arquivo())
        print(f"Quantidade de estados no arquivo: {total_estados}")
    elif opcao == "4":
        criar_resumo()
    elif opcao == "5":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
