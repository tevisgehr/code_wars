def solution(number):
    naturals = []
    sum_naturals = 0
    for i in range (1, number): naturals.append(i)
    for x in naturals:
        if x % 3 == 0 or x % 5 == 0: sum_naturals += x

    return sum_naturals
