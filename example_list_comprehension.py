lst = [x for x in range(10) if x % 2 == 0]
print(lst)
# Output: [0, 2, 4, 6, 8]

lst2 = [[x for x in range(10) if x % 2 == 0] for _ in range(5)]
print(lst2)
# Output: [[0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8]]

print(sum([i for i in range(1000) if i %
      3 == 0 or i % 5 == 0]))  # Output: 233168

print([x for x in range(1, 11) if x % 2 == 0])
