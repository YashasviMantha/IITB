#!/usr/bin/env python
# coding: utf-8

# In[21]:


word_one = input("Enter the first word")
word_two = input("Enter the second word")
# word_one = 'yashasvi'


# In[38]:


def kGram(word):
    word = list(word)
    word_set = []
    for i in range(len(word)):
        if(i == 0 or i == len(word)-1):
            word_set.append(word[i])
        else:
            word_set.append(word[i]+word[i+1])
    up = len(word_set)
    down = 1
    for i in range(len(word_set)):
        if (down < up):
            word_set[i] = str(down) + word_set[i] 
        else:
            word_set[i] =  str(up) + word_set[i]
        down += 1
        up -= 1
    return word_set


# In[42]:


word_one = 'rosmarin'
word_set = kGram(word_one)
print(word_set)

