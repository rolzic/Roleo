<<<<<<< Updated upstream
nimi = input("Mis on sinu nimi? ")
print("Sisesta siia laul või luuletus: ")
print("Kui saad luuletuse sisestatud, vajuta kaks korda enter")
=======
__author__ = 'RolandR'
nimi = input("Mis on sinu nimi?: ")
print("Sisesta siia laul või luuletus. ")
print("Kui luuletus kirjutatud, vajuta ENTER-it kaks korda!")
>>>>>>> Stashed changes

buffer = []
while True:
    line = input()
    if line == "":
        break
    buffer.append(line)
a = "\n".join(buffer)
<<<<<<< Updated upstream




=======



>>>>>>> Stashed changes
a = a.replace(",","").replace(".","").replace("!","").replace(":","")\
    .replace("(","").replace(")","").replace("-","").replace(";","")


a = a.split("\n")
k = 0
while True:
<<<<<<< Updated upstream
    b = input("Sisesta " + str(k+1)+ " " + "rida: ")
    if a[k].lower() == b.lower():
=======
    b = input("Sisesta 1. luulerida: ")
    if a[k] == b:
>>>>>>> Stashed changes
        b = ""
        k += 1
        if k == len(a):
            print("Hästi tehtud,", nimi)
            break
        print("Tubli!")
    else:
        print("Vale")
        print("Õige on:",a[k])
        print("Ära muretse, proovi uuesti")
        k = k
