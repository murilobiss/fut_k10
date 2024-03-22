from collections import Counter
import random

jogadores = {
    "Rafael":       {"posicao": "ATA", "nota":  7.5, "pote": "B" ,"Presente": "P"},
    "Murilo":       {"posicao": "MZA", "nota":  8.0, "pote": "A" ,"Presente": "P"},
    "Everton":      {"posicao": "ATA", "nota":  5.0, "pote": "C" ,"Presente": "P"},
    "Victor":       {"posicao": "MZA", "nota":  9.5, "pote": "A" ,"Presente": "P"},
    "Marlon":       {"posicao": "ZAG", "nota":  4.5, "pote": "C" ,"Presente": "A"},
    "Cattoni":      {"posicao": "ZAG", "nota":  5.5, "pote": "C" ,"Presente": "A"},
    "Will":         {"posicao": "MEI", "nota":  8.5, "pote": "A" ,"Presente": "P"},
    "Paulo":        {"posicao": "MEI", "nota":  8.0, "pote": "A" ,"Presente": "P"},
    "Cezar":        {"posicao": "MEI", "nota":  7.0, "pote": "B" ,"Presente": "P"},
    "Recka":        {"posicao": "ATA", "nota":  5.0, "pote": "C" ,"Presente": "A"},
    "Bruno Rafael": {"posicao": "ZAG", "nota":  5.5, "pote": "C" ,"Presente": "P"},
    "Filipe":       {"posicao": "MEI", "nota":  8.0, "pote": "B" ,"Presente": "A"},
    "Pedro Fuzzo":  {"posicao": "MZA", "nota":  8.0, "pote": "B" ,"Presente": "A"},
    "Pedro K10":    {"posicao": "MZA", "nota":  6.5, "pote": "B" ,"Presente": "P"},
    "Wellington":   {"posicao": "MEI", "nota":  6.5, "pote": "B" ,"Presente": "A"},
    "Hagi":         {"posicao": "MZA", "nota":  5.5, "pote": "C" ,"Presente": "P"},
    "Marcel":       {"posicao": "MEI", "nota":  7.0, "pote": "B" ,"Presente": "A"},
    "Henrique":     {"posicao": "MZA", "nota":  6.5, "pote": "B" ,"Presente": "A"},
    "Gustavo":      {"posicao": "MZA", "nota":  7.0, "pote": "B" ,"Presente": "P"},
    "Guima":        {"posicao": "MZA", "nota":  5.5, "pote": "C" ,"Presente": "P"},
    "Beto":         {"posicao": "MZA", "nota":  7.0, "pote": "B" ,"Presente": "A"},
    "Rodrigo":      {"posicao": "MEI", "nota":  7.0, "pote": "B" ,"Presente": "A"},
    "Benhur":       {"posicao": "ZAG", "nota":  7.0, "pote": "B" ,"Presente": "P"},
    "Provensi":     {"posicao": "ZAG", "nota":  5.0, "pote": "C" ,"Presente": "A"},
    "Denis":        {"posicao": "ATA", "nota":  6.0, "pote": "C" ,"Presente": "A"},
    "Hunas":        {"posicao": "ATA", "nota":  6.0, "pote": "C" ,"Presente": "A"},
    "Dudu":         {"posicao": "ATA", "nota":  7.0, "pote": "B" ,"Presente": "A"},
    "Fone":         {"posicao": "MZA", "nota":  8.5, "pote": "A" ,"Presente": "A"},
    "Matheus":      {"posicao": "ZAG", "nota":  6.0, "pote": "B" ,"Presente": "A"},
    "Thiagão":      {"posicao": "ZAG", "nota":  7.5, "pote": "A" ,"Presente": "A"},
    "Thiago":       {"posicao": "MEI", "nota":  8.0, "pote": "A" ,"Presente": "A"},
    "Abdala":       {"posicao": "ZAG", "nota":  5.5, "pote": "C" ,"Presente": "A"},
    "Guilherme":    {"posicao": "ZAG", "nota":  7.0, "pote": "C" ,"Presente": "P"},
    "Bruno":        {"posicao": "MEI", "nota":  8.0, "pote": "A" ,"Presente": "A"},
    "Leo":          {"posicao": "ATA", "nota":  9.5, "pote": "A" ,"Presente": "A"},
    "Samuel":       {"posicao": "ZAG", "nota":  6.5, "pote": "C" ,"Presente": "A"},
    "Diego":        {"posicao": "MEI", "nota":  7.5, "pote": "B" ,"Presente": "P"},
}

