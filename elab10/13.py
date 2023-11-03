def flatten_list(lst):
    if len(lst) == 0:
        return []
    if isinstance(lst[0], list):
        return set(flatten_list(lst[0])).union(set(flatten_list(lst[1:])))
    else:
        return set([(lst[0])]).union(flatten_list(lst[1:]))
    
print(flatten_list(['1', "hello", True, 7]))
print(flatten_list([1, 2, [[2], [3, 4], 5], 4, [3], [[4]]]))