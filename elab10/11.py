def min(lst, n):
    if len(lst) == 1:
        return lst[0]
    if lst[0] > lst[n-1]:
        return min(lst[1:n], n-1)
    else:
        return min(lst[0:n-1], n-1)

lst = [3, 8, 2, 9, 7, 1, 5]
print(min(lst, 7))
print(min(lst, 4))
print(min(lst, 2))