def relatorio_Geral(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_entrada:
            linhas = arquivo_entrada.readlines()

            if len(linhas) > 0:
                nomes_colunas = linhas[0].strip().split(',')

                with open("relatorio.txt", 'w') as arquivo_relatorio:
                    arquivo_relatorio.write(
                        f"Relatório do Arquivo: {nome_arquivo}\n"
                        f"Número de Linhas: {len(linhas)}\n"
                        f"Nomes das Colunas: {', '.join(nomes_colunas)}\n"
                    )

                print("Relatório gerado com sucesso. Consulte o arquivo 'relatorio.txt'.")
            else:
                print(f"Erro: O arquivo '{nome_arquivo}' está vazio.")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")


relatorio_Geral('aquaviario.csv')