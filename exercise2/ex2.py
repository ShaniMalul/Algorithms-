def merge(a,b,key):
    if is_sorted(a,key) or is_sorted(b,key):
        return None
    merged_array=[]
    i,j=0,0
    while i < len(a) and j < len(b):
        if key(a[i])<= key(b[j]):
            merged_array.append(a[i])
            i+=1
        else:
            merged_array.append(b[j])
            j+=1
    while i < len(a):
        merged_array.append(a[i])
        i+=1
    while j < len(b):
        merged_array.append(b[j])
        j+=1
    return merged_array


def is_sorted(a,key):
    for i in range(len(a)-1):
        if key(a[i]) > key(a[i+1]):
            return False
    return True
    