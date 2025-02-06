# beecrowd 1020
# https://judge.beecrowd.com/pt/problems/view/1020
# @carlosvinicius-ai

idade = int(input())

anos = idade // 365
resto = idade % 365
meses = resto // 30
dias = resto % 30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')