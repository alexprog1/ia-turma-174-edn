# 🔢 Verificador de número par

# Pede um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par usando o operador de módulo (%)
if numero % 2 == 0:
    print("✅ É um número par.")
else:
    print("❌ Não é um número par.")
