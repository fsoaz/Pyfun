import textwrap

def menu():
    return textwrap.dedent('''\
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Criar Usuário
    [n] Nova Conta
    [l] Listar Contas
    [sc] Selecionar Conta
    [q] Sair
    ==========================
    ''')

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, limite, extrato, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(usuarios, cpf)

    if usuario:
        print("Já existe um usuário com esse CPF.")
        return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")
    return novo_usuario

def filtrar_usuario(usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    if not usuarios:
        print("Erro: Nenhum usuário cadastrado. Crie um usuário primeiro.")
        return None
    
    cpf = input("Informe o CPF do usuário para criar a conta: ")
    usuario = filtrar_usuario(usuarios, cpf)
    
    if not usuario:
        print("Usuário não encontrado! Cadastre o usuário primeiro.")
        return None
    
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "limite": 500,
        "extrato": "",
        "numero_saques": 0,
        "LIMITE_SAQUES": 3
    }
    print(f"Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}")
    return conta

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n================ CONTAS ================")
    for i, conta in enumerate(contas):
        print(f"[{i+1}] Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, "
              f"Usuário: {conta['usuario']['nome']}, Saldo: R$ {conta['saldo']:.2f}")
    print("=========================================")

def selecionar_conta(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    
    listar_contas(contas)
    try:
        opcao = int(input("Selecione o número da conta: ")) - 1
        if 0 <= opcao < len(contas):
            return opcao
        else:
            print("Opção inválida!")
            return None
    except ValueError:
        print("Por favor, digite um número válido!")
        return None

def obter_valor_positivo(mensagem):
    try:
        valor = float(input(mensagem))
        if valor <= 0:
            print("O valor deve ser positivo!")
            return None
        return valor
    except ValueError:
        print("Por favor, digite um valor numérico válido!")
        return None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    contas = []
    usuarios = []
    numero_conta = 1
    conta_ativa = None  # Índice da conta selecionada

    while True:
        print(menu())
        opcao = input("Escolha uma opção: ").lower().strip()

        if opcao == 'd':
            if not contas:
                print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
                continue
                
            if conta_ativa is None:
                print("Selecione uma conta primeiro usando a opção [sc].")
                continue
                
            valor = obter_valor_positivo("Informe o valor para depósito: R$ ")
            if valor is not None:
                saldo, extrato = depositar(contas[conta_ativa]['saldo'], valor, contas[conta_ativa]['extrato'])
                contas[conta_ativa]['saldo'] = saldo
                contas[conta_ativa]['extrato'] = extrato

        elif opcao == 's':
            if not contas:
                print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
                continue
                
            if conta_ativa is None:
                print("Selecione uma conta primeiro usando a opção [sc].")
                continue
                
            valor = obter_valor_positivo("Informe o valor para saque: R$ ")
            if valor is not None:
                saldo, extrato, numero_saques = sacar(
                    saldo=contas[conta_ativa]['saldo'], 
                    valor=valor, 
                    limite=contas[conta_ativa]['limite'], 
                    extrato=contas[conta_ativa]['extrato'],
                    numero_saques=contas[conta_ativa]['numero_saques'], 
                    LIMITE_SAQUES=LIMITE_SAQUES
                )
                contas[conta_ativa]['saldo'] = saldo
                contas[conta_ativa]['extrato'] = extrato
                contas[conta_ativa]['numero_saques'] = numero_saques

        elif opcao == 'e':
            if not contas:
                print("Nenhuma conta cadastrada.")
                continue
                
            if conta_ativa is None:
                print("Selecione uma conta primeiro usando a opção [sc].")
                continue
                
            exibir_extrato(contas[conta_ativa]['saldo'], contas[conta_ativa]['extrato'])

        elif opcao == 'c':
            criar_usuario(usuarios)

        elif opcao == 'n':
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == 'l':
            listar_contas(contas)

        elif opcao == 'sc':
            indice = selecionar_conta(contas)
            if indice is not None:
                conta_ativa = indice
                print(f"Conta {contas[conta_ativa]['numero_conta']} selecionada!")

        elif opcao == 'q':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()