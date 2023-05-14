import json
import customtkinter as ctk
from tkinter import *
import tkinter as tk
import TelaBV as TBV

# def abrir_login():
    
janela = ctk.CTk()
class tela_login_cadastro:
    def __init__(self):#deve conter todas as funções que existem - é a principal
    
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark") #modo dark
        ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
        pass

    def tela(self):    
        janela.geometry("800x500") #DEFINO O TAMANHO DA JANELA
        janela.title("Insight 360º")
        janela.iconbitmap("logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
        pass

    def tela_login(self):
        #trabalhando com a imagem da tela
        img = PhotoImage(file="logo_insight.png").subsample(2) # reduzindo o tamanho em 50%
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=50, y=160)
        label_tt = ctk.CTkLabel(master=janela, text='"Obtenha insights poderosos e \nimpulsione a excelência da sua equipe\n com nosso sistema de avaliação 360 e \ndashboards integrados"', font=('Roboto',18, 'bold'), text_color="#00FFFF").place(x=30, y=30)

        #frame a direita
        login_frame = ctk.CTkFrame(master=janela, width=400, height=600)
        login_frame.pack(side=RIGHT)

        #frame widgets
        label = ctk.CTkLabel(master=login_frame, text="Sistema de avaliação 360º", font = ('Roboto', 25, 'bold'), text_color= ('white') )
        label.place(x=45, y=40)

        #entrada de dados
        user_name_label1 = ctk.CTkLabel(master=login_frame, text="E-mail: ", text_color="white", font=('Roboto', 14)).place(x=45,y=100)
        username = tk.StringVar()#criação da variavel 
        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Username", width=300, font = ('Roboto', 14), textvariable=username).place(x=45, y=125)

        password = tk.StringVar()#criação da variavel 
        user_name_label2 = ctk.CTkLabel(master=login_frame, text="Password:", text_color="white", font=('Roboto', 14)).place(x=45,y=160)
        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Password", width=300, font = ('Roboto', 14), show="*", textvariable=password).place(x=45, y=185)

        def login():
    
            incorrect = 0
            acesso = json.load(open("data_json/users.json", "r"))
            for x in range(len(acesso["usuarios"])):
                input_nome = username.get()
                input_senha = password.get()
                if (acesso["usuarios"][x]["id"]) == (input_nome) and acesso["usuarios"][x]["senha"] == input_senha:
                    if(acesso["usuarios"][x]["aceito"] == False):
                        janelaAceito = ctk.CTk()
                        janelaAceito.title("ALERTA!")
                        screen_width = janelaAceito.winfo_screenwidth()
                        screen_height = janelaAceito.winfo_screenheight()
                        x = (screen_width - 300) // 2
                        y = (screen_height - 100) // 2
                        janelaAceito.geometry("600x100+{0}+{0}".format(x,y))
                        janelaAceito.resizable(False, False)
                        label_alerta = ctk.CTkLabel(master=janelaAceito, text="O usuario ainda nao foi aceito. Aguarde o ingresso pelo administrador.\n\n", font=("Roboto", 15, 'bold')).pack()
                        def destroy_alerta_aceito():
                            janelaAceito.destroy()
                            
                        button_ok = ctk.CTkButton(janelaAceito, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta_aceito, fg_color='#5CE1E6', text_color='black').pack()
                        janelaAceito.mainloop()
                    else:
                        aviso_validado = ctk.CTkLabel(master=login_frame, text="Acesso liberado!", text_color="#00FFFF", font=('Roboto', 18)).place(x=45,y=300)
                        acesso["usuarios"][x]["isActive"] = True
                        insert_acesso = str(json.dumps(acesso, indent=4))
                        with open("data_json/users.json", "w") as arq_json:
                            arq_json.write(insert_acesso)
                        janela.destroy()

                        # AS LINHAS ABAIXO FARAO A ANALISE SE USUARIO 'E ALUNO OU ADM

                        # if(acesso["usuarios"][x]["cargo"] == "adm"):
                        #     print("VAI ABRIR TELA ADM")
                        # else:
                        #     print("VAI ABRIR TELA USER")
                        TBV.abrir()
                else:
                    incorrect = incorrect + 1
            if(incorrect == len(acesso["usuarios"])):
                janelaNegado = ctk.CTk()
                janelaNegado.title("ALERTA!")
                screen_width = janelaNegado.winfo_screenwidth()
                screen_height = janelaNegado.winfo_screenheight()
                x = (screen_width - 300) // 2
                y = (screen_height - 100) // 2
                janelaNegado.geometry("300x100+{0}+{0}".format(x,y))
                janelaNegado.resizable(False, False)
                label_alerta = ctk.CTkLabel(master=janelaNegado, text="Usuário ou senha incorretos!\n\n", font=("Roboto", 15, 'bold')).pack()
                def destroy_alerta_Avaliacao():
                    janelaNegado.destroy()
                    
                button_ok = ctk.CTkButton(janelaNegado, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta_Avaliacao, fg_color='#5CE1E6', text_color='black').pack()
                janelaNegado.mainloop()  


                '''janelaNegado = ctk.CTk()
                janelaNegado.title("NEGADO!")
                janelaNegado.resizable(False, False)
                # janelaNegado.geometry("300x100")
                screen_width = janelaNegado.winfo_screenwidth()
                screen_height = janelaNegado.winfo_screenheight()
                x = (screen_width - 300) // 2
                y = (screen_height - 100) // 2
                janelaNegado.geometry("300x100+{0}+{0}".format(x,y)) 
                label_negado = ctk.CTkLabel(master=janelaNegado, text="Usuário ou senha incorretos!\n", font=("Roboto", 15, "bold")).pack()
                def destroy_negado():
                    janelaNegado.destroy()
                button_ok = ctk.CTkLabel(master=janelaNegado, text="Ok", font=("Roboto", 20, "bold"), command=destroy_negado, fg_color="#5CE1E6", text_color='black').pack()
                janelaNegado.mainloop()'''
        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=login).place(x=45, y=250)
        #button.grid(row=35, column=30)
    
        def tela_cadastro():
            #remover o frame de login
            login_frame.pack_forget()
            
            #criação da frame cadastro de usuário comum
            cadastro_frame = ctk.CTkFrame(master=janela, width=400, height=600)
            cadastro_frame.pack(side=RIGHT)

                #titulo frame
            label = ctk.CTkLabel(master=cadastro_frame, text="Cadastro de usuário", font = ('Roboto', 25, 'bold'), text_color= ('white') )
            label.place(x=45, y=40)

            #entrada de dados nome cadastro
            label = ctk.CTkLabel(master=cadastro_frame, text="Nome", font = ('Roboto', 15), text_color= ('white') )
            label.place(x=45, y=80)
            nomecompleto = tk.StringVar()
            nome_cadastro = ctk.CTkEntry(master=cadastro_frame, textvariable=nomecompleto,placeholder_text="Digite seu nome completo", width=300, font = ('Roboto', 14)).place(x=45, y=110)
        
            #entrada de dados email cadastro
            label = ctk.CTkLabel(master=cadastro_frame, text="Email", font = ('Roboto', 15), text_color= ('white') )
            label.place(x=45, y=140)
            email = tk.StringVar()
            email_cadastro = ctk.CTkEntry(master=cadastro_frame,placeholder_text="Digite seu email", width=300, font = ('Roboto', 14), textvariable=email).place(x=45, y=170)

            #entrada de dados senha cadastro
            label = ctk.CTkLabel(master=cadastro_frame, text="Senha", font = ('Roboto', 15), text_color= ('white'))
            label.place(x=45, y=200)
            senha = tk.StringVar()
            senha_cadastro = ctk.CTkEntry(master=cadastro_frame, textvariable=senha,placeholder_text="Digite sua senha", width=300, font = ('Roboto', 14), show='*').place(x=45, y=230)

            #JSON QUE MOSTRARÁ OS TIMES E TURMAS
            with open ("data_json/turmas.json", 'r') as arquivo:
                dados = json.load(arquivo)

            nomesturmas= []

            #seleciono somente as turmas
            for turma in dados['turmas']:
                nomesturmas.append(turma['nometurma'])
            print(nomesturmas)

            

            #entrada de dados turma cadastro          
            label = ctk.CTkLabel(master=cadastro_frame, text="Turma", font = ('Roboto', 15), text_color= ('white'))
            label.place(x=45, y=260)
            options_turma = nomesturmas
            
            turmaSelecionada = StringVar()
            turmaSelecionada.set(options_turma[0])
            #contar para o pessoal
            opcoes_time = ctk.CTkOptionMenu(master=cadastro_frame, fg_color='gray',values=options_turma, variable=turmaSelecionada).place(x=45, y=290)


            #FUNÇÃO QUE IRÁ VERIFICAR A TURMA E MOSTRARÁ OS TIMES DISPONIVEIS NELA
            def verificarTurma():

                if nomecompleto.get() == "" or email.get() == "" or senha.get()== "":
                    janelaAlertadadosFaltando = ctk.CTk()
                    janelaAlertadadosFaltando.title("ALERTA!")
                    janelaAlertadadosFaltando.resizable(False, False)
                    screen_width = janelaAlertadadosFaltando.winfo_screenwidth()
                    screen_height = janelaAlertadadosFaltando.winfo_screenheight()
                    x = (screen_width - 300) // 2
                    y = (screen_height - 100) // 2
                    janelaAlertadadosFaltando.geometry("300x100+{}+{}".format(x, y))
                    label_alerta = ctk.CTkLabel(master=janelaAlertadadosFaltando, text="Dados incompletos!\n", font=('Roboto', 15, 'bold')).pack()
                    
                    def destroy_alerta_Dados_faltando():
                        janelaAlertadadosFaltando.destroy()

                    button_ok = ctk.CTkButton(janelaAlertadadosFaltando, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta_Dados_faltando, fg_color='#5CE1E6', text_color='black').pack()
                    janelaAlertadadosFaltando.mainloop()
                elif nomecompleto.get() != "" or email.get() != "" or senha.get()!= "":

                    #selecionar somente os times da turma escolhida
                    global turmaReferencia
                    turmaReferencia = turmaSelecionada.get()
                    nometimes = []
                    global idturma
                    for idturmaJson in dados['turmas']:
                        if idturmaJson['nometurma'] == turmaReferencia:
                            idturma = idturmaJson['idturma']
                            print(idturmaJson['idturma']) 
                    
                    '''
                    for idturmaJson in dados['turmas']:
                        if idturmaJson['nometurma'] == turmaReferencia:
                            for idJson in idturmaJson['turmas']:
                                idturma.append(idJson['idturma'])
    '''   
                    print(idturma)
                    
                    for turma in dados['turmas']:
                        if turma['nometurma'] == turmaReferencia:
                            for time in turma['times']:
                                nometimes.append(time['nometime'])


                    print(nometimes)
                    print(nomesturmas)

                    label = ctk.CTkLabel(master=cadastro_frame, text="Time", font = ('Roboto', 15), text_color= ('white'))
                    label.place(x=45, y=320)
                    options_time = nometimes
                    timeSelecionado = StringVar()
                    timeSelecionado.set(options_time[0])
                    opt_menu = ctk.CTkOptionMenu(master=cadastro_frame, values=options_time, variable=timeSelecionado, fg_color="gray").place(x=45, y=345)
                    
                    #O BOTÃO CADASTRAR APARECERÁ SOMENTE QUANDO TUDO TIVER PREENCHIDO

                    def cadastro():
                        #FOR QUE PEGA O ID DO TIME SELECIONADO E GRAVA EM JSON
                        timeCadastro = timeSelecionado.get()
                        for turma in dados['turmas']:
                            if turma['nometurma'] == turmaReferencia:
                                for time in turma['times']:
                                    if time['nometime'] == timeCadastro:
                                        idtime = time['idtime']
                                        print(idtime)


                        with open('data_json/users.json', 'r') as f:
                            data = json.load(f)

                        novos_dados = data

                        
                        data_user = nomecompleto.get()
                        data_email = email.get()
                        data_senha = senha.get()

                        global idturma
                        
                        data_cadastro = {
                            "user":data_user,
                            "id":data_email,
                            "idturma": idturma,
                            "idtime": idtime,
                            "cargo":"user",
                            "senha":data_senha,
                            "isActive": False,
                            "aceito": False
                        }


                        novos_dados['usuarios'].append(data_cadastro)
                        novos_dados = json.dumps(novos_dados, indent=4)

                        with open('data_json/users.json', 'w') as arquivo:
                            arquivo.write(novos_dados)
                            print('Cadastrados')


                        back()


                        #TELA ALERTA DE CONFIRMAÇÃO DE CADASTRO
                        janelaConfirmacaoCadastro = ctk.CTk()
                        janelaConfirmacaoCadastro.title("ALERTA!")
                        screen_width = janelaConfirmacaoCadastro.winfo_screenwidth()
                        screen_height = janelaConfirmacaoCadastro.winfo_screenheight()
                        x = (screen_width - 330) // 2
                        y = (screen_height - 180) // 2
                        janelaConfirmacaoCadastro.geometry("330x180+{}+{}".format(x, y))
                        janelaConfirmacaoCadastro.resizable(False, False)
                        label_alerta = ctk.CTkLabel(master=janelaConfirmacaoCadastro, text="\nATENÇÃO!\n\nCadastro enviado com sucesso!\nAguarde a liberação do seu login pelo \nadministrador\n", font=('Roboto', 15, 'bold')).pack()
                        def destroy_alerta():
                            janelaConfirmacaoCadastro.destroy()
                        button_ok = ctk.CTkButton(janelaConfirmacaoCadastro, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()
                        janelaConfirmacaoCadastro.mainloop()


                       # label_confirmacao_cadastro = ctk.CTkLabel(master=login_frame, text="Cadastro enviado com sucesso!\nAguarde a liberação do seu login pelo administrador", text_color="#00FFFF", font=('Roboto', 14)).place(x=45,y=400)
                        pass
                    
                    cadastrar_button = ctk.CTkButton(cadastro_frame, text="Cadastrar", width=150, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=cadastro).place(x=220, y=400)
                    
                    pass
                    pass
            buttonVerificar = ctk.CTkButton(cadastro_frame, text="✅", width=50, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=verificarTurma).place(x=300, y=290)
            #entrada de dados time cadastro          
            #opt_menu = tk.OptionMenu(cadastro_frame, time, *options_turma).place(x=55, y=430)
            

            def back():
                cadastro_frame.pack_forget()
                #devolvendo o frame de login
                login_frame.pack(side=RIGHT)
                pass

            voltar = ctk.CTkButton(cadastro_frame, text="Voltar", width=150, fg_color="gray", font = ('Roboto', 14), cursor="hand2", hover_color='#202020', command=back).place(x=45, y=400)
            

            #voltar_button = ctk.CTkButton(cadastro_frame, text="Voltar", width=100, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14, 'bold'), cursor="hand2", hover_color='#2FCDCD').place(x=45, y=250)
            
        cadastro_button = ctk.CTkButton(login_frame, text="Novo por aqui?",font =('Roboto', 14), command=tela_cadastro, text_color=('black'), cursor="hand2", fg_color='#00FFFF', hover_color='#2FCDCD').place(x=127, y=350)
        pass
        #para mudar a cor do botão no ctk fg_color - hover_color

tela_login_cadastro()