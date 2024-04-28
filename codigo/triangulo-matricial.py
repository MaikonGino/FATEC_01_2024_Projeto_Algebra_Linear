def calcular_custo_sanduiche(ingredientes, ingredientes_sanduiche, mercado):
    custo_sanduiche = {}
    for sanduiche, ingredientes_sanduiche in ingredientes_sanduiche.items():
        custo_total = sum(ingredientes[ingrediente][mercado] * quantidade for ingrediente, quantidade in ingredientes_sanduiche.items())
        custo_sanduiche[sanduiche] = custo_total
    return custo_sanduiche


def aplicar_correcao_precos(custo_sanduiche, fator):
    for sanduiche, custo in custo_sanduiche.items():
        custo_sanduiche[sanduiche] *= fator

def menu_alterar_precos(ingredientes):
    while True:
        print("\nMenu - Alterar Preços dos Ingredientes:")
        print("0. Voltar ao Menu Principal")
        for idx, ingrediente in enumerate(ingredientes.keys(), start=1):
            print(f"{idx}. Alterar Preço de {ingrediente}")
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            return
        elif opcao.isdigit() and 1 <= int(opcao) <= len(ingredientes):
            idx = int(opcao)
            ingrediente = list(ingredientes.keys())[idx - 1]
            mercado = input("Digite o nome do supermercado (COPACABANA ou PAGUE MENOS): ").upper()
            preco_novo = float(input("Digite o novo preço do ingrediente: "))
            ingredientes[ingrediente][mercado] = preco_novo
            print("Preço do ingrediente {} no supermercado {} alterado para R$ {:.2f}".format(ingrediente, mercado, preco_novo))
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
        'TM BURGER': {'Pão': 1, 'Carne De Hambúrguer': 2, 'Alface': 0.05, 'Rúcula': 0, 'Ovo': 1, 'Queijo Muçarela': 0.1, 'Bacon': 0.09, 'Tomate': 0.06, 'Batata Palha': 0.02},
        'TM VEG': {'Pão': 1, 'Alface': 0.05, 'Rúcula': 0.05, 'Queijo Muçarela': 0.14, 'Tomate': 0.08, 'Batata Palha': 0.03}
    }


    while True:
        print("\nMenu Principal:")
        print("1. Visualizar Tabela de Preços dos Ingredientes")
        print("2. Calcular Custo de Produção de Cada Sanduíche")
        print("3. Alterar Preços dos Ingredientes")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            for ingrediente, precos in ingredientes.items():
                print(f"{ingrediente}: {precos}")
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
