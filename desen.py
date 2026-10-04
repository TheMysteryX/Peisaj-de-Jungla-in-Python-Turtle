import turtle

t = turtle.Turtle()

turtle.setup(2560,1600) #latime: 1280 * 2, inaltime: 800 * 2
t.speed(0)
turtle.tracer(0,0)

#solul maroniu
def sol(latime, inaltime, culoare):
    t.color(culoare)
    t.begin_fill()
    for _ in range(2):
        t.forward(latime)
        t.right(90)
        t.forward(inaltime)
        t.right(90)
    t.end_fill()     

#fundalul verde
def fundal(latime, inaltime, culoare):
    t.color(culoare)
    t.begin_fill()
    for _ in range(2):
        t.forward(latime)
        t.left(90)
        t.forward(inaltime)
        t.left(90)
    t.end_fill()   

#copacii din fundal
def copaci(grosime, cul):
    t.color(cul)
    t.begin_fill()
    t.forward(2000)
    t.right(90)
    t.forward(grosime)
    t.right(90)
    t.forward(2000)
    t.right(90)
    t.forward(grosime)
    t.end_fill()   
    
#frunze/vegetatie
def planta3(lungime, culoare): #o planta cu 3 frunze
    t.color(culoare)
    t.begin_fill()
    t.right(200)
    t.left(120)
    t.forward(lungime-(lungime/3))
    t.right(65)
    t.forward(lungime)
    t.right(120)
    t.forward(lungime)
    t.right(65)
    t.forward(lungime-(lungime/3))

    t.left(120)
    t.forward(lungime-(lungime/3))
    t.right(65)
    t.forward(lungime)
    t.right(120)
    t.forward(lungime)
    t.right(65)
    t.forward(lungime-(lungime/3))

    t.left(120)
    t.forward(lungime-(lungime/3))
    t.right(65)
    t.forward(lungime)
    t.right(120)
    t.forward(lungime)
    t.right(70)
    t.forward(lungime-(lungime/3))

    t.end_fill()


def planta6(lungime, culoare1, culoare2): #sau floare cu 6 petale  
    planta3(lungime, culoare1)
    t.color(culoare1)
    t.color(culoare2)
    t.begin_fill()
    t.right(150)
    t.left(120)
    t.forward(lungime-(lungime/3))
    t.right(65)
    t.forward(lungime)
    t.right(120)
    t.forward(lungime)
    t.right(65)
    t.forward(lungime-(lungime/3))
    
    t.left(120)
    t.forward(lungime-(lungime/3))
    t.right(65)
    t.forward(lungime)
    t.right(120)
    t.forward(lungime)
    t.right(65)
    t.forward(lungime-(lungime/3))
    
    t.left(120)
    t.forward(lungime-(lungime/3))
    t.right(65)
    t.forward(lungime)
    t.right(120)
    t.forward(lungime)
    t.right(70)
    t.forward(lungime-(lungime/3))
    
    t.end_fill()


#pietricica sol
def pietricica(marime, culoare):
    t.color(culoare)
    t.begin_fill()
    t.forward(marime)
    t.right(50)
    t.forward(marime/2)
    t.right(90)
    t.forward(marime)
    t.right(30)
    t.forward(marime/2)
    t.end_fill()
    
#betisor sol
def bat(lungime, grosime, culoare):
    t.color(culoare)
    t.pensize(grosime)
    t.begin_fill()
    t.forward(lungime)
    t.end_fill()

#crenguta = bat + ramuri
def crenguta(lung, gros, cul):
    bat(lung,gros,cul)

    t.penup()
    t.backward(lung/2)    
    t.right(60)
    t.pendown()
    bat(lung/2,gros,cul)

    t.penup()
    t.backward(lung/2)
    t.left(60)
    t.backward(lung/2)
    t.right(150)
    t.pendown()
    bat(lung,gros,cul)
    
    t.penup()
    t.backward(lung/2)
    t.right(150)
    t.pendown()
    bat(lung,gros,cul)
    
    t.penup()
    t.backward(lung/3)
    t.right(30)
    t.pendown()
    bat(lung,gros,cul)    
    
    t.penup()
    t.backward(lung/0.75)
    t.right(30)
    t.pendown()
    bat(lung/2,gros,cul)

