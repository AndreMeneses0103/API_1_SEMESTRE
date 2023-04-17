import json
import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

janela = ctk.CTk()

class tela_cadastro_time:
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_nova_turma()
        janela.mainloop()
    
    def tema(self):
        ctk.set_appearance_mode("dark") #modo dark
        ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
        pass

    def tela(self):    
        janela.geometry("1200x800") #DEFINO O TAMANHO DA JANELA
        janela.title("Cadastro novas turmas")
        janela.iconbitmap("logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
        pass

    def tela_nova_turma(self):
        #trabalhando com a imagem da tela
        img = PhotoImage(file="logo_insight.png").subsample(3) # reduzindo o tamanho em 50%
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=10, y=10)
        label_tt = ctk.CTkLabel(master=janela, text='Administrador', font=('Roboto',18, 'bold'), text_color="#00FFFF").place(x=50, y=130)

        
        #frame a direita
        tela_cadastro_frame = ctk.CTkFrame(master=janela, width=900, height=1000)
        tela_cadastro_frame.pack(side=RIGHT)

        #frame widgets
        label = ctk.CTkLabel(master=tela_cadastro_frame, text="Cadastro de turmas e times", font = ('Roboto', 25, 'bold'), text_color= ('white') )
        label.place(x=45, y=40)

        #entrada de dados
        user_name_label1 = ctk.CTkLabel(master=tela_cadastro_frame, text="Nova turma: ", text_color="white", font=('Roboto', 14)).place(x=45,y=100)
        novaturma = tk.StringVar()#criação da variavel 
        novaturma_entry = ctk.CTkEntry(master=tela_cadastro_frame, placeholder_text="Nova turma", width=600, font = ('Roboto', 14), textvariable=novaturma).place(x=45, y=125)

        confirma_nova_turma = ctk.StringVar()#criação da variavel 
        user_name_label2 = ctk.CTkLabel(master=tela_cadastro_frame, text="Confirme nova turma:", text_color="white", font=('Roboto', 14)).place(x=45,y=160)
        confirma_nova_turma_entry = ctk.CTkEntry(master=tela_cadastro_frame, placeholder_text="Confirme nova turma:", width=600, font = ('Roboto', 14), textvariable=confirma_nova_turma).place(x=45, y=185)
       
        def verifica_turma():
                #verificação das variaveis
            if novaturma.get() == confirma_nova_turma.get():
                aviso_validado = ctk.CTkLabel(master=tela_cadastro_frame, text="Nova turma cadastrada!", text_color="#00FFFF", font=('Roboto', 18)).place(x=45,y=220)
            else:
                aviso_negado = ctk.CTkLabel(master=tela_cadastro_frame, text="Os campos não podem ser diferentes.", text_color="#00FFFF", font=('Roboto', 18)).place(x=45,y=220)
                pass
        
        botao_verifica = ctk.CTkButton(tela_cadastro_frame, text="Verificar",font =('Roboto', 14), command=verifica_turma, text_color=('black'), cursor="hand2", fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=230)

        quantidade_sprints_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Qtidade de sprints: ", text_color="white", font=('Roboto', 14)).place(x=45,y=260)
        quantidade_sprints = tk.IntVar()
        quantidade_sprints_entry = ctk.CTkEntry(master=tela_cadastro_frame, placeholder_text="Qtidade de sprints:", width=60, font = ('Roboto', 14), textvariable=quantidade_sprints).place(x=45,y=290)

        def define_numero_sprints():
            # Cria uma variável StringVar() para armazenar a opção selecionada
            var = tk.StringVar()

            num_valores = int(quantidade_sprints.get())
            sprints = [str(i) for i in range(1, num_valores+1)]
            combobox = tk.Combobox(tela_cadastro_frame, texvariable=var)
            combobox.config(width=15)
            combobox.pack()
            combobox.place(x=500,y=450)

            inicio_sprint = DateEntry(width=10, font=("Roboto", 8), background='#00FFFF', foreground='black', borderwidth=2)
            inicio_sprint.pack(pady=70, padx=100)
            inicio_sprint.place(x= 380, y= 450)
            data_seleciona_inicio = inicio_sprint.get_date()

            fim_sprint = DateEntry(width=10, font=("Roboto", 8), background='#00FFFF', foreground='black', borderwidth=2)
            fim_sprint.pack(pady=70, padx=100)
            fim_sprint.place(x=480, y=450)
            data_seleciona_fim = fim_sprint.get_date()

            botao = ctk.CTkButton(master=tela_cadastro_frame, text="OK", command=imprimir_data, text_color=('black'),cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=120, y=390)
            # combobox variável de acordo com o número de sprints
            
            pass
        
        botao_define_sprint = ctk.CTkButton(master=tela_cadastro_frame, text="Confirmar", font = ('Roboto', 14), command = define_numero_sprints, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=120, y=290)

        def imprimir_data():
            data = inicio_sprint.get_date()
            print("Data selecionada:", data)

        
        

tela_cadastro_time()