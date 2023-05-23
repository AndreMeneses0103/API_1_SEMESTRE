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

janelaDashGerencial = ctk.CTk()

class tela_dashboard_Gerencial:
    def __init__(self):
        self.janela=janelaDashGerencial
        self.tema()
        self.tela()
        janelaDashGerencial.mainloop()
    

    def tema(self):
        ctk.set_appearance_mode("dark") #modo dark
        ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
    

    def tela(self):    
        screen_width = janelaDashGerencial.winfo_screenwidth()
        screen_height = janelaDashGerencial.winfo_screenheight()
        x = (screen_width - 1500) // 2
        y = (screen_height - 650) // 2
        janelaDashGerencial.geometry("1200x650+{}+{}".format(x, y))

        img= ctk.CTkImage(dark_image=Image.open("logo_insight.png"),size=(230,140))
        label_img = ctk.CTkLabel(master=janelaDashGerencial, image=img, text='')
        label_img.place(x=980, y=10)


        janelaDashGerencial.title("Insight 360º")
        janelaDashGerencial.iconbitmap("logo_insight.ico")
        janelaDashGerencial.resizable(False, False) #defino que o usuário não pode redimensionar a tela  

        frameTurmaTime = ctk.CTkFrame(master=janelaDashGerencial, width=150, height=150, fg_color="#4f4f4f").place(x=20, y=20)
        frameQuant = ctk.CTkFrame(master=janelaDashGerencial, width=150, height=100, fg_color="#4f4f4f").place(x=20, y=180)
        frameSprint = ctk.CTkFrame(master=janelaDashGerencial, width=150, height=100, fg_color="#4f4f4f").place(x=20, y=290)
        frameLegenda = ctk.CTkFrame(master=janelaDashGerencial, width=150, height=150, fg_color="#4f4f4f").place(x=20, y=400)


        
        label_turma_time = ctk.CTkLabel(master=frameTurmaTime, text="Turma:\n\n\nTime:", font=('Roboto', 15, "bold"), fg_color="#4f4f4f").place(x=65, y=40)
        labelLegenda = ctk.CTkLabel(master=frameLegenda, text="Legenda:\n1 - Muito Ruim\n2 - Ruim\n3 - Regular\n4 - Bom\n5 - Muito bom", font=('Roboto', 15), fg_color="#4f4f4f").place(x=45, y=418)
       # labelQuant = ctk.CTkLabel(master=frameQuant, text="Quant. Integrantes:", font=('Roboto', 13), fg_color="#4f4f4f").place(x=25, y=190)



tela_dashboard_Gerencial()