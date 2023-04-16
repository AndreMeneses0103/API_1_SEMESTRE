import tkinter as tk
import customtkinter as ctk
from tkinter import *

def abrir():
    janela = ctk.CTk()

    class alerta():
        def __init__(self):
            

            self.janela=janela
            self.tela()
            self.tema() 
            self.TelaAlerta()   
            janela.mainloop()
            
        def tema(self):
            ctk.set_appearance_mode("dark") #modo dark
            ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
            pass

        def tela(self):    
            janela.geometry("800x500") #DEFINO O TAMANHO DA JANELA
            janela.title("Sistema de login")
            #janela.iconbitmap("logo_insight.ico")
            janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
            pass
        
        def TelaAlerta(self):
            label_BemVindo=ctk.CTkLabel(master=janela, text=("'BEM VINDO, USUÁRIO'"), font=("Roboto",25),text_color='white').place(x=280, y=230)
            
        
            def logout():
                (janela.destroy())

            logout_button = ctk.CTkButton(master=janela, text="Logout", width=85, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=logout).place(x=700, y=15)
            

    alerta()
