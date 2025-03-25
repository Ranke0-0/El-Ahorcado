import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import random
from Palabras import words_list
from Fases_Ahorcado import Fases_ahorcado

class Ahorcado_App(ttk.Window):
    def __init__(self, themename="cyborg"):

        # SET-UP DE SELF
        super().__init__(themename=themename)
        self.title("El Ahorcado")
        self.geometry("1280x720")
        self.bind("<Escape>", lambda event: self.destroy())

        # PARTES DE LA APP
        self.widgets = Widgets(self)

        # RUN
        self.mainloop()

class Widgets(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x= 0, y= 0, relwidth= 1, relheight= 1)

        # VARIABLES DE LA CLASE
        self.word = ""
        self.hidden_word = []
        self.chances = 5
        self.failed_letters = []
        self.guess_word = False
        self.guess = ""

        # FUNCIONES DE LA CLASE
        self.Choose_Word()
        self.Configure_Grid()
        self.Create_Widgets()
        self.Play()
    
    # LOGICA PARA ESCOGER LA PALABRA AL AZAR
    def Choose_Word(self):
        # ESCOGE LA PALABRA
        self.word = random.choice(words_list)
        self.hidden_word = ["_"] * len(self.word)
        self.chances = 5
        self.failed_letters = []
        self.guess_word = False

        # TEST DE LA FUNCIÓN PARA LA PALABRA OCULTA
        print(self.hidden_word, self.word)

    def Configure_Grid(self):
        # COLUMN CONFIGURE
        self.columnconfigure((0, 9), weight= 3)
        self.columnconfigure((1), weight= 15)
        self.columnconfigure((2), weight= 11)
        self.columnconfigure((3), weight= 13)
        self.columnconfigure((4), weight= 10)
        self.columnconfigure((5), weight= 5)
        self.columnconfigure((6), weight= 27)
        self.columnconfigure((7), weight= 10)
        self.columnconfigure((8), weight= 4)

         # ROW CONFIGURE
        self.rowconfigure((0,6), weight= 4)
        self.rowconfigure((1), weight= 21)
        self.rowconfigure((2), weight= 15)
        self.rowconfigure((3), weight= 18)
        self.rowconfigure((4), weight= 19)
        self.rowconfigure((5), weight= 19)

    def Create_Widgets(self):
        # FUNCIÓN PARA LA SELECCIÓN DEL DIBUJO DEL AHORCADO
        def Elegir_Ahorcado():
            if self.chances == 5:
                return Fases_ahorcado[0]
            elif self.chances == 4:
                return Fases_ahorcado[1]
            elif self.chances == 3:
                return Fases_ahorcado[2]
            elif self.chances == 2:
                return Fases_ahorcado[3]
            elif self.chances == 1:
                return Fases_ahorcado[4]
            elif self.chances == 0:
                return Fases_ahorcado[5]
        Fase_ahorcado = Elegir_Ahorcado() 
        
        Colores_Background=("green","gold","red")
        def Elegir_Background():
            if self.chances == 5:
                return Colores_Background[0]
            elif self.chances >= 3:
                return Colores_Background[1]
            else:
                return Colores_Background[2]
        color_bg = Elegir_Background()

        # FUNCION PARA OBTENER LA GUESS
        def Boton_Enviar():
            self.guess = Entry_Guess.get()
            self.update_game()
        
        # CREAR WIDGETS
        Label_Tittle = ttk.Label(self, font = "Cambria 25 bold", text= "EL AHORCADO", background= "silver", foreground= "black", anchor= "center")
        Label_Guess = ttk.Label(self, font= "Calibri 14", text= "Introduzca una letra o palabra para adivinar:", background= "blue", anchor= "center")
        Entry_Guess = ttk.Entry(self, font= "Calibri 20", foreground= "green", justify= "center")
        Button_Submit = ttk.Button(self, text= "Enviar", command= Boton_Enviar)
        Label_Failed_Guesses = ttk.Label(self, font= "Calibri 14", text= "Estas letras y palabras son incorrectas:", background= "purple", anchor= "center")
        self.Label_Failed_Guesses_List = ttk.Label(self, font= "Calibri 14", text= self.failed_letters, background= "purple", anchor= "center")
        Label_Chances = ttk.Label(self, font= "Calibri 14", text= "Intentos restantes", background= color_bg, anchor= "center") #Fondo dinámico
        self.Label_ChancesNumber = ttk.Label(self, font= "Calibri 36", text= self.chances, background= color_bg, anchor= "center") #Fondo dinámico
        Label_Hangman = ttk.Label(self, font= "Calibri 14", text= Fase_ahorcado, background= color_bg, anchor= "center") #Fondo dinámico
        Label_Hidden_Word = ttk.Label(self, font= "Calibri 20", text = "Esta es la palabra oculta", anchor= "center")
        self.Label_Hidden_Word_Show = ttk.Label(self, font= "Calibri 36", text = self.hidden_word, anchor= "center")
        
        # PLACE
        Label_Tittle.grid(row= 1, column= 1, columnspan= 8, sticky= "nsew", padx= 5, pady= 5)
        Label_Guess.grid(row= 2, column= 2, sticky= "nsew", padx= 5, pady= 40)
        Entry_Guess.grid(row= 2 , column= 4, columnspan= 3, sticky= "nsew", padx= 10, pady= 40)
        Button_Submit.grid(row= 2, column= 7, sticky= "nsew", padx= 10, pady= 50)
        Label_Failed_Guesses.grid(row= 3, column= 2, sticky= "nsew", padx= 5, pady= 25)
        self.Label_Failed_Guesses_List.grid(row= 3, column= 4, columnspan= 4, sticky= "nsew", padx= 50, pady= 25)
        Label_Chances.grid(row= 4 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        self.Label_ChancesNumber.grid(row= 5 , column= 2, columnspan= 1, sticky= "nsew", padx= 33, pady= 5)
        Label_Hangman.grid(row= 4, column= 3, rowspan= 2, columnspan= 2, sticky= "nsew", padx= 20, pady= 10)
        Label_Hidden_Word.grid(row= 4, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)
        self.Label_Hidden_Word_Show.grid(row= 5, column= 6, columnspan= 2, sticky= "nsew", padx= 5, pady= 5)

    
    def update_game(self):
        if self.guess == self.word:
            self.guess_word = True
        elif self.guess in self.word:
            for i, l in enumerate(self.word):
                if l == self.guess:
                    self.hidden_word[i] = self.guess
        elif self.guess not in self.failed_letters:
            self.chances -= 1
            self.failed_letters.append(self.guess)
        else:
            print("Duplicado")

        self.Label_Hidden_Word_Show.config(text=self.hidden_word)
        self.Label_Failed_Guesses_List.config(text=self.failed_letters)
        self.Label_ChancesNumber.config(text=self.chances)
        #self.Label_Hangman.config(text= Elegir_Ahorcado())

        if "_" not in self.hidden_word or self.guess_word == True:
            print("\n¡Felicidades! Adivinó la palabra:", self.word)
        elif self.chances == 0:
            print("\n¡Perdiste! La palabra era:", self.word)

    def Play(self):
        self.update()

Ahorcado_App()