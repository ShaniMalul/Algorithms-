def insertion_sort(a, key):
    for i in range(1, len(a)):
        current = a[i]
        current_key = key(current)
        j = i - 1

        while j >= 0 and key(a[j]) > current_key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = current

if __name__ == "__main__":
    from random_tuples import create_random_tuples

    a1 = create_random_tuples(5, 3, [int, float, str])
    a2 = create_random_tuples(5, 3, [int, float, str])
    a3 = create_random_tuples(5, 3, [int, float, str])

    print("Before sorting (list 1):", a1)
    insertion_sort(a1, key=lambda x: x[0])
    print("After sorting by index 0:", a1, "\n")

    print("Before sorting (list 2):", a2)
    insertion_sort(a2, key=lambda x: x[1])
    print("After sorting by index 1:", a2, "\n")

    print("Before sorting (list 3):", a3)
    insertion_sort(a3, key=lambda x: x[2])
    print("After sorting by index 2:", a3, "\n")