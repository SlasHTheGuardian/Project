import time
import tkinter
import random
from PIL import Image, ImageTk

#img = ImageTk.PhotoImage(Image.open(path))
#panel = tk.Label(root, image = img)


#------------basic statistics------------

RndIm=3
Weather=16
DipTimer=0
BonfireTimer=0
WeatherTimer=0
Season=1
Disease=0
DiseaseTimer=0
PoisoningTimer=0

lvlHRes=1
HRes=0
T=9
HP=0
I=3 #I=Immunity 1-7
D=58
H=random.randint(1,3) #H=Hungry 1-5
S=random.randint(2,5) #S=Sleep 1-9
ETextGood=' кушает ягоды'
ETextBad='Ягоды оказались ядовитыми!'
SText=' отдыхает'
ITextNothing=' пробует настойку из трав: Никакого эффекта'
ITextGood=' пробует настойку из трав: Самочувствие улучшается'
ITextBad=' пробует настойку из трав: Какой ужас!'
BText=' разводит костер'
CText=' купается в озере'


#------------basic statistics------------

def Finish():
    
    global Name
    
    window.title('Жизнь И:Смерть')
    
    DeathL1 = tkinter.Label(text="Этот день настал."+ Name.get() + " умер, прожив целых")
    DeathL1.place(x=400, y=400)
    
    DeathL2 = tkinter.Label(text=D)
    DeathL2.place(x=300, y=300)

    DeathL3 = tkinter.Label(text='Дней')
    DeathL3.place(x=240, y=110)
    
    GGWP = tkinter.Button(text='Покойся с миром, любимый '+Name.get() ) #command= Тут написать выход из программы 
    GGWP.place(x=240, y=10)   

    window.mainloop()


def WandD():
    global Eat1, Respose1
    global EText, Stext, WdEText, WdSText
    global Hunger, Hunger1, HungL
    global Sleep, Sleep1, SleepL
    global Immunity, Immunity1, ImmL
    global console, H, S, D, I, DAY, Heal1
    global Disease, DisL, Dis1
    global Health, HealthL, Health1
    global Temperature, Temp1, TempL
    global PoisL, DipL, BonfireL
    global SeasonL, WeatherL
    global Temp1B,Temp2B
    #death
    if HP>=30:
        try:
            DisL.destroy()
            PoisL.destroy()
            DipL.destroy()
            BonfireL.destroy()
        except OSError:
            pass
        Temp1B.destroy()
        Temp2B.destroy()
        SeasonL.destroy()
        WeatherL.destroy()
        ImmL.destroy()
        Heal1.destroy()
        console.destroy()
        Eat1.destroy()
        Respose1.destroy()
        DAY.destroy()
        HealthL.destroy()
        TempL.destroy()
        HungL.destroy()
        SleepL.destroy()
        time.sleep(1)
        Finish()

def DestroyCC():
    try:
        HungL.destroy()
        SleepL.destroy()
        ImmL.destroy()
        HealthL.destroy()
        TempL.destroy()
        SeasonL.destroy()
        WeatherL.destroy()
        DipL.destroy()
        BonfireL.destroy()
    except OSError:
        pass

