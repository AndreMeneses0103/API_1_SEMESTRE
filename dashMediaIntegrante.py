import customtkinter as ctk
import json
import matplotlib
matplotlib.use('TkAgg') #INFORMA QUAL BACK-END MAT.. USARÁ - INTEGRA O TK COM O MAT
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


janelaDashOp = ctk.CTk()

class tela_dashboard_operacional:
    def __init__(self):
        self.janela=janelaDashOp
        self.tema()
        self.tela()
        self.telaDash()
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


        janelaDashOp.title("Insight 360º")
        janelaDashOp.iconbitmap("logo_insight.ico")
        janelaDashOp.resizable(False, False) #defino que o usuário não pode redimensionar a tela  

    def telaDash(self):

        dados = {
            "Comunicação": 4,
            "Relação Interpessoal": 3,
            "Proatividade": 2,
            "Produtividade": 5, 
            "Prazos de entrega": 2
        }

        indicadores = dados.keys()
        valores = dados.values()
      # Criação da figura e do eixo
        figura = Figure(figsize=(10, 6), dpi=100)
        eixo = figura.add_subplot(111)
        cor_texto = "#fff"
        # Plotagem do gráfico de barras
        barras = eixo.bar(indicadores, valores, color="#00FFFF", width=0.5)
        eixo.set_facecolor("#242424")
        figura.set_facecolor("#242424")
        # Criação do objeto FigureCanvasTkAgg
        eixo.set_xlabel("Indicadores",color=cor_texto)
        eixo.set_ylabel('Pontuação', color=cor_texto)

        
        canvas = FigureCanvasTkAgg(figura, master=janelaDashOp)
        canvas.draw()

        eixo.set_title('Média do time sobre você', color=cor_texto)

        # Exibição do gráfico na janela do Tkinter
        canvas.get_tk_widget().place(x=230, y=30)


        pass
tela_dashboard_operacional()