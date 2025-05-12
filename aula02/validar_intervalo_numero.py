# 🔢 Verificador de intervalo: está entre 10 e 20?

# Solicita ao usuário que digite um número
numero = int(input("Digite um número: "))

# Verifica se o número está dentro do intervalo aberto (10, 20)
if 10 < numero < 20:
    print("✅ O número está entre 10 e 20.")
else:
    print("⚠️ O número está fora do intervalo.")
