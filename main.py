# Алекс Смит владеет двумя предприятиями в Нью-Йорке на улице Бродвей и Парк Авеню. Каждый месяц ему необходимо платить
# заработную плату своим сотрудникам. Зарплата работников состоит из фиксированной оплаты (оклада) и части от стоимости
# каждой продажи, совершенной сотрудником. Для удобства расчетов создана программа, Алексу Смиту нужно ввести
# название улицы, на которой расположено предприятие, оплату с одной продажи, фиксированную оплату и количество
# продаж каждого работника.

address = input('Enter the street of the enterprise: ')

try:
    def Broadway():
        with open('names1.txt') as f_in1:
            names = f_in1.readlines()
            index = 0
            while index < len(names):
                names[index] = names[index].rstrip('\n')
                index += 1

        with open('salary1.txt', 'w') as f_out1:
            pay_rate = float(input('Enter the payment from a one sale: '))
            fix_sal = float(input('Enter a fixed payment: '))
            for i in names:
                print('Enter the integer number of sales of the employee', i + ': ')
                sales = int(input())
                salary = sales * pay_rate + fix_sal
                print('Salary of employee ', i, ': $', salary, sep='', file=f_out1)

    def Park_Avenue():
        with open('names2.txt') as f_in2:
            names2 = f_in2.readlines()
            index_ = 0
            while index_ < len(names2):
                names2[index_] = names2[index_].rstrip('\n')
                index_ += 1

        with open('salary2.txt', 'w') as f_out2:
            pay_rate = float(input('Enter the payment from a one sale: '))
            fix_sal = float(input('Enter a fixed payment: '))
            for q in names2:
                print('Enter the integer number of sales of the employee', q + ': ')
                sales2 = int(input())
                salary2 = sales2 * pay_rate + fix_sal
                print('Salary of employee ', q, ': $', salary2, sep='', file=f_out2)

except ValueError:
    print('Check the correctness of the entered data')

if address == 'Broadway':
    Broadway()
elif address == 'Park Avenue':
    Park_Avenue()
else:
    print('Check the correctness of the entered data')