import os
from tqdm import tqdm

files = os.listdir("../../Cognates")

for i in files:
    if(not i.endswith(".txt")):
        files.remove(i)

distance_file = open("cog_dist.txt",'w+')

for file_i in tqdm(files):

    # print(file_i)

    single_file = open("../../Cognates/" + file_i,'r',encoding='utf8')
    data = single_file.readlines()


    for line in range(len(data)):
        data[line] = data[line].replace("\n",'')
        data[line] = data[line].split(';')

    sim = 0
    for line in range(len(data)):
        sim = sim + float(data[line][3])
    sim = sim / len(data)

    distance_file.writelines(file_i.replace('.txt','') + ':' + str(sim) + '\n')

    single_file.close()

distance_file.close()