__author__ = 'RolandR'

print("Sisesta siia laul või luuletus: ")
print("Ja siis vajuta kaks korda enterit")

buffer = []
while True:
    line = input()
    if line == "":
        break
    buffer.append(line)
a = "\n".join(buffer)
print("You entered...")
print(a)




nimi = input("Mis on sinu nimi?: ")


a = a.replace(",","").replace(".","").replace("!","").replace(":","")\
    .replace("(","").replace(")","").replace("-","").replace(";","")


a = a.split("\n")
k = 0
while True:
    b = input("Pane: ")
    if a[k] == b:
        b = ""
        k += 1
        if k == len(a):
            print("hästi tehtud,", nimi)
            break
        print("Well done")
    else:
        print("fk you")
        k = k