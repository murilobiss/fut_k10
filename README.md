# Sistema de Gerenciamento de Times de Futebol

## Descrição

Este sistema gerencia uma lista de jogadores de futebol e permite realizar diversas operações, incluindo:

- Impressão de informações de um jogador específico.
- Contagem de jogadores por posição.
- Atualização da nota de um jogador.
- Adição de um novo jogador.
- Separação aleatória dos jogadores em times.

## Utilização

### Funções Principais

1. **Imprimir Informações do Jogador**
   - Utilize a função `imprimir_informacoes_jogador(jogador)` passando o nome do jogador como argumento para imprimir detalhes sobre ele.

2. **Contar Jogadores por Posição**
   - Utilize a função `contar_jogadores_por_posicao(jogadores)` para obter uma contagem de jogadores por posição.

3. **Atualizar Nota de um Jogador**
   - Utilize a função `atualizar_nota(jogadores)` para atualizar a nota de um jogador existente.

4. **Adicionar Novo Jogador**
   - Utilize a função `adicionar_jogador(jogadores)` para adicionar um novo jogador à lista.

5. **Separar Times Aleatoriamente**
   - Utilize a função `separar_times(jogadores_presentes)` para dividir aleatoriamente os jogadores presentes em três times.

### Exemplo de Uso

```python
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

