import os
from similarity.normalized_levenshtein import NormalizedLevenshtein
from tqdm import tqdm

normalized_levenshtein = NormalizedLevenshtein()


file_list = os.listdir("../../Final_data")
for i in file_list:
    if(not i.endswith(".csv")):
        file_list.remove(i)

files_increment = 0
for file_i in file_list:
    for file_j in file_list:
        if(file_i != file_j):

            files_increment = files_increment + 1

            file_1 = open("../../Final_data/" + file_i,'r',encoding='utf8')
            file_2 = open("../../Final_data/" + file_j,'r',encoding='utf8')

            data_1 = file_1.readlines()
            data_2 = file_2.readlines()

            for i in range(60000):
                data_1[i] = data_1[i].replace("\n",'')
                data_2[i] = data_2[i].replace("\n",'')

                data_1[i] = data_1[i].split(";")
                data_2[i] = data_2[i].split(";")

                del data_1[i][-1]
                del data_2[i][-1]


                data_1[i][1] = data_1[i][1].replace(", ",',')
                data_2[i][1] = data_2[i][1].replace(", ",',')

                data_1[i][1] = data_1[i][1].replace(",;",'')
                data_2[i][1] = data_2[i][1].replace(",;",'')


                data_1[i][1] = data_1[i][1].split(",")
                data_2[i][1] = data_2[i][1].split(",")


            sim_file = open(str(file_i.replace('.csv','')) + '-' + str(file_j.replace('.csv','')) + '.txt','w+',encoding="utf8")
            print(str(file_i.replace('.csv','')) + '-' + str(file_j.replace('.csv','')) + '.txt: ' + str(files_increment))
            for i in tqdm(range(60000)):
                for w_1 in data_1[i][1]:
                    if(w_1 != 'NULL' and w_1 != 'null' and w_1 != ''):
                        for w_2 in data_2[i][1]:
                            if(w_2 != 'NULL' and w_2 != 'null' and w_2 != ''):
                                simVal = normalized_levenshtein.similarity(w_1, w_2)
                                if(simVal>=0.85):
                                    sim_file.writelines(str(i+1) + ";" + w_1 + ";" + w_2 + ';' + str(simVal) + '\n')

            sim_file.close()