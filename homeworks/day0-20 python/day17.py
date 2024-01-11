#hw1
import random
crew_leaders = ['kruashvili','amiranashvili','tyeshelashvili','janezashvili','molodini','kereselidze','kurtanidze','aruda']
random1 = random.choice(crew_leaders)
random2 = random.choice(crew_leaders)
random3 = random.choice(crew_leaders)
while random1 == random2 or random1 == random3 or random3 == random2:
    random1 = random.choice(crew_leaders)
    random2 = random.choice(crew_leaders)
    random3 = random.choice(crew_leaders)
print(random1)
print(random2)
print(random3)
#hw2
import random
members = ['Alexandre Katsarava','Dato Jachvadze','Dato Mgeladze','Davit Janashia','Gabriel Gogadze','Gabrieli Molodini','Giorgi Gelashvili','Ilia Wiklauri','Muhammedali Mamedov','Nini Nozadze','Sandro Bochorishvili','Sandro Oqropiridze','Vano Motiashvili','ერეკლე გოჩიტაშვილი','ლაშა წამალაიძე','ნიკა ჩოჩია']
for i in range(3):
    random1 = random.choice(members)
    print(random1,'kargad swavlobs')
#hw3
import random
names = ['Alexandre Katsarava','Dato Jachvadze','Dato Mgeladze','Davit Janashia','Gabriel Gogadze','Gabrieli Molodini','Giorgi Gelashvili','Ilia Wiklauri','Muhammedali Mamedov','Nini Nozadze','Sandro Bochorishvili','Sandro Oqropiridze','Vano Motiashvili','erekle gochitashvili','lasha wamalaidze','nika chochia']
random11 = random.choice(names)
random22 = random.choice(names)
random33 = random.choice(names)
if random11[-1] == 'i':
    print(random11,'cool')
    print(random22)
    print(random33)
elif random22[-1] == 'i':
    print(random11,'cool')
    print(random22)
    print(random33)
elif random33[-1] == 'i':
    print(random11,'cool')
    print(random22)
    print(random33)
else:
    print(random11)
    print(random22)
    print(random33)






        
    
    
    
