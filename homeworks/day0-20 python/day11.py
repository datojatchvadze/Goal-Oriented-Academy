#1 to 100,if number is multiple of 15,print(GOA15),if number is multiple of 5,print(GOA11) and if number is multiple of 3,print(GOA)
for i in range(1,100):
    if i % 15 == 0:
        print(i,'GOA15')
    if i % 5 == 0:
        print(i,'GOA11')
    if i % 3 == 0:
        print(i,'GOA')
    else:
        print(i)