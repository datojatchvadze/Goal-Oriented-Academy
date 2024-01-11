#first quiz
#1 
print('hello world!')
print('homework started')
#2
x = 3
if x <= 3:
    print('low')
if x < 1:
    print('very low')
    print(x)
#3
a = 3
b = 2.3
c = 3 < 10
print(type(a))
print(type(b))
print(type(c))
#4
code = input('choose your password: ')
print(len(code))
#5
for char in 'abcdefghi':
    print(char)
#6
word = "elephant"
second_word = word[3]+word[1]+word[5]+word[6]+word[7]
print(second_word)
#7
c = 'no games?'
print(c[2]+c[8])
#8
for num in range(0,45,4):
   print(num)
#second quiz
#1
i = 3
y = 0
while i < 13:
    print('good')
    i += 1
print(i)
#2
v = 0
while v < 12:
    print('goa')
    v += 1
    print('gud')
#3
a1 = int(input('put random number: '))
a2 = int(input('put  another random number: '))
a3 = int(input('put another random number: '))
sum = 0
if a1 % 2 == 1:
    sum += 1
if a2 % 3 == 1:
    sum += 1
if a3 % 5 == 1:
    sum += 1
print('your score is ' + str(sum))
#4
list = ['orange','brown','white','pink']
list.append('blue')
list.insert(3,'purple')
print(list[1] + ' ' + list[4])
#5
v1 = 12-3
v2 = 12//3
if v1<v2:
    print('wrong')
elif v1>v2:
    print('correct')
else:
    print('impossible')
#6
number = int(input('guess random number: '))
if number <= 45:
    print('good')
    if number >= 10:
        print(':)')
else:
    print('fail')
#7
full_name = 'ideebi gamomeliadze'
animal = full_name[11] + full_name[12] + full_name[13] + full_name[14] + full_name[15]
print(animal)
#8
restaurants = ['kfc','macdonalds','dunkin donats']
p_counter = 0
for restaurant in restaurants:
    if restaurant[0] == 'p':
        p_counter += 1
        print(p_counter)
password_checker = input('insert your password and check its strength: ')
if len(password_checker) < 6:
    print('weak')
if len(password_checker) > 6:
    print('normal')
elif len(password_checker) < 12:
    print('normal')
if len(password_checker) >= 12:
    print('strong')
