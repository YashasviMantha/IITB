dist_file = 'cog_dist_fixed.txt'

dist_file = open(dist_file,'r+')
distance = dist_file.readlines()
dist_file.close()

for i in range(len(distance)):
    distance[i] = distance[i].strip('\n')
    distance[i] = distance[i].replace(':','-')
    distance[i] = distance[i].split('-')
    distance[i][2] = float(distance[i][2])
    distance[i][2] = f"{distance[i][2]:.4f}"
    distance[i][2] = float(distance[i][2])

distance = sorted(distance, key=lambda distance: str(distance[0])+str(distance[1]))

file = open('Martix_cog.txt','w+')

ids = []
for i in range(14):
    ids.append(distance[i][1])

id_file = open('id_order_cog.txt','w+')
for i in ids:
    id_file.writelines(i + "\t")
id_file.close()

for i in range(len(distance)):
    if(i%14 == 0):
        if(i != 0):
            file.writelines('\n')
    else:
        file.writelines('\t ')
    file.writelines(str(distance[i][2]))
file.close()