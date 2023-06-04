import json
import tkinter as tk
import customtkinter as ctk
from tkinter import *
import sistema_avaliacao as TelaAV
from datetime import datetime, timedelta
import dashboardOperacional
from customtkinter import *

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


            screen_width = janela.winfo_screenwidth()
            screen_height = janela.winfo_screenheight()
            x = (screen_width - 1200) // 2
            y = (screen_height - 650) // 2
            janela.geometry("1200x650+{}+{}".format(x, y))

            
            janela.title("Insight 360º")
            janela.iconbitmap("btspadrao/logo_insight.ico")
            janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
            pass
        
        def TelaAlerta(self):
            img = PhotoImage(file="btspadrao/logo_insight.png").subsample(2) # reduzindo o tamanho em 50%
            label_img = ctk.CTkLabel(master=janela, image=img, text='')
            label_img.place(x=280, y=210)
        
            user_nome = ""

            acesso = json.load(open("data_json/users.json", "r"))

            ac_turmas = json.load(open("data_json/turmas.json", "r"))


            for x in range(len(acesso["usuarios"])):
                if(acesso["usuarios"][x]["isActive"] == True):
                    user_nome = acesso["usuarios"][x]["user"]
                    user_turma =  acesso["usuarios"][x]["idturma"]
                    user_time = acesso ["usuarios"][x]["idtime"]
                    user_id = acesso ["usuarios"][x]["id"]
            

            
            data_atual = datetime.now()



            label_BemVindo=ctk.CTkLabel(master=janela, text=(f"Bem vindo, {user_nome}"), font=("Roboto",25),text_color='white').place(x=630, y=290)
            
            # Botões para selecionar o time e turma do usuário
            turmas = []
            sprint = []
            times = []
           
            for nome in ac_turmas["turmas"]:  
                if (user_turma == nome["idturma"]):
                    turmas.append(nome["nometurma"]) 

           
            sprintSelecionada = StringVar()
            timeSelecionado = StringVar()
            turmaSelecionada = StringVar()
            

            


            def imprimir(tr):

                acesso = json.load(open("data_json/users.json", "r"))

                for x in range(len(acesso["usuarios"])):
                    if(acesso["usuarios"][x]["isActive"] == True):
                        jaResp = acesso["usuarios"][x]["resp"]
                        sprint_json = acesso["usuarios"][x]["sprint_atual"]

                #as duas variaveis de baixo reiniciam os valores caso o botao de turma seja mudado
                times = []
                sprint = []
                posicao = 0

                
                inicio_sprint = ''
                fim_sprint = ''
                atual_sprint = 0
                #a linha de baixo retorna o numero do da posicao do elemento selecionado no botao de turma
                for x in range (len(ac_turmas["turmas"])):
                    if (tr == ac_turmas["turmas"][x]["nometurma"]):
                        posicao = ac_turmas["turmas"][x]["ordem"]

                todas_sprints = ac_turmas["turmas"][posicao]["sprints"]

                for x in range (len(todas_sprints)):
                    # sprint.append(todas_sprints[x]["indice"])
                    inicio_sprint = todas_sprints[x]["inicioSprint"]
                    fim_sprint = todas_sprints[x]["fimSprint"]

                    inicio_sprint = datetime.strptime(inicio_sprint, "%d/%m/%Y")
                    horas = "11:59:59"
                    fim_sprint = datetime.strptime(fim_sprint + " " + horas, "%d/%m/%Y %H:%M:%S")
                    # print(f'Data final da sprint sem 5 dias: {fim_sprint}')
                    dias_finais = timedelta(days=5)
                    fim_sprint = fim_sprint + dias_finais
                    # print(f'Data final da sprint com 5 dias: {fim_sprint}')

                    agora = datetime.now()
                    

                    if(agora >= inicio_sprint and agora <= fim_sprint):
                        atual_sprint = todas_sprints[x]["indice"]


                    acesso = json.load(open("data_json/users.json", "r"))

                    for x in range(len(acesso["usuarios"])):
                        if(acesso["usuarios"][x]["isActive"] == True):
                            acesso["usuarios"][x]["sprint_atual"] = atual_sprint
                            insert_acesso = (json.dumps(acesso, indent=4))
                            with open("data_json/users.json", "w") as arq_json:
                                arq_json.write(insert_acesso)


                    if(int(atual_sprint) > int(sprint_json)):
                        if(jaResp == True):

                            jaResp = False
                


                if(jaResp == False):
                    cadastrar_button = ctk.CTkButton(master=janela, text="Avaliação", width=150, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=AbrirAv).place(x=1020, y=560)
                else:
                    cadastrar_button = ctk.CTkButton(master=janela, text="Finalizado", width=150, text_color='#fff', fg_color="#404343", font = ('Roboto', 14), cursor="X_cursor", hover_color='#404345').place(x=1020, y=560)




                todos_times = ac_turmas["turmas"][posicao]["times"]
                todas_sprints = ac_turmas["turmas"][posicao]["sprints"]
                #criar uma variavel semelhante a essa de cima, so que para sprint

                times = []
                for x in range(len(todos_times)):

                    if (user_time == todos_times[x]["idtime"]):
                        times.append(todos_times[x]["nometime"])
                    else: 
                        print("===============",todos_times[x]["idtime"])

                #criar um for percorrendo todos os elementos semelhante a de cima, so que para sprint (pegar a chave "indice" dentro do objeto "sprints")

            
                times_option_menu = ctk.CTkOptionMenu(master=janela, values=times, variable=timeSelecionado, fg_color="gray").place(x=440, y=15)

                for x in range (len(todas_sprints)):
                    sprint.append(todas_sprints[x]["indice"])


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

                idtime = ""
                idturma = ""

                with open('data_json/turmas.json', 'r') as usuarios:
                    id_users = json.load(usuarios)
                    usuarios = id_users["turmas"]
                    #usuarios = id_users["usuarios"]


                for turma in usuarios:
                    if (turma['nometurma'] == turmaSelecionada.get()):
                        for time in turma['times']:
                            if time['nometime'] == timeSelecionado.get():
                                    idtime = time['idtime']
                                    idturma = turma['idturma']

                janela.destroy()
                #função de abrir a avaliação
                #TelaAV.abrir_avaliacao(idtime, idturma)
                TelaAV.abrir_avaliacao(sprintSelecionada.get(), timeSelecionado.get(), turmaSelecionada.get(), idturma, idtime)



            def chamarDashboard():
                if turmaSelecionada.get() == "" or sprintSelecionada.get() == "" or timeSelecionado.get()=="":
                    janelaPreenchimentoObrigatorio = ctk.CTk()
                    janelaPreenchimentoObrigatorio.title("ALERTA!")
                    screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                    screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                    x = (screen_width - 330) // 2
                    y = (screen_height - 180) // 2
                    janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                    janelaPreenchimentoObrigatorio.resizable(False, False)
                    label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nO preenchimento de todos\nos campos é obrigatório\n", font=('Roboto', 15, 'bold')).pack()
                    def destroy_alerta():
                            janelaPreenchimentoObrigatorio.destroy()
                    button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                    janelaPreenchimentoObrigatorio.mainloop()
                else:
                    with open('data_json/turmas.json', "r") as arquivo:
                        dados_json_turma = json.load(arquivo)

                    for idturmajson in dados_json_turma['turmas']:
                        if idturmajson['nometurma']==turmaSelecionada.get():
                            idturmaParametro = idturmajson['idturma']
                            for idtime in idturmajson['times']:
                                if idtime['nometime']== timeSelecionado.get():
                                    idtimeParametro = idtime['idtime']

                    with open('data_json/questions.json', "r") as arquivoQuestions:
                        dados_Questions = json.load(arquivoQuestions)
                    sprintValor = sprintSelecionada.get()
                
                    for turmaJsonQuestion in dados_Questions['avaliacao']:
                        verificador = True
                        if turmaJsonQuestion['idturma'] == idturmaParametro:
                            if turmaJsonQuestion['idtime'] == idtimeParametro:
                                if turmaJsonQuestion['sprint'] == sprintValor:
                                    if turmaJsonQuestion['idAvaliador'] == user_id:
                                        janela.destroy()
                                        #dashGerencial.abrir_dash_ge(idturmaParametro, idtimeParametro, sprintSelecionada.get(), turmaSelecionada.get(), timeSelecionado.get())
                                        break
                                    else:
                                        verificador = False
                                else:
                                    verificador = False
                            else:
                                verificador = False
                        
                        else:
                            verificador = False

                    if verificador == False:
                        janelaPreenchimentoObrigatorio = ctk.CTk()
                        janelaPreenchimentoObrigatorio.title("ALERTA!")
                        screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                        screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                        x = (screen_width - 330) // 2
                        y = (screen_height - 180) // 2
                        janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                        janelaPreenchimentoObrigatorio.resizable(False, False)
                        label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nA avaliação da turma,\ntime ou sprint ainda\nnão foi realizada.\n", font=('Roboto', 15, 'bold')).pack()
                        def destroy_alerta():
                                janelaPreenchimentoObrigatorio.destroy()
                        button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                        janelaPreenchimentoObrigatorio.mainloop()
                    else:
                        #janela.destroy()
                        dashboardOperacional.abrir_dash_op(idturmaParametro, idtimeParametro, sprintSelecionada.get(), user_id)
         




            dashboard_button = ctk.CTkButton(master=janela, text="Exibir Dashboards", width=110, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=chamarDashboard).place(x=30, y=560)
            # cadastrar_button = ctk.CTkButton(master=janela, text="Avaliação", width=110, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=AbrirAv).place(x=1020, y=560)
            logout = PhotoImage(file = "btspadrao/logout.png").subsample(2)
            logout_button = ctk.CTkButton(master=janela, width = 50, image=logout, text="", fg_color="#242424", cursor="hand2", command=Close).place(x=1120, y=15)
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
        import Tela_Login_API

        
        
    # Def para exibir a tela de dashboards
    def AbrirDashboards():
        janela.destroy()
        
    alerta()
#abrir()
