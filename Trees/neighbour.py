from _DUMP import me
# import igraph

# me.mark('D')
me.importfix('C:/Users/Zara/Desktop/Internship/Work/Trees')
print('Start Prog --Debug Stat')


# distance_mat Preprocessing----------------------

# file = input("Enter the name of the file which contains the distance matrix: ")
def pre_pross():
    file = 'distance.txt'
    distance_mat = open(file,'r')
    distance_mat = distance_mat.readlines()

    for i in range(len(distance_mat)):
        distance_mat[i] = distance_mat[i].strip("\n")
        distance_mat[i] = distance_mat[i].split(" ")

    for i in range(len(distance_mat)):
        for j in range(1, len(distance_mat[i])):
            distance_mat[i][j] = int(distance_mat[i][j])
    # for i in range(len(distance_mat)):
    #     print(distance_mat[i])
    return distance_mat
# Algorithm implementation--------------------------------------

# Finding the Ui Values for all the tips
def ui_cal(matrix):
    ui_local = []
    n = len(matrix)
    for i in range(n):
        sum_u = 0
        for j in range(1,n+1):
            sum_u = sum_u + matrix[i][j]
        sum_u = sum_u / (n-2)
        ui_local.append(sum_u)

    return ui_local

# Calculating D*
# D* = Dij - Ui - Uj
def d_star_cal(matrix, ui):
    n = len(matrix)
    d_star = []
    d_star_row = [0] * n
    # d_star_row = [0,0,0,0,0,0]
    for i in range(n):
        d_star_row = [0] * n
        # d_star_row = [0,0,0,0,0,0]
        for j in range(1,n+1):
            if(matrix[i][j] == 0):
                d_star_row[j-1] = 0
            else:
                d_star_row[j-1] = matrix[i][j] - ui[i] - ui[j-1]
        d_star.append(d_star_row)
    return d_star

def minium_ele(matrix):
    min = 9999
    for i in range(len(matrix)):
        for j in range(1,len(matrix[i])+1):
            if(matrix[i][j-1] != 0):
                if(min>matrix[i][j-1]):
                    min = matrix[i][j-1]
                    row = i
                    col = j
    return min,row,col-1

def limb_length(dist_mat, ui, i, j):
    i_limb = (0.5 *(ui[i] - ui[j]))
    i_limb = i_limb + 0.5 * float(dist_mat[i][j+1])

    j_limb = (0.5 *(ui[j] - ui[i]))
    j_limb = j_limb + 0.5 * float(dist_mat[i][j+1])

    return i_limb, j_limb

def distance_updater(distance_mat, node_i, node_j):
    # print("Deleting",node_i,node_j)
    distance_mat_local = distance_mat
    del distance_mat_local[node_i]
    del distance_mat_local[node_j-1]
    for i in range(len(distance_mat_local)):
        del distance_mat_local[i][node_i+1]
        del distance_mat_local[i][node_j]

    for i in range(len(distance_mat_local)):
        node_k = ord(distance_mat_local[i][0])%32
        for j in range(len(distance_mat_local)):
            distance_mat_local[i][j+1] = 0.5 * (distance_mat[node_i][node_k-1] + distance_mat[node_j][node_k-1] - distance_mat[node_i][node_j+1])
    print(node_k)
    return distance_mat_local

# if __name__ == '__main__':
#     main()
# def main():

distance_mat = pre_pross()
ui = ui_cal(distance_mat)
d_star = d_star_cal(distance_mat, ui)
neighbours = minium_ele(d_star)
limbs = limb_length(distance_mat, ui, neighbours[1], neighbours[2])
# print(limbs)l
print(distance_updater(distance_mat, neighbours[1], neighbours[2]))
# print(distance_updater(distance_mat, 2, 3))

    # print(ui)
for i in range(len(distance_mat)):
        print(distance_mat[i])



print('End Prog --Debug Stat')