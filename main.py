from logicas.arquivo import cadastrar_dados, itens_total, valor_total, excluir_despesas_receitas

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
            titulo_despesa = input('Informe a origem da despesa:')
            valor_despesa = float(input('Informe o valor da sua despesa: '))
            data_despesa = input('Informe a data de pagamento. Ex.:12/12/2012: \n')
            cadastrar_dados("lista_despesas.txt",titulo_despesa, valor_despesa, data_despesa)
        case 2:
            origem_receita = (input('Informe a origem da sua receita: '))
            valor = float(input('Informe o valor da sua receita : '))
            data = input('Informe a data de pagamento. Ex.:12/12/2012: \n')
            cadastrar_dados("lista_receitas.txt", origem_receita, valor, data)
        case 3:
            print("Lista das suas despesas: ")
            itens_total("lista_despesas.txt")
        case 4:
            print("Lista das suas receitas: ")
            itens_total("lista_receitas.txt")
        case 5: 
            acomulador = valor_total("lista_despesas.txt")
            print(f"O valor total da sua lista de despesas é: {acomulador}")
        case 6:
            acomulador = valor_total("lista_receitas.txt")
            print(f"O valor total da sua lista de receitas é: {acomulador}\n")
        case 7:
            item_excluido = int(input(f'Digite o número referente ao item que deseja excluir na lista "Despesas": ')) - 1
            excluir_despesas_receitas(item_excluido, "lista_despesas.txt")
        case 8:
            item_excluido = int(input(f'Digite o número referente ao item que deseja excluir na lista "Receitas": ')) - 1
            excluir_despesas_receitas(item_excluido, "lista_receitas.txt")
        case 9:
            print('Obrigado por acessar o nosso sistema. Aguardamos o seu retorno em breve.😁')
            break

    acesso = input('Deseja continuar acessando o menu de interação? \nDigite "S" para sim ou digite "n" para encerrar a sessão:\n')
    if acesso == 'S' or acesso == 's':
        continue
    else:
        print('Obrigado por acessar o nosso sistema. Aguardamos o seu retorno em breve.😁')
        break