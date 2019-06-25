import os
file = os.listdir()

for i in file:
    if(not i.endswith(".txt")):
        file.remove(i)

for file_i in file:
    file_open = open(file_i,'r',encoding='utf8')
    data = file_open.readlines()

    for lines in range(len(data)):
        data[lines] = data[lines].split(";")

    for lines in range(len(data)):
        if(len(data[lines]) != 4):
            print(file_i + "--" + str(lines) + '--' + str(data[lines]))

    file_open.close()