def CC():
    global Eat, Respose
    global EText, Stext, WdEText, WdSText
    global Hunger, Hunger1, HungL
    global Sleep, Sleep1, SleepL
    global Immunity, Immunity1, ImmL
    global console, H, S, D, I
    global Disease, DisL, Dis1
    global Health, HealthL, Health1
    global Temperature, Temp1, TempL
    global Season, SeasonL, Season1
    global Weather, WeatherL, Weather1
    global BonfireTimer, BonfireL, Bonfire1
    global DipTimer, DipL, Dip1
    
    if HP==0:
        Health = Image.open('Health0.gif')
    if HP==1:
        Health = Image.open('Health-1.gif')
    if HP==2:
        Health = Image.open('Health-2.gif')
    if HP==3:
        Health = Image.open('Health-3.gif')
    if HP==4:
        Health = Image.open('Health-4.gif')
    if HP==5:
        Health = Image.open('Health-5.gif')
    if HP==6:
        Health = Image.open('Health-6.gif')
    if HP==7:
        Health = Image.open('Health-7.gif')
    if HP==8:
        Health = Image.open('Health-8.gif')
    if HP==9:
        Health = Image.open('Health-9.gif')
    if HP==10:
        Health = Image.open('Health-10.gif')
    if HP==11:
        Health = Image.open('Health-11.gif')
    if HP==12:
        Health = Image.open('Health-12.gif')
    if HP==13:
        Health = Image.open('Health-13.gif')
    if HP==14:
        Health = Image.open('Health-14.gif')
    if HP==15:
        Health = Image.open('Health-15.gif')
    if HP==16:
        Health = Image.open('Health-16.gif')
    if HP==17:
        Health = Image.open('Health-17.gif')
    if HP==18:
        Health = Image.open('Health-18.gif')
    if HP==19:
        Health = Image.open('Health-19.gif')
    if HP==20:
        Health = Image.open('Health-20.gif')
    if HP==21:
        Health = Image.open('Health-21.gif')
    if HP==22:
        Health = Image.open('Health-22.gif')
    if HP==23:
        Health = Image.open('Health-23.gif')
    if HP==24:
        Health = Image.open('Health-24.gif')
    if HP==25:
        Health = Image.open('Health-25.gif')
    if HP==26:
        Health = Image.open('Health-26.gif')
    if HP==27:
        Health = Image.open('Health-27.gif')
    if HP==28:
        Health = Image.open('Health-28.gif')
    if HP==29:
        Health = Image.open('Health-29.gif')
    if HP==30:
        Health = Image.open('Health-30.gif')
    Health1 = ImageTk.PhotoImage(Health)
    HealthL = tkinter.Label(window, image=Health1)
    HealthL.place(x=20, y=40)
    
    if T==1:
        Temperature = Image.open('Temp-8.gif')
    if T==2:
        Temperature = Image.open('Temp-7.gif')
    if T==3:
        Temperature = Image.open('Temp-6.gif')
    if T==4:
        Temperature = Image.open('Temp-5.gif')
    if T==5:
        Temperature = Image.open('Temp-4.gif')
    if T==6:
        Temperature = Image.open('Temp-3.gif')
    if T==7:
        Temperature = Image.open('Temp-2.gif')
    if T==8:
        Temperature = Image.open('Temp-1.gif')
    if T==9:
        Temperature = Image.open('Temp0.gif')
    if T==10:
        Temperature = Image.open('Temp+1.gif')
    if T==11:
        Temperature = Image.open('Temp+2.gif')
    if T==12:
        Temperature = Image.open('Temp+3.gif')
    if T==13:
        Temperature = Image.open('Temp+4.gif')
    if T==14:
        Temperature = Image.open('Temp+5.gif')
    if T==15:
        Temperature = Image.open('Temp+6.gif')
    if T==16:
        Temperature = Image.open('Temp+7.gif')
    if T==17:
        Temperature = Image.open('Temp+8.gif')
    Temp1 = ImageTk.PhotoImage(Temperature)
    TempL = tkinter.Label(window, image=Temp1)
    TempL.place(x=500, y=400)

    if H==1:
        Hunger = Image.open('Hunger1.gif')
    if H==2:
        Hunger = Image.open('Hunger2.gif')
    if H==3:
        Hunger = Image.open('Hunger3.gif')
    if H==4:
        Hunger = Image.open('Hunger4.gif')
    if H==5:
        Hunger = Image.open('Hunger5.gif')
    if H==6:
        Hunger = Image.open('Hunger6.gif')
    if H==7:
        Hunger = Image.open('Hunger7.gif')
    if H==8:
        Hunger = Image.open('Hunger8.gif')
    if H==9:
        Hunger = Image.open('Hunger9.gif')
    if H==10:
        Hunger = Image.open('Hunger10.gif')
    if H==11:
        Hunger = Image.open('Hunger11.gif')
    if H==12:
        Hunger = Image.open('Hunger12.gif')   
    Hunger1 = ImageTk.PhotoImage(Hunger)
    HungL = tkinter.Label(window, image=Hunger1)
    HungL.place(x=400, y=170)

    if I==1:
        Immunity = Image.open('Imm+2.gif')
    if I==2:
        Immunity = Image.open('Imm+1.gif')
    if I==3:
        Immunity = Image.open('Imm0.gif')
    if I==4:
        Immunity = Image.open('Imm-1.gif')
    if I==5:
        Immunity = Image.open('Imm-2.gif')
    if I==6:
        Immunity = Image.open('Imm-3.gif')
    if I==7:
        Immunity = Image.open('Imm-4.gif')
    Immunity1 = ImageTk.PhotoImage(Immunity)
    ImmL = tkinter.Label(window, image=Immunity1)
    ImmL.place(x=530, y=170)
    
    if S==1:
        Sleep = Image.open('Sleep1.gif')
    if S==2:
        Sleep = Image.open('Sleep2.gif')
    if S==3:
        Sleep = Image.open('Sleep3.gif')
    if S==4:
        Sleep = Image.open('Sleep4.gif')
    if S==5:
        Sleep = Image.open('Sleep5.gif')
    if S==6:
        Sleep = Image.open('Sleep6.gif')
    if S==7:
        Sleep = Image.open('Sleep7.gif')
    if S==8:
        Sleep = Image.open('Sleep8.gif')
    if S==9:
        Sleep = Image.open('Sleep9.gif')
    Sleep1 = ImageTk.PhotoImage(Sleep)
    SleepL = tkinter.Label(window, image=Sleep1)
    SleepL.place(x=220, y=170)

    if Season==1:
        SeasonImg = Image.open('Summer.gif')
    if Season==2:
        SeasonImg = Image.open('Autumn.gif')
    if Season==3:
        SeasonImg = Image.open('Winter.gif')
    if Season==4:
        SeasonImg = Image.open('Spring.gif')
    Season1 = ImageTk.PhotoImage(SeasonImg)
    SeasonL = tkinter.Label(window, image=Season1)
    SeasonL.place(x=200, y=600)

    if Weather==1:
        WeatherImg = Image.open('Storm.gif')
    if Weather==2:
        WeatherImg = Image.open('Thunderstorm.gif')
    if Weather==3:
        WeatherImg = Image.open('Cloudy+rain.gif')
    if Weather==4:
        WeatherImg = Image.open('Cloudy+wind+rain.gif')
    if Weather==5:
        WeatherImg = Image.open('Cloudy+wind.gif')
    if Weather==6:
        WeatherImg = Image.open('Cloudy.gif')
    if Weather==7:
        WeatherImg = Image.open('Cloudy+snow.gif')
    if Weather==8:
        WeatherImg = Image.open('Cloudy+snow+wind.gif')
    if Weather==9:
        WeatherImg = Image.open('PCloudy+wind+rain.gif')
    if Weather==10:
        WeatherImg = Image.open('PCloudy+rain.gif')
    if Weather==11:
        WeatherImg = Image.open('PCloudy+wind.gif')
    if Weather==12:
        WeatherImg = Image.open('PCloudy.gif')
    if Weather==13:
        WeatherImg = Image.open('PCloudy+wind+snow.gif')
    if Weather==14:
        WeatherImg = Image.open('PCloudy+wind.gif')
    if Weather==15:
        WeatherImg = Image.open('Sunny+wind.gif')
    if Weather==16:
        WeatherImg = Image.open('Sunny.gif')
    Weather1 = ImageTk.PhotoImage(WeatherImg)
    WeatherL = tkinter.Label(window, image=Weather1)
    WeatherL.place(x=300, y=500)

    if BonfireTimer>0:
        BonfireImg = Image.open('Bonfire.gif')
        Bonfire1 = ImageTk.PhotoImage(BonfireImg)
        BonfireL = tkinter.Label(window, image=Bonfire1)
        BonfireL.place(x=200, y=700)

    if DipTimer>0:
        DipImg = Image.open('Cooling.gif')
        Dip1 = ImageTk.PhotoImage(DipImg)
        DipL = tkinter.Label(window, image=Dip1)
        DipL.place(x=100, y=600)

    

