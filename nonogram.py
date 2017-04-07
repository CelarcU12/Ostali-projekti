from tkinter import *
from random import*
from random import*
import time

#Igrica Nonogram
#risanje mreže

n= 600  #velikost mreže
b= 50 #polje za števila
c= 5 #c x c - število kvadratkov v mreži
  
barvaOzadja='cyan'

class Nonogram:

    def __init__(self,master):
        self.canvas = Canvas(master, width=n, height=n, bg=barvaOzadja)
        self.canvas.grid(row=0,column=0,columnspan=4)
        self.canvas.bind("<Button-1>", self.polozaj)
        self.canvas.bind("<Button-3>", self.polozaj2)
        self.poteza = 0
        b=Button(master, text='Preveri')
        b.grid(row=1,column=0)
        self.preberi(c)
        self.mreza()
        


        gumb1=Button(master, text='Preveri',command=self.matrika2)
        gumb2=Button(master, text='Nova igra' ,command=self.novaIgra)
        gumb3=Button(master, text='Počisti', command= self.pocisti)
    
        gumb1.grid(row=1,column=0)
        gumb2.grid(row=1,column=1)
        gumb3.grid(row=1,column=2)

        
        # Glavni meni:
        menu = Menu(master)
        master.config(menu=menu) # Dodamo meni


        # meniji in podmeniji:
        menu2=Menu(menu)
        menu.add_cascade(label="Možnosti", menu=menu2)
        menu2.add_command(label="Pomoč", command= self.pomoc)
        menu2.add_separator()
        menu2.add_command(label="Izhod", command= master.destroy)

        velikost = Menu(menu)
        menu.add_cascade(label="Velikost mreže", menu=velikost)
        
        velikost.add_command(label="5 x 5",command= self.novaIgra5 )
        velikost.add_command(label="7 x 7", command= self.novaIgra7)
        velikost.add_command(label="10 x 10", command= self.novaIgra10)
        velikost.add_command(label="15 x 15", command= self.novaIgra15)

        
   


       

    def matrika(self,c):
        self.risba=[]
        for i in range(c):
            self.risba.append([])
            for j in range(c):
                self.risba[i].append(randint(0,1))
        return self.risba
        



    def preberi(self,c):
        m=self.matrika(c)
        self.vr=[[] for i in range(c)]
        self.st=[[] for i in range(c)]
        k=0
        
        for vrstica in range(c):
            for el in range(c):
                if m[vrstica][el] == 1:
                    k+=1
                    if el==c-1:
                        self.vr[vrstica].append(k)
                        k=0
                        pass
                else:
                    if k> 0 and m[vrstica][el] == 0 :
                        self.vr[vrstica].append(k)
                        k=0
        for vrstica in range(c):
            for el in range(c):
                if m[el][vrstica] ==1:
                    k+=1
                    if el == c-1:
                        self.st[vrstica].append(k)
                        k=0
                        pass
                else:
                    if k> 0 and m[el][vrstica] == 0:
                        self.st[vrstica].append(k)
                        k=0
        št=[] #seznam z velikostjo seznama
        for el in range(c):
            št.append(len(self.vr[el]))
            št.append(len(self.st[el]))
            
        global a,b
        b=20*max(št)+20
        
        a=(n-b)/c
        #max število pove koliko števil bo v vrsti oz stolpcu
        st=0
        for el in self.vr:
            if len(el)==1:  #samo ena cifra
                x=b-(10+(len(el))*20)
                    
                y=b+st*a+a/2
                številka=str(el[0])
                self.canvas.create_text(x,y,text=številka)
                
            elif len(el)==0: #prazen sez
                x=b-(10+ 1*20)
                y=  b+st*a+a/2
                številka='0'
                self.canvas.create_text(x,y,text=številka)
                
            else:
                #seznam z vec ciframi
                st2=0
                for i in el:
                    x=b-(10+(len(el)-st2)*20)
                    y=b+st*a +a/2
                    številka=str(i)
                    self.canvas.create_text(x,y,text=številka)
                    st2+=1
            st+=1
        st=0
        for el in self.st:
            
            if len(el)==1:  #samo ena cifra
                y=b-(10+(len(el))*20)
                x=b+ st*a +a/2
                številka=str(el[0])
                self.canvas.create_text(x,y,text=številka)
                
            elif len(el)==0: #prazen seznam
                y=b-(10+ 1*20)
                x=b+ st*a +a/2
                številka='0'
                self.canvas.create_text(x,y,text=številka)
                
            else:
                #seznam z vec ciframi
                st2=0
                for i in el:
                    y=b-(10+(len(el)-st2)*20)
                    x=b+ st*a +a/2
                    številka=str(i)
                    self.canvas.create_text(x,y,text=številka)
                    st2+=1
            st+=1

        

    
                
    def mreza(self):
        '''funkcuja narise mrezo velikosti c x c'''
        #Risanje crt v mreži
        self.canvas.create_rectangle(0,0,b,b,outline="black")
        self.stanje = []
        for i in range(c):
            self.stanje.append([])
            for j in range(c):
                self.stanje[i].append(self.canvas.create_rectangle(b+a*(i),b+a*(j),b+a*(i+1),b+a*(j+1), outline="black"))

    def polozaj(self,event):
        '''funkcija ob kliku na prvi gumb kvadratek pobarva z zeleno barvo
           oz. ga obarva na prvotno barvo, če je ta pred klikom zelen'''
        #risanje kvadratkov
        vrstica, stolpec = (event.x-b)*c//(n-b), (event.y-b)*c//(n-b)
        kvadratek = self.stanje[vrstica][stolpec]
        if vrstica<0 or stolpec<0:
            pass
        elif self.canvas.itemcget(kvadratek, "fill")== 'green':
            self.canvas.itemconfig(kvadratek, fill= barvaOzadja)
        else:
            self.canvas.itemconfig(kvadratek, fill="green")
        
        
   
    def polozaj2(self,event):
        '''funkcija ob kliku na tretji gumb kvadratek pobarva s sivo barvo
           oz. ga obarva na prvotno barvo, če je ta pred klikom siv'''
        #risanje kvadratkov
        vrstica, stolpec = (event.x-b)*c//(n-b), (event.y-b)*c//(n-b)
        kvadratek = self.stanje[vrstica][stolpec]
        if vrstica<0 or stolpec<0:
            pass
        elif self.canvas.itemcget(kvadratek, "fill")== 'grey':
            self.canvas.itemconfig(kvadratek, fill= barvaOzadja)
        else:
            self.canvas.itemconfig(kvadratek, fill="grey")



        

    def matrika2(self):
        self.risba2=[]
        for i in range(c):
            self.risba2.append([])
            for j in range(c):
                kvadratek=self.stanje[j][i]
                if self.canvas.itemcget(kvadratek, "fill")== "green":
                    self.risba2[i].append(1)
                else:
                    self.risba2[i].append(0)
        if self.risba2==self.risba:
            pravilno=self.canvas.create_text(n/2,n/2,fill='black',text= 'PRAVILNO!', font=("Purisa",35))
        else:
            messagebox.showinfo(message='Vaša rešitev je NEPRAVILNA, poizkusite ponovno')
        
        

    def novaIgra(self):
        '''na novo izbere stevilke za izbrano velikost mreze'''
        self.canvas.delete('all')
        self.matrika(c)
        self.preberi(c)    
        self.mreza()


    def novaIgra5(self):
        '''velikost mreze nastavi na 5x5'''
        global c
        c=5
        self.novaIgra()

    def novaIgra7(self):
        '''velikost mreze nastavi na 7x7'''
        global c
        c=7
        self.novaIgra()

    def novaIgra10(self):
        '''velikost mreze nastavi na 10x10'''
        global c
        c=10
        self.novaIgra()

    def novaIgra15(self):
        '''velikost mreze nastavi na 15x15'''
        global c
        c=15
        self.novaIgra()


    def pocisti(self):
        '''funkcija pocisti vse kar je igralec do sedaj vnesel oz spreminjal.
        pocisti tudi morebitne napise, ki so se pojavili tekom igre'''
        for i in range(c):
            for j in range(c):
                kvadratek=self.stanje[j][i]
                if self.canvas.itemcget(kvadratek, "fill")!= barvaOzadja:
                    self.canvas.itemconfig(kvadratek, fill= barvaOzadja )
        self.canvas.delete(self.narobe)

    def pomoc(self):
        '''Funkcija odpre novo okno, kjer so navodila igre'''
        navodilo='''Imate mrežo kvadratov, kateri morajo biti ali pobarvani (polni) ali pa ne (prazni). Na začetku vsake vrstice/stolpca na mreži, so navedene dolžine nizov pobarvanih kvadratov v tej vrstici/stolpcu. Vaš cij je najti vse pobarvane kvadrate. Kliknite z levo miškino tipko da pobarvate kvadrat z zeleno. Z desno tipko si lahko označite kvadratek, za katerega menite, da zagotovo ne sme oz ne more biti pobarvan. '''
        messagebox.showinfo(title="Pravila igre",message=navodilo)
        return

    def izhod(self):
        '''Zapustimo igro'''
        izhod=messagebox.askyesno(title='Izhod',message='Ali res želite zapustiti igro?')
        if izhod > 0:
            self.canvas.destroy
        return
        
root=Tk()
root.title('Nonogram')
app=Nonogram(root)
root.mainloop()



            
                
    

