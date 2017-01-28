n=1165

results_list = []
s = (n**2+n)/2
for x in range(1,n):
    if (s - x)%(x+1) == 0:
        a = x
        b = (s - a)/(a+1)
        if b < n:
            results_list.append((a,b))

print results_list









def removNb(n):
    results_list = []
    s = (n**2+n)/2
    for x in range(1,n):
        if (s - x)%(x+1) == 0:
            a = x
            b = (s - a)/(a+1)
            if b < n:
                results_list.append((a,b))

    return results_list