def PickingBerries():
    global Eat, Respose, Name
    global EText, Stext, WdEText, WdSText
    global Hunger, Hunger1, HungL
    global Sleep, Sleep1, SleepL
    global Immunity, Immunity1, ImmL
    global console, H, S, D, I
    global Disease, DisL, Dis1
    global Health, HealthL, Health1
    global Temperature, Temp1, TempL
    global PoisL

    global Dayconsole

    SeasonF()
    WeatherWithTimer()
    TemperatureF()
    DayRandom()
    BerriesRnd=random.randint(1,15)
    if BerriesRnd<15 and D!=60:
        console.destroy()
        console = tkinter.Label(text=Name.get()+ETextGood)
        console.place(x=350, y=750)
        if H>1:
            H-=1
    if BerriesRnd==15 and D!=60:
        console.destroy()
        console = tkinter.Label(text=Name.get()+ETextBad)
        console.place(x=350, y=750)
        Poisoning()
        
    if S<9:
        S+=1
    D+=1
    CheckHealth()
    DestroyCC()
    CC()
    WandD()

def Rest():
    global Eat, Respose, Name
    global EText, Stext, WdEText, WdSText
    global Hunger, Hunger1, HungL
    global Sleep, Sleep1, SleepL
    global Immunity, Immunity1, ImmL
    global console, H, S, D, I
    global Disease, DisL, Dis1
    global Health, HealthL, Health1
    global Temperature, Temp1, TempL

    global Dayconsole

    SeasonF()
    WeatherWithTimer()
    TemperatureF()
    DayRandom()
    S=1
    if H<12:
        H+=1
    D+=1
    CheckHealth()
    if D!=60:
        console.destroy()
        console = tkinter.Label(text=Name.get()+SText)
        console.place(x=350, y=750)
    DestroyCC()
    CC()
    WandD()


