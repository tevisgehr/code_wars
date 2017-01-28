import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




ints = [7,4,4,9,1,1,1,2,7,4,7,9,9,4,5,10,6,1,3,9,8,0,0,1,1,6,3,7,10,6,4,0,2,6,3,9,5,2,10,10,6,6,7,7,10]
#ints = [1,5,3,2,5,7,2,4,1,9]
s = 14
result = []
match_list = []
for x in range(0, len(ints)):
	for y in range(x + 1, len(ints)):
		if ints[x] + ints[y] == s:
			match_list.append([x, y, ints[x], ints[y], max(x,y)])

df = pd.DataFrame(data = match_list, columns = ["X", "Y", "Ints[X]", "Ints[Y]", "Max_Index"])
df = df.sort_values(["Max_Index","X","Y"])
print df
result = list(df.iloc[0])
result = result[2:-1]
print result




def sum_pairs(ints, s):
    #import pandas as pd
    result = []
    match_list = []
    for x in range(0, len(ints)):
        for y in range(x + 1, len(ints)):
            if ints[x] + ints[y] == s:
                match_list.append([x, y, ints[x], ints[y], max(x,y)])

    #df = pd.DataFrame(data = match_list, columns = ["X", "Y", "Ints[X]", "Ints[Y]", "Max_Index"])
    #df = df.sort_values(["Max_Index","X","Y"])
    #print df
    #result = list(df.iloc[0])
    #result = result[2:-1]
    #print result
    return result
