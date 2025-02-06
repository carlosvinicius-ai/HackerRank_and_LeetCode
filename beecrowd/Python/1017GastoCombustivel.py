# beecrowd 1017
# https://judge.beecrowd.com/pt/problems/view/1017
# @carlosvinicius-ai

tempo = int(input())
velocidade = int(input())

gasto_combustivel = (velocidade * tempo) / 12

print(f'{gasto_combustivel:.3f}')