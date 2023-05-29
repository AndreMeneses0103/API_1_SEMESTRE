import customtkinter as ctk
import json
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg') #INFORMA QUAL BACK-END MAT.. USARÁ - INTEGRA O TK COM O MAT
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from PIL import Image


janelaDash = ctk.CTk()

class tela_dashboard_operacional:
    def __init__(self):
        self.janela=janelaDash
        self.tema()
        self.tela()
        janelaDash.mainloop()
    

    def tema(self):
        ctk.set_appearance_mode("dark") #modo dark
        ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
    

    def tela(self):    
            screen_width = janelaDash.winfo_screenwidth()
            screen_height = janelaDash.winfo_screenheight()
            x = (screen_width - 1200) // 2
            y = (screen_height - 650) // 2
            janelaDash.geometry("1200x650+{}+{}".format(x, y))

    def telaDashMediaInt():
            

            media_time_frame = ctk.CTkFrame(master=janelaDash, width=800, height=650)
            media_time_frame.place(x=200, y=20)
            with open("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)
            
            idturma = "123"
            resposta1 = 0
            resposta2 = 0
            resposta3 = 0
            resposta4 = 0
            resposta5 = 0
            controler = 0

            for i in dados_json['avaliacao']:
                if i['idturma'] == idturma:
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
        # Criação da figura e do eixo
            figura = Figure(figsize=(8, 6), dpi=100)
            eixo = figura.add_subplot(111)
            cor_texto = "#fff"
            # Plotagem do gráfico de barras
            barras = eixo.bar(indicadores, valores, color="#00FFFF", width=0.3)
            eixo.set_facecolor("#404040")
            figura.set_facecolor("#323232")
            # Criação do objeto FigureCanvasTkAgg
            eixo.set_ylabel('Pontuação', color=cor_texto)

            eixo.axhline(y=1, color='gray', linestyle='--')
            eixo.axhline(y=2, color='gray', linestyle='--')
            eixo.axhline(y=3, color='gray', linestyle='--')
            eixo.axhline(y=4, color='gray', linestyle='--')
            eixo.axhline(y=5, color='gray', linestyle='--')

            ytick_labels = eixo.get_yticklabels()
            for label in ytick_labels:
                label.set_color('white')

            xtick_labels = eixo.get_xticklabels()
            for label in xtick_labels:
                label.set_color('white') 
            
            canvas = FigureCanvasTkAgg(figura, master=media_time_frame)
            canvas.draw()

            eixo.set_title('Média da turma', color=cor_texto)

            # Exibição do gráfico na janela do Tkinter
            canvas.get_tk_widget().place(x=100, y=100)
            pass

    botaoAnalise = ctk.CTkButton(master=janelaDash, text= "Média Turma", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=telaDashMediaInt).place(x=1030, y =350)

tela_dashboard_operacional()