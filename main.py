lista_despesas = []
lista_receita = []

while True:
    print('\nMENU\n'
          '\n1. Cadastrar Despesa\n'
          '\n2. Cadastrar Receita\n'
          '\n3. Listar Despesas\n'
          '\n4. Listar Receitas\n'
          '\n5. Valor Total das Despesas\n'
          '\n6. Valor Total das Receitas\n'
          '\n7. Exclusão de Despesa\n'
          '\n8. Exclusão de Receita\n'
          '\n9. Sair do Programa\n')
    menu = int(input('Escolha uma opção do menu. Ex.:1: \n'))
    match menu:
        case 1:
            título_despesa = input('Informe a origem da despesa:')
            valor_despesa = float(input('Informe o valor da sua despesa: '))
            data_despesa = input('Informe a data de pagamento. Ex.:12/12/2012: \n')
            with open('lista_despesas.txt', 'a') as arquivo:
                arquivo.write(f"{título_despesa}||{valor_despesa}||{data_despesa}\n")
        case 2:
            origem_receita = (input('Informe a origem da sua receita: '))
            valor = float(input('Informe o valor da sua receita : '))
            data = input('Informe a data de pagamento. Ex.:12/12/2012: \n')
            elemento_receita = {
                'Origem da Receita': origem_receita,
                'Valor da Receita': valor,
                'Data': data
            }
            lista_receita.append(elemento_receita)
        case 3:
            iterator = 0
            print("Lista das suas despesas: ")
            with open('lista_despesas.txt', 'r') as arquivo:
                index = 0
                for linha in arquivo:
                    titulo_despesa, valor_despesa, data_despesa = linha.split("||")
                    print(f"{index + 1} - {titulo_despesa} - {valor_despesa} - {data_despesa}")
                    index += 1
        case 4:
            print("Lista das suas receitas: ")
            iterador = 0
            if len(lista_receita) == 0:
                print("Você ainda cadastrou nenhuma receita.")
            else:
                for item in lista_receita:
                    print(f"{iterator + 1} - Titulo: {item['Origem da Receita']} - Valor: {item['Valor da Receita']} - Data: {item['Data']}")
                    iterator += 1
        case 5: 
            iterador = 0
            if len(lista_despesas) == 0:
                print("Você ainda cadastrou nenhuma despesa.")
            else: 
                for elemento in lista_despesas: 
                    iterador += elemento['valor']
                print(f"O valor total da sua lista de despesas é: {iterador}")
        case 6:
            acomulador = 0
            for elemento in lista_receita:
                acomulador += elemento['valor']
            print(f"O valor total da sua lista de receitas é: {acomulador}")
        case 7:
            excluir_despesa = int(input(f'Digite o item da lista de despesas {lista_despesas} que você deseja deletar: '))
            del lista_despesas[excluir_despesa]
        case 8:
            excluir_receita = int(input(f'Digite o item da lista de receitas {lista_receita} que você deseja deletar: '))
            del lista_receita[excluir_receita]
        case 9:
            print('Obrigado por acessar o nosso sistema. Aguardamos o seu retorno em breve.😁')
            break

    acesso = input('Deseja continuar acessando o menu de interação? \nDigite "S" para sim ou digite "n" para encerrar a sessão:\n')
    if acesso == 'S' or acesso == 's':
        continue
    else:
        print('Obrigado por acessar o nosso sistema. Aguardamos o seu retorno em breve.😁')
        break
