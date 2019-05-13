from _DUMP import me
me.mark('D')
print('Start Prog --Debug Stat')

word_one = input("Enter word 1: ")
word_two = input("Enter word 2: ")
# word_one = "night"
# word_two = "nacht"

word_one_array = list(word_one)
word_one_set = []

for i in range(len(word_one_array)-1):
	subset = word_one_array[i] + word_one_array[i+1]
	word_one_set.append(subset)

word_two_array = list(word_two)
word_two_set = []

for i in range(len(word_two_array)-1):
	subset = word_two_array[i] + word_two_array[i+1]
	word_two_set.append(subset)


print(word_one_set)
print(word_two_set)

# calculating the number of common biagrams in the sets
common_biagrams = 0
for i in word_one_set:
    for j in word_two_set:
        if(i == j):
            common_biagrams = common_biagrams + 1
# print(common_biagrams)

similarity = (2*(common_biagrams))/(len(word_one_set)+len(word_two_set))
print("similarity = ",similarity*100,"%")




print('End Prog --Debug Stat')