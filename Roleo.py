from timeit import default_timer as timer
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

def luuletus():
    a = t.get(1.0,END)
    a = str(a.strip())
    a = a.replace(",","").replace(".","").replace("!","").replace(":","")\
    .replace("(","").replace(")","").replace("-","").replace(";","")
    a = a.lower()
    a = a.split("\n")
    print(a)
    raam.destroy()
    def luuletus2():

        global i
        global j
        b = c.get()
        b = str(b.strip())
        b = b.replace(",","").replace(".","").replace("!","").replace(":","")\
        .replace("(","").replace(")","").replace("-","").replace(";","")
        b = b.lower()
        print(b)
        if a[i] == b:
            messagebox.showinfo(message="Väga tubli")
            c.delete(0, END)
            if i+1 == len(a):
                end = timer()
                messagebox.showinfo(message="Vigade arv: " + str(j) + "." \
                + " Sul läks aega  " + str(round(end - start, 2)) + " sekundit.")
                raam2.destroy()

            else:
                i+=1
        else:
            messagebox.showinfo(message="Läks valesti, aga pole hullu,proovime uuesti!")
            c.delete(0, END)
            j += 1
    raam2 = Tk()
    raam2.title("Luuletuse meeldejätmine")
    tahvel = Canvas(raam2, width=600, height=600, background="black")
    tahvel.grid()
    nupp2 = Button(tahvel,text = "OK",command = luuletus2, fg="black",bg="SkyBlue").pack()
    c = Entry(tahvel)
    c.pack()
    start = timer()


i = 0
j = 0

#Esimene raam
raam = Tk()
raam.title("Luuletuse sisestamine")
raam.geometry("800x800")

#Esimese raami nupp
nupp = ttk.Button(raam,text = "OK",command = luuletus)
nupp.place(x=400, y=370, width=70)

#Esimese raami tekstikast
t = Text(raam, width=40,height=20)
t.place(x=400,y=30)

#Käsnakalle foto
photo = PhotoImage(file='pilt2.gif')
label= Label(raam, image=photo)
label.place(x=30, y=20)

#Jutumull
photo2 = PhotoImage(file='pilt3.gif')
label2= Label(raam, image=photo2)
label2.place(x=320, y=400)

#Nupu style
s = ttk.Style()
s.theme_use("vista")
raam.mainloop()


