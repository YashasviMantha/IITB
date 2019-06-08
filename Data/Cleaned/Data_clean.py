import os
from tqdm import tqdm
file_list_full = os.listdir()

file_list = []
for i in range(len(file_list_full)):
    if(file_list_full[i].endswith(".csv")):
        file_list.append(file_list_full[i])

for i in range(len(file_list)):
    print("processing ",file_list[i])
    file = open(file_list[i],'r',encoding='utf8')
    data = file.readlines()
    for j in range(len(data)):
        data[j] = data[j].strip('\n')
        data[j] = data[j].split(';')
    new_file = open("./ABC/"+str(file_list[i].replace(".csv","") + 'Normalised.csv'),'w+',encoding='utf8')
    m = 0
    for k in tqdm(range(1,60000)):
        if(k<len(data)):
            if(data[m][0]==str(k)):
                string_data = ';'.join(data[m])
                new_file.writelines(string_data+'\n')
                m = m + 1
                # print("NOT",end='')
            else:
                new_file.writelines(str(k)+';NULL;NULL;NULL;NULL\n')
                # m = m - 1
                # print("OK",end='')
        else:
            new_file.writelines(str(k)+';NULL;NULL;NULL;NULL\n')
