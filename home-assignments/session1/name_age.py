import json

with open('name_age.json' ,'r') as nameage:
    data = json.load(nameage)
dict = data

file = open("name_age.yaml","w")
file.write("0-11\n")
for name,age in dict.items():
    if age>0 and age<11:
        print(name, file=file)
file.write("\n11-20\n")
for name,age in dict.items():
    if age>11 and age<20:
        print(name, file=file)
file.write("\n20-25\n")
for name,age in dict.items():
    if age>20 and age<25:
        print(name, file=file)
file.write("\n25-40\n")
for name,age in dict.items():
    if age>25 and age<40:
        print(name, file=file)
file.write("\n40-102\n")
for name, age in dict.items():
    if age>40 and age<102:
        print(name, file=file)


file = open("notinlist.json","w")
for name,age in dict.items():
    if not (age>0 and age<11 or age>11 and age<20 or age>20 and age<25 or age>25 and age<40 or age>40 and age<102):
        print (name, file=file)












