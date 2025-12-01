def lomuto_partition(a, key):
    pivot = a[-1]                
    pivot_key = key(pivot)
    i = -1                         

    for j in range(len(a) - 1):
        if key(a[j]) <= pivot_key:
            i += 1
            a[i], a[j] = a[j], a[i]
    
    a[i + 1], a[-1] = a[-1], a[i + 1]
    return i + 1                 


def hoare_partition(a, key):
    pivot = a[0]       
    pivot_key = key(pivot)
    
    i = -1               
    j = len(a)            
    
    while True:
        j -= 1
        while key(a[j]) > pivot_key:
            j -= 1

        i += 1
        while key(a[i]) < pivot_key:
            i += 1
        
        if i >= j:
            return j
        
        a[i], a[j] = a[j], a[i]
        