import os
from similarity.normalized_levenshtein import NormalizedLevenshtein
from tqdm import tqdm

normalized_levenshtein = NormalizedLevenshtein()


os.listdir("../../Final_data")

file_1 = open("../../Final_data/as.csv",'r',encoding='utf8')
file_2 = open("../../Final_data/bn.csv",'r',encoding='utf8')

data_1 = file_1.readlines()
data_2 = file_2.readlines()

for i in range(60000):
    data_1[i] = data_1[i].replace("\n",'')
    data_2[i] = data_2[i].replace("\n",'')

    data_1[i] = data_1[i].split(";")
    data_2[i] = data_2[i].split(";")

    del data_1[i][-1]
    del data_2[i][-1]

sim_file = open("as-bn.txt",'w+',encoding="utf8")

for i in tqdm(range(60000)):
    for w_1 in data_1[i][1]:
        if(w_1 != 'NULL' and w_1 != 'null'):
            for w_2 in data_2[i][1]:
                if(w_2 != 'NULL' and w_2 != 'null'):
                    simVal = normalized_levenshtein.similarity(w_1, w_2)
                    if(simVal>=0.95):
                        sim_file.writelines(str(i) + ";" + w_1 + ";" + w_2 + ';' + str(simVal))

sim_file.close()