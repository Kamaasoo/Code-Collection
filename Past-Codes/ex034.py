salary = float(input('Type your actual salary:R$ '))

if salary > 1250:
    print(f'The salary will be: :${(salary * 10) / 100 + (salary):.2f}')
else:
    print(f'The salary will be::${(salary * 15) / 100 + (salary):.2f}')
