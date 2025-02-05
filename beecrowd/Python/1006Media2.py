# beecrowd 1006
# https://judge.beecrowd.com/pt/problems/view/1006
# @carlosvinicius-ai

a = input()
b = input()
c = input()

try:
    a = float(a)
    b = float(b)
    c = float(c)

    media = ((a * 2) + (b * 3) + (c * 5)) / 10
    print(f'MEDIA = {media:.1f}')

except ValueError:
    print('Error')