from _DUMP import me
import csv


me.mark('D')
print('Start Prog --Debug Stat')

input_rows = []

for i in range(64):
    binary = bin(i)[2:]
    binary = binary.zfill(6)
    binary = list(binary)
    input_rows.append(binary)

with open("Input.csv","w+", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(input_rows)

file.close()

output_rows = []
for i in range(64):
    a = 0
    for j in range(6):
        a = int(input_rows[i][j]) ^ a

    a = str(a)
    output_rows.append(a)

with open("Output.csv", "w+", newline='') as fileOut:
    write = csv.writer(fileOut)
    write.writerows(output_rows)


# for i in range(63):
#     print(i,"\t",input_rows[i])

print('End Prog --Debug Stat')
