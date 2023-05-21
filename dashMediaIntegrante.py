import customtkinter as ctk
import json
import matplotlib
matplotlib.use('TkAgg') #INFORMA QUAL BACK-END MAT.. USARÁ - INTEGRA O TK COM O MAT
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from PIL import Image


janelaDashOp = ctk.CTk()

class tela_dashboard_operacional:
    def __init__(self):
        self.janela=janelaDashOp
        self.tema()
        self.tela()
        janelaDashOp.mainloop()
    

    def tema(self):
        ctk.set_appearance_mode("dark") #modo dark
        ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
    

    def tela(self):    
        screen_width = janelaDashOp.winfo_screenwidth()
        screen_height = janelaDashOp.winfo_screenheight()
        x = (screen_width - 1500) // 2
        y = (screen_height - 650) // 2
        janelaDashOp.geometry("1200x650+{}+{}".format(x, y))

        img= ctk.CTkImage(dark_image=Image.open("logo_insight.png"),size=(230,140))
        label_img = ctk.CTkLabel(master=janelaDashOp, image=img, text='')
        label_img.place(x=980, y=10)


        janelaDashOp.title("Insight 360º")
        janelaDashOp.iconbitmap("logo_insight.ico")
        janelaDashOp.resizable(False, False) #defino que o usuário não pode redimensionar a tela  

    def telaDash():


        media_time_frame = ctk.CTkFrame(master=janelaDashOp, width=1000, height=650)
        media_time_frame.place(x=0, y=0)
        with open("data_json/questions.json", "r") as arquivo:
            dados_json = json.load(arquivo)
        
        idturma = "123"
        idtime = "3"
        idavaliado = "gui@gmail.com"
        resposta1 = 0
        resposta2 = 0
        resposta3 = 0
        resposta4 = 0
        resposta5 = 0
        controler = 0

        for i in dados_json['avaliacao']:
            if i['idturma'] == idturma:
                if i['idtime']==idtime:
                    controler += 1
                    for x in i['respostas']:
                        if x['idavaliado']== idavaliado:
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
        figura = Figure(figsize=(8, 5), dpi=100)
        eixo = figura.add_subplot(111)
        cor_texto = "#fff"
        # Plotagem do gráfico de barras
        barras = eixo.bar(indicadores, valores, color="#00FFFF", width=0.3)
        eixo.set_facecolor("#404040")
        figura.set_facecolor("#323232")
        # Criação do objeto FigureCanvasTkAgg
        eixo.set_ylabel('Pontuação', color=cor_texto)


        ytick_labels = eixo.get_yticklabels()
        for label in ytick_labels:
            label.set_color('white')

        xtick_labels = eixo.get_xticklabels()
        for label in xtick_labels:
            label.set_color('white') 
        
        canvas = FigureCanvasTkAgg(figura, master=media_time_frame)
        canvas.draw()

        eixo.set_title('Média do time sobre você', color=cor_texto)

        # Exibição do gráfico na janela do Tkinter
        canvas.get_tk_widget().place(x=100, y=100)


        pass

    botaoMediaTime = ctk.CTkButton(master=janelaDashOp, text= "Média times", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD' ).place(x=1030, y =150)
    botaoMediaInt = ctk.CTkButton(master=janelaDashOp, text= "Média sobre Você", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=telaDash).place(x=1030, y =200)

tela_dashboard_operacional()