import sqlite3
from datetime import datetime,time
import os.path
import tkinter as tk
from tkinter import ANCHOR, CENTER, Tk, Text, ttk
from tkinter.messagebox import NO
from tkinter import Tk, Checkbutton, IntVar
from tkinter import *
import json

class logi_programu:
    '''
    Klasa do Inicjalizacji logow
    '''
    def __init__(self):
        self.f = open("logi.txt","w")

class odczytaj_txt:
    '''
    Klasa do Inicjalizacji slownikow

    Zmienne:
    Zmienne:
    a = polski
    b = angielski
    wybor = aktualnie wybrany jezyk
    '''

    def __init__(self,ktory):
        self.a ='polish.txt'
        self.b ='english.txt'
        self.wybor = 1
        if ktory == 1:
            self.wybor = self.a
        if ktory == 2:
            self.wybor = self.b
        with open(self.wybor) as sl:
            info = sl.read()
        self.slownik = json.loads(info)

    def zmiana_nazwy(self,nazwa):
        self.slownik.update({'Nazwa_studia' : nazwa})
        with open('polish.txt','w') as wp:
            json.dump(self.slownik,wp)


class baza_danych:
    '''
    Klasa do Inicjalizacji baz danych:
    1. Baza muzyki
    2. Baza loginow
    '''
    def __init__(self):

        print ("Proba polaczenia z baza muzyki")
        if (os.path.isfile('baza_muzyki.db')==False):
            conn = sqlite3.connect('baza_muzyki.db')
            print('Brak bazy muzyki, Tworzenie bazy')
            conn.execute('''CREATE TABLE "Baza Muzyki" (
	                "utwor"	TEXT,
	                "artysta"		TEXT,
	                "plyta"			TEXT);''')
        else:
            conn = sqlite3.connect('baza_muzyki.db')
            print('Baza muzyki istnieje i polaczono')
        
        print ("Proba polaczenia z baza loginow")
        if (os.path.isfile('baza_loginow.db')==False):
           conn = sqlite3.connect('baza_loginow.db')
           print('Brak bazy kont, Tworzenie bazy')
           conn.execute('''CREATE TABLE "uzytkownicy" (
					"login"			TEXT,
					"haslo"			TEXT,
					"stanowisko"	TEXT );''')
        else:
            conn = sqlite3.connect('baza_muzyki.db')
            print('Baza Loginow Istnieje i Polaczono')

      
