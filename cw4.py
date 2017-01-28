import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
master_list = []
for x in range(a, b + 1):
    digits_list = [int(i) for i in str(x)]
    master_list.append(digits_list)

pwr_sum = []
output = []
for l in master_list:
    power = 1
    l_sum = 0
    for i in l:
        l_sum = l_sum + i**power
        power += 1
    pwr_sum.append(l_sum)
output = []

numbers_list = [x for x in range(a, b + 1)]
for i in range(0,len(pwr_sum)):
    if pwr_sum[i] == numbers_list[i]:
        output.append(pwr_sum[i])

print output




def sum_dig_pow(a, b):
    master_list = []
    for x in range(a, b + 1):
        digits_list = [int(i) for i in str(x)]
        master_list.append(digits_list)

    pwr_sum = []
    output = []
    for l in master_list:
        power = 1
        l_sum = 0
        for i in l:
            l_sum = l_sum + i**power
            power += 1
        pwr_sum.append(l_sum)
    output = []

    numbers_list = [x for x in range(a, b + 1)]
    for i in range(0,len(pwr_sum)):
        if pwr_sum[i] == numbers_list[i]:
            output.append(pwr_sum[i])

    return output
