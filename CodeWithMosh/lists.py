names = ["John", "Josh", "Sarah", "Carrie", "Cindy"]
print(names)
print(names[0])
print(names[2])
print(names[-1])
print(names[2:])
print(names[2:4])

names[0] = "Jon"
print(names)

nums = [402, 5892, 5101, 23, 9, 4883, 4123, 43, 89]
max = nums[0]
for num in nums:
    if num > max:
        max = num
print(max)

# 2 dimensional lists (2D Lists) - each item in a list is another list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1] = 20  # how to change the value of a position

print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)


list_of_numbers = [5, 2, 7, 1, 7, 4]
list_of_numbers.append(20)  # adds 20 to list as last number in list
list_of_numbers.insert(0, 10)  # adds number 10 to first spot in list
list_of_numbers.remove(5)  # removes specific item from list
# removes last item in list - in our case 20 since it was appended above
list_of_numbers.pop()
# list_of_numbers.clear() clears the entire list out
print(f"The index for 2 is: {list_of_numbers.index(2)}")
print(list_of_numbers)
print(50 in list_of_numbers)  # returns a boolean
print(7 in list_of_numbers)
# returns number of occurences it sees this value
print(list_of_numbers.count(7))
list_of_numbers.sort()
print(list_of_numbers)
list_of_numbers.reverse()
print(list_of_numbers)

list_of_numbers2 = list_of_numbers.copy()  # makes a copy of the original list
print(list_of_numbers2)

# Example of removing duplicates from a list
practice_list = [1, 4, 62, 92, 4, 62, 99, 18, 15, 6, 1, 23, 11, 9, 99]
practice_list2 = practice_list.copy()

for x in practice_list2:
    if practice_list.count(x) > 1:
        practice_list.remove(x)
        practice_list.sort()
print(practice_list)

# Another way to solve removing duplicates; better way
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
