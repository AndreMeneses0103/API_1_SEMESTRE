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

            
            # logout_button = ctk.CTkButton(master=janela, text="Logout", width=85, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD').place(x=700, y=15)

            # espaco = ctk.CTkFrame(master=janela, width=500, height= 500, fg_color="#3d3a3a")
            # espaco.place(x=0, y=200)


            scroll = ctk.CTkScrollableFrame(master=janela, width=500, height=50)
            barra = scroll._scrollbar
            barra.configure(height= 0)
            scroll.pack()

            for x in range(10):
                label = ctk.CTkLabel(master=scroll, text=f"NUMERO {x}")
                label.pack()
    #         janela.protocol("WM_DELETE_WINDOW", Close)


    # def Close():
    #     acesso = json.load(open("data_json/users.json", "r"))

    #     for x in range(len(acesso["usuarios"])):
    #         acesso["usuarios"][x]["isActive"] = False

    #     insert_acesso = str(json.dumps(acesso, indent=4))

    #     with open("data_json/users.json", "w") as arq_json:
    #         arq_json.write(insert_acesso)

    #     janela.destroy()
    #     janela.mainloop()

    def AbrirAv():
        janela.destroy()
        TelaAV.abrir_avaliacao()

    alerta()

abrir()