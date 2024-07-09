menu = """
Escolha a operação a ser realizada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor_depositado = float(input("Digite o valor a ser depositado: "))
        
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
        else:
            print("Valor inválido, não é possível depositar!")
       
    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor a ser sacado (Limite de 500): "))
            
            if valor_saque <= 500:
                
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                else:
                    print("Saldo insuficiente, não é possível efetuar o saque.")
            
            else:
                print("Valor superior a 500, não é possível efetuar o saque.")

        else:
            print("Você alcançou o número máximo de saques hoje, volte amanhã!")

    elif opcao == "3":
        print("\n======================================== EXTRATO ========================================")
        if not extrato:
            print("Não foram realizadas movimentações!\n")
        else:
            print(extrato)
        print(f"Seu saldo atual é de: R$ {saldo:.2f}.")
        print("==================================================")

    elif opcao == "4":
        break
    
    else:
        print("Opção inválida, selecione novamente a operação desejada!")