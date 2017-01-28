import csv
a = 1000
b = 2000

n_dict = {}
n_list = []
for n in range(a,b+1):
    results_list = []
    n_sum = sum(range(1,n+1))

    for x in range(1,n+1):
        for y in range(1,n+1):
            if x*y == n_sum-x-y:
                results_list.append((x,y))
    n_dict[n] = results_list
    n_list.append([n,results_list])
print n_dict

with open('cw12.csv', 'wb') as csvfile_w:
    csvwriter = csv.writer(csvfile_w,delimiter=',')
    for row in n_list:
        csvwriter.writerow(row)



def removNb(n):
    results_list = []
    n_sum = sum(range(1,n+1))

    for x in range(1,n+1):
        for y in range(1,n+1):
            if x*y == n_sum-x-y:
                results_list.append((x,y))

    return results_list
