import json
import tkinter as tk
import customtkinter as ctk
from tkinter import *
import sistema_avaliacao as TelaAV

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

            ac_turmas = json.load(open("data_json/turmas.json", "r"))

            for x in range(len(acesso["usuarios"])):
                if(acesso["usuarios"][x]["isActive"] == True):
                    user_nome = acesso["usuarios"][x]["user"]
                    jaResp = acesso["usuarios"][x]["resp"]

            label_BemVindo=ctk.CTkLabel(master=janela, text=(f"Bem vindo, {user_nome}"), font=("Roboto",25),text_color='white').place(x=420, y=214)
            # Botões para selecionar o time e turma do usuário
            times = []
            turmas = []
           
            for nome in ac_turmas["turmas"]:
                # times = acesso["usuarios"][x]["times"]
                turmas.append(nome["nometurma"])

            print(turmas)
            timeSelecionado = StringVar()
            turmaSelecionada = StringVar()

            turmaSelecionada.set(turmas[0])

            # Option Menu para selecionar o time
            times_label = ctk.CTkLabel(master=janela, text="Time:", font=("Roboto", 14), text_color='white').place(x=50, y=15)
            times_option_menu = ctk.CTkOptionMenu(master=janela, values=times, variable=timeSelecionado, fg_color="gray").place(x=120, y=15)

            # Option Menu para selecionar a turma
            turmas_label = ctk.CTkLabel(master=janela, text="Turma:", font=("Roboto", 14), text_color='white').place(x=300, y=15)
            turmas_option_menu = ctk.CTkOptionMenu(master=janela, values=turmas, variable=turmaSelecionada, fg_color="gray").place(x=380, y=15)

            dashboard_button = ctk.CTkButton(master=janela, text="Dashboards", width=110, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=AbrirDashboards).place(x=50, y=450)
            cadastrar_button = ctk.CTkButton(master=janela, text="Avaliação", width=110, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=AbrirAv).place(x=60, y=450)
            logout_button = ctk.CTkButton(master=janela, text="Logout", width=90, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=Close).place(x=680, y=15)
            #times_button = ctk.CTkButton(master=janela, text="Times", width=200, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=Close).place(x=50, y=15)
            #turmas_button = ctk.CTkButton(master=janela, text="Turmas", width=200, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=Close).place(x=300, y=15)
            
            janela.protocol("WM_DELETE_WINDOW", Close)

    def Close():
        acesso = json.load(open("data_json/users.json", "r"))

        for x in range(len(acesso["usuarios"])):
            acesso["usuarios"][x]["isActive"] = False

        insert_acesso = str(json.dumps(acesso, indent=4))

        with open("data_json/users.json", "w") as arq_json:
            arq_json.write(insert_acesso)

        janela.destroy()
        janela.mainloop()

    def AbrirAv():
        janela.destroy()
        TelaAV.abrir_avaliacao()

    # Def para exibir a tela de dashboards
    def AbrirDashboards():
        janela.destroy()
        
    alerta()
# abrir()