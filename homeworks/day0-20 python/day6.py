#creating programs
#n1-employee is ready for promotion if he has worked 500hours+ and missed less then 5 work day
#employees work time
employee1_work_time_in_hours = 525
employee2_work_time_in_hours = 385
employee3_work_time_in_hours = 400
employee4_work_time_in_hours = 600
#employees missed days
eployee1_missed_work_day = 2
eployee2_missed_work_day = 4
eployee3_missed_work_day = 4
eployee4_missed_work_day = 7

print(employee1_work_time_in_hours > 500 and eployee1_missed_work_day < 5)
print(employee2_work_time_in_hours > 500 and eployee2_missed_work_day < 5)
print(employee3_work_time_in_hours > 500 and eployee3_missed_work_day < 5)
print(employee4_work_time_in_hours > 500 and eployee4_missed_work_day < 5)

#n2-user is teleporting to the next level if he has found at least 15 keys or bought at least 1 gamepass
#keys found by users
user1_keys_found = 10
user2_keys_found = 16
user3_keys_found = 5
user4_keys_found = 20
user5_keys_found = 17
#amount of purchassed gamepasses
user_1_gamepass_bought = 1
user_2_gamepass_bought = 0
user_3_gamepass_bought = 0
user_4_gamepass_bought = 3
user_5_gamepass_bought = 4 

print(user1_keys_found > 15 or user_1_gamepass_bought > 0)
print(user2_keys_found > 15 or user_2_gamepass_bought > 0)
print(user3_keys_found > 15 or user_3_gamepass_bought > 0)
print(user4_keys_found > 15 or user_4_gamepass_bought > 0)
print(user5_keys_found > 15 or user_5_gamepass_bought > 0)