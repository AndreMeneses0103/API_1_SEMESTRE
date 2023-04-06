import customtkinter as ctk
from tkinter import *
import tkinter as tk

janela = ctk.CTk()

class Application:
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
        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Username", width=300, font = ('Roboto', 14)).place(x=45, y=105)
        #label comum
        user_name_label1 = ctk.CTkLabel(master=login_frame, text="O campo nome de usuário é de carater obrigatório.", text_color="#00FFFF", font=('Roboto', 10)).place(x=45,y=135)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Password", width=300, font = ('Roboto', 14), show="*").place(x=45, y=175)
        user_name_label2 = ctk.CTkLabel(master=login_frame, text="A senha de usuário é de carater obrigatório.", text_color="#00FFFF", font=('Roboto', 10)).place(x=45,y=205)

        login_button = ctk.CTkButton(login_frame, text="Login", width=300, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD').place(x=45, y=250)
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
            nome_cadastro = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Digite seu nome completo", width=300, font = ('Roboto', 14)).place(x=45, y=110)

            #entrada de dados email cadastro
            label = ctk.CTkLabel(master=cadastro_frame, text="Email", font = ('Roboto', 15), text_color= ('white') )
            label.place(x=45, y=140)
            email_cadastro = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Digite seu email", width=300, font = ('Roboto', 14)).place(x=45, y=170)

            #entrada de dados senha cadastro
            label = ctk.CTkLabel(master=cadastro_frame, text="Senha", font = ('Roboto', 15), text_color= ('white') )
            label.place(x=45, y=200)
            senha_cadastro = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Digite sua senha", width=300, font = ('Roboto', 14)).place(x=45, y=230)

            #entrada de dados turma cadastro          
            label = ctk.CTkLabel(master=cadastro_frame, text="Turma", font = ('Roboto', 15), text_color= ('white'))
            label.place(x=45, y=260)
            options_turma = ["Opção 1", "Opção 2", "Opção 3"]
            variable = tk.StringVar(cadastro_frame)
            variable.set(options_turma[0])
            opt_menu = tk.OptionMenu(cadastro_frame, variable, *options_turma).place(x=55, y=365)

            #entrada de dados time cadastro          
            label = ctk.CTkLabel(master=cadastro_frame, text="Time", font = ('Roboto', 15), text_color= ('white'))
            label.place(x=45, y=320)
            options_turma = ["Opção 1", "Opção 2", "Opção 3"]
            variable = tk.StringVar(cadastro_frame)
            variable.set(options_turma[0])
            opt_menu = tk.OptionMenu(cadastro_frame, variable, *options_turma).place(x=55, y=430)
            

            def back():
                cadastro_frame.pack_forget()
                #devolvendo o frame de login
                login_frame.pack(side=RIGHT)
                pass

            voltar = ctk.CTkButton(cadastro_frame, text="Voltar", width=150, fg_color="gray", font = ('Roboto', 14), cursor="hand2", hover_color='#202020', command=back).place(x=45, y=380)
            cadastrar_button = ctk.CTkButton(cadastro_frame, text="Cadastrar", width=150, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD').place(x=220, y=380)
            pass
            #voltar_button = ctk.CTkButton(cadastro_frame, text="Voltar", width=100, text_color='black', fg_color="#00FFFF", font = ('Roboto', 14, 'bold'), cursor="hand2", hover_color='#2FCDCD').place(x=45, y=250)
        cadastro_button = ctk.CTkButton(login_frame, text="Novo por aqui?",font =('Roboto', 14), command=tela_cadastro, text_color=('black'), cursor="hand2", fg_color='#00FFFF', hover_color='#2FCDCD').place(x=120, y=350)
        pass
        #para mudar a cor do botão no ctk fg_color - hover_color

Application()