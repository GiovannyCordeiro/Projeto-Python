def listar_dados(arquivo, titulo, valor, data):
        with open(arquivo, 'a') as arquivo:
                arquivo.write(f"{titulo}||{valor}||{data}\n")
def itens_total(arquivo):
        with open(arquivo, "r") as arquivo:
                index = 0
                for linha in arquivo:
                    titulo_receita, valor_receita, data_receita = linha.split("||")
                    print(f"{index + 1} - {titulo_receita} - {valor_receita} - {data_receita}")
                    index += 1
def valor_total(arquivo):
        acomulador = 0
        with open(arquivo, "r") as arquivo:
                lista_despesas = arquivo.readlines()
                for despesa in lista_despesas:
                    titulo_despesa, valor_despesa, data_despesa = despesa.split("||")
                    acomulador += float(valor_despesa)
                return acomulador
def excluir_despesas_receitas(itens_excluidos, arquivo_definido):
        with open(arquivo_definido) as arquivo:
                linhas = arquivo.readlines()
                del linhas[itens_excluidos]
        with open(arquivo_definido, 'w') as arquivo:
                for despesas in linhas:
                    titulo_despesa, valor_despesa, data_despesa = despesas.split("||")
                    arquivo.write(f"{titulo_despesa}||{valor_despesa}||{data_despesa}")