#ferigi
def frunzaFeriga(lungime, culoare):
    t.color(culoare)
    t.begin_fill()
    for _ in range(2):
        t.forward(lungime)
        t.left(40)
        t.forward(lungime)
        t.left(140)
    t.end_fill()

def pereche_frunze(lungime, culoare): #o pereche de frunze opuse
    frunzaFeriga(lungime, culoare)
    t.right(100)
    frunzaFeriga(lungime, culoare)
    t.left(70)
    
def inainte(lungime): #mutare inainte pentru urmatoarea pereche de frunze
    t.penup()
    t.forward(lungime/2)
    t.left(30)
    t.pendown()

#feriga dreapta    
def feriga(lungime, grosime, cul1, cul2):
    for _ in range(2):
        bat(lungime*4, grosime, "#572c00")
        t.penup()
        t.backward(lungime*4)
        t.left(30)
        t.pendown()
        pereche_frunze(lungime, cul1)
        
        culori = [cul2, cul1, cul2, cul1, cul2, cul1, cul2, cul1]
        for c in culori:
            inainte(lungime)
            pereche_frunze(lungime, c)    
        
#feriga aplecata
def pereche_frunze2(lungime, culoare):
    frunzaFeriga(lungime, culoare)
    t.right(90)
    frunzaFeriga(lungime, culoare)
    t.left(60)

def inainte2(lungime):
    t.color("#30281e")
    t.forward(lungime/2)
    t.left(20)

def feriga2(lungime, cul1, cul2):
    t.penup()
    t.backward(lungime*4)
    t.left(20)
    t.pendown()
    pereche_frunze2(lungime, cul1)

    culori = [cul2, cul1, cul2, cul1, cul2, cul1, cul2, cul1, cul2]

    for c in culori:
        inainte2(lungime)
        pereche_frunze2(lungime, c)


#ferigi oglindite
def frunzaFeriga_mirror(lungime, culoare):
    t.color(culoare)
    t.begin_fill()
    for _ in range(2):
        t.forward(lungime)
        t.right(40)     
        t.forward(lungime)
        t.right(140)    
    t.end_fill()

def pereche_frunze_mirror(lungime, culoare):
    frunzaFeriga_mirror(lungime, culoare)
    t.left(100)            
    frunzaFeriga_mirror(lungime, culoare)
    t.right(70)            

def inainte_mirror(lungime):
    t.penup()
    t.forward(lungime/2)
    t.right(30)      
    t.pendown()

#feriga dreapta oglindita
def feriga_mirror(lungime, grosime, cul1, cul2):
    for _ in range(2):
        bat(lungime*4, grosime, "#9dae6c")
        t.penup()
        t.backward(lungime*4)
        t.right(30)                    
        t.pendown()
        pereche_frunze_mirror(lungime, cul1)
        
        culori = [cul2, cul1, cul2, cul1, cul2, cul1, cul2, cul1]
        for c in culori:
            inainte_mirror(lungime)
            pereche_frunze_mirror(lungime, c)

def pereche_frunze2_mirror(lungime, culoare):
    frunzaFeriga_mirror(lungime, culoare)
    t.left(90)
    frunzaFeriga_mirror(lungime, culoare)
    t.right(60)

def inainte2_mirror(lungime):
    t.color("#9dae6c")
    t.forward(lungime/2)
    t.right(20)

#feriga aplecata oglindita
def feriga2_mirror(lungime, cul1, cul2):
    t.penup()
    t.backward(lungime*4)
    t.right(20)                           
    t.pendown()
    pereche_frunze2_mirror(lungime, cul1)

    culori = [cul2, cul1, cul2, cul1, cul2, cul1, cul2, cul1, cul2]

    for c in culori:
        inainte2_mirror(lungime)
        pereche_frunze2_mirror(lungime, c)

#ferigile din fundal drepte
def ferigaback(lungime, grosime, cul1, cul2):
    for _ in range(2):
        bat(lungime*4, grosime, "#b2c67c")
        t.penup()
        t.backward(lungime*4)
        t.left(30)
        t.pendown()
        pereche_frunze(lungime, cul1)
        
        culori = [cul2, cul1, cul2, cul1, cul2, cul1, cul2, cul1]
        for c in culori:
            inainte(lungime)
            pereche_frunze(lungime, c) 

#ferigile din fundal aplecate                
def inainte2back(lungime):
    t.color("#b2c67c")
    t.forward(lungime/2)
    t.left(20)   
            
