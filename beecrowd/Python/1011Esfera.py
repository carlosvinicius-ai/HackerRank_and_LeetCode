# beecrowd 1011
# https://judge.beecrowd.com/pt/problems/view/1011
# @carlosvinicius-ai

raio = input()
PI =  3.14159

try:
    raio = float(raio)
    volume = (4/3) * PI * raio ** 3

    print(f'VOLUME = {volume:.3f}')

except:
    print('Error')