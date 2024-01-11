#hw1
print("0")
y = 2
x = 1
while x < 100:
    print(x,"odd")
    print(y,"even")
    x = x + 2
    y = y + 2
#hw2
user_age = input("insert your age: ")
user_father_age = input("insert your father's age: ")
if int(user_father_age) / 2 == int(user_age):
    print("bingo")
else:
    print("mouse")
#hw3
user_age1 = input("insert your age: ")
user_gender = input("insert your gender: ")
if int(user_age1) > 65 and user_gender == "male":
    print("pension granted")
if user_gender == "none binery":
    print(" good bye :) ")
if user_gender == "female" and int(user_age1) > 60:
    print("pension granted")
#hw4
user_education_sourse = input("where are you studying? ")
if user_education_sourse == "GOA":
    print("congrets,you are progressing in life.as long as you stay there you will keep improving.now continue studying")
        
    
    