from collections import Counter
import random

jogadores = {
    "Rafael": {"posicao": "ATA", "nota": 7, "Presente": "P"},
    "Murilo": {"posicao": "MZA", "nota": 7, "Presente": "P"},
    "Everton": {"posicao": "ATA", "nota": 5, "Presente": "P"},
    "Victor": {"posicao": "MZA", "nota": 10, "Presente": "P"},
    "Marlon": {"posicao": "ZAG", "nota": 4, "Presente": "P"},
    "Cattoni": {"posicao": "ZAG", "nota": 5, "Presente": "P"},
    "Will": {"posicao": "MEI", "nota": 8, "Presente": "P"},
    "Paulo": {"posicao": "MEI", "nota": 8, "Presente": "P"},
    "Recka": {"posicao": "ATA", "nota": 5, "Presente": "A"},
    "Filipe": {"posicao": "MEI", "nota": 8, "Presente": "P"},
    "Pedro": {"posicao": "MZA", "nota": 8, "Presente": "A"},
    "Wellington": {"posicao": "MEI", "nota": 7, "Presente": "A"},
    "Hagi": {"posicao": "MZA", "nota": 5, "Presente": "P"},
    "Marcel": {"posicao": "MEI", "nota": 7, "Presente": "P"},
    "Henrique": {"posicao": "MZA", "nota": 6, "Presente": "P"},
    "Gustavo": {"posicao": "MZA", "nota": 7, "Presente": "P"},
    "Guima": {"posicao": "MZA", "nota": 5, "Presente": "P"},
    "Beto": {"posicao": "MZA", "nota": 7, "Presente": "A"},
    "Rodrigo": {"posicao": "MEI", "nota": 7, "Presente": "A"},
    "Benhur": {"posicao": "ZAG", "nota": 7, "Presente": "A"},
    "Provensi": {"posicao": "ZAG", "nota": 5, "Presente": "A"},
    "Denis": {"posicao": "ATA", "nota": 6, "Presente": "A"},
    "Hunas": {"posicao": "ATA", "nota": 6, "Presente": "A"},
    "Dudu": {"posicao": "ATA", "nota": 7, "Presente": "A"},
    "Fone": {"posicao": "MZA", "nota": 8, "Presente": "A"},
    "Matheus": {"posicao": "ZAG", "nota": 6, "Presente": "A"},
    "Thiagão": {"posicao": "ZAG", "nota": 7, "Presente": "A"},
    "Thiago": {"posicao": "MEI", "nota": 8, "Presente": "A"},
    "Abdala": {"posicao": "ZAG", "nota": 5, "Presente": "A"},
    "Guilherme": {"posicao": "ZAG", "nota": 7, "Presente": "A"},
    "Bruno": {"posicao": "MEI", "nota": 8, "Presente": "A"},
    "Leo": {"posicao": "ATA", "nota": 9, "Presente": "A"},
    "Samuel": {"posicao": "ZAG", "nota": 6, "Presente": "A"},
    "Diego": {"posicao": "MEI", "nota": 7, "Presente": "P"},
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

    # Obter uma lista aleatória de jogadores
    jogadores_aleatorios = list(jogadores.keys())
    random.shuffle(jogadores_aleatorios)

    # Inicializar os times
    times = {"Time 1": {}, "Time 2": {}, "Time 3": {}}

    # Dividir os jogadores aleatórios entre os times
    for idx, jogador in enumerate(jogadores_aleatorios):
        times[f"Time {idx % 3 + 1}"][jogador] = jogadores[jogador]

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
print("Jogadores presentes:")
for jogador, dados in jogadores_presentes.items():
    print(
        f"{jogador} - Posição: {descricao_posicoes[dados['posicao']]}, Nota: {dados['nota']:.2f}"
    )

print("\nTimes:")
for time, jogadores_time in times.items():
    print(f"\n{time}:")
    for jogador, dados in jogadores_time.items():
        print(f"  - {jogador} - Posição: {descricao_posicoes[dados['posicao']]}")

print("\nSoma das notas dos times:")
for time, soma_notas in soma_notas_times.items():
    print(f"{time}: {soma_notas:.2f}")
