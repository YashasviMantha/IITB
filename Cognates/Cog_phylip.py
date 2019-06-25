file = open("Martix_cog.txt",'r+')
distance = file.readlines()

ids_file = open("id_order_cog.txt",'r+')
ids = ids_file.readlines()

ids = ids[0]
ids = ids.split('\t')

phylip = open("phylip_input_cog.txt",'w+')

for i in range(len(distance)):
    phylip.writelines(ids[i] + '\t' + distance[i])
phylip.close()