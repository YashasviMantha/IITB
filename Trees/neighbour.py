from _DUMP import me
# me.mark('D')
me.importfix('C:/Users/Zara/Desktop/Internship/Work/Trees')
print('Start Prog --Debug Stat')


# distance_mat Preprocessing----------------------

# file = input("Enter the name of the file which contains the distance matrix: ")
file = 'distance.txt'
distance_mat = open(file,'r')
distance_mat = distance_mat.readlines()

for i in range(len(distance_mat)):
    distance_mat[i] = distance_mat[i].strip("\n")
    distance_mat[i] = distance_mat[i].split(" ")

for i in range(len(distance_mat)):
    for j in range(1, len(distance_mat[i])):
        distance_mat[i][j] = int(distance_mat[i][j])
for i in range(len(distance_mat)):
    print(distance_mat[i])

# Algorithm implementation--------------------------------------

# Finding the Ui Values for all the tips
ui = []
n = len(distance_mat)
for i in range(n):
    sum_u = 0
    for j in range(1,n+1):
        sum_u = sum_u + distance_mat[i][j]
    sum_u = sum_u / (n-2)
    ui.append(sum_u)

# Calculating D*
# D* = Dij - Ui - Uj

d_star = []
d_star_row = [0,0,0,0]
for i in range(n):
    d_star_row = [0,0,0,0]
    for j in range(1,n+1):
        if(distance_mat[i][j] == 0):
            d_star_row[j-1] = 0
        else:
            d_star_row[j-1] = distance_mat[i][j] - ui[i] - ui[j-1]
    d_star.append(d_star_row)

def minium_ele(matrix):
    min = 9999
    for i in range(len(matrix)):
        for j in range(1,len(matrix[i])+1):
            if(matrix[i][j-1] != 0):
                if(min>matrix[i][j-1]):
                    min = matrix[i][j-1]
                    row = i
                    col = j
    return min,i,j

print(minium_ele(d_star))



print('End Prog --Debug Stat')