def feriga2back(lungime, cul1, cul2):
    t.penup()
    t.backward(lungime*4)
    t.left(20)
    t.pendown()
    pereche_frunze2(lungime, cul1)

    culori = [cul2, cul1, cul2, cul1, cul2, cul1, cul2, cul1, cul2]

    for c in culori:
        inainte2back(lungime)
        pereche_frunze2(lungime, c)

#DESENUL PROPRIU-ZIS
#sol    
t.penup()
t.goto(-1280,-200)
t.pendown()   
sol(2560, 600, "#47331d")
t.left(90)

#fundal   
t.penup()
t.goto(-1280, -200)
t.pendown()
t.right(90)
fundal(2560, 1400, "#dbf291")
t.right(90)

#copac
t.penup()
t.goto(30,-300)
t.pendown()
t.color("#3b320c")
t.begin_fill()
#radacini
t.left(90)
t.left(20)
t.forward(160)
t.left(40)
t.forward(200)
#trunchi
t.left(30)
t.forward(2000)
t.right(90)
t.forward(200)
t.right(90)
t.forward(2000)
#radacini
t.left(20)
t.forward(80)
t.left(40)
t.forward(160)
t.right(150)
t.forward(120)
t.goto(30,-300)
t.end_fill()

#umbra copac
t.color("#52460f")
t.begin_fill()
t.penup()
t.goto(280,1280)
t.pendown()
t.right(180)
t.forward(80)
t.right(90)
t.forward(1200)
t.right(27)
t.forward(200)
t.backward(27)
t.right(153)
t.forward(2000)
t.left(90)
t.goto(280,1280)
# t.left(90)
# t.forward(2000)
t.end_fill()

#plante diverse
t.penup()
t.goto(1200,0)    
t.pendown()
planta6(130, "#2b5423", "#223421")

t.penup()
t.right(90)
t.goto(900,-100)    
t.pendown()
planta3(75, "#405B3E")

t.penup()
t.right(50)
t.goto(800,-200)    
t.pendown()
planta3(85,"#264F24")

t.penup()
t.right(100)
t.goto(1000,-300)    
t.pendown()
planta3(95,"#496C47")

t.penup()
t.right(60)
t.goto(1050,-100)    
t.pendown()
planta3(80,"#364635")

t.penup()
t.right(90)
t.goto(1100,-50)    
t.pendown()
planta3(110,"#426841")

t.penup()
t.right(40)
t.goto(1100,-200)    
t.pendown()
planta3(130,"#274626")

t.penup()
t.right(90)
t.goto(1100,-300)    
t.pendown()
planta3(110,"#293629")

t.penup()
t.right(120)
t.goto(1200,-400)    
t.pendown()
planta3(150,"#154613")

t.penup()
t.right(30)
t.goto(1000,-500)    
t.pendown()
planta3(110,"#284926")

t.penup()
t.right(70)
t.goto(900,-600)    
t.pendown()
planta3(120,"#355433")

t.penup()
t.right(50)
t.goto(1200,-700)    
t.pendown()
planta3(150,"#3E5C3C")

t.penup()
t.right(30)
t.goto(1000,-500)    
t.pendown()
planta3(110,"#284926")

t.penup()
t.right(60)
t.goto(800,-400)    
t.pendown()
planta6(150, "#374d33", "#232C22")

t.penup()
t.right(70)
t.goto(1200,-650)    
t.pendown()
planta6(170, "#33522e", "#263125") 

t.penup()
t.right(30)
t.goto(1200,-300)    
t.pendown()
planta3(110,"#395F37")

t.penup()
t.right(50)
t.goto(1200,-200)    
t.pendown()
planta3(150,"#344933")


#floricica
t.penup()
t.right(90)
t.goto(700,-600)    
t.pendown()
planta6(170, "#e27171", "#B41B1B")
t.penup()
t.goto(670,-570)
t.pendown()
t.begin_fill()
t.color("#E7CF6F")
t.circle(50,360) 
t.end_fill()


#pietricele si crengute sol
t.penup()
t.right(30)
t.goto(-200,-250)    
t.pendown()
pietricica(20,"#3d2c1a")

t.penup()
t.right(60)
t.goto(-500,-400)    
t.pendown()
pietricica(15,"#2E1E0F")

