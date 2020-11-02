from tkinter import *           # tkinteri põhivahendid
from tkinter import ttk         # platvormi ühise stiili saamiseks
from tkinter import Text
import sys
import os
from tkinter import Tk, Label, Button

raam = Tk()
raam.title('Flixnet')

def clickExitButton():
    raam.destroy()      

def kustuta(x):
    x.destroy()
    return x

def restart_program():
    f = open('andmed.txt', 'r+')
    f.truncate(0)
    python = sys.executable
    os.execl(python, python, * sys.argv)


ttk.Style().configure("TButton", padding=1, relief="flat", background='#000000', foreground='#000000')
s = ttk.Style()
s.configure('my.TButton', font=('Roboto', 12, "bold"))

# loome akna

raam.geometry("930x720")
tahvel = Canvas(raam, width=930, height=720, background="black")
tahvel.grid()

#lisame logo

logo = PhotoImage(file="flixnet.png")
img = tahvel.create_image(50, 10, image=logo, anchor = NW)

exitButton = ttk.Button(raam, text="QUIT", style='my.TButton', command=clickExitButton)
exitButton.place(x=0, y=680, width=120, height=40)

       
silt1 = ttk.Label(raam, text = "TERE TULEMAST")
silt1.place(x=320, y=310)
silt1.config(font=("Rockwell", 25), background = "black", foreground = "white")

silt2 = ttk.Label(raam, text = "       Sarjade soovituste saamiseks\n" + "valige endale kõige sobivam vastus.")
silt2.place(x=185, y=390)
silt2.config(font=("Rockwell", 25), background = "black", foreground = "white")

silt3 = ttk.Label(raam, text = "Jätkamiseks vajutage nuppu:")
silt3.place(x=185, y=540)
silt3.config(font=("Rockwell", 25), background = "black", foreground = "white")

def command1():
    f = open("andmed.txt", "a")
    f.write("1")
    f.close()
def command2():
    f = open("andmed.txt", "a")
    f.write("2")
    f.close()
def command3():
    f = open("andmed.txt", "a")
    f.write("3")
    f.close()
def command4():
    f = open("andmed.txt", "a")
    f.write("4")
    f.close()
def command5():
    f = open("andmed.txt", "a")
    f.write("5")
    f.close()
def command6():
    f = open("andmed.txt", "a")
    f.write("6")
    f.close()
def command7():
    f = open("andmed.txt", "a")
    f.write("7")
    f.close()
def command8():
    f = open("andmed.txt", "a")
    f.write("8")
    f.close()


def zanrid():
    global nuppx
    kustuta(silt1)
    kustuta(silt2)
    kustuta(silt3)
    kustuta(nuppx)
    
    f = open('andmed.txt', 'r+')
    f.truncate(0)
    
    edasi = ttk.Button(raam, text="Next ->", style='my.TButton', command=rating)
    edasi.place(x=810, y=680, width=120, height=40)
    
    silt_zanr = ttk.Label(raam, text = "Palun valige endale meeldiv žanr")
    silt_zanr.place(x=205, y=300)
    silt_zanr.config(font=("Rockwell", 25), background = "black", foreground = "white")
    
    nupp1 = ttk.Button(raam, text="Action", command=command1)
    nupp1.place(x=185, y=360, width=70, height=30)
    nupp1 = ttk.Button(raam, text="Adventure", command=command2)
    nupp1.place(x=255, y=360, width=70, height=30)
    nupp3 = ttk.Button(raam, text="Comedies", command=command3)
    nupp3.place(x=325, y=360, width=70, height=30)
    nupp5 = ttk.Button(raam, text="Dramas", command=command4)
    nupp5.place(x=395, y=360, width=70, height=30)
    nupp8 = ttk.Button(raam, text="Horror", command=command5)
    nupp8.place(x=465, y=360, width=70, height=30)
    nupp0 = ttk.Button(raam, text="Romance", command=command6)
    nupp0.place(x=535, y=360, width=70, height=30)
    nupp = ttk.Button(raam, text="Sci-Fi", command=command7)
    nupp.place(x=605, y=360, width=70, height=30)
    nupp11 = ttk.Button(raam, text="Thriller", command=command8)
    nupp11.place(x=675, y=360, width=70, height=30)   


