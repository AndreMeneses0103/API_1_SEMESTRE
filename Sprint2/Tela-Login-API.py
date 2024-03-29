import json
import customtkinter as ctk
from tkinter import *
import tkinter as tk
import TelaBV as TBV

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
        janela.title("Sistema de login")
        #janela.iconbitmap("logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
        pass

    def tela_login(self):
        #trabalhando com a imagem da tela
        '''img = PhotoImage(file="logo_insight.png").subsample(2) # reduzindo o tamanho em 50%
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=50, y=160)'''
        label_tt = ctk.CTkLabel(master=janela, text='"Obtenha insights poderosos e \nimpulsione a excelência da sua equipe\n com nosso sistema de avaliação 360 e \ndashboards integrados"', font=('Roboto',18, 'bold'), text_color="#00FFFF").place(x=30, y=30)

        #frame a direita
        login_frame = ctk.CTkFrame(master=janela, width=400, height=600)
        login_frame.pack(side=RIGHT)

        #frame widgets
        label = ctk.CTkLabel(master=login_frame, text="Sistema de avaliação 360º", font = ('Roboto', 25, 'bold'), text_color= ('white') )
        label.place(x=45, y=40)

        #entrada de dados
        user_name_label1 = ctk.CTkLabel(master=login_frame, text="Username: ", text_color="white", font=('Roboto', 14)).place(x=45,y=100)
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
                if (acesso["usuarios"][x]["user"]) == (input_nome) and acesso["usuarios"][x]["senha"] == input_senha:
                    aviso_validado = ctk.CTkLabel(master=login_frame, text="Acesso liberado!", text_color="#00FFFF", font=('Roboto', 18)).place(x=45,y=300)
                    acesso["usuarios"][x]["isActive"] = True
                    insert_acesso = str(json.dumps(acesso, indent=4))
                    with open("data_json/users.json", "w") as arq_json:
                        arq_json.write(insert_acesso)
                    janela.destroy()
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

            #entrada de dados turma cadastro          
            label = ctk.CTkLabel(master=cadastro_frame, text="Turma", font = ('Roboto', 15), text_color= ('white'))
            label.place(x=45, y=260)
            options_turma = ["Opção 1", "Opção 2", "Opção 3"]
            turma = tk.StringVar(cadastro_frame)
            turma.set(options_turma[0])
            #contar para o pessoal
            opt_menu = ctk.CTkOptionMenu(master=cadastro_frame, values=options_turma, variable=turma, fg_color="gray").place(x=45, y=290)

            #entrada de dados time cadastro          
            label = ctk.CTkLabel(master=cadastro_frame, text="Time", font = ('Roboto', 15), text_color= ('white'))
            label.place(x=45, y=320)
            options_time = ["Opção 1", "Opção 2", "Opção 3"]
            time = tk.StringVar(cadastro_frame)
            time.set(options_time[0])
            opt_menu = ctk.CTkOptionMenu(master=cadastro_frame, values=options_time, variable=time, fg_color="gray").place(x=45, y=345)
            #opt_menu = tk.OptionMenu(cadastro_frame, time, *options_turma).place(x=55, y=430)
            

            def back():
                cadastro_frame.pack_forget()
                #devolvendo o frame de login
                login_frame.pack(side=RIGHT)
                pass

            voltar = ctk.CTkButton(cadastro_frame, text="Voltar", width=150, fg_color="gray", font = ('Roboto', 14), cursor="hand2", hover_color='#202020', command=back).place(x=45, y=400)
            def cadastro():

                with open('data_json/users.json', 'r') as f:
                    data = json.load(f)

                novos_dados = data

                
                data_user = nomecompleto.get()
                data_email = email.get()
                data_senha = senha.get()

                data_cadastro = {
                    "user":data_user,
                    "id":data_email,
                    "cargo":"user",
                    "senha":data_senha,
                    "isActive": False
                }


                novos_dados['usuarios'].append(data_cadastro)
                novos_dados = json.dumps(novos_dados, indent=4)

                with open('data_json/users.json', 'w') as arquivo:
                    arquivo.write(novos_dados)
                    print('Cadastrados')


                back()
                label_confirmacao_cadastro = ctk.CTkLabel(master=login_frame, text="Cadastro enviado com sucesso!\nAguarde a liberação do seu login pelo administrador", text_color="#00FFFF", font=('Roboto', 14)).place(x=45,y=400)
                pass
            
            cadastrar_button = ctk.CTkButton(cadastro_frame, text="Cadastrar", width=150, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command=cadastro).place(x=220, y=400)
            
            pass

            #voltar_button = ctk.CTkButton(cadastro_frame, text="Voltar", width=100, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14, 'bold'), cursor="hand2", hover_color='#2FCDCD').place(x=45, y=250)
             
        cadastro_button = ctk.CTkButton(login_frame, text="Novo por aqui?",font =('Roboto', 14), command=tela_cadastro, text_color=('black'), cursor="hand2", fg_color='#00FFFF', hover_color='#2FCDCD').place(x=127, y=350)
        pass
        #para mudar a cor do botão no ctk fg_color - hover_color

tela_login_cadastro()
