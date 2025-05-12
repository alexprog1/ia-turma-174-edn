# 📚 Registro de Notas dos Alunos e Cálculo da Média

# Lista que armazenará as notas dos alunos
notas = []
numero_de_alunos = 0

while True:
    # Entrada do professor: nota ou 'fim' para encerrar
    entrada = input("Digite a nota do aluno (ou escreva 'fim' para encerrar): ").strip()

    # 🚨 Se o professor digitar 'fim', encerra o loop
    if entrada.lower() == 'fim':
        break

    try:
        # Tenta converter a entrada para float
        nota = float(entrada)

        # 💡 Verifica se a nota está no intervalo válido de 0 a 10
        if 0 <= nota <= 10:
            notas.append(nota)  # Adiciona a nota à lista
            numero_de_alunos += 1  # Incrementa o contador de alunos
        else:
            print("⚠️ Nota inválida! Digite um valor de 0 a 10.")

    except ValueError:
        # Captura erro caso a entrada não seja um número válido
        print("❌ Entrada inválida. Por favor, digite um número de 0 a 10 ou 'fim'.")

# 🎯 Cálculo e exibição da média da turma, se houver notas registradas
if numero_de_alunos > 0:
    media = sum(notas) / numero_de_alunos
    print(f"\n✅ A média da turma é: {media:.2f}")
    print(f"👩‍🏫 Total de alunos computados: {numero_de_alunos}")
else:
    print("❗ Nenhuma nota foi registrada.")