class logowanie():
    '''
    Klasa do systemu logowania/rejestracji i tworzenia ich okna
    '''
    def __init__(self,okno,poczatkowytxt):
        super().__init__()
        
        self.przekaztxt = poczatkowytxt
       

        self.aktualny_uzytkownik = None
        self.aktualne_stanowisko = None

        self.okno_logowania = tk.Toplevel(okno)
        self.okno_logowania.geometry('285x85')
        self.okno_logowania.resizable(False,False)
        self.okno_logowania.title('Logowanie')
        self.okno_logowania.attributes("-topmost",True)

        self.okno_logowania.rowconfigure(0, weight=1)
        self.okno_logowania.columnconfigure(0, weight=1)

        self.logowanie_czy_rejestr = None

        print('Tworze Okno Logowania')

        
        style = ttk.Style(okno)         
        style.theme_use('styl') 
       
        


  
        self.paddings = {'padx':5, 'pady':5}
        self.logowanie_o()

        ##LOGOWANIE##
    def logowanie_o(self):
        self.okno_logowania.title(self.przekaztxt.slownik.get("Logowanie"))
        self.logowanie_czy_rejestr = 1
        self.logowanie_ramka = ttk.Frame(self.okno_logowania)
        self.logowanie_ramka.grid(sticky="nsew")

        paddings = {'padx':5, 'pady':5}
        self.login_logowanie = tk.StringVar()
        self.haslo_logowanie = tk.StringVar()
 
        login_logowanie_tytul = ttk.Label(self.logowanie_ramka, text = self.przekaztxt.slownik.get("Login:"))
        login_logowanie_tytul.grid(column=0, row=0, sticky =tk.W,**paddings )

        login_logowanie_pole = ttk.Entry(self.logowanie_ramka,textvariable=self.login_logowanie)
        login_logowanie_pole.grid(column=1, row=0, sticky=tk.E, **paddings)

        haslo_logowanie_tytul = ttk.Label(self.logowanie_ramka, text = self.przekaztxt.slownik.get("Haslo:"))
        haslo_logowanie_tytul.grid(column=0, row=1, sticky =tk.W,**paddings )
        

        haslo_logowanie_pole = ttk.Entry(self.logowanie_ramka,textvariable=self.haslo_logowanie)
        haslo_logowanie_pole.grid(column=1, row=1, sticky=tk.E, **paddings)
        haslo_logowanie_pole.config(show="*")

        logowanie_przycisk = ttk.Button(self.logowanie_ramka, text=self.przekaztxt.slownik.get("Zaloguj"),command=self.przekaz_logowanie)
        logowanie_przycisk.grid(column=1, row=3, sticky=tk.E, **paddings)

        logowanie_przycisk2 = ttk.Button(self.logowanie_ramka, text=self.przekaztxt.slownik.get("Do rejestracji"),command=lambda: (self.rejestracja(),self.logowanie_ramka.grid_forget()))
        logowanie_przycisk2.grid(column=2, row=3, sticky=tk.E, **paddings)
        ############

        ##REJESTRACJA##
    def rejestracja(self):
        self.okno_logowania.title(self.przekaztxt.slownik.get("Rejestracja"))
        self.logowanie_czy_rejestr = 2
        paddings = {'padx':5, 'pady':5}
        self.rejestracja_ramka = ttk.Frame(self.okno_logowania)
        self.rejestracja_ramka.grid(sticky="nsew")

        self.login_rejestracja = tk.StringVar()
        self.haslo_rejestracja = tk.StringVar()

        login_rejestracja_tytul = ttk.Label(self.rejestracja_ramka, text =self.przekaztxt.slownik.get("Login:"))
        login_rejestracja_tytul.grid(column=0, row=0, sticky =tk.W,**paddings )

        login_rejestracja_pole = ttk.Entry(self.rejestracja_ramka, textvariable=self.login_rejestracja)
        login_rejestracja_pole.grid(column=1, row=0, sticky=tk.E, **paddings)

        haslo_rejestracja_tytul = ttk.Label(self.rejestracja_ramka, text =self.przekaztxt.slownik.get("Haslo:"))
        haslo_rejestracja_tytul.grid(column=0, row=1, sticky =tk.W,**paddings )

        haslo_rejestracja_pole = ttk.Entry(self.rejestracja_ramka, textvariable=self.haslo_rejestracja)
        haslo_rejestracja_pole.config(show="*")
        haslo_rejestracja_pole.grid(column=1, row=1, sticky=tk.E, **paddings)

        login_rejestracja_przycisk = ttk.Button(self.rejestracja_ramka, text=self.przekaztxt.slownik.get("Zarejestruj"),command=self.przekaz_rejestracja)
        login_rejestracja_przycisk.grid(column=1, row=3, sticky=tk.E, **paddings)

        login_rejestracja_przycisk2 = ttk.Button(self.rejestracja_ramka, text=self.przekaztxt.slownik.get("Do logowania"),command=lambda: (self.logowanie_o(),self.rejestracja_ramka.grid_forget()))
        login_rejestracja_przycisk2.grid(column=2, row=3, sticky=tk.E, **paddings)
        ############
    def zmien_jezyk(self):
        if (self.logowanie_czy_rejestr == 1):
            self.logowanie_ramka.grid_forget()
            self.rejestracja()
        if (self.logowanie_czy_rejestr == 2):
            self.rejestracja_ramka.grid_forget()
            self.logowanie_o()
    def do_rejestracji(self):
        '''
        Metoda do zmiany trybu Z LOGOWANIA NA REJESTRACJE
        '''
        self.logowanie_ramka.forget()
        self.okno_logowania.title('Rejestracja')
        self.rejestracja()
        

    def do_logowania(self):
        '''
        Metoda do zmiany trybu Z REJESTRACJI NA LOGOWANIE
        '''
        self.rejestracja_ramka.forget()
        self.okno_logowania.title('Logowanie')
        self.logowanie_o()
        self.logowanie_ramka.grid()

    def przekaz_logowanie(self):
        '''
        Metoda do komunikacji bazy danych z oknem logowania [ tryb logowania ]
        '''
        self.okno_logowania.title('Logowanie')
        self.nazwa = self.login_logowanie.get()
        conn = sqlite3.connect('baza_loginow.db')
        cur = conn.cursor()
        cur.execute('''SELECT stanowisko FROM uzytkownicy WHERE login =(?) AND haslo=(?)''',(self.login_logowanie.get(),self.haslo_logowanie.get()))
        conn.commit()
        self.stanowisko = cur.fetchone()
        if (self.stanowisko!=None):
            print("Logowanie pomyslne, Zalogowano jako:",self.stanowisko,"Nazwa uzytkownika:",self.nazwa)
            self.aktualny_uzytkownik = self.nazwa
            self.aktualne_stanowisko = self.stanowisko
            self.okno_logowania.destroy()
        else:
            print("Login lub haslo niepoprawne")
    
 

    def przekaz_rejestracja(self):
        '''
        Metoda do komunikacji bazy danych z oknem logowania [ tryb rejestracji ]
        '''
        conn = sqlite3.connect('baza_loginow.db')
        cur = conn.cursor()
        cur.execute('''SELECT 1 FROM uzytkownicy WHERE login=(?) LIMIT 1''',(self.login_rejestracja.get(),))
        if(cur.fetchone()!= None):
            print("login zajety, sprobuj inny")
        else:
            cur.execute('''SELECT 1 FROM uzytkownicy WHERE stanowisko="headadmin" LIMIT 1''')
            if (cur.fetchone()==None):
                print("Brak HeadAdmina, Nastepny uzytkownik zostanie HeadAdminem")
                cur.execute   ('''INSERT INTO uzytkownicy(login,haslo,stanowisko) 
                              VALUES (?,?,?)''',(self.login_rejestracja.get(),self.haslo_rejestracja.get(),'headadmin'))
            else:
                cur.execute   ('''INSERT INTO uzytkownicy(login,haslo,stanowisko) 
                          VALUES (?,?,?)''',(self.login_rejestracja.get(),self.haslo_rejestracja.get(),'uzytkownik'))
        conn.commit()          


       
