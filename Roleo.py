from timeit import default_timer as timer
nimi = input("Mis on sinu nimi? ")
print("Sisesta siia laul või luuletus: ")
print("Kui saad luuletuse sisestatud, vajuta kaks korda enter")




buffer = []
while True:
    line = input()
    if line == "":
        break
    buffer.append(line)
a = "\n".join(buffer)




a = a.replace(",","").replace(".","").replace("!","").replace(":","")\
    .replace("(","").replace(")","").replace("-","").replace(";","")

start = timer()
a = a.split("\n")
k = 0
while True:
    b = input("Sisesta " + str(k+1)+ " " + "rida: ")
    b = b.replace(",","").replace(".","").replace("!","").replace(":","")\
    .replace("(","").replace(")","").replace("-","").replace(";","")
    if a[k].lower() == b.lower():
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
end = timer()
print("Sul läks aega " + str(round(end - start, 2)) + " sekundit")


