import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from PIL import Image
import json

janela = ctk.CTk()

class tela_dash:
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        janela.mainloop()


    def tema(self):
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("dark-blue") 
    

    def tela(self):    
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        x = (screen_width - 1500) // 2
        y = (screen_height - 650) // 2
        janela.geometry("1200x650+{}+{}".format(x, y))

        img= ctk.CTkImage(dark_image=Image.open("btspadrao/logo_insight.png"),size=(230,140))
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=980, y=10)

        janela.title("btspadrao/Insight 360º")
        janela.iconbitmap("btspadrao/logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela  


    def mostra_media_time():

        with open("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)
        
        global idturma, idtime, sprint
        idturma = "123"
        idtime = "3"
        sprint ="1"
        
        resposta1 = 0
        resposta2 = 0
        resposta3 = 0
        resposta4 = 0
        resposta5 = 0
        controler = 0

        for i in dados_json['avaliacao']:
            if i['idturma'] == idturma:
                if i['idtime']==idtime:
                        if i['sprint'] == sprint:
                            for x in i['respostas']:
                                    controler += 1
                                    resposta1 += x['resposta1']
                                    resposta2 += x['resposta2']
                                    resposta3 += x['resposta3']
                                    resposta4 += x['resposta4']
                                    resposta5 += x['resposta5']
                    
        #PROCESSAMENTO DE MÉDIAS

        medResp1 = resposta1/controler
        medResp2 = resposta2/controler
        medResp3 = resposta3/controler
        medResp4 = resposta4/controler
        medResp5 = resposta5/controler

        dados = {
            "Comunicação": medResp1,
            "Relação Interpessoal": medResp2,
            "Proatividade": medResp3,
            "Produtividade": medResp4, 
            "Prazos de entrega": medResp5
        }

        indicadores = dados.keys()
        valores = dados.values()
        #Frame 
        media_time_frame = ctk.CTkFrame(master=janela, width=1000, height=650)
        media_time_frame.place(x=0, y=0)
        #Labels
        #label_nome = ctk.CTkLabel(master=media_time_frame, text='Dashboards: Vinicius Domingues Mangaba', font=('Roboto',18, 'bold'), text_color="#00FFFF",).place(x= 300, y= 50)
        metricas = indicadores
        valores = valores
        
        with open ("data_json/questions.json", "r") as arquivo:
            dados_json = json.load(arquivo)        
        
        
        fig, ax = plt.subplots(facecolor='#323232', figsize=(8, 5))
        ax.clear()
        ax.bar(metricas, valores, color="#66FFFF", width=0.3, align='center')
        ax.set_xlabel('', color="white")
        ax.set_ylabel('Valores', color="white")
        ax.set_title('Média de avaliação sobre time geral', color="white")
        ax.set_facecolor('#404040')
        ax.yaxis.set_tick_params(color='white')
        ax.axhline(y=1, color='gray', linestyle='--')
        ax.axhline(y=2, color='gray', linestyle='--')
        ax.axhline(y=3, color='gray', linestyle='--')
        ax.axhline(y=4, color='gray', linestyle='--')
        ax.axhline(y=5, color='gray', linestyle='--')
        
        # Aqui seto as cores das legendas X e Y para branco
        ytick_labels = ax.get_yticklabels()
        for label in ytick_labels:
            label.set_color('white')

        xtick_labels = ax.get_xticklabels()
        for label in xtick_labels:
            label.set_color('white')  

        canvas = FigureCanvasTkAgg(fig, master=media_time_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=200, y=150)

    def mostra_autoavaliacao():
        #Frame 
        idavaliador = "gilvane@email.com"
        with open('data_json/questions.json', "r") as arquivoAuto:
             dados_Auto = json.load(arquivoAuto)
        respostas =[]
        for i in dados_Auto['avaliacao']:
             if i['idAvaliador'] == idavaliador:
                  for x in i['respostas']:
                       if x['idavaliado'] == idavaliador:
                            respostas.append(x['resposta1'])
                            respostas.append(x['resposta2'])
                            respostas.append(x['resposta3'])
                            respostas.append(x['resposta4'])
                            respostas.append(x['resposta5'])

                  
        autoavaliacao_frame = ctk.CTkFrame(master=janela, width=1000, height=650)
        autoavaliacao_frame.place(x=0, y=0)

        #label_nome = ctk.CTkLabel(master=autoavaliacao_frame, text='Dashboards: Vinicius Domingues Mangaba', font=('Roboto',18, 'bold'), text_color="#00FFFF",).place(x= 300, y= 50)
        metricas = ['Comunicação', 'Relacionamento', 'Proatividade', 'Produtividade','Entregas']
        valores = respostas
        
        fig, ax = plt.subplots(facecolor='#323232', figsize=(8, 5))
        ax.clear()
        ax.bar(metricas, valores, color="#66FFFF", width=0.3, align='center')
        ax.set_xlabel('', color="white")
        ax.set_ylabel('Valores', color="white")
        ax.set_title('Autoavaliação', color="white")
        ax.set_facecolor('#404040')
        ax.yaxis.set_tick_params(color='white')
        ax.axhline(y=1, color='gray', linestyle='--')
        ax.axhline(y=2, color='gray', linestyle='--')
        ax.axhline(y=3, color='gray', linestyle='--')
        ax.axhline(y=4, color='gray', linestyle='--')
        ax.axhline(y=5, color='gray', linestyle='--')
    
        # Aqui seto as cores das legendas X e Y para branco
        ytick_labels = ax.get_yticklabels()
        for label in ytick_labels:
            label.set_color('white')

        xtick_labels = ax.get_xticklabels()
        for label in xtick_labels:
            label.set_color('white')  

        canvas = FigureCanvasTkAgg(fig, master=autoavaliacao_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=200, y=150)    


    botaoMediaTime = ctk.CTkButton(master=janela, text= "Média times", command=mostra_media_time, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD' ).place(x=1030, y =150)
    botaoAutoavaliacao = ctk.CTkButton(master=janela, text= "Média times", command=mostra_autoavaliacao, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD' ).place(x=1030, y =200)


tela_dash()