descricao_posicoes = {
    "ZAG": "Zagueiro",
    "MZA": "Meia recuado",
    "MEI": "Meia atacante",
    "ATA": "Atacante",
}


def imprimir_informacoes_jogador(jogador):
    if jogador in jogadores:
        nome = jogador
        posicao = jogadores[jogador]["posicao"]
        nota = jogadores[jogador]["nota"]
        descricao_posicao = descricao_posicoes.get(posicao, "Posição desconhecida")
        print(f"{nome} joga como {descricao_posicao} e sua nota é {nota:.2f}")
    else:
        print(f"{jogador} não encontrado na lista de jogadores.")


def contar_jogadores_por_posicao(jogadores):
    posicoes_contagem = Counter(jogador["posicao"] for jogador in jogadores.values())
    return posicoes_contagem


def atualizar_nota(jogadores):
    nome = input("Nome do jogador para atualizar a nota: ")
    if nome in jogadores:
        nova_nota_str = input("Nova nota do jogador (entre 6 e 10): ")
        if nova_nota_str.isnumeric() and 6 <= float(nova_nota_str) <= 10:
            jogadores[nome]["nota"] = float(nova_nota_str)
            print(f"Nota de {nome} atualizada com sucesso!")
        else:
            print("Nota inválida. Certifique-se de que está entre 6 e 10.")
    else:
        print("Jogador não encontrado.")


def adicionar_jogador(jogadores):
    nome = input("Nome do novo jogador: ")
    posicao = input("Posição do novo jogador (ZAG, MZA, MEI, ATA): ").upper()

    if posicao not in descricao_posicoes:
        print("Posição inválida. Certifique-se de que a posição é válida.")
        return

    nota_str = input("Nota do novo jogador (entre 6 e 10): ")
    if nota_str.isnumeric() and 6 <= float(nota_str) <= 10:
        nota = float(nota_str)
        jogadores[nome] = {"posicao": posicao, "nota": nota}
        print(f"{nome} adicionado com sucesso!")
    else:
        print("Nota inválida. Certifique-se de que está entre 6 e 10.")


def separar_times(jogadores_presentes):
    jogadores = {
        nome: dados
        for nome, dados in jogadores_presentes.items()
        if dados["Presente"] == "P"
    }

    num_jogadores_presentes = len(jogadores)
    num_times = 3 if num_jogadores_presentes >= 15 else 2

    # Obter uma lista aleatória de jogadores
    jogadores_aleatorios = list(jogadores.keys())
    random.shuffle(jogadores_aleatorios)

    # Inicializar os times
    times = {f"Time {i+1}": {} for i in range(num_times)}

    # Dividir os jogadores aleatórios entre os times
    for idx, jogador in enumerate(jogadores_aleatorios):
        times[f"Time {idx % num_times + 1}"][jogador] = jogadores[jogador]

    # Calcular a soma das notas de cada time
    soma_notas_times = {
        time: sum(dados["nota"] for dados in jogadores.values())
        for time, jogadores in times.items()
    }

    return times, soma_notas_times


def filtrar_jogadores_presentes(jogadores):
    jogadores_presentes = {
        nome: dados for nome, dados in jogadores.items() if dados.get("Presente") == "P"
    }
    contagem_posicoes = {
        posicao: sum(
            1
            for dados in jogadores_presentes.values()
            if dados.get("posicao") == posicao
        )
        for posicao in descricao_posicoes
    }
    return jogadores_presentes, contagem_posicoes


# imprimir_informacoes_jogador('Diego')
# contar_jogadores_por_posicao(jogadores)
# atualizar_nota(jogadores)
# adicionar_jogador(jogadores)

jogadores_presentes, contagem_posicoes = filtrar_jogadores_presentes(jogadores)
times, soma_notas_times = separar_times(jogadores_presentes)

# Exibir resultados
print(f"Total de jogadores presentes: {len(jogadores_presentes)}")

print("\nJogadores:")

for jogador, dados in jogadores_presentes.items():
    print(
        f"{jogador} - Posição: {descricao_posicoes[dados['posicao']]}"
    )

if len(jogadores_presentes) < 15:
    print("\nSerão 2 times:")
else:
    print("\nSerão 3 times:")

for time, jogadores_time in times.items():
    print(f"\n{time}:")
    for jogador, dados in jogadores_time.items():
        print(f"  - {jogador} - Posição: {descricao_posicoes[dados['posicao']]}")

print("\nSoma das notas dos times:")
for time, soma_notas in soma_notas_times.items():
    print(f"{time}: {soma_notas:.2f}")