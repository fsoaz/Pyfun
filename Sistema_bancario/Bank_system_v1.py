#Sistema bancario
#implementar três operações essenciais: depósito, saque e extrato.
#só pode realizar 3 saque por dia. Com limite de 500 reais por saque.
#e o saldo não pode ser negativo.
#o extrato deve mostrar o saldo atual e as transações realizadas.



def extrato(saldo):
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    if not transacoes:
        print("Nenhuma transação realizada.")
    else:
        for transacao in transacoes:
            tipo, valor = transacao
            print(f"{tipo}: R$ {valor:.2f}")
    print("Fim do extrato.\n")
# Início do programa
input("Bem-vindo ao sistema bancário!\n Pressione Enter para continuar...")

menu = input("Escolha uma opção:\n"
             "1. Depósito\n"
             "2. Saque\n"
             "3. Extrato\n"
             "0. Sair\n"
             "Opção: ")
saldo = 0.0
transacoes = []
limite_saques = 3
limite_valor_saque = 500.0

while True:
    if menu == "1":
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            transacoes.append(("Depósito", valor))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")
    elif menu == "2":
        if len([t for t in transacoes if t[0] == "Saque"]) < limite_saques:
            valor = float(input("Digite o valor do saque: R$ "))
            if 0 < valor <= limite_valor_saque and saldo >= valor:
                saldo -= valor
                transacoes.append(("Saque", valor))
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido ou saldo insuficiente.")
        else:
            print("Limite de saques diários atingido.")
    elif menu == "3":
        extrato(saldo)
    elif menu == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
    continue_input = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    if continue_input != 's':
        print("Saindo do sistema. Até logo!")
        break
    menu = input("Escolha uma opção:\n"
                 "1. Depósito\n"
                 "2. Saque\n"
                 "3. Extrato\n"
                 "0. Sair\n"
                 "Opção: ")