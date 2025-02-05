# beecrowd 1010
# https://judge.beecrowd.com/pt/problems/view/1010
# @carlosvinicius-ai

#separando as entradas em uma lista, para consultar através do indice o valor passado
#o espaço em branco é usado para falar aonde acontecerá a separação do valor
values1 = input().split(' ')
values2 = input().split(' ')

try:
    qtd_parts1 = int(values1[1])
    unity_price1 = float(values1[2])
    qtd_parts2 = int(values2[1])
    unity_price2 = float(values2[2])

    total = (qtd_parts1 * unity_price1) + (qtd_parts2 * unity_price2)

    print(f'VALOR A PAGAR: R$ {total:.2f}')

except:
    print('Error')
