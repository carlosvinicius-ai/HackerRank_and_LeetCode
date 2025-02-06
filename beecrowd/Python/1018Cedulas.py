# beecrowd 1018
# https://judge.beecrowd.com/pt/problems/view/1018
# @carlosvinicius-ai

dinheiro = int(input())
notas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

while dinheiro > 0:
    if dinheiro >= 100:
        notas[100] += 1
        dinheiro -= 100
        continue

    elif dinheiro >= 50:
        notas[50] += 1
        dinheiro -= 50
        continue

    elif dinheiro >= 20:
        notas[20] += 1
        dinheiro -= 20
        continue

    elif dinheiro >= 10:
        notas[10] += 1
        dinheiro -= 10
        continue

    elif dinheiro >= 5:
        notas[5] += 1
        dinheiro -= 5
        continue

    elif dinheiro >= 2:
        notas[2] += 1
        dinheiro -= 2
        continue

    elif dinheiro >= 1:
        notas[1] += 1
        dinheiro -= 1
        continue


for k, v in notas.items():
    print(f'{v} nota(s) de R$ {k},00')