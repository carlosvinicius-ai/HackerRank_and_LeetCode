# beecrowd 1007
# https://judge.beecrowd.com/pt/problems/view/1007
# @carlosvinicius-ai

a = input()
b = input()
c = input()
d = input()

try:
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    diferenca = (a * b) - (c*d)

    print(f'DIFERENCA = {diferenca}')

except ValueError:
    print('Error')