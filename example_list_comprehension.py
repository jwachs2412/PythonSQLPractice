lst = [x for x in range(10) if x % 2 == 0]
print(lst)
# Output: [0, 2, 4, 6, 8]

lst2 = [[x for x in range(10) if x % 2 == 0] for _ in range(5)]
print(lst2)
# Output: [[0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8]]
