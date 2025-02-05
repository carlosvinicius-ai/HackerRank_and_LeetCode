# beecrowd 1005
# https://judge.beecrowd.com/pt/problems/view/1005
# @carlosvinicius-ai

a = input()
b = input()

try:
    a = float(a)
    b = float(b)
    media = ((a * 3.5) + (b * 7.5)) / 11
    print(f'MEDIA = {media:.5f}')

except ValueError:
    print('Error')