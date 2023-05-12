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
            janela.geometry("1200x650") #DEFINO O TAMANHO DA JANELA
            janela.title("Sistema de login")
            janela.iconbitmap("logo_insight.ico")
            janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
            pass
        
        def TelaAlerta(self):
            img = PhotoImage(file="logo_insight.png").subsample(2) # reduzindo o tamanho em 50%
            label_img = ctk.CTkLabel(master=janela, image=img, text='')
            label_img.place(x=280, y=210)
        
            user_nome = ""

            acesso = json.load(open("data_json/users.json", "r"))

            ac_turmas = json.load(open("data_json/turmas.json", "r"))


            for x in range(len(acesso["usuarios"])):
                if(acesso["usuarios"][x]["isActive"] == True):
                    user_nome = acesso["usuarios"][x]["user"]
                    jaResp = acesso["usuarios"][x]["resp"]

            label_BemVindo=ctk.CTkLabel(master=janela, text=(f"Bem vindo, {user_nome}"), font=("Roboto",25),text_color='white').place(x=630, y=290)
            
            # Botões para selecionar o time e turma do usuário
            turmas = []
            sprint = []
            times = []
           
            for nome in ac_turmas["turmas"]:  
                turmas.append(nome["nometurma"])

            # print(times)
            # print(turmas)
           
            sprintSelecionada = StringVar()
            timeSelecionado = StringVar()
            turmaSelecionada = StringVar()
            

            turmaSelecionada.set(turmas[0])


            def imprimir(tr):
                #as duas variaveis de baixo reiniciam os valores caso o botao de turma seja mudado
                times = []
                sprint = []

                #a linha de baixo retorna o numero do da posicao do elemento selecionado no botao de turma
                posicao = turmas.index(tr)

                todos_times = ac_turmas["turmas"][posicao]["times"]
                todas_sprints = ac_turmas["turmas"][posicao]["sprints"]
                #criar uma variavel semelhante a essa de cima, so que para sprint


                for x in range(len(todos_times)):
                    times.append(todos_times[x]["nometime"])

                #criar um for percorrendo todos os elementos semelhante a de cima, so que para sprint (pegar a chave "indice" dentro do objeto "sprints")

                print(times)

                timeSelecionado.set(times[0])
                times_option_menu = ctk.CTkOptionMenu(master=janela, values=times, variable=timeSelecionado, fg_color="gray").place(x=440, y=15)

                for x in range (len(todas_sprints)):
                    sprint.append(todas_sprints[x]["indice"])

                print(sprint)

                sprintSelecionada.set(sprint[0])
                sprint_option_menu = ctk.CTkOptionMenu(master=janela, values=sprint, variable=sprintSelecionada, fg_color="gray").place(x=800, y=15)

                #apos fazer o for, inserir no botao as sprints, semelhante as duas linhas acima

                

            #Option Menu para selecionar a sprint
            sprint_label = ctk.CTkLabel(master=janela, text="Sprint:", font=("Roboto", 14), text_color='white').place(x=750, y=15)
            sprint_option_menu = ctk.CTkOptionMenu(master=janela, values=sprint, variable=sprintSelecionada, fg_color="gray").place(x=800, y=15)

            # Option Menu para selecionar o time
            times_label = ctk.CTkLabel(master=janela, text="Time:", font=("Roboto", 14), text_color='white').place(x=390, y=15)
            times_option_menu = ctk.CTkOptionMenu(master=janela, values=times, variable=timeSelecionado, fg_color="gray").place(x=440, y=15)

            # Option Menu para selecionar a turma
            turmas_label = ctk.CTkLabel(master=janela, text="Turma:", font=("Roboto", 14), text_color='white').place(x=30, y=15)
            turmas_option_menu = ctk.CTkOptionMenu(master=janela, values=turmas, variable=turmaSelecionada, fg_color="gray", command=imprimir).place(x=90, y=15)





            def AbrirAv():


                
                janela.destroy()
                #função de abrir a avaliação
                TelaAV.abrir_avaliacao(sprintSelecionada.get(), timeSelecionado.get(), turmaSelecionada.get())




            dashboard_button = ctk.CTkButton(master=janela, text="Dashboards", width=110, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=AbrirDashboards).place(x=30, y=560)
            cadastrar_button = ctk.CTkButton(master=janela, text="Avaliação", width=110, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=AbrirAv).place(x=1020, y=560)
            logout_button = ctk.CTkButton(master=janela, text="Logout", width=90, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=Close).place(x=1050, y=15)
            #sprint_button = ctk.CTkButton(master=janela, text="Sprint", width=90, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=Close).place(x=30, y=15)
            

            
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

    # Def para exibir a tela de dashboards
    def AbrirDashboards():
        janela.destroy()
        
    alerta()