t.penup()
t.right(90)
t.goto(-400,-300)    
t.pendown()
pietricica(10,"#392616")

t.penup()
t.right(110)
t.goto(-300,-450)    
t.pendown()
pietricica(25,"#372818")

t.penup()
t.right(140)
t.goto(-700,-450)    
t.pendown()
pietricica(20,"#332312")

t.penup()
t.right(30)
t.goto(-800,-400)    
t.pendown()
pietricica(20,"#44301C")

t.penup()
t.right(30)
t.goto(-400,-400)    
t.pendown()
crenguta(200,10,"#543523")

t.penup()
t.right(30)
t.goto(-900,-500)    
t.pendown()
pietricica(20,"#3d2c1a")

t.penup()
t.right(60)
t.goto(-950,-550)    
t.pendown()
pietricica(15,"#2E1E0F")

t.penup()
t.right(90)
t.goto(-1000,-600)    
t.pendown()
pietricica(10,"#392616")

t.penup()
t.right(110)
t.goto(-1100,-650)    
t.pendown()
pietricica(25,"#372818")

t.penup()
t.right(140)
t.goto(-800,-575)    
t.pendown()
pietricica(20,"#332312")

t.penup()
t.right(30)
t.goto(-875,-675)    
t.pendown()
pietricica(20,"#44301C")

t.penup()
t.right(80)
t.goto(200,-500)    
t.pendown()
crenguta(200,15,"#3E2A1E")


t.penup()
t.right(30)
t.goto(0,-250)    
t.pendown()
pietricica(20,"#3d2c1a")

t.penup()
t.right(60)
t.goto(50,-400)    
t.pendown()
pietricica(15,"#2E1E0F")

t.penup()
t.right(90)
t.goto(100,-300)    
t.pendown()
pietricica(10,"#392616")

t.penup()
t.right(110)
t.goto(150,-450)    
t.pendown()
pietricica(25,"#372818")

t.penup()
t.right(140)
t.goto(200,-450)    
t.pendown()
pietricica(20,"#332312")

t.penup()
t.right(30)
t.goto(450,-400)    
t.pendown()
pietricica(20,"#44301C")


t.penup()
t.right(30)
t.goto(-100,-400)    
t.pendown()
pietricica(20,"#3d2c1a")

t.penup()
t.right(60)
t.goto(-25,-400)    
t.pendown()
pietricica(15,"#2E1E0F")

t.penup()
t.right(90)
t.goto(-50,-600)    
t.pendown()
pietricica(10,"#392616")

t.penup()
t.right(110)
t.goto(-150,-700)    
t.pendown()
pietricica(25,"#372818")

t.penup()
t.right(140)
t.goto(-200,-765)    
t.pendown()
pietricica(20,"#332312")

t.penup()
t.right(30)
t.goto(-150,-670)    
t.pendown()
pietricica(20,"#44301C")


t.penup()
t.right(30)
t.goto(-50,-250)    
t.pendown()
pietricica(20,"#3d2c1a")

t.penup()
t.right(60)
t.goto(-25,-400)    
t.pendown()
pietricica(15,"#2E1E0F")

t.penup()
t.right(90)
t.goto(0,-600)    
t.pendown()
pietricica(10,"#392616")

t.penup()
t.right(110)
t.goto(25,-700)    
t.pendown()
pietricica(25,"#372818")

t.penup()
t.right(140)
t.goto(50,-670)    
t.pendown()
pietricica(20,"#332312")

t.penup()
t.right(30)
t.goto(75,-735)    
t.pendown()
pietricica(20,"#44301C")


t.penup()
t.right(30)
t.goto(-250,-250)    
t.pendown()
pietricica(20,"#3d2c1a")

t.penup()
t.right(60)
t.goto(-300,-400)    
t.pendown()
pietricica(15,"#2E1E0F")

t.penup()
t.right(90)
t.goto(-350,-600)    
t.pendown()
pietricica(10,"#392616")

t.penup()
t.right(110)
t.goto(-400,-700)    
t.pendown()
pietricica(25,"#372818")

t.penup()
t.right(140)
t.goto(-450,-745)    
t.pendown()
pietricica(20,"#332312")

t.penup()
t.right(30)
t.goto(-500,-770)    
t.pendown()
pietricica(20,"#44301C")


