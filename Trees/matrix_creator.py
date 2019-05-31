from numpy import genfromtxt
import math
import numpy

file = open("CLWE_angular.csv",'rt')
data = file.readlines()
data = list(data)
ids = []
for i in range(len(data)-1):
    row = data[i+1]
    row = row.split(',')
    ids.append(row[0])

my_data = genfromtxt('CLWE_angular.csv', delimiter=',')


my_data = my_data.tolist()
del my_data[0]
for i in range(len(my_data)):
    del my_data[i][0]    

for i in range(len(my_data)):
    for j in range(len(my_data[i])):
        if(math.isnan(my_data[i][j])):
            my_data[i][j] = 0

my_data = numpy.array(my_data)

data = my_data.T + my_data

file_a = open('infile','w+')

for i in range(len(data)):
    file_a.write(str(ids[i]+'        \t'))
    for j in range(len(data[i])):
        string = str(data[i][j]) + "\t"
        file_a.write(string)
    file_a.write('\n')

file_a.close()