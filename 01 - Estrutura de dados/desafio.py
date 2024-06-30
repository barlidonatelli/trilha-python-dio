import textwrap

def menu():
    menu = """\n
    ================ MENU =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))    

def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"


    while True:

        opcao = input(menu)

        if opcao == "d":
                
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":

            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
                )


        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
         
        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")    

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucessp! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def cadastrar_conta(AGENCIA, numero_conta, usuarios):

    cpf = input("Insira o numero de CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario não encontrado!")

def exibir_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o seu numero de CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuario já cadastrado com esse CPF!")
        return

    nome_usuario = input("Insira seu nome: ")
    data_nascimento = input("Qual é a sua data de nascimento? Ex.: 01-01-2001: ")
    endereço = input("Forneça seu endereço no formato: Logradouro, Nº - Bairro - Cidade / Sigla do estado: ")

    usuarios.append({"Nome": nome_usuario, "Data de nascimento": data_nascimento, "CPF": cpf, "Endereço": endereço})
    
    print("Usuário cadastrado com sucesso!")

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
                
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
        print("\nSaque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def filtrar_usuario(cpf, usuarios):

    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

main()










