# impordi tk vidinad ja konstandid
from tkinter import *           # tkinteri põhivahendid
from tkinter import ttk         # platvormi ühise stiili saamiseks
from tkinter import messagebox 
import tkinter
import random
from tkinter import Text

raam = Tk()

#def command1():
#    x = "1"
#def command2():
#    x = "2"
#def command3():
#    x = "3"
#def command4():
#    x = "4"
#def command5():
#    x = "5"
#def command6():
#    x = "6"
#def command7():
#    x = "7"
#def command8():
#    x = "8"

def tervitus():
    tervitus = 'Tere'
    messagebox.showinfo(message=tervitus)
asd=0
def loodus(x):
    y="1"
    x=x+y
    print(x)
def loodus2(x):
    y="2"
    x=x+y
    print(x)

def kustuta(x):
    x.destroy()
    return x
def rate(x):
    nup1 = ttk.Button(raam, text="1+", asd=loodus(x))
#    nup1 = ttk.Button(raam, text="1+",)
    nup1.place(x=165, y=400, width=110)
    nup3 = ttk.Button(raam, text="3+", asd=loodus2(x))
    nup3.place(x=275, y=400, width=110)
    nup5 = ttk.Button(raam, text="5+", )
    nup5.place(x=385, y=400, width=110)
    nup7 = ttk.Button(raam, text="7+",)
    nup7.place(x=495, y=400, width=110)
    nup9 = ttk.Button(raam, text="9+", )
    nup9.place(x=605, y=400, width=110)
    
    
def lehekylg():
    def hinnang():
        silt2 = ttk.Label(raam, text="Palun valige sarja hinnang bby boy")
        silt2.config(font=("Courier", 25), background = "black", foreground = "white")
        silt2.place(x=150, y=350)
        x="1"
        print(x)
        rate(x)
        
        
        
        
    def hinnang2():
        silt2 = ttk.Label(raam, text="Palun valige sarja hinnang bby boy")
        silt2.config(font=("Courier", 25), background = "black", foreground = "white")
        silt2.place(x=150, y=350)
        x="2"
        print(x)
        rate(x)
        
        
        
    def hinnang3():
        silt2 = ttk.Label(raam, text="Palun valige sarja hinnang bby boy")
        silt2.config(font=("Courier", 25), background = "black", foreground = "white")
        silt2.place(x=150, y=350)
        x="3"
        print(x)
        rate(x)
        
        
    def hinnang4():
        silt2 = ttk.Label(raam, text="Palun valige sarja hinnang bby boy")
        silt2.config(font=("Courier", 25), background = "black", foreground = "white")
        silt2.place(x=150, y=350)
        x="4"
        print(x)
        rate(x)
    def hinnang5():
        silt2 = ttk.Label(raam, text="Palun valige sarja hinnang bby boy")
        silt2.config(font=("Courier", 25), background = "black", foreground = "white")
        silt2.place(x=150, y=350)
        x="5"
        print(x)
        rate(x)
        
        
    def hinnang6():
        silt2 = ttk.Label(raam, text="Palun valige sarja hinnang bby boy")
        silt2.config(font=("Courier", 25), background = "black", foreground = "white")
        silt2.place(x=150, y=350)
        x="6"
        print(x)
        rate(x)
        
        
    def hinnang7():
        silt2 = ttk.Label(raam, text="Palun valige sarja hinnang bby boy")
        silt2.config(font=("Courier", 25), background = "black", foreground = "white")
        silt2.place(x=150, y=350)
        x="7"
        print(x)
        rate(x)
        
        
    def hinnang8():
        silt2 = ttk.Label(raam, text="Palun valige sarja hinnang bby boy")
        silt2.config(font=("Courier", 25), background = "black", foreground = "white")
        silt2.place(x=150, y=350)
        x="8"
        print(x)
        rate(x)
#        kustuta(nupp11)
#        kustuta(nupp)
#        kustuta(nupp0)
#        kustuta(silt)
        
    # loome tekstikasti jaoks sildi
    silt = ttk.Label(raam, text="Palun valige endale meeldiv žanr")
    silt.config(font=("Courier", 25), background = "black", foreground = "white")
    silt.place(x=150, y=350)
    nupp1 = ttk.Button(raam, text="Action", command=hinnang)
    nupp1.place(x=165, y=400, width=50)
    nupp1 = ttk.Button(raam, text="Adventure", command=hinnang2)
    nupp1.place(x=215, y=400, width=70)
    nupp3 = ttk.Button(raam, text="Comedies", command=hinnang3 )
    nupp3.place(x=285, y=400, width=70)
    nupp5 = ttk.Button(raam, text="Dramas", command=hinnang4)
    nupp5.place(x=355, y=400, width=50)
    nupp8 = ttk.Button(raam, text="Horror", command=hinnang5)
    nupp8.place(x=405, y=400, width=50)
    nupp0 = ttk.Button(raam, text="Romance", command=hinnang6)
    nupp0.place(x=455, y=400, width=70)
    nupp = ttk.Button(raam, text="Sci-Fi", command=hinnang7)
    nupp.place(x=525, y=400, width=50)
    nupp11 = ttk.Button(raam, text="Thriller", command=hinnang8)
    nupp11.place(x=575, y=400, width=50)
    kustuta(nuppx)
    kustuta(silt1)

# loome akna

raam.geometry("930x720")
tahvel = Canvas(raam, width=930, height=720, background="black")
tahvel.grid()

#lisame logo

logo = PhotoImage(file="flixnet.png")
img = tahvel.create_image(50, 10, image=logo, anchor = NW)


   
nuppx = ttk.Button(raam, text="Edasi", command=lehekylg)
nuppx.place(x=365, y=350, width=200, height=100)
        
silt1 = ttk.Label(raam, text = "Tere tulemast")
silt1.place(x=335, y=270)
silt1.config(font=("Courier", 25), background = "black", foreground = "white")




# ilmutame akna ekraanile
raam.mainloop()
