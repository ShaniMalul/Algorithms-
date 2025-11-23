def find_min(a, key):
    if not a:
        raise ValueError("List is empty")

    min_item = a[0]
    max_item = a[0]
    min_key = key(a[0])
    max_key = key(a[0])

    for item in a[1:]:
        k = key(item)
        if k < min_key:
            min_key = k
            min_item = item
        if k > max_key:
            max_key = k
            max_item = item

    return min_item, max_item

from random_tuples import create_random_tuples

a = create_random_tuples(5, 3, [int, float, str])

mn, mx = find_min(a, key=lambda x: x[1])
print("min:", mn)
print("max:", mx)