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

janelaDashComp = ctk.CTk()

class tela_dashboard_operacional:
    def __init__(self):
        self.janela=janelaDashComp
        self.tema()
        self.tela()
        janelaDashComp.mainloop()
    

    def tema(self):
        ctk.set_appearance_mode("dark") #modo dark
        ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
    

    def tela(self):    
        screen_width = janelaDashComp.winfo_screenwidth()
        screen_height = janelaDashComp.winfo_screenheight()
        x = (screen_width - 1500) // 2
        y = (screen_height - 650) // 2
        janelaDashComp.geometry("1200x650+{}+{}".format(x, y))

        img= ctk.CTkImage(dark_image=Image.open("logo_insight.png"),size=(230,140))
        label_img = ctk.CTkLabel(master=janelaDashComp, image=img, text='')
        label_img.place(x=980, y=10)


        janelaDashComp.title("Insight 360º")
        janelaDashComp.iconbitmap("logo_insight.ico")
        janelaDashComp.resizable(False, False) #defino que o usuário não pode redimensionar a tela  

    def telaDash():
        comp_frame = ctk.CTkFrame(master=janelaDashComp, width=1000, height=650)
        comp_frame.place(x=0, y=0)
        
        with open ("data_json/questions.json", "r") as arquivo:
            dados_json = json.load(arquivo)

        #MÉDIA DO INTEGRANTE
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

        #DADOS DO INTEGRANTE
        dados2 = {
            "Comunicação": medResp1,
            "Relação Interpessoal": medResp2,
            "Proatividade": medResp3,
            "Produtividade": medResp4, 
            "Prazos de entrega": medResp5
        }
        #DADOS DO TIME
        dados1 = {
            "Comunicação": 4,
            "Relação Interpessoal": 2,
            "Proatividade": 3,
            "Produtividade": 5, 
            "Prazos de entrega": 1
        }

        indicadores = dados1.keys()
        valores1 = dados1.values()
        valores2 = dados2.values()

        print(indicadores)
        print(valores1)
        print(valores2)
    
        figura = Figure(figsize=(8,5), dpi=100)
        eixo = figura.add_subplot(111)

        eixo.plot(indicadores, valores1, color="#c8c8c8", label = "Time")    
        eixo.plot(valores2, color="#00FFFF", label = "Você")
        eixo.set_title("Análise comparativa entre você e o time", color="white")
        eixo.set_facecolor("#404040")
        figura.set_facecolor("#323232")
        eixo.legend()
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

        canvas = FigureCanvasTkAgg(figura, master=comp_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=100)

    botaoMediaTime = ctk.CTkButton(master=janelaDashComp, text= "Média times", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD' ).place(x=1030, y =150)
    botaoMediaInt = ctk.CTkButton(master=janelaDashComp, text= "Média sobre Você", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=1030, y =200)
    botaoComp = ctk.CTkButton(master=janelaDashComp, text= "Análise Comparativa", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=telaDash).place(x=1030, y =250)

tela_dashboard_operacional()