#hw==printing how many consonant letters are in my name and surname
#first way
x = 'dato jatchvadze'
y = 0
for char in x:
    if char in  'bcdfghjklmnpqrstvwxyz':
        y += 1
print(y)
#second way
full_name = ['d','a','t','o','j','a','t','c','h','v','a','d','z','e']
i = 0
sum_of_consonants = 0
zoo = full_name[i]
while i < len(full_name):
    if zoo  != 'a' or zoo != 'e' or zoo != 'i' or zoo != 'o' or zoo != 'u':  
        sum_of_consonants += 1
    i += 1
print(sum_of_consonants)
full_name = ['d', 'a', 't', 'o', 'j', 'a', 't', 'c', 'h', 'v', 'a', 'd', 'z', 'e']
i = 0
sum_of_consonants = 0
while i < len(full_name):
    zoo = full_name[i]
    if zoo != 'a' and zoo != 'e' and zoo != 'i' and zoo != 'o' and zoo != 'u':
        sum_of_consonants += 1
    i += 1
print(sum_of_consonants)  