#frunze cazute
t.penup()
t.right(30)
t.goto(-75,-275)    
t.pendown()
pietricica(25,"#3A481F")

t.penup()
t.right(60)
t.goto(-125,-430)    
t.pendown()
pietricica(20,"#3A411F")

t.penup()
t.right(90)
t.goto(35,-630)    
t.pendown()
pietricica(15,"#47481E")

t.penup()
t.right(110)
t.goto(130,-730)    
t.pendown()
pietricica(30,"#434B2E")

t.penup()
t.right(140)
t.goto(175,-700)    
t.pendown()
pietricica(25,"#3A4112")

t.penup()
t.right(30)
t.goto(230,-670)    
t.pendown()
pietricica(30,"#3B4123")


t.penup()
t.right(30)
t.goto(-225,-275)    
t.pendown()
pietricica(25,"#3A481F")

t.penup()
t.right(60)
t.goto(-325,-430)    
t.pendown()
pietricica(20,"#3A411F")

t.penup()
t.right(90)
t.goto(-425,-630)    
t.pendown()
pietricica(15,"#47481E")

t.penup()
t.right(110)
t.goto(-535,-730)    
t.pendown()
pietricica(30,"#434B2E")

t.penup()
t.right(140)
t.goto(-675,-700)    
t.pendown()
pietricica(25,"#3A4112")

t.penup()
t.right(30)
t.goto(-725,-800)    
t.pendown()
pietricica(30,"#3B4123")


t.penup()
t.right(30)
t.goto(-775,-275)    
t.pendown()
pietricica(25,"#3A481F")

t.penup()
t.right(60)
t.goto(-675,-430)    
t.pendown()
pietricica(20,"#3A411F")

t.penup()
t.right(90)
t.goto(-575,-630)    
t.pendown()
pietricica(15,"#47481E")

t.penup()
t.right(110)
t.goto(-475,-730)    
t.pendown()
pietricica(30,"#434B2E")

t.penup()
t.right(140)
t.goto(-375,-775)    
t.pendown()
pietricica(25,"#3A4112")

t.penup()
t.right(30)
t.goto(-275,-725)    
t.pendown()
pietricica(30,"#3B4123")


#piatra mare + detalii
t.penup()
t.right(90)
t.goto(-1350,-600)    
t.pendown()
pietricica(500,"#868B7F")

t.penup()
t.right(30)
t.goto(-1200,-725)    
t.pendown()
pietricica(50,"#5B6052")

t.penup()
t.right(60)
t.goto(-1000,-600)    
t.pendown()
pietricica(100,"#72776A")

t.penup()
t.right(90)
t.goto(-900,-725)    
t.pendown()
pietricica(70,"#71756A")

t.penup()
t.right(90)
t.goto(-850,-650)    
t.pendown()
pietricica(80,"#797C73")

t.penup()
t.right(30)
t.goto(-750,-675)    
t.pendown()
pietricica(25,"#52554B")

t.penup()
t.right(60)
t.goto(-875,-730)    
t.pendown()
pietricica(20,"#4B4D46")

t.penup()
t.right(90)
t.goto(-1000,-730)    
t.pendown()
pietricica(50,"#5F6052")

t.penup()
t.right(110)
t.goto(-830,-600)    
t.pendown()
pietricica(30,"#63665C")

t.penup()
t.right(140)
t.goto(-1125,-700)    
t.pendown()
pietricica(25,"#505342")

t.penup()
t.right(30)
t.goto(-1150,-655)    
t.pendown()
pietricica(70,"#626554")


#ferigi
t.penup()
t.left(90)
t.goto(-1300,-250)    
t.pendown()    
feriga(50, 5, "#2b4221", "#3a5a2e")

t.penup()
t.left(60)
t.goto(-1200,-180)    
t.pendown() 
feriga2(100, "#334825", "#2b4221")

t.penup()
t.left(60)
t.goto(-1150,0)    
t.pendown() 
feriga2(50, "#325330", "#22441D")


t.penup()
t.left(90)
t.goto(-1400,0)    
t.pendown()    
feriga(70, 7, "#1b2d14", "#44552f")

t.penup()
t.left(-10)
t.goto(-1200,-50)    
t.pendown()    
feriga(50, 5, "#2a3c23", "#364721")

t.penup()
t.left(10)
t.goto(-1200,50)    
t.pendown()    
feriga2(30, "#22351a", "#5a6b45")

