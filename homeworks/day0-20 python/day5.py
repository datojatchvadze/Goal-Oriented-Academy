#asking user his age and printing if the age is below or above 18
user_age = input("what's your age? ")
print(18 < int(user_age))
#asking user about his and his father's age and printing both of the numbers combined are above or below 60
user_age2 = input("insert your age: ")
age_of_users_father =input('insert your fathers age ')
print(int(user_age2) + int(age_of_users_father) > 60)