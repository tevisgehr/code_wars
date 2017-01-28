


results = {1}
done_list = []
for x in results:
    if x not in done_list:
        done_list.append(x)
        if (2*x+1) not in results:
            y = 2*x+1
            results=results|{y}
        if (3*x+1) not in results:
            y = 3*x+1
            results=results|{y}
        if len(results) > 10000:
            break
print results
print "Length: ", len(results)




def dbl_linear(n):
    results = {1}
    done_list = []
    print n
    for x in results:
        if x not in done_list:
            done_list.append(x)
            if (2*x+1) not in results:
                results.update(2*x+1)
            if (3*x+1) not in results:
                results.update(3*x+1)
            if len(results) > 5*n:
                break

    return results[n]





def dbl_linear(n):
    results = [1]
    done_list = []

    for x in results:
        if x not in done_list:
            done_list.append(x)
            if (2*x+1) not in results:
                results.append(2*x+1)
            if (3*x+1) not in results:
                results.append(3*x+1)
            if len(results) > n:
                break
    results = sorted(results)
    return results[n]


def dbl_linear(n):
    results = [1]
    done_list = []
    print n
    for x in results:
        if x not in done_list:
            done_list.append(x)
            if (2*x+1) not in results:
                results.append(2*x+1)
            if (3*x+1) not in results:
                results.append(3*x+1)
            if len(results) > 4.6*n:
                break
    results = sorted(results)
    return results[n]
