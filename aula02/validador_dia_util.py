# 📅 Verificador de Dia Útil ou Final de Semana

# Solicita ao usuário o dia da semana e converte para minúsculas para evitar erros de digitação
dia = input("Digite o dia da semana: ").strip().lower()

# Verifica se é fim de semana ou dia útil
if dia == "sábado" or dia == "domingo":
    print("🎉 É fim de semana! Uhuuuuu!")
else:
    print("💼 É dia útil. Bora trabalhar ou estudar!")
