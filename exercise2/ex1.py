from random_tuples import create_random_tuples

data = create_random_tuples(5, 3, [int, float, str])

sorted_by_int = sorted(data, key=lambda x: x[0])
print("Sort by the first place", sorted_by_int)

sorted_by_float = sorted(data, key=lambda x: x[1])
print("Sort by the second place", sorted_by_float)

sorted_by_string = sorted(data, key=lambda x: x[2])
print("Sort by the third place", sorted_by_string)