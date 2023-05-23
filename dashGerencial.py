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
import matplotlib.pyplot as plt

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

        frameTurmaTime = ctk.CTkFrame(master=janelaDashGerencial, width=150, height=150, fg_color="#4f4f4f").place(x=20, y=55)
        frameQuant = ctk.CTkFrame(master=janelaDashGerencial, width=150, height=100, fg_color="#4f4f4f").place(x=20, y=215)
        frameSprint = ctk.CTkFrame(master=janelaDashGerencial, width=150, height=100, fg_color="#4f4f4f").place(x=20, y=325)
        frameLegenda = ctk.CTkFrame(master=janelaDashGerencial, width=150, height=150, fg_color="#4f4f4f").place(x=20, y=435)


        
        label_turma_time = ctk.CTkLabel(master=frameTurmaTime, text="Turma:\n\n\nTime:", font=('Roboto', 15, "bold"), fg_color="#4f4f4f").place(x=65, y=75)
        labelQuant = ctk.CTkLabel(master=frameQuant, text="Quant. Integrantes:\n", font=('Roboto', 15, 'bold'), fg_color="#4f4f4f").place(x=25, y=230)
        labelSprint = ctk.CTkLabel(master=frameSprint, text="Sprint:\n", font=('Roboto', 15, 'bold'), fg_color="#4f4f4f").place(x=70, y=345)
        labelLegenda = ctk.CTkLabel(master=frameLegenda, text="Legenda:\n1 - Muito Ruim\n2 - Ruim\n3 - Regular\n4 - Bom\n5 - Muito bom", font=('Roboto', 15), fg_color="#4f4f4f").place(x=45, y=453)
        
        labelEscrito  = ctk.CTkLabel(master=janelaDashGerencial, text="Dashboard Gerencial", font=("Roboto", 30, 'bold'), text_color="#00FFFF").place(x=450, y=40)


    def dashQuantRespostas():

        frameDashRespost = ctk.CTkFrame(master=janelaDashGerencial, width=600, height=400). place(x=300, y=130)

        with open('data_json/users.json', "r") as arquivoUser:
            dados_user = json.load(arquivoUser)
        

        with open('data_json/questions.json', 'r') as arquivoQuestions:
            dados_questions = json.load(arquivoQuestions)

        idturmaUser = "123"
        idtimeUser = "3"
        quantIntegrantes = 0
        quantRespostas = 0


        for idturmajson in dados_user['usuarios']:
            if idturmaUser == idturmajson['idturma'] and idtimeUser == idturmajson['idtime']:
                quantIntegrantes+=1
                for idusuario in dados_questions['avaliacao']:
                    if idusuario['idturma'] == idturmajson['idturma'] and idusuario['idtime'] == idturmajson['idtime'] and idusuario['idAvaliador'] == idturmajson['id']:
                        quantRespostas +=1

        #conferindo
        print(quantIntegrantes, "\n", quantRespostas)  
        figura = Figure(figsize=(8, 5), dpi=100)
        labels = ['Categoria 1', 'Categoria 2',]

        sizes = [quantIntegrantes, quantRespostas]
        colors = ['#7fdbda', '#94d3a2', '#5eb9b7']

        figura, ax = plt.subplots()
    
    # Criar o gráfico de pizza
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
        ax.axis('equal')  # Assegura que o gráfico é desenhado como um círculo
        
        # Mostrar o gráfico na janela
       

        ax.set_facecolor("#404040")
        figura.set_facecolor("#323232")
        ytick_labels = ax.get_yticklabels()
        for label in ytick_labels:
            label.set_color('white')

        xtick_labels = ax.get_xticklabels()
        for label in xtick_labels:
            label.set_color('white') 
      
        canvas = FigureCanvasTkAgg(figura, master=frameDashRespost)
        canvas.draw()

        ax.set_title('Quantidade de respostas do time', color='white')

        # Exibição do gráfico na janela do Tkinter
        canvas.get_tk_widget().place(x=100, y=100)
     

    pass
    dashQuantRespostas()
    botaoQuantResp = ctk.CTkButton(master=janelaDashGerencial, text= "Quantidade Respostas", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD' ).place(x=1030, y =150)
    botaoMediaTime = ctk.CTkButton(master=janelaDashGerencial, text= "Média turmas", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=1030, y =200)
    botaoAutoAv = ctk.CTkButton(master=janelaDashGerencial, text= "Média times", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=1030, y =250)
    botaoMediaInt = ctk.CTkButton(master=janelaDashGerencial, text= "Análise Comparativa", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=1030, y =300)
    botaoAnalise = ctk.CTkButton(master=janelaDashGerencial, text= "Voltar", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=1030, y =350)
     


tela_dashboard_Gerencial()