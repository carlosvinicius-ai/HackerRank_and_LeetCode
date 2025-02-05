PI = 3.14159
raio = input()

try:
    raio = float(raio)
    area = PI * raio**2
    print(f'A={area:.4f}')

except ValueError:
    print('Error')
