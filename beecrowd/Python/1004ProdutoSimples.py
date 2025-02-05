# beecrowd 1004
# https://judge.beecrowd.com/pt/problems/view/1004
# @carlosvinicius-ai

a = input()
b = input()

try:
    a = int(a)
    b = int(b)
    prod = a * b
    print(f'PROD = {prod}')

except ValueError:
    print('Error')