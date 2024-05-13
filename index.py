import textwrap
def menu():
    print('''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [nu] Cadastrar cliente
    [nc] Criar conta
    [lc] Listar contas

    => ''')
    return input()


def depositar(saldo, valor, extrato):
    if valor < 0:
        print("Não foi possível realizar operação, valor de depósito inválido")
    else:
        saldo += valor
        print("Depósito realizado com sucesso")
        extrato = f"Depósito de: R$ {valor:.2f} \n"
    return saldo, extrato

def sacar(saldo, valor, extrato, Limite, LIMITES_SAQUES, quantidade_saque):
    if valor > Limite:
        print("Não foi possível realizar operação, saque excede limite")
    elif quantidade_saque >= LIMITES_SAQUES:
        print("Você excedeu seu limite de saque diário")
    elif valor < 0:
        print("Não foi possível realizar operação, valor de saque inválido")
    elif saldo < valor:
        print("Não foi possível sacar, saldo em conta insuficiente")
    else:
        saldo -= valor
        extrato += f"Saque de: R$ {valor:.2f} \n"
        quantidade_saque +=1
        print("Saque realizado com sucesso")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
    if extrato == "":
        print("########## Extrato ##########")
        print("Não foi realizada movimentações")
        print("#############################")
    else:
        print("########## Extrato ##########")
        print(f"{extrato} \n Saldo total = R$ {saldo:.2f}")
        print("#############################")


def cadastrar_cliente(clientes):
    cpf = input("Informe seu cpf:")
    cliente = filtrar_clientes(cpf, clientes)
    if cliente:
        print("Esse usuário ja existe")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe sua data de nascimento")
    endereco = input("Informe seu endereço completo: ")
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
    

def filtrar_clientes(cpf, clientes):
    cliente_filtrado = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return cliente_filtrado[0] if cliente_filtrado else None


def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": cliente}

    print("\n Usuário não encontrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    saldo = 0
    Limite = 500
    extrato = ""
    numero_saques = 0
    LIMITES_SAQUES = 3
    quantidade_saque = 0
    clientes = []
    AGENCIA = "0001"
    contas = []


    while True:
        opcao = menu()

       
        if opcao == "d":
            print("Qual valor deseja depositar:")
            valor = float(input())
            saldo, extrato = depositar(saldo, valor, extrato)
        
        
        elif opcao == "s":
            print("Qual valor deseja sacar:")
            valor = float(input())
            saldo, extrato = sacar(saldo, valor, extrato, Limite, LIMITES_SAQUES, quantidade_saque)


        
        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            cadastrar_cliente(clientes)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        
        elif opcao == "q":
            break
        
       
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()
