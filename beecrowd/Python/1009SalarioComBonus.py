# beecrowd 1009
# https://judge.beecrowd.com/pt/problems/view/1009
# @carlosvinicius-ai

name = input()
salary = input()
total_sales = input()

try:
    salary = float(salary)
    total_sales = float(total_sales)

    final_salary = (total_sales * 0.15) + salary
    print(f'TOTAL = R$ {final_salary:.2f}')

except:
    print('Error')