def ImmunityUp():
    global S, H, I, console, Dayconsole ,DiseaseTimer, Name, RndIm, D
    SeasonF()
    WeatherWithTimer()
    TemperatureF()
    DayRandom()
    if S<9:
        S+=1
    if H<12:
        H+=1
    Irnd=random.randint(1,10)
    if Irnd>0 and Irnd<RndIm and D!=60:
        console.destroy()
        console = tkinter.Label(text=Name.get()+ITextGood)
        console.place(x=350, y=750)
        if I>1:
            I-=1
            DiseaseTimer=0
    if Irnd==RndIm and D!=60:
        console.destroy()
        console = tkinter.Label(text=Name.get()+ITextBad)
        console.place(x=350, y=750)
        if I<7:
            I+=1
    if Irnd>RndIm and D!=60:
        console.destroy()
        console = tkinter.Label(text=Name.get()+ITextNothing)
        console.place(x=350, y=750)
    D+=1
    CheckHealth()
    DestroyCC()
    CC()
    WandD()

def TemperatureF():
    global T, Season, Weather, BonfireTimer
    T=9
    if Season==1:
        T+=2
    if Season==2:
        T-=1
    if Season==3:
        T-=2
    if Season==4:
        T+=1  
    if Weather==16:
        T+=2
    if Weather==2 or Weather==3 or Weather==7 or Weather==10 or Weather==14:
        T-=1
    if Weather==5 or Weather==11:
        T-=2
    if Weather==1 or Weather==4 or Weather==8 or Weather==9 or Weather==13:
        T-=3
    if BonfireTimer>0:
        T+=2
    if DipTimer>0:
        T-=2
    
    

def DayRandom():
    global Eat, Respose
    global EText, Stext, WdEText, WdSText
    global Hunger, Hunger1, HungL
    global Sleep, Sleep1, SleepL
    global Immunity, Immunity1, ImmL
    global console, H, S, D, I, HP
    global Disease, DisL, Dis1, DiseaseTimer
    global Health, HealthL, Health1
    global Temperature, Temp1, TempL
    global PoisL, PoisoningTimer
    global BonfireTimer, DipTimer

    if D>15 and DiseaseTimer==0:
        if I==1:
            Disease=random.randint(1,1000)
        if I==2:
            Disease=random.randint(1,150)
        if I==3:
            Disease=random.randint(1,75)
        if I==4:
            Disease=random.randint(1,50)
        if I==5:
            Disease=random.randint(1,35)
        if I==6:
            Disease=random.randint(1,25)
        if I==7:
            Disease=random.randint(1,7)
            
    if Disease==1 and DiseaseTimer==0:    
        Sickness()

    if DiseaseTimer>0:
        DiseaseTimer-=1
        HP+=1
    elif DiseaseTimer==0:
        DisL.destroy()

    if PoisoningTimer>0:
        PoisoningTimer-=1
        HP+=1
    elif PoisoningTimer==0:
        try:
            PoisL.destroy()
        except OSError:
            pass
    if BonfireTimer>0:
        BonfireTimer-=1
    if DipTimer>0:
        DipTimer-=1

    if D==60:
        console.destroy()
        console = tkinter.Label(text='Похоже, '+ Name.get() + ' начинает различать травы.')
        console.place(x=350, y=750)
        HealReserch = tkinter.Button(text='Изучать травы', command=HReserch)
        HealReserch.place(x=150, y=310)


