def three_way_partition(A, key=lambda x: x):
    n = len(A)
    if n < 2:
        return 0, n - 1

    P1_val = key(A[0])
    P2_val = key(A[n - 1])

    if P1_val > P2_val:
        A[0], A[n - 1] = A[n - 1], A[0]
        P1_val, P2_val = P2_val, P1_val

    lt = 1 
    gt = n - 2 
    i = 1

    while i <= gt:
        current_val = key(A[i])
        if current_val < P1_val:
            A[i], A[lt] = A[lt], A[i]
            lt += 1
            i += 1
        elif current_val > P2_val:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1 
        else:
            i += 1

    A[0], A[lt - 1] = A[lt - 1], A[0]
    A[n - 1], A[gt + 1] = A[gt + 1], A[n - 1]

    return lt, gt