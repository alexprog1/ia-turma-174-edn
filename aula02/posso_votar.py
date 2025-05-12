# 🗳️ Verificador de elegibilidade para votação

# Solicita a idade do usuário
idade = int(input("Informe sua idade: "))

# Verifica se a idade é suficiente para votar
if idade >= 16:
    print("✅ Você pode votar!")
else:
    print("❌ Você ainda não pode votar.")