class okno_glowne(ttk.Frame):
    def __init__(self):
        '''
        log = inicjalizacja logow
        ot  = inicjalizacja slownikow [jezykow]

        Zmienne:
        aktualny_motyw          =  aktualnie ustawiony wyglad
        zablokowane             =  tymczasowa zmienna do okna plyt po prawej
        tymczasowa_zmienna      =  tymczasowa zmienna do okna plyt po prawej
        tymczas_zmien_sort      =  tymczasowa zmienna do sortowania alfabetycznego kolumn
        tymczas_iteracja_sort   = 
        artyst_blok             =  tryb blokowania pola tekstowego artysty
        utwor_blok              =  tryb blokowania pola tekstowego utworu
        plyta_blok              =  tryb blokowania pola tekstowego plyty
        nazwa_studia            =  aktualna nazwa studia
        '''

        self.log = logi_programu()
        self.ot = odczytaj_txt(1)
        self.tryb_ciemny()
        self.log.f.write("[Otwieram Okno Glowne]")

        # Budowa okna Glownego#
        self.aktualny_uzytkownik_okno_glowne = None
        self.aktualne_stanowisko_okno_glowne = None
        self.main_okno = tk.Tk()
        self.main_okno.grid_columnconfigure(0,weight=1)
        self.main_okno.grid_rowconfigure(0,weight=1)


        self.main_okno.geometry('500x500')
        self.main_okno.resizable(False,False)
        self.main_okno.title(self.ot.slownik.get("Nazwa_studia"))
        self.main_okno.config(background=self.kolor_tla)

        self.style = ttk.Style(self.main_okno)    
        self.style.theme_create('styl')
        self.style.theme_use('styl')
        #####

        self.stworz_menu_opcje()

        self.ustaw_styl()
        
       
        
        # ZMIENNE #
        self.aktualny_motyw = None
        self.zablokowane = False
        self.tymczasowa_zmienna = []
        self.tymczas_zmien_sort = {}
        self.tymczas_iteracja_sort = []
        self.artyst_blok = True
        self.utwor_blok = True
        self.plyta_blok = True
        self.nazwa_studia = tk.StringVar()
        self.aktualna_ramka = None
        ##########
        self.styl_poczatkowy()
        


        self.logow  = logowanie(self.main_okno,self.ot)
        self.main_okno.wait_window(self.logow.okno_logowania)




        if ( self.logow.aktualne_stanowisko!=None and  self.logow.aktualny_uzytkownik!=None):
            print("Zalogowano do okna glownego")
            self.aktualny_uzytkownik_okno_glowne = self.logow.aktualny_uzytkownik
            self.aktualne_stanowisko_okno_glowne = self.logow.aktualne_stanowisko
            self.log.f.write("\n[Zalogowano pomyslnie]"+self.aktualny_uzytkownik_okno_glowne)
            self.pokaz_menu()
    def stworz_menu_opcje(self):
        '''
        Metoda do tworzenia menu w formie paska narzedzi po prawej u gory ekranu
        '''
        self.wartosc_menu = tk.StringVar(self.main_okno,'None')
        self.menu_opcje = ["Menu",self.ot.slownik.get("Zmien Motyw"),self.ot.slownik.get("polish"),self.ot.slownik.get("english")]
        self.menu_wyboru = ttk.OptionMenu(self.main_okno,self.wartosc_menu,*self.menu_opcje,command=lambda x:(self.opcja_menu(),self.odswiez_menu_opcje(),self.odswiez_ramke()))
        self.menu_wyboru.grid(row=0,column=0,sticky=tk.NE,ipadx=15,ipady=2)
        


    def opcja_menu(self):
        '''
        Metoda do obslugi menu w formie paska narzedzi
        '''
        if (self.ot.slownik.get("polish")) in self.wartosc_menu.get():
            self.ot = odczytaj_txt(1)
            if (self.aktualny_uzytkownik_okno_glowne == None):
                self.logow.przekaztxt = self.ot
                self.logow.zmien_jezyk()
        if (self.ot.slownik.get("english")) in self.wartosc_menu.get():
            self.ot = odczytaj_txt(2)
            if (self.aktualny_uzytkownik_okno_glowne == None):
                self.logow.przekaztxt = self.ot
                self.logow.zmien_jezyk()
        if (self.ot.slownik.get("Zmien Motyw")) in self.wartosc_menu.get():
            self.zmien_motyw()

    def odswiez_menu_opcje(self):
        '''
        Metoda do odswiezania automatycznego okna opcji
        '''
        self.menu_wyboru.destroy()
        self.stworz_menu_opcje()

    def pokaz_menu(self):
        '''
        Metoda do tworzenia menu w oknie glownym programu i ustalania jakie stanowisko do jakis opcji menu ma dostep
        '''
        self.aktualna_ramka = 1
        paddings = {'padx':155, 'pady':30, 'ipady':20}
        menu_ramka = ttk.Frame(self.main_okno)
        if ('headadmin' in self.aktualne_stanowisko_okno_glowne) or ('admin' in self.aktualne_stanowisko_okno_glowne):

            
            menu_ramka.grid(row=0,column=0,sticky="nsew",pady=25)


            studio_przycisk = ttk.Button(menu_ramka, text=self.ot.slownik.get("Otworz Studio"), command=lambda: (self.okno_studia(),menu_ramka.grid_forget()))
            studio_przycisk.config(width=30)
            studio_przycisk.grid(column=1, row=0, sticky=tk.NE, **paddings)
        
        if  'headadmin' in self.aktualne_stanowisko_okno_glowne:
            headadmin_przycisk = ttk.Button(menu_ramka, text=self.ot.slownik.get("Panel Admina"), command=lambda: [self.panel_admina(),menu_ramka.grid_forget()])
            headadmin_przycisk.config(width=30)
            headadmin_przycisk.grid(column=1, row=1, sticky=tk.NE, **paddings)

        #######
        testowy_p = ttk.Button(menu_ramka, text=self.ot.slownik.get("Zmiana Wygladu"), command=lambda: [self.zmien_motyw()])
        testowy_p.config(width=30)
        testowy_p.grid(column=1, row=2, sticky=tk.NE,**paddings)
        ######
        

    def okno_studia(self):
        '''
        Metoda do wyswietlania i obslugi glownego okna studia
        Zmienne:

        tabela  = tabela utwor/artysta/plyta
        tabela5 = tabela podgladu plyt [lewa strona ekranu]

        artyst_blok             =  tryb blokowania pola tekstowego artysty
        utwor_blok              =  tryb blokowania pola tekstowego utworu
        plyta_blok              =  tryb blokowania pola tekstowego plyty


        artyst                  =  lanuch znakow w ktorym zapisywane sa dane z pola tekstowego "artysta"
        utwo                    =  lanuch znakow w ktorym zapisywane sa dane z pola tekstowego "utwor"
        plyt                    =  lanuch znakow w ktorym zapisywane sa dane z pola tekstowego "plyta"
        '''
        self.aktualna_ramka = 2

        self.artyst_blok = True
        self.utwor_blok = True
        self.plyta_blok = True

        print("Okno studia odpalone")
        paddings = {'padx':5, 'pady':5}
        ramka_st = ttk.Frame(self.main_okno)
        ramka_st.grid(row=0,column=0,sticky="nsew",pady=25)
        style = ttk.Style(self.main_okno)         
        style.theme_use('styl')                  

        



        self.tabela = ttk.Treeview(ramka_st,height=12)

        

        self.tabela['columns']=('utwor','artysta','plyta')

        self.tabela.column("#0",width=0, stretch=NO)
        self.tabela.column("utwor",anchor=CENTER,width=120)
        self.tabela.column("artysta",anchor=CENTER,width=120)
        self.tabela.column("plyta",anchor=CENTER,width=120)

        self.tabela.heading("#0",text="",anchor=CENTER)
        self.tabela.heading("utwor",text=self.ot.slownik.get("Utwor"),anchor=CENTER,command=lambda: self.sortuj_rzedy(self.tabela,1))
        self.tabela.heading("artysta",text=self.ot.slownik.get("Artysta"),anchor=CENTER,command=lambda: self.sortuj_rzedy(self.tabela,2))
        self.tabela.heading("plyta",text=self.ot.slownik.get("Plyta"),anchor=CENTER,command=lambda: self.sortuj_rzedy(self.tabela,3))


        self.dodaj_z_bazy(self.tabela)
        self.tabela.grid(column=1,row=2,columnspan=6,rowspan=5,sticky=tk.W)


        self.tabela5 = ttk.Treeview(ramka_st,height=12)
        self.tabela5['columns']=('plyta')

        self.tabela5.column("#0",width=0, stretch=NO)
        self.tabela5.column("plyta",anchor=CENTER,width=100)
        self.tabela5.heading("#0",text="",anchor=CENTER)
        self.dodaj_plyty(self.tabela,self.tabela5)
        self.tabela5.heading("plyta",text=self.ot.slownik.get("Plyta/Wszystko"),anchor=CENTER,command=lambda: (self.pokaz_konkretna(self.tabela,self.tabela5),self.dodaj_plyty(self.tabela,self.tabela5)))
        


        self.tabela5.grid(column=0,row=2,columnspan=5,rowspan=4,sticky=tk.W)



        self.artyst = tk.StringVar()
        self.utwo = tk.StringVar()
        self.plyt = tk.StringVar()
       

        ##################################
        label1 = ttk.Label(ramka_st,text=self.ot.slownik.get("Artysta"))
        label1.grid(column=1,row=14,padx=30)

        artysta_pole = ttk.Entry(ramka_st, textvariable=self.artyst, state =DISABLED)
        artysta_pole.grid(column=1,row=15,sticky=tk.W,padx=30,ipadx=10)


        artysta_blok_box = ttk.Checkbutton(ramka_st,command=lambda: self.zablok_artyst(artysta_pole))
        artysta_blok_box.grid(column=1,row=15,sticky=tk.E,padx=30)
        ##################################
        label2 = ttk.Label(ramka_st,text=self.ot.slownik.get("Utwor"))
        label2.grid(column=0,row=14)

        utwor_pole = ttk.Entry(ramka_st, textvariable=self.utwo,state =DISABLED)
        utwor_pole.grid(column=0,row=15,sticky=tk.E,ipadx=10)

        utwor_blok_box = ttk.Checkbutton(ramka_st,command=lambda: self.zablok_utwor(utwor_pole))
        utwor_blok_box.grid(column=0,row=15,sticky=tk.E)
        ##################################
        label3 = ttk.Label(ramka_st,text=self.ot.slownik.get("Plyta"))
        label3.grid(column=2,row=14,padx=0)

        plyta_pole = ttk.Entry(ramka_st, textvariable=self.plyt,state =DISABLED)
        plyta_pole.grid(column=2,row=15,sticky=tk.E,padx=0,ipadx=10)

        plyta_blok_box = ttk.Checkbutton(ramka_st,command=lambda: self.zablok_plyta(plyta_pole))
        plyta_blok_box.grid(column=2,row=15,sticky=tk.E,padx=0,ipadx=0)
        
        ##################################
        edytuj_przycisk = ttk.Button(ramka_st, text=self.ot.slownik.get("Skopiuj do pola"), command=lambda:(self.skopiuj_pole(self.tabela)))
        edytuj_przycisk.place(relx=0,rely=0.75,width=100, height=25)
        ##################################
        zapisz_przycisk = ttk.Button(ramka_st, text=self.ot.slownik.get("Podmien"), command=lambda:(self.zamien_dane_na(self.tabela)))
        zapisz_przycisk.place(relx=0.27,rely=0.75,width=100, height=25)
        ##################################
        dodaj_przycisk = ttk.Button(ramka_st, text=self.ot.slownik.get("Dodaj"), command=lambda:(self.dodaj_pole(self.tabela)))
        dodaj_przycisk.place(relx=0.54,rely=0.75,width=100, height=25)
        ##################################
        usun_przycisk = ttk.Button(ramka_st, text=self.ot.slownik.get("Usun"), command=lambda:(self.usun_pole(self.tabela)))
        usun_przycisk.place(relx=0.8,rely=0.75,width=100, height=25)
        ##################################
        powrot_przycisk = ttk.Button(ramka_st, text=self.ot.slownik.get("Powrot"), command=lambda:[self.pokaz_menu(),ramka_st.grid_forget()])
        powrot_przycisk.place(relx=0.3,rely=0.90,width=200, height=40)

    def panel_admina(self):
        '''
        Metoda do wyswietlania i tworzenia panelu admina
        '''
        self.aktualna_ramka = 3
        print("Panel admina odpalony")
        paddings = {'padx':5, 'pady':5}
        admin_st = ttk.Frame(self.main_okno) 

        admin_st.grid(row=0,column=0,sticky="nsew",pady=25)
        
        tabela_uzytkownikow = ttk.Treeview(admin_st,height=12)
        tabela_uzytkownikow['columns']=('login','stanowisko')

        tabela_uzytkownikow.column("#0",width=0, stretch=NO)
        tabela_uzytkownikow.column("login",anchor=CENTER,width=120)
        tabela_uzytkownikow.column("stanowisko",anchor=CENTER,width=120)
        
        tabela_uzytkownikow.heading("#0",text="",anchor=CENTER)
        tabela_uzytkownikow.heading("login",text=self.ot.slownik.get("Login"),anchor=CENTER)
        tabela_uzytkownikow.heading("stanowisko",text=self.ot.slownik.get("Stanowisko"),anchor=CENTER)
        self.dodaj_z_bazy_do_tabeli_uzytkownikow(tabela_uzytkownikow)
        tabela_uzytkownikow.grid(row=0,column=5,columnspan=6,rowspan=5,padx=135,sticky=tk.E)




        awansuj_przycisk = ttk.Button(admin_st, text=self.ot.slownik.get("Awansuj"), command=lambda: self.awansuj_uzytkownika(tabela_uzytkownikow))
        awansuj_przycisk.place(relx=0.01,rely=0.65,width=100, height=25)

        degraduj_przycisk = ttk.Button(admin_st, text=self.ot.slownik.get("Degraduj"), command=lambda: self.degraduj_uzytkownika(tabela_uzytkownikow))
        degraduj_przycisk.place(relx=0.25,rely=0.65,width=100, height=25)

        usun_uzytkownika_przycisk = ttk.Button(admin_st, text=self.ot.slownik.get("Usun"), command=lambda: (self.usun_uzytkownika(tabela_uzytkownikow)))
        usun_uzytkownika_przycisk.place(relx=0.5,rely=0.65,width=100, height=25)

        przekaz_head_admina = ttk.Button(admin_st, text=self.ot.slownik.get("Przekaz HEADADMINA"), command=lambda: (self.przekaz_head(tabela_uzytkownikow,admin_st)))
        przekaz_head_admina.place(relx=0.75,rely=0.65,width=120, height=25)


        powrot_przycisk_admin = ttk.Button(admin_st, text=self.ot.slownik.get("Powrot"), command=lambda:[self.pokaz_menu(),admin_st.grid_forget()])
        powrot_przycisk_admin.place(relx=0.3,rely=0.78,width=200, height=25)

        nazwa_pole = ttk.Entry(admin_st, textvariable=self.nazwa_studia)
        nazwa_pole.place(relx=0.3,rely=0.88,width=200, height=25)

        nazwa_przycisk_admin = ttk.Button(admin_st, text=self.ot.slownik.get("Zmien Nazwe"), command=lambda: (self.zmien_nazwe_studia(self.nazwa_studia.get())))
        nazwa_przycisk_admin.place(relx=0.3,rely=0.94,width=200, height=25)

    def odswiez_ramke(self):
        if (self.aktualna_ramka == 1):
            self.pokaz_menu()
        if (self.aktualna_ramka == 2):
            self.okno_studia()
        if (self.aktualna_ramka == 3):
            self.panel_admina()
