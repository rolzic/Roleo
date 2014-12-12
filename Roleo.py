from timeit import default_timer as timer
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
def õp():
    valik.destroy()
    def luuletus():
        nimi = d.get()
        a = t.get(1.0,END)
        a = str(a.strip())
        a = a.replace(",","").replace(".","").replace("!","").replace(":","")\
        .replace("(","").replace(")","").replace("-","").replace(";","").replace("\t","")
        a = a.lower()
        a = a.split("\n")
        print(a)
        messagebox.showinfo(message="Vaata oma luuletus veel korra üle!")
        messagebox.showinfo(message=t.get(1.0,END))
        raam.destroy()
        def luuletus2():
            global i_e
            global j_e
            global g_e
            global uus_e
            b = c.get()
            b = str(b.strip())
            b = b.replace(",","").replace(".","").replace("!","").replace(":","")\
            .replace("(","").replace(")","").replace("-","").replace(";","").replace("\t","")
            b = b.lower()
            if a[i_e].strip() == b:
                messagebox.showinfo(message="Väga tubli")
                c.delete(0, END)
                if i_e+1 == len(a):
                    end = timer()
                    h = str(round(end - start, 2))
                    messagebox.showinfo(message="Vigade arv: " + str(j_e) + "." + " Sul läks aega: " + h + " sekundit.")
                    raam2.destroy()
                    f = open(nimi +"_educational" + ".txt","w")
                    f.write("Vigu: " + str(j_e) + "\n")
                    f.write("Läks aega: " +h + "\n")
                    f.write("Tekst: " + "\n")
                    f.write("\n".join(a))
                    f.close()
                else:
                    i_e+=1
                    g_e = 0
                    uus_e = []
            else:
                lisa = a[i_e].split()
                pikkus = len(lisa)
                if g_e+1 == len(lisa):
                    messagebox.showinfo(message="Siin on sinu rida, proovi see meelde jätta: " + str(a[i_e]))
                    c.delete(0, END)
                    j_e += 1
                    g_e = g_e
                else:
                    uus_e += [lisa[g_e]]
                    messagebox.showinfo(message="Läks valesti, aga pole hullu. Proovi uuesti!")
                    messagebox.showinfo(message="Siin on väike vihje: " + str(" ".join(uus_e)))
                    c.delete(0, END)
                    j_e += 1
                    g_e +=1
        raam2 = Tk()
        raam2.title("Luuletuse meeldejätmine")
        raam2.bind("<Return>", lambda event: luuletus2())
        tahvel3 = Canvas(raam2, width=300, height=500)
        tahvel3.grid()
        nupp2 = ttk.Button(tahvel3,text = "OK",command = luuletus2)
        nupp2.place(x=30,y=60)
        start = timer()
        c = Entry(tahvel3)
        c.pack()
        c.place(x=30,y=30,width=240)
        edu = PhotoImage(file="edu.gif")
        img3 = tahvel3.create_image(160, 300, image=edu)
        tahvel3.pack()
        raam2.mainloop()


    raam = Tk()
    raam.title("Luuletuse sisestamine")
    tahvel2 = Canvas(raam, width=900, height=700, background="white")
    tahvel2.grid()
    nupp = ttk.Button(tahvel2,text = "OK",command = luuletus)
    nupp.place(x=30,y=660)
    d = Entry(tahvel2)
    d.pack()
    d.place(x = 70,y=50, width= 200)
    t = Text(tahvel2, width=30,height=35, background="black", fg="white")
    t.place(x=30,y=80)
    silt = ttk.Label(tahvel2, text="Nimi", background= "white")
    silt.place(x=30, y=50)

    nelson = PhotoImage(file="nelson.gif")
    img = tahvel2.create_image(580, 490, image=nelson)
    jutumull = PhotoImage(file="jutumull.gif")
    img2 = tahvel2.create_image(580, 180, image=jutumull)
    tahvel2.pack()
    raam.mainloop()

