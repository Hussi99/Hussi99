import tkinter
canvas = tkinter.Canvas(width=600,height=600,bg='white')
canvas.pack()
from random import*

def lopticka (x,y):
    canvas.create_oval(x-5,y-5,x+5,y+5,fill='red',width=0,tag='lopta')

def lopatka(x,y):
    canvas.create_line(x,y,x+25,y,fill='blue',tag='lopata')

def hra():
    canvas.delete('lopta')
    canvas.delete('lopata')
    global surx, sury, kurzorx, kurzory, pocetbodov, m
    sury = sury+5
    lopticka(surx,  sury)
    lopatka(kurzorx, kurzory)
    if kurzorx<surx<kurzorx+25 and kurzory-5<sury<kurzory+5:
        pocetbodov +=1
        canvas.delete('pb')
        canvas.create_text(500,10,text=pocetbodov,tag='pb')
        surx = randint(5,int(canvas['width'])-5)
        sury = 5
        m = randint(100,400)
    if sury > int (canvas['height']):
        surx = randint(5,int(canvas['width'])-5)
        sury = 5

    kurzory = int (canvas['height'])-m
    canvas.after(10,hra)
    
    

def pohyb(event):
    global kurzorx
    kurzorx = event.x
    

pocetbodov = 0
surx = randint(5,int(canvas['width'])-5)
sury = 5
kurzorx = 200
m = randint(100,400)
kurzory = int (canvas['height'])-m

hra()
canvas.bind('<Motion>',pohyb)
