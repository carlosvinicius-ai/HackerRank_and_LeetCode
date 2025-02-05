# beecrowd 1003
# https://judge.beecrowd.com/pt/problems/view/1003
# @carlosvinicius-ai

a = input()
b = input()

try:
    a = int(a)
    b = int(b)
    soma = a + b
    print(f'SOMA = {soma}')

except ValueError:
    print('Error')