############# DLA PANELU ADMINA ###############
    def zmien_nazwe_studia(self,nazwa):
        self.main_okno.title(nazwa)
        
        self.ot.zmiana_nazwy(nazwa)

    def awansuj_uzytkownika(self,tab):
        
        if(tab.focus()!=''):
            a,b = tab.item(tab.focus(),'values')
            if (b!= 'headadmin'):
                b = 'admin'
                tab.item(tab.focus(),values=[a,b])
                conn = sqlite3.connect('baza_loginow.db')
                cur = conn.cursor()
                cur.execute(''' UPDATE 'uzytkownicy' SET stanowisko = 'admin' WHERE login=(?) ''',(a,))
                conn.commit()

    def degraduj_uzytkownika(self,tab):
        
        if(tab.focus()!=''):
            a,b = tab.item(tab.focus(),'values')
            if ( b!= 'headadmin'):
                b = 'uzytkownik'
                tab.item(tab.focus(),values=[a,b])
                conn = sqlite3.connect('baza_loginow.db')
                cur = conn.cursor()
                cur.execute(''' UPDATE 'uzytkownicy' SET stanowisko = 'uzytkownik' WHERE login=(?) ''',(a,))
                conn.commit()

    def usun_uzytkownika(self,tab):
        
        if(tab.focus()!=''):
            a,b = tab.item(tab.focus(),'values')
            if (b!= 'headadmin'):              
                tab.delete(tab.focus())
                conn = sqlite3.connect('baza_loginow.db')
                cur = conn.cursor()
                cur.execute('''DELETE FROM 'uzytkownicy' WHERE login=(?)''',(a,))       
                conn.commit()

    def przekaz_head(self,tab,odniesienie_do_panelu):
        '''
        Metoda do przekazywania headadmina innej osobie
        '''
        if(tab.focus()!=''):
            a,b = tab.item(tab.focus(),'values')
            conn = sqlite3.connect('baza_loginow.db')
            cur = conn.cursor()
            cur.execute('''UPDATE 'uzytkownicy' SET stanowisko = 'headadmin' WHERE login=(?) ''',(a,))       
            conn.commit()
            cur.execute('''UPDATE 'uzytkownicy' SET stanowisko = 'uzytkownik' WHERE login=(?)''',(self.aktualny_uzytkownik_okno_glowne,))
            conn.commit()
            odniesienie_do_panelu.grid_forget()
            self.pokaz_menu()

    def dodaj_z_bazy_do_tabeli_uzytkownikow(self,tab):
        '''
        Metoda do pobierania danych z bazy danych i tworzenia tabeli uzytkownikow
        '''
        print("Dodaje dane z bazy do tabeli uzytkownikow")
        conn = sqlite3.connect('baza_loginow.db')
        cur = conn.cursor()
        cur.execute(''' SELECT * FROM 'uzytkownicy' ''')
        conn.commit()
        lista = cur.fetchall()
        for x in range(len(lista)):
            a,b,c = lista[-1]
            lista.pop()
            tab.insert(parent='',index='end',text='',value=(a,c))
    

