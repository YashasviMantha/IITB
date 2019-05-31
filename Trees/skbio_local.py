from skbio.tree import nj
from skbio import DistanceMatrix

# def pre_pross():
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
    del distance_mat[i][0]

# return distance_mat
# print(distance_mat)

ids = list('abcd')

dm = DistanceMatrix(distance_mat,ids)

tree = nj(dm)
print(tree.ascii_art())

new_a = nj(dm, result_constructor=str)
# for i in range(len(new_a)):
#         print(new_a[i])
print(new_a)