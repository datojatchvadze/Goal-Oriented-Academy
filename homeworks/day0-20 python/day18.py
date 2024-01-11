#hw1
names = ['alexandre Katsarava','dato Jachvadze','dato Mgeladze','davit Janashia','gabriel Gogadze','gabrieli Molodini','giorgi Gelashvili','ilia Wiklauri','muhammedali Mamedov','nini Nozadze','sandro Bochorishvili','sandro Oqropiridze','vano Motiashvili','erekle gochitashvili','lasha wamalaidze','nika chochia']
selected_names = []
for name in names:
    i_count = 0  
    for char in name:
        if char == 'i':
            i_count += 1 
    if i_count > 2:
        selected_names.append(name.capitalize())
print(selected_names)
#hw2
names1 = ['alexandre Katsarava','dato Jachvadze','dato Mgeladze','davit Janashia','gabriel Gogadze','gabrieli Molodini','giorgi Gelashvili','ilia Wiklauri','muhammedali Mamedov','nini Nozadze','sandro Bochorishvili','sandro Oqropiridze','vano Motiashvili','erekle gochitashvili','lasha wamalaidze','nika chochia']
for squad in names1:
    if len(squad) < 16:
        print(squad.upper())






    

        
            
        