nuppx = ttk.Button(raam, text="Edasi", style='my.TButton', command=zanrid)
nuppx.place(x=635, y=542, width=120, height=40)


def series():
    edasi3 = ttk.Button(raam, text="SEARCH", style='my.TButton', command=vastus)
    edasi3.place(x=810, y=680, width=120, height=40)
    
    silt_series = ttk.Label(raam, text = "Palun valige sarja hooaegade arv")
    silt_series.place(x=210, y=540)
    silt_series.config(font=("Rockwell", 25), background = "black", foreground = "white")
    
    nub1 = ttk.Button(raam, text="1+", command=command1)
    nub1.place(x=325, y=600, width=70, height=30)
    nub2 = ttk.Button(raam, text="3+", command=command2)
    nub2.place(x=395, y=600, width=70, height=30)
    nub3 = ttk.Button(raam, text="6+", command=command3)
    nub3.place(x=465, y=600, width=70, height=30)
    nub4 = ttk.Button(raam, text="9+", command=command4)
    nub4.place(x=535, y=600, width=70, height=30)
    
    

def rating():
    edasi2 = ttk.Button(raam, text="Next ->", style='my.TButton', command=series)
    edasi2.place(x=810, y=680, width=120, height=40)
    
    silt_rating = ttk.Label(raam, text = "Palun valige sarja hinnang")
    silt_rating.place(x=262, y=420)
    silt_rating.config(font=("Rockwell", 25), background = "black", foreground = "white")
    
    nup1 = ttk.Button(raam, text="1+", command=command1)
    nup1.place(x=290, y=480, width=70, height=30)
    nup2 = ttk.Button(raam, text="3+", command=command2)
    nup2.place(x=360, y=480, width=70, height=30)
    nup3 = ttk.Button(raam, text="5+", command=command3)
    nup3.place(x=430, y=480, width=70, height=30)
    nup4 = ttk.Button(raam, text="7+", command=command4)
    nup4.place(x=500, y=480, width=70, height=30)
    nup5 = ttk.Button(raam, text="9+", command=command5)
    nup5.place(x=570, y=480, width=70, height=30)
    
def vastus():
    def clickExitButton2():
        aken.destroy()
        
    raam.destroy()
    aken = Tk()
    
    aken.geometry("930x820")
    tahvel2 = Canvas(aken, width=930, height=820, background="black")
    tahvel2.grid()
    
    logo2 = PhotoImage(file="flixnet.png")
    img = tahvel2.create_image(50, 10, image=logo2, anchor = NW)
    
    s = ttk.Style()
    s.configure('my.TButton', font=('Roboto', 12, "bold"))
    
    tagasi = ttk.Button(aken, text="Main Page", style='my.TButton', command=restart_program)
    tagasi.place(x=0, y=740, width=120, height=40)
    
    exitButton2 = ttk.Button(aken, text="QUIT", style='my.TButton', command=clickExitButton2)
    exitButton2.place(x=0, y=780, width=120, height=40)

    
    fail = open("andmed.txt", encoding="UTF-8")
    read = []
    for rida in fail:
        read.append(rida)
        
    fail.close()
    
    
    fail2 = open("sarjad.txt", encoding = "UTF-8")
    sõnastik = {}
    
    for rida2 in fail2:
        
        sõnad = rida2.split('\t') 

        sari = sõnad[0].strip("\ufeff")

        nr = sõnad[-1].strip("\n")

        sõnastik[nr] = sari 
        
        
    
    try:
        if ":" in sõnastik[rida]:
            sõnastik[rida]=sõnastik[rida].replace(":", "\n")
        silt_vastus = ttk.Label(aken, text = "Teile sobivad sarjad:\n\n" + sõnastik[rida])
        silt_vastus.place(x=260, y=290)
        silt_vastus.config(font=("Rockwell", 25), background = "black", foreground = "white")
    except:
        silt_vastus2 = ttk.Label(aken, text = "Sarju ei leitud :(")
        silt_vastus2.place(x=260, y=290)
        silt_vastus2.config(font=("Rockwell", 25), background = "black", foreground = "white")
    
    
                      
    fail2.close()
    aken.mainloop()
    

# ilmutame akna ekraanile
raam.mainloop()
