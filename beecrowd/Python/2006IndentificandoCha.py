# beecrowd 2006
# https://judge.beecrowd.com/pt/problems/view/2006
# @carlosvinicius-ai

T = int(input())

respostas = input().split(' ')
qtd_certo = 0

for resultado in respostas:
    resultado = int(resultado)

    if resultado == T:
        qtd_certo += 1


print(qtd_certo)