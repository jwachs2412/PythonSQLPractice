weight = int(input('Enter your weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 0.454
    print(f'You are {converted:.2f} kilos')
else:
    converted = weight / 0.454
    print(f'You are {converted:.2f} pounds')
