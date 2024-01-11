#1
a = 3
b = 2.3
c = 'good'
d = 3 < 4 or 3*3 > 3*4
e = [1,2,3,4,5,6,7]
print(type(a),type(b),type(c),type(d),type(e))
#2
income_per_month = 1000
rent_per_month = 650
food_worth = 300
profit = income_per_month > rent_per_month + food_worth
print(profit)
#3
import random
sports = ['football','basketball','tennis']
z = sports.append('rugby')
sport = random.choice(sports)
print(sport)
#4
def favourite_food():
    x = input('whats your favourite food: ')
    print(x,'sounds delicious!')
favourite_food()
#5
first = 12
second = '13'
third = 'friends'
print(first+second-third) #string+int = error
text = input('enter text: ')
print(text.upper())
