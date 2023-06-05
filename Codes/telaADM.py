import customtkinter as ctk
import tkinter as tk
from tkinter import *
import TelaBV as TBV
import json
import dashGerencial
from customtkinter import *

def abrir_tela_adm():
    #Padrão temas da tela
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    #padrão da tela
    janelaADM = ctk.CTk()

    screen_width = janelaADM.winfo_screenwidth()
    screen_height = janelaADM.winfo_screenheight()
    x = (screen_width - 1200) // 2
    y = (screen_height - 650) // 2
    janelaADM.geometry(f"1200x650+{x}+{y}")
    janelaADM.title("Insight 360º")
    janelaADM.iconbitmap("btspadrao/logo_insight.ico")
    janelaADM.resizable(False, False)

    #imagem logo 360
    img = PhotoImage(file = "btspadrao/logo_insight.png").subsample(2)
    label_img = ctk.CTkLabel(master=janelaADM, image=img, text="")
    label_img.place(x=60, y=20)
    #titulo ADM
    label_tt = ctk.CTkLabel(master=janelaADM, text='Administrador', font=('Roboto',32, 'bold'), text_color="white").place(x=600, y=80)


    def Close():
        acesso = json.load(open("data_json/users.json", "r"))

        for x in range(len(acesso["usuarios"])):
            acesso["usuarios"][x]["isActive"] = False

        insert_acesso = str(json.dumps(acesso, indent=4))

        with open("data_json/users.json", "w") as arq_json:
            arq_json.write(insert_acesso)

        janelaADM.destroy()
        import Tela_Login_API
        #TLOGIN.abrir_login()

    #Imagem do botão logout
    logout = PhotoImage(file = "btspadrao/logout.png").subsample(2)
    Button = ctk.CTkButton(master=janelaADM, width = 50, image=logout, text="", fg_color="#242424", command=Close)
    Button.place(x=1100, y=40)

    #frame esquerda
    frame1 = ctk.CTkFrame(master=janelaADM, width=370, height=450)
    frame1.place(x=15, y=160)

    #lado direito

    def abre_turmas():
        horizonte = 0
        vertical = 0
        frame = ctk.CTkFrame(master=janelaADM, width=750, height=350)
        acesso = json.load(open("data_json/users.json", "r"))
        for x in range(len(acesso["usuarios"])):
            user_nome = acesso["usuarios"][x]["user"]
            btn_user = ctk.CTkButton(master=frame, text=user_nome, fg_color="#1a1a1a")
            btn_user.place(x=horizonte, y= vertical)
            horizonte = horizonte + 205
            if(horizonte > 750):
                vertical = vertical + 100
                horizonte = 0

        frame.place(x=300, y=180)

    def abre_times():
        frame = ctk.CTkFrame(master=janelaADM, width=750, height=350)
        texto =ctk.CTkLabel(master=frame, text="TIMES ABERTO", font=("Roboto",25),text_color='white').place(x=420, y=214)
        frame.place(x=300, y=180)

    def abrir_cadastro_turma():
        janelaADM.destroy()
        import cadastro_turma_time
    def aceite_usuario():
        janelaADM.destroy()
        import Tela_Aceite_Usuários

    def abrir_tela_administradores():
        janelaADM.destroy()
        import Tela_Administradores

    with open("data_json/turmas.json", "r") as arquivo:
        turmas = json.load(arquivo)


        nomesturmas = []
        for turma in turmas['turmas']:
            nomesturmas.append(turma['nometurma'])
    print(nomesturmas)

    nomestimes = []
    sprints = []
    integrantes = []


    turmaSelecionada = StringVar()
    timeSelecionado = StringVar()
    sprintSelecionada = StringVar()
    integranteSelecionado = StringVar()



    def imprimirTimes(t):

        timeSelecionado.set("")
        global turmaReferencia
        turmaReferencia = turmaSelecionada.get()
        nometimes = []
        nomestimes.clear()
        global idturma
        for idturmaJson in turmas['turmas']:
            if idturmaJson['nometurma'] == turmaReferencia:
                idturma = idturmaJson['idturma']
                print(idturmaJson['idturma']) 


        for turma in turmas['turmas']:
            if turma['nometurma'] == turmaReferencia:
                for time in turma['times']:
                    nomestimes.append(time['nometime'])

       # labelTime = ctk.CTkLabel(master=frame1, text="Times: ", font=('Roboto', 14)).place(x=44, y=180)
        optionMenuTimes = ctk.CTkOptionMenu(master=janelaADM, values=nomestimes, variable=timeSelecionado, fg_color='gray', width=270)
        optionMenuTimes.place(x=53, y=370)


        quantidade_sprints = []
        quantidade_sprints.clear()
        integrantes.clear()
        for turma in turmas['turmas']:
            if turma['nometurma'] == turmaReferencia:
                for x in turma['sprints']:
                    quantidade_sprints.append(x['indice'])
                print(quantidade_sprints)
                for time in turma['times']:
                    if time['nometime'] == timeSelecionado.get():
                        idtime = time['idtime']
        
      #  labelTime = ctk.CTkLabel(master=frame1, text="Sprint: ", font=('Roboto', 14)).place(x=44, y=240)
        optionMenuSprint = ctk.CTkOptionMenu(master=janelaADM, values=quantidade_sprints, variable=sprintSelecionada, fg_color='gray', width=270)
        optionMenuSprint.place(x=53, y=430)


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
                    dados_questions = json.load(arquivoQuestions)
                sprintValor = sprintSelecionada.get()
            
                for turmaJsonQuestion in dados_questions['avaliacao']:
                    verificador = True
                    if turmaJsonQuestion['idturma'] == idturmaParametro:
                        if turmaJsonQuestion['idtime'] == idtimeParametro:
                            if turmaJsonQuestion['sprint'] == sprintValor:
                                janelaADM.destroy()
                                dashGerencial.abrir_dash_ge(idturmaParametro, idtimeParametro, sprintSelecionada.get(), turmaSelecionada.get(), timeSelecionado.get())
                                break
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

        ButtonDash = ctk.CTkButton(master=janelaADM,width=180, fg_color="#5CE1E6", text="Exibir Dashboard", font = ('Roboto', 18), text_color= ('black'), command=chamarDashboard)
        ButtonDash.place(x=100, y=550)

    #botoes widgets
    Button = ctk.CTkButton(master=frame1,width=180, fg_color="#5CE1E6", text="Cadastros", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=abrir_cadastro_turma)
    Button.place(x=85, y=5)
    Button = ctk.CTkButton(master=frame1, width=180, fg_color="#5CE1E6", text="Aceites", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=aceite_usuario)
    Button.place(x=85, y=45)
    Button = ctk.CTkButton(master=frame1, width=180, fg_color="#5CE1E6", text="Administradores", font = ('Roboto', 18, 'bold'), text_color= ('black'), cursor="hand2", command=abrir_tela_administradores)
    Button.place(x=85, y=85)

    labelTurma = ctk.CTkLabel(master=frame1, text="Turmas: ", font=('Roboto', 14)).place(x=44, y=120)
    optionMenuTurmas= ctk.CTkOptionMenu(master=janelaADM, values=nomesturmas, variable=turmaSelecionada, fg_color='gray', width=270, command=imprimirTimes)
    optionMenuTurmas.place(x=53, y=310)
    
    vazio = tk.StringVar()
    lista = []
    labelTime = ctk.CTkLabel(master=frame1, text="Times: ", font=('Roboto', 14)).place(x=44, y=180)
    optionMenuTimes = ctk.CTkOptionMenu(master=janelaADM, fg_color='gray', width=270, variable=vazio, values=lista)
    optionMenuTimes.place(x=53, y=370)


    labelTime = ctk.CTkLabel(master=frame1, text="Sprint: ", font=('Roboto', 14)).place(x=44, y=240)
    optionMenuSprint = ctk.CTkOptionMenu(master=janelaADM, fg_color='gray', width=270,variable=vazio, values=lista)
    optionMenuSprint.place(x=53, y=430)

    janelaADM.protocol("WM_DELETE_WINDOW", Close)



   
    janelaADM.mainloop()
