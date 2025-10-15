price_of_house = 1000000
good_credit = False

if good_credit:
    down_payment = 0.1 * price_of_house
else:
    down_payment = 0.2 * price_of_house
print(f'Down payment: ${down_payment:.2f}')
