#hw1
names = ['alexandre Katsarava','dato Jachvadze','dato Mgeladze','davit Janashia','gabriel Gogadze','gabrieli Molodini','giorgi Gelashvili','ilia Wiklauri','muhammedali Mamedov','nini Nozadze','sandro Bochorishvili','sandro Oqropiridze','vano Motiashvili','erekle gochitashvili','lasha wamalaidze','nika chochia']
length = len(names[1])
x = 0
for name in names:
    x += 1
    if x == length:
        names.remove(name)
print(names)
#hw2
name1 = 'dato jatchvadze'
x = 0
for letters in name1:
    x += 1
for i in range(0,x):
    print('magaria')
#hw3
# თქვენი რაზმელების სიიდან, ტოპ 2 ყველაზე გრძელგვარიანი შეაგდეთ ახალ სიაში და დაპრინტეთ
razmelebi = ['alexandre Katsarava','dato Jachvadze','dato Mgeladze','davit Janashia','gabriel Gogadze','gabrieli Molodini','giorgi Gelashvili','ilia Wiklauri','muhammedali Mamedov','nini Nozadze','sandro Bochorishvili','sandro Oqropiridze','vano Motiashvili','erekle gochitashvili','lasha wamalaidze','nika chochia']
razmelebi2 = []
o = 0
for razmeli in razmelebi:
    if len(razmeli) > o:
        o = len(razmeli)
        result = razmeli



razmelebi2.append(result)
razmelebi.remove(result)


o = 0
for razmeli in razmelebi:
    if len(razmeli) > o:
        o = len(razmeli)
        result = razmeli
razmelebi2.append(result)
print(razmelebi2)




