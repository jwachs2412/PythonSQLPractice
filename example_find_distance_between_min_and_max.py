def dist(points):
    smallest_num = min(points)
    largest_num = max(points)
    distance = largest_num - smallest_num
    return distance


# Example usage
num_list = [10, 3, 6, 2, 8, 4]
calculated_distance = dist(num_list)
print(
    f"The distance between the smallest and largest numbers is: {calculated_distance}")

num_list2 = [1, 5, 9, -2, 7]
calculated_distance2 = dist(num_list2)
print(
    f"The distance between the smallest and largest numbers is: {calculated_distance2}")

num_list3 = [42, 100384, 4312, 93892, 38, 2,
             4959393, -3943, 0, 583, 90384, 239843]
calculated_distance3 = dist(num_list3)
print(
    f"The distance between the smallest and largest numbers is: {calculated_distance3}")

num_list4 = [1, 2]
calculated_distance4 = dist(num_list4)
print(
    f"The distance between the smallest and largest numbers is: {calculated_distance4}")
