price=0
tickets=int(input('Введите необходимое количество билетов: '))

for age in range(tickets):
    age = int(input('Введите возраст посетителя: '))
    if age < 18:
        price += 0
    elif 18 <= age <= 25:
        price += 990
    elif age > 25:
        price += 1390

if price == 0:
    print('Проход на конференцию бесплатно')
else:
    print('Общее количество билетов ', tickets, 'шт.')
    print('Стоимость билетов составляет ', price, 'руб.')

if tickets > 3:
    discount = price * 10 / 100
    print('Скидка составила = ', "%.2f" % discount, 'руб.')
    print('С учётом скидки к оплате ', "%.2f" % (price - discount), 'руб.')

if tickets <= 3:
    not_discount = price
    print('Общая сумма к оплате ', "%.2f" % not_discount, 'руб.')