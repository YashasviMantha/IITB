import os
file_list = os.listdir("WNdatanon/")

for j in range(len(file_list)):
    file_name = str(file_list[j])
    file_name = file_name.replace("'","")
    dir_file = "WNdatanon/" + file_name
    file = open(dir_file,"r+",encoding='utf8')
    data = file.readlines()

    for i in range(len(data)):
        data[i] = data[i].strip('\n')
        data[i] = data[i].replace('"','')
        data[i] = data[i].replace(';NULL','')
        data[i] = data[i].split(";")
        data[i][-1] = data[i][-1].lower()
        data[i] = ';'.join(data[i])
        data[i] = data[i] + '\n'
        print('processing- ',file_list[j],end='')
    print()

    cleaned_file =  str(file_list[j])
    as_file = open(cleaned_file,"w+",encoding='utf8')
    for i in range(len(data)):
        as_file.writelines(data[i])
        print('w',end='')