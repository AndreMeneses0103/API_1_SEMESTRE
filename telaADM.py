import customtkinter as ctk
import tkinter as tk
from tkinter import *
import TelaBV as TBV
import json

def abrir_tela_adm():
    #Padrão temas da tela
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    #padrão da tela
    janela = ctk.CTk()

    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x = (screen_width - 1200) // 2
    y = (screen_height - 650) // 2
    janela.geometry(f"1200x650+{x}+{y}")
    janela.title("Insight 360º")
    janela.iconbitmap("logo_insight.ico")
    janela.resizable(False, False)

    #imagem logo 360
    img = PhotoImage(file = "logo_insight.png").subsample(2)
    label_img = ctk.CTkLabel(master=janela, image=img, text="")
    label_img.place(x=60, y=20)
    #titulo ADM
    label_tt = ctk.CTkLabel(master=janela, text='Administrador', font=('Roboto',32, 'bold'), text_color="white").place(x=600, y=80)

    def Close():
        acesso = json.load(open("data_json/users.json", "r"))

        for x in range(len(acesso["usuarios"])):
            acesso["usuarios"][x]["isActive"] = False

        insert_acesso = str(json.dumps(acesso, indent=4))

        with open("data_json/users.json", "w") as arq_json:
            arq_json.write(insert_acesso)

        janela.destroy()
        import Tela_Login_API
        #TLOGIN.abrir_login()

    #Imagem do botão logout
    logout = PhotoImage(file = "logout.png").subsample(2)
    Button = ctk.CTkButton(master=janela, width = 50, image=logout, text="", fg_color="#242424", command=Close)
    Button.place(x=1100, y=40)

    #frame esquerda
    frame1 = ctk.CTkFrame(master=janela, width=370, height=450)
    frame1.place(x=15, y=160)

    #lado direito

    def abre_turmas():
        horizonte = 0
        vertical = 0
        frame = ctk.CTkFrame(master=janela, width=750, height=350)
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
        frame = ctk.CTkFrame(master=janela, width=750, height=350)
        texto =ctk.CTkLabel(master=frame, text="TIMES ABERTO", font=("Roboto",25),text_color='white').place(x=420, y=214)
        frame.place(x=300, y=180)

    def abrir_cadastro_turma():
        janela.destroy()
        import cadastro_turma_time
    def aceite_usuario():
        janela.destroy()
        import Tela_Aceite_Usuários

    def abrir_tela_administradores():
        janela.destroy()
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



    def imprimirTimes():

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

        labelTime = ctk.CTkLabel(master=frame1, text="Times: ", font=('Roboto', 14)).place(x=44, y=230)
        optionMenuTimes = ctk.CTkOptionMenu(master=janela, values=nomestimes, variable=timeSelecionado, fg_color='gray', width=270)
        optionMenuTimes.place(x=53, y=415)



        def imprimirSprintsIntegrantes():
            
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
            with open("data_json/users.json", 'r') as arquivo:
                users = json.load(arquivo)

                for x in users['usuarios']:
                    if x['idtime'] == idtime:
                        integrantes.append(x['user'])

            labelTime = ctk.CTkLabel(master=frame1, text="Sprint: ", font=('Roboto', 14)).place(x=44, y=300)
            optionMenuSprint = ctk.CTkOptionMenu(master=janela, values=quantidade_sprints, variable=sprintSelecionada, fg_color='gray', width=270)
            optionMenuSprint.place(x=53, y=485)

            ButtonDash = ctk.CTkButton(master=janela,width=180, fg_color="#5CE1E6", text="Dashboard", font = ('Roboto', 18, 'bold'), text_color= ('black'))
            ButtonDash.place(x=960, y=550)

            # Colocar integração DASHBOARD


        imgcheck = PhotoImage(file = "check.png").subsample(4)
        buttonVerificar = ctk.CTkButton(janela, text="", image=imgcheck, width=10,fg_color='#302929',border_color='#2a2b2a', bg_color='#2a2b2a', cursor="hand2", command=imprimirSprintsIntegrantes).place(x=330, y=410)



    #botoes widgets
    Button = ctk.CTkButton(master=frame1,width=180, fg_color="#5CE1E6", text="Cadastros", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=abrir_cadastro_turma)
    Button.place(x=85, y=15)
    Button = ctk.CTkButton(master=frame1, width=180, fg_color="#5CE1E6", text="Aceites", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=aceite_usuario)
    Button.place(x=85, y=60)
    Button = ctk.CTkButton(master=frame1, width=180, fg_color="#5CE1E6", text="Administradores", font = ('Roboto', 18, 'bold'), text_color= ('black'), cursor="hand2", command=abrir_tela_administradores)
    Button.place(x=85, y=105)

    labelTurma = ctk.CTkLabel(master=frame1, text="Turmas: ", font=('Roboto', 14)).place(x=44, y=170)
    optionMenuTurmas= ctk.CTkOptionMenu(master=janela, values=nomesturmas, variable=turmaSelecionada, fg_color='gray', width=270)
    optionMenuTurmas.place(x=53, y=355)
    
    imgcheck = PhotoImage(file = "check.png").subsample(4)
    buttonVerificar = ctk.CTkButton(janela, text="", image=imgcheck, width=10,fg_color='#2a2b2a',border_color='#2a2b2a', bg_color='#2a2b2a', cursor="hand2", command=imprimirTimes).place(x=330, y=350)


    janela.mainloop()