import json
import tkinter as tk
import customtkinter as ctk
from tkinter import *


avaliador = input("Digite o nome do avaliador: ")
avaliados = []
avaliados.append(avaliador)
r = "S"
while r == "S":
    avaliados.append(input("Digite o nome do integrante do grupo: "))
    r = input("Deseja adicionar mais um participante S - SIM N - NÃO: ")

janela = ctk.CTk()

#CRIEI CLASSE AVALIAÇÃO
class Avaliação:
    #função principal que chama todas as outras
    def __init__(self):
        self.tela()
        self.tema()
        self.tela_avaliação()
        janela.mainloop()  
        pass

    #configarações de tela
    def tela(self):    
        janela.geometry("1500x700") #DEFINO O TAMANHO DA JANELA
        janela.title("Sistema de login")
        janela.iconbitmap("logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
        pass

    #definição do modo dark
    def tema(self):
        ctk.set_appearance_mode("dark") #modo dark
        ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
        pass
    
    def tela_avaliação(self):
        img = PhotoImage(file="logo_insight.png").subsample(2) # reduzindo o tamanho em 50%
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=20, y=20)

        nome = avaliador
        sprint = "Sprint 1"
        label_nome_usuario = ctk.CTkLabel(master=janela, text=nome, font=('Roboto', 20, 'bold')).place(x=50, y=150)
        label_sprint = ctk.CTkLabel(master=janela, text=sprint, font=('Roboto', 20, 'bold')).place(x=50, y=190)



        label_autoavaliacao = ctk.CTkLabel(master=janela, text='Autoavaliação', font=('Roboto', 25, 'bold')).place(x=50, y=260)
        label_autoavaliacao = ctk.CTkLabel(master=janela, text='Integrante para integrante', font=('Roboto', 25, 'bold'), text_color='gray').place(x=50, y=300)

        button_voltar = ctk.CTkButton(janela, width=200, fg_color='#5CE1E6', text_color='black', hover_color='#00FFFF', text='Tela Inicial', font = ('Roboto', 20), cursor="hand2").place(x=90, y=400)

        #CRIAÇÃO DO FRAME PERGUNTAS
        perguntas_frame = ctk.CTkFrame(master=janela, width=1100, height=700)
        perguntas_frame.pack(side=RIGHT)
      
        for i in range(len(avaliados)):
            verificacao = 1
            while verificacao == 1: 
                
                avaliado = avaliados[i]
                titulo_pergunta = ctk.CTkLabel(master=perguntas_frame, text='Avaliado: '+avaliado, font=('Roboto', 30, 'bold'), text_color='#5CE1E6').place(x=300, y=20)
                
                def questionario():
                        perguntas = ['Como você avalia sua comunicação com o grupo durante essa Sprint?',
                                    'Como você avalia o seu trabalho em equipe durante essa Sprint?',
                                    'Como você avalia sua proatividade durante essa Sprint?',
                                    'Como você avalia sua proatividade durante essa Sprint?',
                                    'Como você avalia sua entrega com relação ao prazo do projeto nessa Sprint?'                        
                                    ]   
                        metricas = ['Muito Ruim', 'Ruim', 'Regular', 'Bom', 'Muito Bom']
                        y_direcao_tela = 0
                        x_direcao_tela = 50
                        y_direcao_tela_resposta = 160
                        for linha in range(len(perguntas)):
                            y_direcao_tela += 90
                            label_pergunta = ctk.CTkLabel(master=perguntas_frame, text=perguntas[linha], font=('Roboto', 18)).place(x=50, y=y_direcao_tela)
                            
                            x_direcao_tela_perguntas = 80
                            
                            for i in range (len(metricas)):
                                #resolver problema de seleção do radioButton - acredito que as resposta terão que ser guardadas numa lista JSON
                                var = tk.StringVar()
                                checkbutton_respostas = tk.Radiobutton(perguntas_frame, text=metricas[i], font=('Roboto', 18), variable=var, background='#212121', foreground='white').place(x=x_direcao_tela_perguntas, y=y_direcao_tela_resposta)
                                x_direcao_tela_perguntas += 200
                            y_direcao_tela_resposta +=110
                        def validar_pergunta():
                            verificacao = 0
                            pass
                        button_proximo = ctk.CTkButton(perguntas_frame, text='Próximo', font=('Roboto', 20, 'bold'), fg_color='#5CE1E6', text_color='black', cursor="hand2", width=230, command=validar_pergunta).place(x=600, y=550)
                questionario()   

                    
                 
            pass
       

#INSTANCIEI (CHAMEI) A CLASSE AVALIAÇÃO
Avaliação()