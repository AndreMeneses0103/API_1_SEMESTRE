import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from PIL import Image

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

        img= ctk.CTkImage(dark_image=Image.open("logo_insight.png"),size=(230,140))
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=980, y=10)

        janela.title("Insight 360º")
        janela.iconbitmap("logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela  


    def mostra_media_time():
        #Frame 
        media_time_frame = ctk.CTkFrame(master=janela, width=1000, height=650)
        media_time_frame.place(x=0, y=0)
        #Labels
        label_nome = ctk.CTkLabel(master=media_time_frame, text='Dashboards: Vinicius Domingues Mangaba', font=('Roboto',18, 'bold'), text_color="#00FFFF",).place(x= 300, y= 50)
        metricas = ['Comunicação', 'Relacionamento', 'Proatividade', 'Produtividade','Entregas']
        valores = [5, 5, 4, 3, 4]
        
        fig, ax = plt.subplots(facecolor='#323232', figsize=(8, 5))
        ax.clear()
        ax.bar(metricas, valores, color="#66FFFF", width=0.3, align='center')
        ax.set_xlabel('', color="white")
        ax.set_ylabel('Valores', color="white")
        ax.set_title('Média de avaliação sobre time geral', color="white")
        ax.set_facecolor('#404040')
        ax.yaxis.set_tick_params(color='white')
        
        # Aqui seto as cores das legendas X e Y para branco
        ytick_labels = ax.get_yticklabels()
        for label in ytick_labels:
            label.set_color('white')

        xtick_labels = ax.get_xticklabels()
        for label in xtick_labels:
            label.set_color('white')  

        canvas = FigureCanvasTkAgg(fig, master=media_time_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=100)
    


    botaoMediaTime = ctk.CTkButton(master=janela, text= "Média times", command=mostra_media_time, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD' ).place(x=1030, y =150)


tela_dash()