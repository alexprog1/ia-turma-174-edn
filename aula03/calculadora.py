# 🧮 Calculadora Simples com Validação Total

while True:
    try:
        # ✏️ Entrada dos números - já convertendo pra float
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # ➕➖✖️➗ Operação desejada
        operacao = input("Digite a operação (+, -, *, /): ").strip()

        # 💡 Checa a operação e realiza o cálculo
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("❌ Coleguinha, dividir por zero não dá certo!")
            resultado = num1 / num2
        else:
            raise ValueError("⚠️ Operação inválida. Tente novamente com +, -, * ou /.")

        # ✅ Mostra o resultado final
        print(f"✅ Resultado: {resultado}")
        break  # Sai do loop se tudo deu certo

    # 🛑 Captura erro de operação ou de entrada inválida
    except ValueError as e:
        print(e if "Operação" in str(e) else "🚫 Entrada inválida. Digite números válidos.")

    # 🚫 Divisão por zero
    except ZeroDivisionError as e:
        print(e)
