def exibir_tabela_precos_unitarios(ingredientes):
    print("\nTabela de Preços Unitários dos Ingredientes:")
    print("{:<20} {:<15} {:<15}".format("Ingrediente", "COPACABANA", "PAGUE MENOS"))
    for ingrediente, precos in ingredientes.items():
        print("{:<20} R$ {:<13.2f} R$ {:<13.2f}".format(ingrediente, precos['COPACABANA'], precos['PAGUE MENOS']))

def exibir_tabela_precos_ingredientes(ingredientes):
    print("\nTabela de Preços dos Ingredientes em cada Supermercado:")
    print("{:<15} {:<15} {:<15}".format("", "COPACABANA", "PAGUE MENOS"))
    for ingrediente, precos in ingredientes.items():
        print("{:<15} R$ {:<11.2f} R$ {:<11.2f}".format(ingrediente, precos['COPACABANA'], precos['PAGUE MENOS']))

def calcular_custo_sanduiche(ingredientes, ingredientes_sanduiche, mercado):
    custo_sanduiche = {}
    for sanduiche, ingredientes_sanduiche in ingredientes_sanduiche.items():
        custo_total = sum(ingredientes[ingrediente][mercado] for ingrediente in ingredientes_sanduiche)
        custo_sanduiche[sanduiche] = custo_total
    return custo_sanduiche

def aplicar_correcao_precos(ingredientes, fator):
    for ingrediente, precos in ingredientes.items():
        for mercado, preco in precos.items():
            ingredientes[ingrediente][mercado] *= fator

def menu_alterar_precos(ingredientes):
    while True:
        print("\nMenu - Alterar Preços dos Ingredientes:")
        print("1. Visualizar Tabela de Preços Unitários")
        print("2. Alterar Preço de um Ingrediente")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_tabela_precos_unitarios(ingredientes)
        elif opcao == '2':
            ingrediente = input("Digite o nome do ingrediente que deseja alterar o preço: ")
            mercado = input("Digite o nome do supermercado (COPACABANA ou PAGUE MENOS): ").upper()
            preco_novo = float(input("Digite o novo preço do ingrediente: "))
            ingredientes[ingrediente][mercado] = preco_novo
            print("Preço do ingrediente {} no supermercado {} alterado para R$ {:.2f}".format(ingrediente, mercado, preco_novo))
        elif opcao == '3':
            return
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def menu_principal():
    ingredientes = {
        'Pão': {'COPACABANA': 2.47, 'PAGUE MENOS': 1.67},
        'Carne De Hambúrguer': {'COPACABANA': 1.69, 'PAGUE MENOS': 1.69},
        'Alface': {'COPACABANA': 16.33, 'PAGUE MENOS': 19.97},
        'Rúcula': {'COPACABANA': 21.95, 'PAGUE MENOS': 29.95},
        'Ovo': {'COPACABANA': 1.00, 'PAGUE MENOS': 1.08},
        'Queijo Muçarela': {'COPACABANA': 45.90, 'PAGUE MENOS': 29.90},
        'Bacon': {'COPACABANA': 29.90, 'PAGUE MENOS': 22.99},
        'Tomate': {'COPACABANA': 5.98, 'PAGUE MENOS': 5.99},
        'Batata Palha': {'COPACABANA': 85.62, 'PAGUE MENOS': 76.10}
    }

    ingredientes_sanduiche = {
        'TM BURGER': ['Pão', 'Carne De Hambúrguer', 'Alface', 'Rúcula', 'Ovo', 'Queijo Muçarela', 'Bacon', 'Tomate', 'Batata Palha'],
        'TM VEG': ['Pão', 'Alface', 'Rúcula', 'Queijo Muçarela', 'Tomate', 'Batata Palha']
    }

    while True:
        print("\nMenu Principal:")
        print("1. Visualizar Tabela de Preços dos Ingredientes")
        print("2. Calcular Custo de Produção de Cada Sanduíche")
        print("3. Alterar Preços dos Ingredientes")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_tabela_precos_ingredientes(ingredientes)
        elif opcao == '2':
            mercado = input("Digite o nome do supermercado para calcular os custos (COPACABANA ou PAGUE MENOS): ").upper()
            custo_sanduiche = calcular_custo_sanduiche(ingredientes, ingredientes_sanduiche, mercado)
            for sanduiche, custo in custo_sanduiche.items():
                print("{} ({}): R$ {:.2f}".format(sanduiche, mercado, custo))
            aplicar_correcao_precos(custo_sanduiche, 1.5)  # Aplica a correção de 50% nos custos calculados
            print("\nCustos com correção de 50%:")
            for sanduiche, custo in custo_sanduiche.items():
                print("{} ({}): R$ {:.2f}".format(sanduiche, mercado, custo))
        elif opcao == '3':
            menu_alterar_precos(ingredientes)
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Execução do programa
menu_principal()
