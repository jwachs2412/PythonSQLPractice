def sort_by_mark(my_class):
    return sorted(my_class, key=lambda item: item[0], reverse=True)


def sort_by_name(my_class):
    return sorted(my_class, key=lambda item: item[1])


# Uncomment the following lines as needed
# if you want to test your implementation a bit:

my_class = [(50, "Alan"), (75, "Ada"), (25, "Shannon"), (90, "Craig")]

print(sort_by_mark(my_class))
print(sort_by_name(my_class))
