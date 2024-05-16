menu = """                  SELECIONE UMA OPÇÃO

                           [1] Depósitos
                           [2] Saques
                           [3] Extrato
                           [4] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == '1':
        print("Depósito selecionado\n")
        valor = float(input("Informe o valor para depósito: "))
        print(f"R$ {valor} creditado")

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\nFalha na operação, valor inválido!\n")

    elif opcao == '2':
        print("Saque selecionado\n")
        valor = float(input("Informe o valor para o saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("\nFalha na operação. Saldo insuficiente\n")
        elif excedeu_limite:
            print("\nFalha na operação. Valor excedeu o limite de saque\n")
        elif excedeu_saques:
            print("\nVocê excedeu o limite de saques diários!\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1
            print(f"Saque efetuado no valor de R$ {valor}")
        else:
            print("\nValor inválido! Falha na operação\n")
        
    elif opcao == '3':
        print("Extrato selecionado\n")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == '4':
        print("Obrigado pela preferência! Até a próxima!")
        break
    else:
        print("Opção inválida, tente novamente e selecione a opção desejada\n")
  