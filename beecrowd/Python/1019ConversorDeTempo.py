# beecrowd 1019
# https://judge.beecrowd.com/pt/problems/view/1019
# @carlosvinicius-ai

entrada = int(input())

horas = entrada // 3600
resto = entrada % 3600
minutos = resto // 60
resto %= 60
segundos = resto

print(f'{horas}:{minutos}:{segundos}')