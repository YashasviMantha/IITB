assamese_file = 'oriya.csv'

file = open('oriya.csv','r+',encoding='utf8')
data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].strip('\n')
    data[i] = data[i].replace('"','')
    data[i] = data[i].replace(';NULL','')
    data[i] = data[i].split(";")
    data[i][-1] = data[i][-1].lower()
    data[i] = ';'.join(data[i])
    data[i] = data[i] + '\n'
    print('w/r')


as_file = open('Cleaned/or.csv','w+',encoding='utf8')

for i in range(len(data)):
    as_file.writelines(data[i])
    print('w')
as_file.close()
file.close()
