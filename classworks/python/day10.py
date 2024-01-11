#1
for i in range(3):
    print("A")
for i in range(3):
    print("B")
#2
password="SecretWord"
guess = input()
while guess != password:  
  guess = input() 
print("Access Granted")
#3
age = 22
if age >= 18:
  print("Regular price")
else:
  print("Discount")