assamese_file = 'NLP/Data/WNData/tbl_all_assamese_synset_data.csv'

file = open(assamese_file,'r+')
data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].strip('\n')
    data[i] = data[i].replace('"','')
    data[i] = data[i].replace(';NULL','')
    data[i] = data[i].split(";")
    data[i][-1] = data[i][-1].lower()
    data[i] = ';'.join(data[i])


as_file = open('NLP/Data/Cleaned/as.csv','w+')

for i in range(len(data)):
    as_file.writelines(data[i])