def Poisoning():
    global Pois, Pois1, PoisL, PoisoningTimer, I
    Pois = Image.open('Poisoning.gif')
    Pois1 = ImageTk.PhotoImage(Pois)
    PoisL = tkinter.Label(window, image=Pois1)
    PoisL.place(x=120, y=400)
    if I<3:
        PoisoningTimer=2
    if I>2:
        PoisoningTimer=4
    I+=1
        
def Sickness():
    global I, DiseaseTimer
    global Dis, Dis1, DisL
    Dis = Image.open('Disease.gif')
    Dis1 = ImageTk.PhotoImage(Dis)
    DisL = tkinter.Label(window, image=Dis1)
    DisL.place(x=120, y=300)
    if I==1:
        DiseaseTimer=1
    if I==2:
        DiseaseTimer=2
    if I==3:
        DiseaseTimer=3
    if I==4:
        DiseaseTimer=4
    if I==5:
        DiseaseTimer=5
    if I==6:
        DiseaseTimer=6
    if I==7:
        DiseaseTimer=7
    
    
def CheckHealth():
    global H, S, HP, T
    if H==5:
        HP+=1
    if S==9:
        HP+=1
        
    if I==1:
        if HP>2:
            HP-=3
        if HP==2:
            HP-=2
        if HP==1:
            HP-=1
    if I==2:
        if HP>2:
            HP-=2
        if HP==1:
            HP-=1
    if I==3:
        if HP>0:
           HP-=1       
    if T<7:
        HP+=1
        if T<5:
            HP+=1
    if T>12:
        HP+=1
        if T>14:
            HP+=1

