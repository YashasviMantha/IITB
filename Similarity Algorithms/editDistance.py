Word_one = "FLOMAX"
Word_two = "LOWMAX"

w1 = list(Word_one)
w2 = list(Word_two)

if(len(w1)>len(w2)):
    Max = w1
    low = w2
else:
    Max = w2
    low = w1

for i in Max:
    for j in low:
        if(i == j):
            Max.remove(i)
            low.remove(j)

print(len(Max))