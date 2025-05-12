# 🧮 Calculadora de IMC (Índice de Massa Corporal)
# Fórmula: IMC = peso / (altura ao quadrado)

# Entrada de dados do usuário
while True:
    entrada = input("Digite sua altura em metros (ex: 1.75): ")
    
    if "." not in entrada:
        print("❌ Use ponto para separar a altura (ex: 1.75)")
        continue
    try:
        altura = float(entrada)
        break
    except ValueError:
        print("❌ Entrada inválida. Tente novamente.")

while True:
    entrada = input("Digite seu peso em kg (ex: 70): ")
       
    try:
        peso = float(entrada)
        break
    except ValueError:
        print("❌ Entrada inválida. Tente novamente.")


# Cálculo do IMC
imc = peso / (altura ** 2)

# Mostra o resultado com 2 casas decimais
print(f"\n✅ Seu IMC é: {imc:.2f}")

# Interpretação do resultado
if imc < 18.5:
    print("🔎 Situação: Abaixo do peso")
elif imc < 25:
    print("✅ Situação: Peso normal")
elif imc < 30:
    print("⚠️ Situação: Sobrepeso")
else:
    print("🚨 Situação: Acima do peso")
