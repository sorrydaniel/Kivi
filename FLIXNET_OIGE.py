from tkinter import *           # tkinteri põhivahendid
from tkinter import ttk         # platvormi ühise stiili saamiseks
from tkinter import messagebox 
import tkinter
import random
from tkinter import Text


raam = Tk()
# loome akna

raam.geometry("930x720")
tahvel = Canvas(raam, width=930, height=720, background="black")
tahvel.grid()

#lisame logo

logo = PhotoImage(file="flixnet.png")
img = tahvel.create_image(50, 10, image=logo, anchor = NW)

f = open("sarjad.txt", "r")

def kustuta(x):
    x.destroy()
    return x
        
silt1 = ttk.Label(raam, text = "Tere tulemast!")
silt1.place(x=335, y=270)
silt1.config(font=("Courier", 25), background = "black", foreground = "white")

silt2 = ttk.Label(raam, text = "Antud programm küsib kasutajalt küsimusi")
silt2.place(x=60, y=350)
silt2.config(font=("Courier", 25), background = "black", foreground = "white")

silt3 = ttk.Label(raam, text = "ning nende põhjal soovitab sarju.")
silt3.place(x=130, y=390)
silt3.config(font=("Courier", 25), background = "black", foreground = "white")

def command1():
    x = "1"
    f = open("andmed.txt", "a")
    f.write("1")
    f.close()
def command2():
    x = "2"
    f = open("andmed.txt", "a")
    f.write("2")
    f.close()
def command3():
    x = "3"
    f = open("andmed.txt", "a")
    f.write("3")
    f.close()
def command4():
    x = "4"
    f = open("andmed.txt", "a")
    f.write("4")
    f.close()
def command5():
    x = "5"
    f = open("andmed.txt", "a")
    f.write("5")
    f.close()
def command6():
    x = "6"
    f = open("andmed.txt", "a")
    f.write("6")
    f.close()
def command7():
    x = "7"
    f = open("andmed.txt", "a")
    f.write("7")
    f.close()
def command8():
    x = "8"
    f = open("andmed.txt", "a")
    f.write("8")
    f.close()
    
def close_window():
    raam.destroy()
    


def zanrid():
    global nuppx
    kustuta(silt1)
    kustuta(silt2)
    kustuta(silt3)
    kustuta(nuppx)
    
    edasi = ttk.Button(raam, text="Next", command=rating)
    edasi.place(x=800, y=600, width=50)
    
    silt_zanr = ttk.Label(raam, text = "Palun valige endale meeldiv žanr")
    silt_zanr.place(x=135, y=350)
    silt_zanr.config(font=("Courier", 25), background = "black", foreground = "white")
    
    nupp1 = ttk.Button(raam, text="Action", command=command1)
    nupp1.place(x=165, y=400, width=50)
    nupp1 = ttk.Button(raam, text="Adventure", command=command2)
    nupp1.place(x=215, y=400, width=50)
    nupp3 = ttk.Button(raam, text="Comedies", command=command3)
    nupp3.place(x=265, y=400, width=50)
    nupp5 = ttk.Button(raam, text="Dramas", command=command4)
    nupp5.place(x=315, y=400, width=50)
    nupp8 = ttk.Button(raam, text="Horror", command=command5)
    nupp8.place(x=365, y=400, width=50)
    nupp0 = ttk.Button(raam, text="Romance", command=command6)
    nupp0.place(x=415, y=400, width=50)
    nupp = ttk.Button(raam, text="Sci-Fi", command=command7)
    nupp.place(x=465, y=400, width=50)
    nupp11 = ttk.Button(raam, text="Thriller", command=command8)
    nupp11.place(x=515, y=400, width=50)   


nuppx = ttk.Button(raam, text="Edasi", command=zanrid)
nuppx.place(x=365, y=550, width=200, height=100)


def series():
    edasi3 = ttk.Button(raam, text="Otsi", command=vastus)
    edasi3.place(x=800, y=600, width=50)
    
    silt_series = ttk.Label(raam, text = "Palun valige sarja hooaegade arv")
    silt_series.place(x=135, y=550)
    silt_series.config(font=("Courier", 25), background = "black", foreground = "white")
    
    nub1 = ttk.Button(raam, text="1", command=command1)
    nub1.place(x=165, y=600, width=50)
    nub2 = ttk.Button(raam, text="1-3", command=command2)
    nub2.place(x=215, y=600, width=50)
    nub3 = ttk.Button(raam, text="3-6", command=command3)
    nub3.place(x=265, y=600, width=50)
    nub4 = ttk.Button(raam, text="6-9", command=command4)
    nub4.place(x=315, y=600, width=50)
    
    

def rating():
    edasi2 = ttk.Button(raam, text="Next", command=series)
    edasi2.place(x=800, y=600, width=50)
    
    silt_rating = ttk.Label(raam, text = "Palun valige sarja hinnang")
    silt_rating.place(x=135, y=450)
    silt_rating.config(font=("Courier", 25), background = "black", foreground = "white")
    
    nup1 = ttk.Button(raam, text="1+", command=command1)
    nup1.place(x=165, y=500, width=50)
    nup2 = ttk.Button(raam, text="3+", command=command2)
    nup2.place(x=215, y=500, width=50)
    nup3 = ttk.Button(raam, text="5+", command=command3)
    nup3.place(x=265, y=500, width=50)
    nup4 = ttk.Button(raam, text="7+", command=command4)
    nup4.place(x=315, y=500, width=50)
    nup5 = ttk.Button(raam, text="9+", command=command5)
    nup5.place(x=365, y=500, width=50)
    
def vastus():
    
    silt_vastus = ttk.Label(raam, text = "Sarja nimi/nimed...")
    silt_vastus.place(x=260, y=640)
    silt_vastus.config(font=("Courier", 25), background = "black", foreground = "white")
    
    fail = open("andmed.txt", encoding="UTF-8")
    read = []
    for rida in fail:
      read.append(rida)
    fail.close()
    
    my_file = open("the100.txt", "r")
    content = my_file.read()
    
    for rida2 in content:
        if read == content:
            print(content[0:1])
    

    

# ilmutame akna ekraanile
raam.mainloop()