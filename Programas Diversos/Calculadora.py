#Loop principal da Calculadora
while True:
    print('\n ---Calculadora---')
    print('[1] - Somar')
    print('[2] - Subtrair')
    print('[3] - Multiplicar')
    print('[4] - Dividir')
    print('[5] - Sair')
    operacao = input("Escolha uma opção:")

    if operacao == "5":
        print("Encerranco calculadora.")
        break

    if operacao == "1":
        numero1 = float(input("digite o primeiro número:"))
        numero2 = float(input("digite o segundo número:"))
        print ('O resultado é: {:.2f}'.format(numero1 + numero2))
    elif operacao == "2":
        numero1 = float(input("digite o primeiro número:"))
        numero2 = float(input("digite o segundo número:"))
        print ('O resultado é: {:.2f}'.format(numero1 - numero2))
    elif operacao == "3":
        numero1 = float(input("digite o primeiro número:"))
        numero2 = float(input("digite o segundo número:"))
        print ('O resultado é: {:.2f}'.format(numero1 * numero2))
    elif operacao == "4":
        numero1 = float(input("digite o primeiro número:"))
        numero2 = float(input("digite o segundo número:"))
        print ('O resultado é: {:.2f}'.format(numero1 / numero2))

    else:
        print("Opção invalida. Tente novamente.")

