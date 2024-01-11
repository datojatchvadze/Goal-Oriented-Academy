#hw1==creating list of my name and surname and then counting vowels in it
full_name = ['d','a','t','o','j','a','t','c','h','v','a','d','z','e']
i = 0
sum_of_vowels = 0
while(i < len(full_name)):
    if full_name[i] == 'a' or full_name[i] == 'e' or full_name[i] == 'i' or full_name[i] == 'o' or full_name[i] =='u': 
        sum_of_vowels = sum_of_vowels + 1
    i = i + 1
print(sum_of_vowels)

#hw2==first three element of the list are names,last three are surnames of myself and parents.then printing names with correct surnames
family_name = ['dato','devi','xatuna','jatchvadze','jatchvadze','gvaberidze']
print(family_name[0] + family_name[3])
print(family_name[1] + family_name[4])
print(family_name[2] + family_name[5])
a = 'dato jatchvadze'
y = 0
for char in a:
    if char in 'aeiou':
        y = y + 1
print(y)
# vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
# input_text = input("Enter a text: ")

# vowel_count = 0  # Initialize a counter to keep track of the vowel count

# for char in input_text:
#     if char in vowels:
#         vowel_count += 1

# print("Number of vowels:", vowel_count)
    
        


