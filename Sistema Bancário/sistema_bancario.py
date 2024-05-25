import textwrap

def menu():
    menu = """                  SELECIONE UMA OPÇÃO

                                    [1] Depósitos
                                    [2] Saques
                                    [3] Extrato
                                    [4] Nova conta
                                    [5] Listar contas
                                    [6] Novo Usuário
                                    [7] Sair
                        
"""
    return input(textwrap.dedent(menu))

def deposit(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!\n")
        print(f"\nSaldo atual: R$ {saldo}\n")
    else:
        print("Operação falhou! O valor informado é inválido!")
    
    return saldo, extrato

def withdraw(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nFalha na operação. Saldo insuficiente\n")
    elif excedeu_limite:
        print("\nFalha na operação. Valor excedeu o limite de saque\n")
    elif excedeu_saques:
        print("\nVocê excedeu o limite de saques diários!\n")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque efetuado no valor de R$ {valor}")
        print(f"\nSaldo atual: R$ {saldo}\n")
    else:
        print("\nValor inválido! Falha na operação\n")
    
    return saldo, extrato, numero_saques

def show_extrato(saldo, /, *, extrato):
    print("Extrato selecionado\n")
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def new_user(users):
    cpf = input("Informe somente os números do seu CPF: ")
    user = filter_users(cpf, users)
    
    if user:
        print("\n Já existe um usuário cadastrado com esse CPF!\n")
        return

    name = input("Informe seu nome completo: ")
    birthday = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    address = input("Informe seu endereço (logradouro, número - bairro - cidade/estado): ")

    users.append({"Nome": name, "Data de nascimento": birthday, "CPF": cpf, "Endereço": address})

    print("\nUsuário cadastrado com sucesso!\n")

def filter_users(cpf, users):
    filtered_users = [user for user in users if user["CPF"] == cpf]
    return filtered_users[0] if filtered_users else None
    
def create_account(agency, account_number, users):
    cpf = input("Informe o CPF do usuário: ")
    user = filter_users(cpf, users)

    if user:
        account = {"agencia": agency, "numero_conta": account_number, "usuario": user}
        print("\nConta criada com sucesso!\n")
        print(f"Agência: {account['agencia']}")
        print(f"Conta Corrente: {account['numero_conta']}")
        print(f"Titular: {account['usuario']['Nome']}")
        return account
        
    print("\nUsuário não encontrado! Por favor, primeiro crie um novo usuário!\n")

def list_accounts(accounts):
    if not accounts:
        print("\nNenhuma conta criada!\n")
        
    for account in accounts:
        line = f"""\
            Agência:\t{account['agencia']}
            C/C:\t\t{account['numero_conta']}
            Titular:\t{account['usuario']['Nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))

def main():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    users = []
    accounts = []
    
    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input("Informe o valor para depósito: "))
            saldo, extrato = deposit(saldo, valor, extrato)        
        
        elif opcao == '2':
            valor = float(input("Informe o valor para saque: "))
            
            saldo, extrato, numero_saques = withdraw(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITES_SAQUES,
            )

        elif opcao == '3':
            show_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            account_number = len(accounts) + 1
            account = create_account(AGENCIA, account_number, users)

            if account:
                accounts.append(account)

        elif opcao == '5':
            list_accounts(accounts)
        
        
        elif opcao == '6':
            new_user(users)

        elif opcao == '7':
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()

print("Obrigado por usar os nossos serviços!")
