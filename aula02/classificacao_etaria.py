# 👶🧒🧑👴 Classificador de faixa etária

# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))

# Verifica a faixa etária com base na idade fornecida
if idade >= 65:
    print("Você é idoso.")
elif idade >= 18:
    print("Você é adulto.")
elif idade >= 12:
    print("Você é adolescente.")
elif idade >= 3:
    print("Você é uma criança.")
else:
    print("Você é um bebê.")
