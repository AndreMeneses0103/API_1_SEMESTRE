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
    

    def tela(self):    
        janela.geometry("1200x800") #DEFINO O TAMANHO DA JANELA
        janela.title("Cadastro novas turmas")
        janela.iconbitmap("logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela  


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
        label = ctk.CTkLabel(master=tela_cadastro_frame, text="Cadastro de nova turma", font = ('Roboto', 25, 'bold'), text_color= ('white') ).place(x=45, y=40)
        
        #entrada de dados
        user_name_label1 = ctk.CTkLabel(master=tela_cadastro_frame, text="Nome da turma: ", text_color="white", font=('Roboto', 14)).place(x=45,y=100)
        novaturma = tk.StringVar()#criação da variavel 
        novaturma_entry = ctk.CTkEntry(master=tela_cadastro_frame, placeholder_text="Nova turma", width=600, font = ('Roboto', 14), textvariable=novaturma).place(x=45, y=125)

        quantidade_sprints_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Número de sprints: ", text_color="white", font=('Roboto', 14)).place(x=45,y=175)
        quantidade_sprints = tk.IntVar()
        quantidade_sprints_entry = ctk.CTkEntry(master=tela_cadastro_frame, placeholder_text="Número de sprints:", width=60, font = ('Roboto', 14), textvariable=quantidade_sprints).place(x=45,y=200)


        def define_numero_sprints():

            valor_sprint = tk.StringVar(tela_cadastro_frame)
            num_valores = int(quantidade_sprints.get())
            sprints = [str(i) for i in range(1, num_valores+1)]
            opcoes_time = tk.OptionMenu(tela_cadastro_frame, valor_sprint, *sprints).place(x=50,y=380)

            titulo_periodo_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Período das sprints", text_color="white", font=('Roboto', 25, 'bold')).place(x=45,y=270)
            numero_sprints_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Escolha a sprint", text_color="white", font=('Roboto', 14)).place(x=45,y=320)

            inicio_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Início da sprint", text_color="white", font=('Roboto', 14)).place(x=350,y=320)
            inicio_sprint = DateEntry(master=tela_cadastro_frame, width=10, font=("Roboto", 8), background='#00FFFF', foreground='black', borderwidth=2)
            inicio_sprint.place(x= 350, y= 380)
            data_seleciona_inicio = inicio_sprint.get_date()

            fim_sprint_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Fim da sprint", text_color="white", font=('Roboto', 14)).place(x=550,y=320)
            fim_sprint = DateEntry(master=tela_cadastro_frame,width=10, font=("Roboto", 8), background='#00FFFF', foreground='black', borderwidth=2)
            fim_sprint.place(x=550, y=380)
            data_seleciona_fim = fim_sprint.get_date()
            #Esse botão vai pegar Sprint e datas e salvar em JSOn
            botao = ctk.CTkButton(master=tela_cadastro_frame, text="OK", text_color=('black'),cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=450)
            
            botao_proxima_etapa = ctk.CTkButton(master=tela_cadastro_frame, text="Próxima etapa", command=tela_cadastro_time, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=600)
            
               
        botao_define_sprint = ctk.CTkButton(master=tela_cadastro_frame, text="Confirmar", font = ('Roboto', 14), command = define_numero_sprints, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=200)
    

        def tela_cadastro_time():
            #Apaga o frame de cadastro de turmas
            tela_cadastro_frame.pack_forget()

            #frame a direita
            tela_times_frame = ctk.CTkFrame(master=janela, width=900, height=1000)
            tela_times_frame.pack(side=RIGHT)

            #criar novos times
            label_novos_times = ctk.CTkLabel(master=tela_times_frame, text="Cadastro de novos times", font = ('Roboto', 25, 'bold'), text_color= ('white') ).place(x=45, y=40)
            label_num_times = ctk.CTkLabel(master=tela_times_frame, text="Defina o número de times", font = ('Roboto', 14), text_color= ('white') ).place(x=45, y=100)

            #define quantidade de times


            def tela_cadastro_time():
                # Apaga o frame de cadastro de turmas
                tela_cadastro_frame.pack_forget()

                # frame a direita
                tela_times_frame = ctk.CTkFrame(master=janela, width=900, height=1000)
                tela_times_frame.pack(side=RIGHT)

                # criar novos times
                label_novos_times = ctk.CTkLabel(master=tela_times_frame, text="Cadastro de novos times", font=('Roboto', 25, 'bold'), text_color=('white')).place(x=45, y=40)
                label_num_times = ctk.CTkLabel(master=tela_times_frame, text="Defina o número de times", font=('Roboto', 14), text_color=('white')).place(x=45, y=100)

                # define quantidade de times
                num_times = tk.IntVar()
                num_times_entry = ctk.CTkEntry(master=tela_times_frame, placeholder_text="Número de times:", width=60, font=('Roboto', 14), textvariable=num_times).place(x=45, y=180)
                
                #def cria_novos_times():
                numero_times = int(num_times.get())
                lista_times = list(range(1, numero_times+1))
                print(lista_times)

            num_times_botao = ctk.CTkButton(master=tela_times_frame, text="OK", font=('Roboto', 14), text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=150, y=240)


tela_cadastro_time()