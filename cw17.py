'''
cd '.\Python\TevisPrograms\Code Wars'
python
from cw17 import *
find_nb(10252519345963644753026)


https://www.codewars.com/kata/build-a-pile-of-cubes/train/python
Your task is to construct a building which will be a pile of n cubes. The cube
at the bottom will have a volume of n^3, the cube above will have volume of
(n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find
the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb) will be an integer m
and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if
such a n exists or -1 if there is no such n.
'''
'''
#n_long = long((1.0/2.0)*(math.sqrt(8.0*math.sqrt(m)+1.0)-1))
#n_float = float((1.0/2.0)*(math.sqrt(8.0*math.sqrt(m)+1.0)-1))
#getcontext().prec = 28
#n=Decimal(2.0)*Decimal(math.sqrt(Decimal(8.0)))
#n=Decimal(math.sqrt(Decimal(2)))
##n=Decimal(1.0/2.0)*(Decimal(math.sqrt(8.0*math.sqrt(m)+Decimal(1.0)))-Decimal(1.0))
#n=Decimal(Decimal(1.0000000000000000000000000000000000000001)/Decimal(2.00000000000000000000000000000000000000001))*(Decimal(math.sqrt(Decimal(8.0)*Decimal(math.sqrt(m))+Decimal(1.0)))-Decimal(1.0))
#Decimal(math.sqrt(Decimal(8.0)*Decimal(math.sqrt(m))+Decimal(1.0)))-Decimal(1.0)

n = Decimal(1.0/2.0)*Decimal(Decimal(8.0)*Decimal(Decimal(Decimal(m)).sqrt())+Decimal(1.0)).sqrt()-Decimal(1.0)
n = (1.0/2.0)*(math.sqrt(8.0*math.sqrt(m)+1.0)-1)



#n = Decimal(1.0/2.0)*Decimal(8.0*Decimal(Decimal(m).sqrt())+1.0).sqrt()-Decimal(1.0)
#Decimal(math.sqrt(Decimal(8.0)*Decimal(math.sqrt(m))+Decimal(1.0)))
#print type(n)
#print "n_long:{0}\nn_float:{1}\nn:{2}".format(n_long,n_float,n)
print n
print m
'''
import math
from decimal import *

def find_nb(m):
    if Decimal(m).sqrt()%1 == 0:
        return int((1.0/2.0)*(math.sqrt(8.0*math.sqrt(m)+1.0)-1))
    else:
        return -1
