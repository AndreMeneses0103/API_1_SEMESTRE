import json
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
            janela.iconbitmap("logo_insight.ico")
            janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
            pass
        
        def TelaAlerta(self):
            img = PhotoImage(file="logo_insight.png").subsample(2) # reduzindo o tamanho em 50%
            label_img = ctk.CTkLabel(master=janela, image=img, text='')
            label_img.place(x=50, y=160)
        
            user_nome = ""

            acesso = json.load(open("data_json/users.json", "r"))

            for x in range(len(acesso["usuarios"])):
                if(acesso["usuarios"][x]["isActive"] == True):
                    user_nome = acesso["usuarios"][x]["user"]

            label_BemVindo=ctk.CTkLabel(master=janela, text=(f"Bem vindo, {user_nome}"), font=("Roboto",25),text_color='white').place(x=420, y=214)
            

            logout_button = ctk.CTkButton(master=janela, text="Logout", width=85, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=Close).place(x=700, y=15)
            janela.protocol("WM_DELETE_WINDOW", Close)


    def Close():
        acesso = json.load(open("data_json/users.json", "r"))

        for x in range(len(acesso["usuarios"])):
            acesso["usuarios"][x]["isActive"] = False

        insert_acesso = str(json.dumps(acesso, indent=4))

        with open("data_json/users.json", "w") as arq_json:
            arq_json.write(insert_acesso)

        (janela.destroy())

    alerta()