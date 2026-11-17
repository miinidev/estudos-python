# Função para receber e validar os números
def obter_numeros():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        return numero1, numero2
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        return None


# Loop principal da calculadora
while True:
    print("\n--- Calculadora ---")
    print("[1] - Somar")
    print("[2] - Subtrair")
    print("[3] - Multiplicar")
    print("[4] - Dividir")
    print("[5] - Sair")

    operacao = input("Escolha uma opção: ")

    if operacao == "5":
        print("Encerrando calculadora.")
        break

    elif operacao not in ("1", "2", "3", "4"):
        print("Opção inválida. Tente novamente.")
        continue

    numeros = obter_numeros()

    if numeros is None:
        continue

    numero1, numero2 = numeros

    if operacao == "1":
        resultado = numero1 + numero2

    elif operacao == "2":
        resultado = numero1 - numero2

    elif operacao == "3":
        resultado = numero1 * numero2

    elif operacao == "4":
        if numero2 == 0:
            print("Não é possível dividir por zero.")
            continue

        resultado = numero1 / numero2

    print("O resultado é: {:.2f}".format(resultado))
