import os
print("directory"+os.getcwd())  # print the current directory
noms = []
prenoms = []
ages = []
notes = []
# opening the text file
file = open("eleves.txt", "r")
next(file)  # skip the first line
for line in file:
    test = list(line.split())
    noms.append(test[0])
    prenoms.append(test[1])
    ages.append(test[2])
    notes.append(test[3])
file.close()
i = 0
while (i < len(noms)):
    noms[i] = noms[i].upper()
    i = i+1
print(noms)
i = 0
while (i < len(prenoms)):
    prenoms[i] = prenoms[i].capitalize()
    i = i+1
print(prenoms)
i = 0
somme = 0
while (i < len(ages)):
    somme = somme+int(ages[i])
    i = i+1
print(f"la moyenne des ages est {somme/len(ages)}")
i = 0
somme = 0
while (i < len(notes)):
    somme = somme+float(notes[i])
    i = i+1
print(f"la moyenne des notes est {somme/len(notes)}")
notes.sort()
file1 = open("Resultats.txt", "a")
file1.write("les notes triés sont :")
i = 0
while (i < len(notes)):
    file1.write(str(notes[i]))
    file1.write(" ")
    i = i+1
file1.close()