def SeasonF():
    global Season
    Season=1+(D//90)
    while Season>4:
        Season-=4

def WeatherWithTimer():
    global WeatherTimer
    if WeatherTimer==0:
        WeatherF()
    else:
        WeatherTimer-=1

def HReserch():
    global HRes, lvlHRes, RndIm, console, S, H, HResL, HRes1, D, RndHReserch
    SeasonF()
    WeatherWithTimer()
    TemperatureF()
    DayRandom()
    console.destroy()
    HResL.destroy()
    RndHReserch=random.randint(1,6)
    Flag=0
    if S<9:
        S+=2
    if H<12:
        H+=2
    D+=1
    if lvlHRes<3:
        HRes+=1
    if lvlHRes>2 and lvlHRes<5:
        if HRes>0:
            if RndHReserch<5:
                HRes+=1
            else:
                console = tkinter.Label(text='Слишком сложно, ничего не выходит. Стоит отдохнуть и попробовать снова')
        else:
            HRes+=1
    if lvlHRes==5:
        if HRes>0:
            if S<9:
                S+=2
            if RndHReserch<3:
                HRes+=1
            else:
                console = tkinter.Label(text='Слишком сложно, ничего не выходит. Стоит отдохнуть и попробовать снова')
        else:
            HRes+=1
    if lvlHRes==1 and Flag==0:       
        if HRes==1:      
            HResImg = Image.open('1HR1.gif')
            console = tkinter.Label(text=Name.get() + ' начинает изучать азы ботаники, наблюдая за эффектами от растений')
        if HRes==2:
            HResImg = Image.open('1HR2.gif')
            console = tkinter.Label(text='Глава 1.1: Листья грецкого ореха прекрасно повышают работу иммунной системы')
        if HRes==3:   
            HResImg = Image.open('1HR3.gif')
            console = tkinter.Label(text='Глава 1.2: Женьшень - прекрасный имуностимулятор')
        if HRes==4:   
            HResImg = Image.open('1HRF.gif')
            console = tkinter.Label(text='Изучение 1 главы завершено. Теперь '+ Name.get() + ' знает чуть больше')
            RndIm=4
            lvlHRes=2
            Flag=1
            HRes=0
        HRes1 = ImageTk.PhotoImage(HResImg)
        HResL = tkinter.Label(window, image=HRes1)
        HResL.place(x=450, y=500)
        
    if lvlHRes==2 and Flag==0:
        if HRes==1 :      
            HResImg = Image.open('2HR1.gif')
            console = tkinter.Label(text='Глава 2.1: Ятрышник пятнистый помогает восстановиться после тяжелых заболеваний')
        if HRes==2:
            HResImg = Image.open('2HR2.gif')
            console = tkinter.Label(text='Глава 2.2: Родиола розовая помогает повысить физическую активность')
        if HRes==3:   
            HResImg = Image.open('2HR3.gif')
            console = tkinter.Label(text='Глава 2.3: Шалфей содержит необходимый для человека кремний')
        if HRes==4:   
            HResImg = Image.open('2HRF.gif')
            console = tkinter.Label(text='Изучение 2 главы завершено. Определенно, это успех')
            RndIm=5
            lvlHRes=3
            Flag=1
            HRes=0
        HRes1 = ImageTk.PhotoImage(HResImg)
        HResL = tkinter.Label(window, image=HRes1)
        HResL.place(x=450, y=500)

    if lvlHRes==3 and Flag==0:
        if HRes==1:      
            HResImg = Image.open('3HR1.gif')
            console = tkinter.Label(text='Глава 3.1: Клевер содержит много клетчатки')
        if HRes==2:
            HResImg = Image.open('3HR2.gif')
            console = tkinter.Label(text='Глава 3.2: Имбирь - источник цинка')
        if HRes==3:   
            HResImg = Image.open('3HR3.gif')
            console = tkinter.Label(text='Глава 3.3: Зверобой - "Лекарство от 100 болезней"')
        if HRes==4:   
            HResImg = Image.open('3HRF.gif')
            console = tkinter.Label(text='Изучение 3 главы завершено. Эти знания точно пригодятся!')
            RndIm=6
            lvlHRes=4
            Flag=1
            HRes=0
        HRes1 = ImageTk.PhotoImage(HResImg)
        HResL = tkinter.Label(window, image=HRes1)
        HResL.place(x=450, y=500)
            
    if lvlHRes==4 and Flag==0:
        if HRes==1:      
            HResImg = Image.open('4HR1.gif')
            console = tkinter.Label(text='Глава 4.1: Корень имбиря полезный и вкусный')
        if HRes==2:
            HResImg = Image.open('4HR2.gif')
            console = tkinter.Label(text='Глава 4.2: Алое отлично смягчает, питает кожу')
        if HRes==3:   
            HResImg = Image.open('4HR3.gif')
            console = tkinter.Label(text='Глава 4.3: Каланхоэ перистое содержит органические кислоты')
        if HRes==4:   
            HResImg = Image.open('4HRF.gif')
            console = tkinter.Label(text='Изучение 4 главы завершено. Но это еще не все')
            RndIm=8
            lvlHRes=5
            Flag=1
            HRes=0
        HRes1 = ImageTk.PhotoImage(HResImg)
        HResL = tkinter.Label(window, image=HRes1)
        HResL.place(x=450, y=500)

    if lvlHRes==5 and Flag==0:
        if HRes==1:      
            HResImg = Image.open('5HR1.gif')
            console = tkinter.Label(text='Глава 5.0: Экстраординарные травы: Очень сложно!')
        if HRes==2:
            HResImg = Image.open('5HR2.gif')
            console = tkinter.Label(text='Глава 5.1: Элеутерококк колючий:тонизирует, избавляет от хронической усталости')
        if HRes==3:   
            HResImg = Image.open('5HR3.gif')
            console = tkinter.Label(text='Глава 5.2: Гинкго Билоба: улучшает концентрацию внимания, ясность мышления и память')
        if HRes==4:   
            HResImg = Image.open('5HR4.gif')
            console = tkinter.Label(text='Глава 5.3: Люцерна: останавливает назальные кровотечения')
        if HRes==5:   
            HResImg = Image.open('5HR5.gif')
            console = tkinter.Label(text='Глава 5.4: Левзея: улучшает состав крови')
        if HRes==6:   
            HResImg = Image.open('5HRF.gif')
            console = tkinter.Label(text='Ботаника изучена! '+ Name.get() + ' -эксперт по травам.')
            RndIm=11
            lvlHRes=6
            Flag=1
            HRes=0
        HRes1 = ImageTk.PhotoImage(HResImg)
        HResL = tkinter.Label(window, image=HRes1)
        HResL.place(x=450, y=500)
            
    if lvlHRes==6 and Flag==0:
        console = tkinter.Label(text='Похоже, что ' + Name.get() + ' изучил ботанику идеально')
        HResImg = Image.open('5HRF.gif')
        HRes1 = ImageTk.PhotoImage(HResImg)
        HResL = tkinter.Label(window, image=HRes1)
        HResL.place(x=450, y=500)
    
    console.place(x=350, y=750)
    CheckHealth()
    DestroyCC()
    CC()
    WandD()

def BonfireF():
    global Bonfire, BonfireTimer, H, S, D, Dayconsole, console, Name
    SeasonF()
    WeatherWithTimer()
    DayRandom()
    BonfireTimer=3
    if H<12:
        H+=1
    if S<9:
        S+=3
    D+=1
    if D!=60:
        console.destroy()
        console = tkinter.Label(text=Name.get()+BText)
        console.place(x=350, y=750)
    TemperatureF()
    CheckHealth()
    DestroyCC()
    CC()
    WandD()
    
def DipF():
    global Dip, DipTimer, H, S, D, Dayconsole, console, Name
    SeasonF()
    WeatherWithTimer()
    DayRandom()
    DipTimer=3
    if H<12:
        H+=1
    if S<9:
        S+=3
    D+=1
    if D!=60:
        console.destroy()
        console = tkinter.Label(text=Name.get()+CText)
        console.place(x=350, y=750)
    TemperatureF()
    CheckHealth()
    DestroyCC()
    CC()
    WandD()
    
def WeatherF():
    global Weather, Season, WeatherRnd, WindRnd, StormRnd, PrecipitationRnd, WeatherTimer
    WeatherTimer=random.randint(5,14)
    WeatherRnd=random.randint(1,3)
    WindRnd=random.randint(1,2)
    StormRnd=random.randint(1,3)
    PrecipitationRnd=random.randint(1,2)
    if WeatherRnd==1:
        if Season!=3: 
            if PrecipitationRnd==1 and WindRnd==1 and StormRnd==1:
                Weather=1 #Storm.gif
            elif PrecipitationRnd==1 and WindRnd==2  and StormRnd==1:
                Weather=2 #Thunderstorm.gif
            elif PrecipitationRnd==1 and WindRnd==2  and StormRnd!=1:
                Weather=3 #Cloudy+rain.gif
            elif PrecipitationRnd==1 and WindRnd==1  and StormRnd!=1:
                Weather=4 #Cloudy+wind+rain.gif
            elif PrecipitationRnd==2 and WindRnd==1  and StormRnd!=1:
                Weather=5 #Cloudy+wind.gif
            elif PrecipitationRnd==2 and WindRnd==2  and StormRnd!=1:
                Weather=6 #Cloudy.gif
        elif Season==3:
            if PrecipitationRnd==1 and WindRnd==1 and StormRnd==1:
                Weather=1 #Storm.gif
            elif PrecipitationRnd==1 and WindRnd==2  and StormRnd!=1:
                Weather=7 #Cloudy+snow.gif
            elif PrecipitationRnd==1 and WindRnd==1  and StormRnd!=1:
                Weather=8 #Cloudy+snow+wind.gif
            elif PrecipitationRnd==2 and WindRnd==1  and StormRnd!=1:
                Weather=5 #Cloudy+wind.gif
            elif PrecipitationRnd==2 and WindRnd==2  and StormRnd!=1:
                Weather=6 #Cloudy.gif
    if WeatherRnd==2: #PCloudy
        if Season!=3:
            if PrecipitationRnd==1 and WindRnd==1:
                Weather=9 #PCloudy+wind+rain.gif
            if PrecipitationRnd==1 and WindRnd==2:
                Weather=10 #PCloudy+rain.gif
            if PrecipitationRnd==2 and WindRnd==1:
                Weather=11 #PCloudy+wind.gif
            if PrecipitationRnd==2 and WindRnd==2:
                Weather=12 #PCloudy.gif
        elif Season==3:
            if PrecipitationRnd==1 and WindRnd==1:
                Weather=13 #PCloudy+wind+snow.gif
            if PrecipitationRnd==1 and WindRnd==2:
                Weather=14 #PCloudy+snow.gif
            if PrecipitationRnd==2 and WindRnd==1:
                Weather=11 #PCloudy+wind.gif
            if PrecipitationRnd==2 and WindRnd==2:
                Weather=12 #PCloudy.gif
    if WeatherRnd==3: #Sunny
        if WindRnd==1:
            Weather=15 #Sunny+wind.gif
        elif WindRnd==2:
            Weather=16 #Sunny.gif
            
            
def day():
    global D, Dayconsole
    SeasonF()
    WeatherWithTimer()
    TemperatureF()
    D+=1
    DayRandom()
    CheckHealth()
    CC()
    WandD()
    

def EffectsLabels():
    global DisL, PoisL, SeasonL, BonfireL, DipL, HResL
    DisL= tkinter.Label(window)
    DisL.place(x=120, y=300)
    PoisL= tkinter.Label(window)
    PoisL.place(x=120, y=400)
    SeasonL = tkinter.Label(window)
    SeasonL.place(x=200, y=600) 
    BonfireL = tkinter.Label(window)
    BonfireL.place(x=200, y=600)
    DipL = tkinter.Label(window)
    DipL.place(x=200, y=600)
    HResL = tkinter.Label(window)
    HResL.place(x=200, y=600)
    
def Game():
    global Eat1, Respose1
    global EText, Stext, WdEText, WdSText
    global Hunger, Hunger1, HungL
    global Sleep, Sleep1, SleepL
    global Immunity, Immunity1, ImmL
    global console, H, S, D, I, DAY, Heal1
    global Disease, DisL, Dis1
    global Health, HealthL, Health1
    global Temperature, Temp1B, Temp2B, TempL
    global Wheather
    
    global Dayconsole
    
    window.title('Жизнь И:Игра')

    EffectsLabels()

    SeasonF()

    WeatherWithTimer()

    Eat1 = tkinter.Button(text='Сбор ягод', command=PickingBerries)
    Eat1.place(x=300, y=270)
    
    Respose1 = tkinter.Button(text='Сон', command=Rest)
    Respose1.place(x=400, y=270)

    Heal1 = tkinter.Button(text='Сбор трав на настойку', command=ImmunityUp)
    Heal1.place(x=150, y=270)
    
    Temp1B = tkinter.Button(text='Развести костер', command=BonfireF)
    Temp1B.place(x=400, y=350)
    
    Temp2B = tkinter.Button(text='Искупаться в озере', command=DipF)
    Temp2B.place(x=400, y=380)
  
    console = tkinter.Label(text=Name.get()+" потерялся в лесу")
    console.place(x=350, y=750)

    DAY=tkinter.Button(text='Day', command=day)
    DAY.place(x=500, y=700)

    Dayconsole = tkinter.Label(text=D)
    Dayconsole.place(x=4, y=4)

    CC()
    
    window.mainloop()
    
def ENToGame():
    global EntryName, StartGame, LEName
    EntryName.destroy()
    StartGame.destroy()
    LEName.destroy()
    Game()
    
def EName():
    global EntryName, LEName, Name, StartGame
    LEName = tkinter.Label(text="Введите ваше имя")
    LEName.place(x=250, y=150)
    Name=tkinter.StringVar()
    EntryName = tkinter.Entry(textvariable=Name)
    EntryName.place(x=250,y=300)
    StartGame = tkinter.Button(text='Ну, с Богом!', command=ENToGame)
    StartGame.place(x=325, y=260)

def PravToGame():
    global console
    global label2
    global Start
    global H
    global S
    label2.destroy()
    Start.destroy()   
    EName()

def ToGame():
    global console
    global H
    global S
    Da.destroy()
    No.destroy()
    label1.destroy()
    EName()

def Pravila():
    global label2
    global Start
    Da.destroy()
    No.destroy()
    label1.destroy()
    window.title('Жизнь И:Правила игры')
    label2 = tkinter.Label(text="В таком случае, вам необходимо ознакомиться с правилами игры.\n\nПравила игры \nВаша главная задача-защищать Игоря от этого жестокого мира.\nДля этого Игорь должен кушать и спать.\nПоддерживайте основные характеристики в норме, и ваш Игорь будет жить долго и счастливо")
    label2.place(x=150, y=150)
    Start = tkinter.Button(text='Я все понял,я готов попробовать', command=PravToGame)
    Start.place(x=325, y=260)


window = tkinter.Tk()

window.title('Жизнь И:Главное Меню')

window.geometry("600x800+256+128")

label1 = tkinter.Label( text="Доброго времени суток. \nВы впервые в этой игре?")
label1.place(x=335, y=180)

Da = tkinter.Button(text='Да', height=1, width=5, command=Pravila)
Da.place(x=350, y=230)

No = tkinter.Button(text='Нет', height=1, width=5, command=ToGame)
No.place(x=410, y=230)  

window.mainloop()



