from _DUMP import me
# me.mark('D')
me.importfix('C:/Users/Zara/Desktop/Internship/Work/Trees')
print('Start Prog --Debug Stat')



# file = input("Enter the name of the file which contains the distance matrix: ")
file = 'distance.txt'
data = open(file,'r')
data = data.readlines()

for i in range(len(data)):
    data[i] = data[i].strip("\n")
    data[i] = data[i].split(" ")

for i in range(len(data)):
    for j in range(1, len(data[i])):
        data[i][j] = int(data[i][j])
for i in range(len(data)):
    print(data[i])


print('End Prog --Debug Stat')