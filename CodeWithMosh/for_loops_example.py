for item in 'Python':
    print(item)
print('Done')

for item in ['Josh', 'Cindy', 'Banner', 'Davis', 'Jovi']:
    print(item)
print('Done')

for item in [1, 2, 3, 5, 343, 3424, 2663, 77342]:
    print(item)
print('Done')

for item in range(10):
    print(item)
print('Done')

for item in range(5, 10):
    print(item)
print('Done')

for item in range(5, 10, 2):  # step size (moves 2 steps forward)
    print(item)
print('Done')


prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f"Total: {total}")

squares = []
for i in range(10):
    squares.append(i * 1)
print(squares)

squares2 = [i * 1 for i in range(10)]  # More efficient and uses less memory
print(squares2)
