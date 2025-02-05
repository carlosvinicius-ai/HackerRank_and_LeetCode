# beecrowd 1008
# https://judge.beecrowd.com/pt/problems/view/1008
# @carlosvinicius-ai

number = input()
hours = input()
hourly_salary = input()

try:
    number = int(number)
    hours = int(hours)
    hourly_salary = float(hourly_salary)

    salary = hourly_salary * hours

    print(f'NUMBER = {number}')
    print(f'SALARY = U$ {salary:.2f}')

except:
    print('Error')