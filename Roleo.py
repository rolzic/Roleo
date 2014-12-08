from timeit import default_timer as timer
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font


def roleo():
    nimi = input("Mis on sinu nimi? ")
    print("Sisesta siia laul või luuletus: ")
    print("Kui saad luuletuse sisestatud, vajuta kaks korda ENTERIT")




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
            print("Proovi uuesti")
            k = k
    end = timer()
    print("Sul läks aega " + str(round(end - start, 2)) + " sekundit")

raam = Tk()
raam.title("Roleo")
tahvel = Canvas(raam, width=1000, height=1000, background="SkyBlue")
tahvel.grid()

suur_font = font.Font(family='Helvetica', size=32, weight='bold')
tahvel.create_text(30, 500, text="Oled valmis luuletust õppima?", font=suur_font, anchor=NW)

nupp = ttk.Button(raam, text="Alusta luuletuse õppimist!", command=roleo)
nupp.place(x=70, y=40, width=150)


raam.mainloop()