############# DLA OKNA STUDIA #################

    def zablok_artyst(self,a):
        if self.artyst_blok==False:
            self.artyst_blok=True
            a.config(state=DISABLED)
        else:
            self.artyst_blok=False
            a.config(state=NORMAL)

    def zablok_utwor(self,a):
        if self.utwor_blok==False:
            self.utwor_blok=True
            a.config(state=DISABLED)
        else:
            self.utwor_blok=False
            a.config(state=NORMAL)

    def zablok_plyta(self,a):
        if self.plyta_blok==False:
            self.plyta_blok=True
            a.config(state=DISABLED)
        else:
            self.plyta_blok=False
            a.config(state=NORMAL)


    def pokaz_konkretna(self,tab1,tab2):
        '''
        Metoda zmieniajaca tryb wyswietlania 
        1. Tryb wybranej plyty
        2. Tryb wszystkich utworow
        '''
        if(self.zablokowane == False):
            self.zablokowane=True
            tymczas = tab2.item(tab2.focus(),'values')
            for x in tab1.get_children():
                a,b,c = tab1.item(x,'values')
                if c not in tymczas:
                    self.tymczasowa_zmienna.append(x)
                    tab1.detach(x)
        else:
            self.zablokowane = False
            for i in self.tymczasowa_zmienna:
                tab1.reattach(i,'',0)



    def sortuj_rzedy(self,tab,ktore): 
        '''
        Metoda sortujaca rzedy w kolumnie alfabetycznie dla wybranej kategorii
        '''
        for i in tab.get_children():
            a,b,c = tab.item(i,'values')
            if ktore == 1: #utwor
                self.tymczas_zmien_sort.update({i:a})
                
            if ktore == 2: #artysta
                self.tymczas_zmien_sort.update({i:b})
                
            if ktore == 3: #plyta
                self.tymczas_zmien_sort.update({i:c})
                
        tymczas = sorted(self.tymczas_zmien_sort.items(), key = lambda kv: 
                            (kv[1], kv[0]))
        for i,(v,k) in enumerate(tymczas):
            if(tab.exists(v)==True):
                tab.move(v,'',i)

        
    def dodaj_plyty(self,tab1,tab2):
        '''
        Metoda dodajaca plyty automatycznie do tabela5 [tabela po lewej z plytami]
        '''
        tymczasowa_zmienna = []
        for x in tab1.get_children():
            a,b,c = tab1.item(x,'values')
            if c not in tymczasowa_zmienna:
                tymczasowa_zmienna.append(c)

        wysokosc_drzewa = tab2.get_children()
        
        for x in tymczasowa_zmienna:
            czy_istnieje = False
            for i in wysokosc_drzewa:
                wartosc = tab2.item(i,'values')
                if x in wartosc:
                    czy_istnieje=True
                if x in " ":
                    czy_istnieje=True
            if czy_istnieje == False:
                tab2.insert(parent='',index='end',text='',values=(x))
                    

    def skopiuj_pole(self,tab):
        '''
        Metoda kopiuje wartosci "utwor" "artysta" "plyta" z aktualnie wybranego rzedu do pol tekstowych
        '''
        if(tab.focus()!=''):
            a,b,c = tab.item(tab.focus(),'values')
            if self.utwor_blok == False:
                self.utwo.set(a) 
            if self.artyst_blok == False:
                self.artyst.set(b)
            if self.plyta_blok == False:
                self.plyt.set(c) 
            print("Tryb edycji Pola",tab.focus())
            print(self.plyt)

    def zamien_dane_na(self,tab):
        '''
        Metoda zamieniajaca wartosci aktualnie wybranego rzedu na podane w polach tekstowych i podmieniajaca w bazie danych
        '''
        if(tab.focus()!=''):
            a,b,c=tab.item(tab.focus(),'values')
            nie_zmienna = a
            n_zb = b
            n_zc = c

            if self.utwor_blok==False:
                a=self.utwo.get()
            if self.artyst_blok==False:
                b=self.artyst.get()
            if self.plyta_blok==False:
                c=self.plyt.get()
            tab.item(tab.focus(),values=[a,b,c]) 

            self.log.f.write("\n[WARTOSC EDYTOWANA]"+nie_zmienna+"  "+n_zb+"  "+n_zc+" [EDYTOWANA NA:]"+ a +"  "+ b +"  "+c)


            conn = sqlite3.connect('baza_muzyki.db')
            cur = conn.cursor()
            if self.utwor_blok == False:
                cur.execute(''' UPDATE 'baza muzyki' SET utwor = (?) WHERE utwor=(?) ''',(self.utwo.get(),nie_zmienna))
                conn.commit()
            if self.artyst_blok == False:
                cur.execute(''' UPDATE 'baza muzyki' SET artysta = (?) WHERE utwor=(?) ''',(self.artyst.get(),nie_zmienna))
                conn.commit()
            if self.plyta_blok == False:
                cur.execute(''' UPDATE 'baza muzyki' SET plyta = (?) WHERE utwor=(?) ''',(self.plyt.get(),nie_zmienna))
                conn.commit()

    def dodaj_pole(self,tab):
        '''
        Metoda dodajaca wartosci do tabeli i bazy danych
        '''
        a,b,c = " "," "," "
        if self.utwor_blok==False:
            a=self.utwo.get()
        if self.artyst_blok==False:
            b=self.artyst.get()
        if self.plyta_blok==False:
            c=self.plyt.get()
        tab.insert(parent='',index='end',text='',values=(a,b,c))
        #i dodaj do bazy
        self.log.f.write("\n[WARTOSC Dodana]"+"  Utwor:" +a+"  Artysta:"+b+"  Plyta:"+c)
        conn = sqlite3.connect('baza_muzyki.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO 'baza muzyki' (utwor,artysta,plyta)
                       VALUES(?,?,?)''',(a,b,c))
        conn.commit()
        self.dodaj_plyty(self.tabela,self.tabela5)

    def usun_pole(self,tab):
        '''
        Metoda usuwajaca wartosci do tabeli i bazy danych
        '''
        if(tab.focus()!=''):
            a,b,c = tab.item(tab.focus(),'values')
            self.log.f.write("\n[WARTOSC Usunieta]"+"  Utwor:" +a+"  Artysta:"+b+"  Plyta:"+c)
            tab.delete(tab.focus())
            conn = sqlite3.connect('baza_muzyki.db')
            cur = conn.cursor()
            cur.execute('''DELETE FROM 'baza muzyki' WHERE utwor=(?)''',(a,))
            conn.commit()
            self.tabela5.delete(*self.tabela5.get_children())
            self.dodaj_plyty(self.tabela,self.tabela5)
           
            
            
        
    def dodaj_z_bazy(self,tab):
        conn = sqlite3.connect('baza_muzyki.db')
        cur = conn.cursor()
        cur.execute(''' SELECT * FROM 'baza muzyki' ''')
        conn.commit()
        lista = cur.fetchall()
        for x in range(len(lista)):
            a,b,c = lista[-1]
            lista.pop()
            tab.insert(parent='',index='end',text='',value=(a,b,c))
        
    def styl_poczatkowy(self):
        czas_lokalny = datetime.utcnow()
        czas_zmiany  = czas_lokalny.replace(hour=15,minute=30)
        print (czas_lokalny)
        print (czas_zmiany)
        if ( czas_zmiany > czas_lokalny):
            self.aktualny_motyw = 2
            self.tryb_jasny()
        else:
            self.aktualny_motyw = 1
            self.tryb_ciemny()
        self.ustaw_styl()

    def zmien_motyw(self):
        '''
        Metoda do zmieniania motywow
        1. Tryb Jasny
        2. Tryb ciemny
        '''
        print("Zmiana motywu")
        a = self.aktualny_motyw
        if a == 1:
            self.tryb_jasny()
            self.aktualny_motyw = 2

        if a == 2:
            self.tryb_ciemny()
            self.aktualny_motyw = 1
        self.ustaw_styl()

    def ustaw_styl(self):
        
        '''
        Metoda ktora laczaca zmienne z biblioteka, tak zeby podmieniac tylko wartosci zmiennych, zamiast tworzyc osobnej klasy dla kazdego motywu

        kolor_wyboru_tabelka        = kolor aktualnie zaznaczonego rzedu / podswietlenia
        kolor_tabela_tlo            = kolor tla tabelki
        kolor_srodka_przyciskow     = kolor przyciskow wewnetrzny
        kolor_tla                   = kolor tla okna
        kolor_tabela_belka          = kolor belki znajdujacej sie na samym gorze tabeli
        kolor_tekstu                = kolor tekstu
        kolor_obwodu_przyciskow     = kolor obwodu przyciskow
        kolor_pola                  = kolor pola
        '''

        self.style.map('Treeview',background=[('selected',self.kolor_wyboru_tabelka)])
        self.style.configure('Treeview'             ,fieldbackground= self.kolor_tabela_tlo)
        
        self.style.configure('TButton'              ,background=self.kolor_srodka_przyciskow,foreground=self.kolor_tekstu)
        self.style.configure('TButton'              ,anchor='center')

        self.style.configure('TFrame'               ,background=self.kolor_tla)

        self.style.configure('TLabel'               ,background=self.kolor_tla,foreground=self.kolor_tekstu)
        
        self.style.configure('TEntry'               ,fieldbackground=self.kolor_pola,foreground=self.kolor_tekstu)
        self.style.map('TEntry',fieldbackground=[('disabled','red')])
        
        self.style.configure('Treeview.Heading'     ,background = self.kolor_tabela_belka)
        
        self.style.configure('TMenubutton'     ,background = self.kolor_tabela_belka)

        self.style.map('TCheckbutton',background=[('selected',self.kolor_tla)])
        self.style.configure('TCheckbutton'         ,background='red',foreground=self.kolor_tekstu,fieldforeground='red')
        self.main_okno.config(background=self.kolor_tla)
    def tryb_jasny(self): 
        print("Tryb jasny")
        self.kolor_tla                     = '#b3b3b3' 
        self.kolor_srodka_przyciskow       = '#d9d9d9'
        self.kolor_obwodu_przyciskow       = '#737373'
        self.kolor_pola                    = '#f2f2f2'
        self.kolor_tabela_tlo              = '#b3b3b3'
        self.kolor_tabela_belka            = '#a6a6a6'
        self.kolor_tekstu                  = '#000000'
        self.kolor_wyboru_tabelka          = '#b3b3cc'

    def tryb_ciemny(self):
        print("Tryb ciemny")
        self.kolor_tla                     = '#262626' 
        self.kolor_srodka_przyciskow       = '#4d4d4d'
        self.kolor_obwodu_przyciskow       = '#000000'
        self.kolor_pola                    = '#1a1a1a'
        self.kolor_tabela_tlo              = '#4d4d4d'
        self.kolor_tabela_belka            = '#404040'
        self.kolor_tekstu                  = '#f2f2f2'
        self.kolor_wyboru_tabelka          = '#737373'


#################################
        
        



baza = baza_danych()
og = okno_glowne()
og.main_okno.mainloop()