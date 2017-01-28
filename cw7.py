iterable = "AABBcDDDEf"
lst = list(iterable)
lst2 = []
print "length: ", len(lst)
if len(lst) > 0:
    lst2.append(lst[0])
    for x in range(1, len(lst)):
        if lst[x] != lst[x - 1]:
            lst2.append(lst[x])
else: lst2 = []
print lst2



def unique_in_order(iterable):
    lst = list(iterable)
    lst2 = []
    print "length: ", len(lst)
    if len(lst) > 0:
        lst2.append(lst[0])
        for x in range(1, len(lst)):
            if lst[x] != lst[x - 1]:
                lst2.append(lst[x])
    else: lst2 = []
    return lst2
