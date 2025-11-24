from ex2 import merge
def merged_sorted_lists(lists,key):
    merged_lists=[]
    for lst in lists:
        merge(merged_lists,lst,key)
    return merged_lists