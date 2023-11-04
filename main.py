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
            elemento_despesa = {
                'título': título_despesa,
                'valor': valor_despesa,
                'data': data_despesa
            }
            lista_despesas.append(elemento_despesa)
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
            print(lista_despesas)
        case 4:
            print(lista_receita)
        case 5: 
            acomulador = 0
            for elemento in lista_despesas: 
                acomulador += elemento['valor']
            print(f"O valor total da sua lista de despesas é: {acomulador}")
        case 6:
            acomulador = 0
            for elemento in lista_receita:
                acomulador += elemento['valor']
            print(f"O valor total da sua lista de receitas é: {acomulador}")