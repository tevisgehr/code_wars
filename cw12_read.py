import csv

n = 1972

n_dict = {}

with open('cw12.csv', 'rb') as csvfile_r:
    csvreader = csv.reader(csvfile_r,delimiter=',')
    for row in csvreader:
        n_dict[int(row[0])] = row[1]

print n_dict[n]