t.penup()
t.left(140)
t.goto(-1100,300)    
t.pendown()    
feriga(30, 4, "#273522", "#384428")

t.penup()
t.left(-40)
t.goto(-1100,400)    
t.pendown()    
feriga2(70, "#2d3729", "#405835")

t.penup()
t.left(90)
t.goto(-1300,400)    
t.pendown()    
feriga(30, 3, "#3D4B31", "#54653E")

t.penup()
t.left(90)
t.goto(-1300,500)    
t.pendown()    
feriga2(30,"#324322", "#435828")

t.penup()
t.left(0)
t.goto(-1300,550)    
t.pendown()    
feriga(20, 3, "#3C5039", "#4B6044")

t.penup()
t.left(40)
t.goto(-1250,650)    
t.pendown()    
feriga2(20,"#3F4B34", "#323F21")

t.penup()
t.left(90)
t.goto(-1050,-525)    
t.pendown()    
feriga(20, 4, "#2a3a23", "#3f5238")

t.penup()
t.left(70)
t.goto(-1100,-430)    
t.pendown()    
feriga2(30, "#253320", "#35492e")

t.penup()
t.left(30)
t.goto(-1300,-400)    
t.pendown()    
feriga(30, 4, "#293125", "#44533f")

t.penup()
t.left(0)
t.goto(-1200,-400)    
t.pendown()    
feriga2(50, "#3A4535", "#1f3418")


#copacii din fundal
t.penup()
t.left(150)
t.goto(-725,-199)
t.pendown()
copaci(150, "#b2c67b")

t.penup()
t.right(90)
t.goto(-400,-199)
t.pendown()
copaci(100, "#bcd280")

t.penup()
t.right(90)
t.goto(-200,-199)
t.pendown()
copaci(125, "#b3c879")

t.penup()
t.right(90)
t.goto(75,-199)
t.pendown()
copaci(75, "#c4da86")

t.penup()
t.right(90)
t.goto(600,-199)
t.pendown()
copaci(150, "#b6cb7b")


#ferigile din fundal        
t.penup()
t.right(120)
t.goto(800,300)    
t.pendown()    
feriga2back(50, "#afc378", "#b2c67c")

t.penup()
t.left(90)
t.goto(800,400)    
t.pendown()    
feriga2back(30, "#afc378", "#b2c67c")

t.penup()
t.right(200)
t.goto(-600,-10)    
t.pendown()    
feriga2back(50, "#afc378", "#abbd78")

t.penup()
t.left(90)
t.goto(-600,-200)    
t.pendown()    
ferigaback(30, 4, "#a2b46f", "#adbf7c")

t.penup()
t.left(0)
t.goto(-650,-10)    
t.pendown()    
feriga2_mirror(40, "#a6b973", "#a0b271")

t.penup()
t.right(120)
t.goto(-100,37)    
t.pendown()    
feriga2_mirror(60, "#a6b973", "#a0b271")

t.penup()
t.right(90)
t.goto(-100,-200)    
t.pendown()    
ferigaback(30, 4, "#a2b46f", "#adbf7c")

t.penup()
t.right(0)
t.goto(-100,0)    
t.pendown()    
feriga2back(50, "#9cad6b", "#a2b374")

t.penup()
t.left(120)
t.goto(1200,500)    
t.pendown()    
feriga2_mirror(60, "#afc378", "#abbd78")

t.penup()
t.right(90)
t.goto(1300,400)    
t.pendown()    
feriga_mirror(40, 5, "#9eb06e", "#aec17e")

t.penup()
t.left(0)
t.goto(1200,800)    
t.pendown()    
feriga2_mirror(50, "#afc378", "#abbd78")

t.penup()
t.right(60)
t.goto(1300,400)    
t.pendown()    
feriga_mirror(30, 5, "#a0b074", "#b8cb88")

t.penup()
t.left(-10)
t.goto(1200,850)    
t.pendown()    
feriga2_mirror(30, "#a1b077", "#bad07e")

t.penup()
t.left(-10)
t.goto(1200,550)    
t.pendown()    
feriga2_mirror(30, "#adbc81", "#c4dc83")

t.penup()
t.left(180)
t.goto(1200,310)    
t.pendown()    
feriga2_mirror(30, "#a1b077", "#bad07e")
turtle.done()