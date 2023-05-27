import json
import customtkinter as ctk
from tkinter import *
import hashlib
import tkinter as tk
import TelaBV as TBV
import telaADM

def abrir_feedback():
       
    janelaFeedback = ctk.CTk()
    class tela_feedback:
        def __init__(self):#deve conter todas as funções que existem - é a principal
        
            self.janela=janelaFeedback
            self.tema()
            self.tela()
            self.tela_feed()
            janelaFeedback.mainloop()

        def tema(self):
            ctk.set_appearance_mode("dark") #modo dark
            ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
            pass

        def tela(self):    
            larg_janela = 800
            alt_janela = 500

            larg_tela = janelaFeedback.winfo_screenwidth()
            alt_tela = janelaFeedback.winfo_screenheight()

            x = (larg_tela - larg_janela) // 2
            y = (alt_tela - alt_janela) // 2
            janelaFeedback.geometry(f"{larg_janela}x{alt_janela}+{x}+{y}") #DEFINO O TAMANHO DA JANELA
            janelaFeedback.title("Insight 360º")
            janelaFeedback.iconbitmap("logo_insight.ico")
            janelaFeedback.resizable(False, False) #defino que o usuário não pode redimensionar a tela
            pass

        def tela_feed(self):
        
            sprint = "2"
            labelNome = ctk.CTkLabel(master=janelaFeedback, text="Feedbacks", font=('Roboto', 30, 'bold'), text_color='#00FFFF').place(x=330, y=20)
            sprintLabel = ctk.CTkLabel(master=janelaFeedback, text="Sprint: "+sprint, font=('Roboto', 16, 'bold'), text_color='#a0a0a0').place(x=70, y=60)
            scrool = ctk.CTkFrame(master=janelaFeedback, width=700, height=340).place(x=40, y=90)

            with open('data_json/questions.json', "r") as arquivo:
                dados_json = json.load(arquivo)
            
            idturma = "123"
            idtime = "3"
            idavaliado = "gui@gmail.com"
            controler = 0
            posicaoy = 110
            for idturmajson in dados_json['avaliacao']:
                if idturmajson['idturma'] == idturma and idturmajson['idtime'] == idtime:
                    for respostas in idturmajson['respostas']:
                        if respostas['idavaliado'] == idavaliado:
                            if respostas['feedback1'] != "":
                                labelFeed = ctk.CTkLabel(master=scrool, text="• "+respostas['feedback1'], font=('Roboto', 12)).place(x=60, y=posicaoy)
                                posicaoy +=30
                            if respostas['feedback2'] != "":
                                    labelFeed = ctk.CTkLabel(master=scrool, text="• "+respostas['feedback2'], font=('Roboto', 12)).place(x=60, y=posicaoy)
                                    posicaoy +=30
                            if respostas['feedback3'] != "":
                                    labelFeed = ctk.CTkLabel(master=scrool, text="• "+respostas['feedback3'], font=('Roboto', 12)).place(x=60, y=posicaoy)
                                    posicaoy +=30
                            if respostas['feedback4'] != "":
                                    labelFeed = ctk.CTkLabel(master=scrool, text="• "+respostas['feedback4'], font=('Roboto', 12)).place(x=60, y=posicaoy)
                                    posicaoy +=30
                            if respostas['feedback5'] != "":
                                    labelFeed = ctk.CTkLabel(master=scrool, text="• "+respostas['feedback5'], font=('Roboto', 12)).place(x=60, y=posicaoy)
                                    posicaoy +=30
            botaoVoltar = ctk.CTkButton(janelaFeedback, text="Voltar", width=100, cursor="hand2", fg_color="#00FFFF", text_color='black').place(x=660, y=450)
                        
            
    tela_feedback()