def män():
    valik.destroy()
    def luuletus():
        player1 = d.get()
        player2 = v.get()
        a = t.get(1.0,END)
        a = str(a.strip())
        a = a.replace(",","").replace(".","").replace("!","").replace(":","")\
        .replace("(","").replace(")","").replace("-","").replace(";","").replace("\t","")
        a = a.lower()
        a = a.split("\n")
        messagebox.showinfo(message="Korrake üle oma teksti!")
        messagebox.showinfo(message=t.get(1.0,END))
        messagebox.showinfo(message="Edu!")
        raam.destroy()
        def luuletus2():
            global i_m1
            global j_m1
            global g_m1
            global uus_m1
            esimene = c.get()
            esimene = str(esimene.strip())
            esimene = esimene.replace(",","").replace(".","").replace("!","").replace(":","")\
            .replace("(","").replace(")","").replace("-","").replace(";","").replace("\t","")
            esimene = esimene.lower()
            if a[i_m1].strip() == esimene:
                messagebox.showinfo(message="Õigesti")
                c.delete(0, END)
                if i_m1+1 == len(a):
                    end1 = timer()
                    h = str(round(end1 - start1, 2))
                    messagebox.showinfo(message="Vigade arv: " + str(j_m1) + "." + " Teile läks aega " + h + " sekundit.")
                    raam2.destroy()
                    f = open(player1 + "_1player" + ".txt","w")
                    f.write("Vigu: " + str(j_m1) + "\n")
                    f.write("Läks aega: " +h + "\n")
                    f.write("Tekst: " + "\n")
                    f.write("\n".join(a))
                    f.close()
                    def luuletus3():
                        global i_m2
                        global j_m2
                        global g_m2
                        global uus_m2
                        teine = z.get()
                        teine = str(teine.strip())
                        teine = teine.replace(",","").replace(".","").replace("!","").replace(":","")\
                        .replace("(","").replace(")","").replace("-","").replace(";","").replace("\t","")
                        teine = teine.lower()
                        if a[i_m2].strip() == teine:
                            messagebox.showinfo(message="Õigesti")
                            z.delete(0, END)
                            if i_m2+1 == len(a):
                                end2 = timer()
                                x = str(round(end2 - start2, 2))
                                messagebox.showinfo(message="Vigade arv: " + str(j_m2) + "." + " Teil läks aega " + x + " sekundit.")
                                f = open(player2 +"_2player" + ".txt","w")
                                f.write("Vigu: " + str(j_m2) + "\n")
                                f.write("Läks aega: " +x + "\n")
                                f.write("Tekst: " + "\n")
                                f.write("\n".join(a))
                                f.close()
                                if x < h:
                                    messagebox.showinfo(message= player2 + " " +  "oli kiirem")
                                elif x ==h:
                                    messagebox.showinfo(message="Mõlemad mängijad olid sama kiired")
                                else:
                                    messagebox.showinfo(message=player1 + " " +  "oli kiirem")
                                if j_m1 > j_m2:
                                    messagebox.showinfo(message="Võitis: " + player2)
                                    raam3.destroy()
                                elif j_m1 == j_m2:
                                    messagebox.showinfo(message="Jäite viiki")
                                    raam3.destroy()
                                else:
                                    messagebox.showinfo(message="Võitis: " + player1)
                                    raam3.destroy()
                            else:
                                i_m2+=1
                        else:
                            if i_m2+1 == len(a):
                                j_m2 +=1
                                messagebox.showinfo(message="Valesti")
                                end2 = timer()
                                x = str(round(end2 - start2, 2))
                                messagebox.showinfo(message="Vigade arv: " + str(j_m2) + "." + " Teil läks aega " + x + " sekundit.")
                                f = open(player2 + "_2player" + ".txt","w")
                                f.write("Vigu: " + str(j_m2) + "\n")
                                f.write("Läks aega: " +x + "\n")
                                f.write("Tekst: " + "\n")
                                f.write("\n".join(a))
                                f.close()
                                if x < h:
                                    messagebox.showinfo(message= player2 + " " +  "oli kiirem")
                                elif x ==h:
                                    messagebox.showinfo(message="Mõlemad mängijad olid sama kiired")
                                else:
                                    messagebox.showinfo(message=player1 + " " +  "oli kiirem")
                                if j_m1 > j_m2:
                                    messagebox.showinfo(message="Võitis: " + player2)
                                    raam3.destroy()
                                elif j_m1 == j_m2:
                                    messagebox.showinfo(message="Jäite viiki")
                                    raam3.destroy()
                                else:
                                    messagebox.showinfo(message="Võitis: " + player1)
                                    raam3.destroy()
                            else:
                                messagebox.showinfo(message="Valesti")
                                z.delete(0, END)
                                j_m2 +=1
                                i_m2 +=1
                            
                    raam3 = Tk()
                    raam3.title("2. player")
                    raam3.bind("<Return>", lambda event: luuletus3())
                    tahvel4 = Canvas(raam3, width=300, height=500)
                    tahvel4.grid()
                    nupp3 = ttk.Button(tahvel4,text = "OK",command = luuletus3)
                    nupp3.place(x=30,y=60)
                    start2 = timer()
                    z = Entry(tahvel4)
                    z.pack()
                    z.place(x=30,y=30,width=240)
                    player2foto = PhotoImage(file="player2.gif")
                    img3 = tahvel4.create_image(160, 300, image=player2foto)
                    tahvel4.pack()
                    raam3.mainloop()
                else:
                    i_m1+=1
            else:
                if i_m1+1 == len(a):
                    j_m1 +=1
                    messagebox.showinfo(message="Valesti")
                    end1 = timer()
                    h = str(round(end1 - start1, 2))
                    messagebox.showinfo(message="Vigade arv: " + str(j_m1) + "." + " Teil läks aega " + h + " sekundit.")
                    raam2.destroy()
                    f = open(player1 + "_1player" + ".txt","w")
                    f.write("Vigu: " + str(j_m1) + "\n")
                    f.write("Läks aega: " +h + "\n")
                    f.write("Tekst: " + "\n")
                    f.write("\n".join(a))
                    f.close()
                    def luuletus3():
                        global i_m2
                        global j_m2
                        global g_m2
                        global uus_m2
                        teine = z.get()
                        teine = str(teine.strip())
                        teine = teine.replace(",","").replace(".","").replace("!","").replace(":","")\
                        .replace("(","").replace(")","").replace("-","").replace(";","").replace("\t","")
                        teine = teine.lower()
                        if a[i_m2].strip() == teine:
                            messagebox.showinfo(message="Õigesti")
                            z.delete(0, END)
                            if i_m2+1 == len(a):
                                end2 = timer()
                                x = str(round(end2 - start2, 2))
                                messagebox.showinfo(message="Vigade arv: " + str(j_m2) + "." + " Teil läks aega " + x + " sekundit.")
                                f = open(player2 +"_2player" + ".txt","w")
                                f.write("Vigu: " + str(j_m2) + "\n")
                                f.write("Läks aega: " +x + "\n")
                                f.write("Tekst: " + "\n")
                                f.write("\n".join(a))
                                f.close()
                                if x < h:
                                    messagebox.showinfo(message= player2 + " " +  "oli kiirem")
                                elif x ==h:
                                    messagebox.showinfo(message="Mõlemad mängijad olid sama kiired")
                                else:
                                    messagebox.showinfo(message=player1 + " " +  "oli kiirem")
                                if j_m1 > j_m2:
                                    messagebox.showinfo(message="Võitis: " + player2)
                                    raam3.destroy()
                                elif j_m1 == j_m2:
                                    messagebox.showinfo(message="Jäite viiki")
                                    raam3.destroy()
                                else:
                                    messagebox.showinfo(message="Võitis: " + player1)
                                    raam3.destroy()
                            else:
                                i_m2+=1
                        else:
                            if i_m2+1 == len(a):
                                j_m2 +=1
                                messagebox.showinfo(message="Valesti")
                                end2 = timer()
                                x = str(round(end2 - start2, 2))
                                messagebox.showinfo(message="Vigade arv: " + str(j_m2) + "." + " Teil läks aega " + x + " sekundit.")
                                f = open(player2 + "_2player" + ".txt","w")
                                f.write("Vigu: " + str(j_m2) + "\n")
                                f.write("Läks aega: " +x + "\n")
                                f.write("Tekst: " + "\n")
                                f.write("\n".join(a))
                                f.close()
                                if x < h:
                                    messagebox.showinfo(message= player2 + " " +  "oli kiirem")
                                elif x ==h:
                                    messagebox.showinfo(message="Mõlemad mängijad olid sama kiired")
                                else:
                                    messagebox.showinfo(message=player1 + " " +  "oli kiirem")
                                if j_m1 > j_m2:
                                    messagebox.showinfo(message="Võitis: " + player2)
                                    raam3.destroy()
                                elif j_m1 == j_m2:
                                    messagebox.showinfo(message="Jäite viiki")
                                    raam3.destroy()
                                else:
                                    messagebox.showinfo(message="Võitis: " + player1)
                                    raam3.destroy()
                            else:
                                messagebox.showinfo(message="Valesti")
                                z.delete(0, END)
                                j_m2 +=1
                                i_m2 +=1
                    raam3 = Tk()
                    raam3.title("2. player")
                    raam3.bind("<Return>", lambda event: luuletus3())
                    tahvel4 = Canvas(raam3, width=300, height=500)
                    tahvel4.grid()
                    nupp3 = ttk.Button(tahvel4,text = "OK",command = luuletus3)
                    nupp3.place(x=30,y=60)
                    start2 = timer()
                    z = Entry(tahvel4)
                    z.pack()
                    z.place(x=30,y=30,width=240)
                    player2foto = PhotoImage(file="player2.gif")
                    img3 = tahvel4.create_image(160, 300, image=player2foto)
                    tahvel4.pack()
                    raam3.mainloop()
                            
                else:
                    messagebox.showinfo(message="Valesti")
                    c.delete(0, END)
                    j_m1 +=1
                    i_m1 +=1

        raam2 = Tk()
        raam2.title("1. player")
        raam2.bind("<Return>", lambda event: luuletus2())
        canvas = Canvas(raam2, width=300, height=500)
        canvas.grid()
        nupp2 = ttk.Button(canvas,text = "OK",command = luuletus2)
        nupp2.place(x=30,y=60)
        start1 = timer()
        c = Entry(canvas)
        c.pack()
        c.place(x=30,y=30,width=240)
        player1foto = PhotoImage(file="player1.gif")
        img3 = canvas.create_image(160, 300, image=player1foto)
        canvas.pack()
        canvas.mainloop()
    raam = Tk()
    raam.title("Luuletuse sisestamine")
    tahvel = Canvas(raam, width=900, height=700, background="white")
    tahvel.grid()
    nupp = ttk.Button(tahvel,text = "OK",command = luuletus)
    nupp.place(x=30, y=670)
    d = Entry(tahvel)
    d.pack()
    d.place(x = 100,y=50, width=150)
    v = Entry(tahvel)
    v.pack()
    v.place(x = 100, y=70, width=150)
    silt1 = ttk.Label(tahvel, text="Player 1", background="white")
    silt1.place(x=30,y=50)

    silt2 = ttk.Label(tahvel, text="Player 2", background="white")
    silt2.place(x=30,y=70)
    t = Text(tahvel, width=30,height=35, background="black", fg="white")
    t.place(x=30,y=100)

    nelson = PhotoImage(file="nelson.gif")
    img = tahvel.create_image(580, 490, image=nelson)
    jutumull = PhotoImage(file="jutumull.gif")
    img2 = tahvel.create_image(580, 180, image=jutumull)
    tahvel.pack()
    raam.mainloop()

uus_e =  []
g_e = 0
i_e = 0
j_e = 0
i_m1 = 0
j_m1 = 0
i_m2 = 0
j_m2 = 0
valik = Tk()
valik.title("Vali mode")
tahvel = Canvas(valik, width=450, height=452, background="black")
tahvel.grid()
educational = Button(tahvel,text = "Educational",command = õp, fg ="black", bg="yellow", padx=30,pady=30)
educational.pack()
educational.place(x= 90,y=45)
mäng = Button(tahvel,text = "Mäng",command=män, fg ="black",bg="yellow", padx=46,pady=30)
mäng.pack()
mäng.place(x=90,y=150)

photo = PhotoImage(file='mustpilt.gif')
label= Label(tahvel, image=photo, background="black")
label.place(x=240, y=2)

