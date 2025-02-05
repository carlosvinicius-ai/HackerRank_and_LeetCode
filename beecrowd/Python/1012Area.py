# beecrowd 1012
# https://judge.beecrowd.com/pt/problems/view/1012
# @carlosvinicius-ai

values = input().split(' ')

try:
    a = float(values[0])
    b = float(values[1])
    c = float(values[2])

    triangle = a * c / 2
    circle = 3.14159 * c ** 2
    trapeze = (a+b) * c / 2
    square = b ** 2
    rectangle = a * b

    print(f'TRIANGULO: {triangle:.3f}')
    print(f'CIRCULO: {circle:.3f}')
    print(f'TRAPEZIO: {trapeze:.3f}')
    print(f'QUADRADO: {square:.3f}')
    print(f'RETANGULO: {rectangle:.3f}')

except:
    print('Error')