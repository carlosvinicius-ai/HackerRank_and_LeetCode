# beecrowd 1013
# https://judge.beecrowd.com/pt/problems/view/1013
# @carlosvinicius-ai

values = input().split(' ')

try:
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])

    maior_ab = (a + b + abs(a-b)) // 2

    if c > maior_ab:
        maior_ab = c

    print(f'{maior_ab} eh o maior')


except:
    print('Error')

