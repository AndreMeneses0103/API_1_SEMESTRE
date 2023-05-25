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
 
    
        img= ctk.CTkImage(dark_image=Image.open("logo_insight.png"),size=(230,140))
        label_img = ctk.CTkLabel(master=janelaDash, image=img, text='')
        label_img.place(x=980, y=10)


        janelaDash.title("Insight 360º")
        janelaDash.iconbitmap("logo_insight.ico")
        janelaDash.resizable(False, False) #defino que o usuário não pode redimensionar a tela  

    def telaDashMediaInt():
        

        media_time_frame = ctk.CTkFrame(master=janelaDash, width=800, height=650)
        media_time_frame.place(x=200, y=20)
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
        figura = Figure(figsize=(6, 4), dpi=100)
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

        eixo.set_title('Média do time sobre você', color=cor_texto)

        # Exibição do gráfico na janela do Tkinter
        canvas.get_tk_widget().place(x=100, y=100)
        pass



    def telaDashAnalise():
        comp_frame = ctk.CTkFrame(master=janelaDash, width=800, height=650)
        comp_frame.place(x=200, y=20)
        
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
    
        figura = Figure(figsize=(6, 4), dpi=100)
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

    def mostrar_total_respostas():
        with open('data_json/questions.json', 'r') as arquivo:
            dados_json_questions = json.load(arquivo)

        with open('data_json/users.json', 'r') as arquivou:
            dados_json_users = json.load(arquivou)

        idturma = "123"
        idtime = "3"
        qnt_turma = 0
        qnt_resp = 0 
        for idturmajson in dados_json_users['usuarios']:
            if idturmajson['idturma'] == idturma:
                if idturmajson['idtime'] == idtime:
                    qnt_turma += 1 

        for idturmajson in dados_json_questions['avaliacao']:
            if idturmajson['idturma'] == idturma:
                if idturmajson['idtime'] == idtime:
                    qnt_resp += 1 

        #Processamento de dados
        qnt_n_resp = qnt_turma - qnt_resp
               
        #Frame
        mostrar_total_resposta = ctk.CTkFrame(master=janelaDash, width=800, height=650)
        mostrar_total_resposta.place(x=200, y=50)
        #Labels
        metricas = ['Respondidos', 'Não Respondidos']
        valores = [qnt_resp, qnt_n_resp]

        #def abrir():
        #     plt.show()

        # Botão
        #Botaoamplia=ctk.CTkButton(master=mostrar_total_resposta, text= "Ampliar", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=abrir).grid(column=1, row=2)
        cores= ['#00ffff', 'white']

        fig, ax = plt.subplots(facecolor='#323232', figsize=(7, 5),dpi=(100))
        ax.clear()

        # Gráfico de pizza
        ax.pie(valores, labels=metricas, startangle=90, autopct='%1.1f%%', colors=cores)
        ax.axis('equal')

        # Círculo no centro
        centre_circle = plt.Circle((0, 0), 0.45, fc='#404040')
        ax.add_artist(centre_circle)

        # Propriedades estéticas
        
        
        plt.title('Total de Respostas')
        
        canvas =  FigureCanvasTkAgg(fig, master=mostrar_total_resposta)
        canvas.draw()
        canvas.get_tk_widget().place(x=50, y=50)
            

    def mostra_media_time():
        #Frame 
        media_time_frame = ctk.CTkFrame(master=janelaDash, width=800, height=650)
        media_time_frame.place(x=200, y=50)
        #Labels
        metricas = ['Comunicação', 'Relacionamento', 'Proatividade', 'Produtividade','Entregas']
        valores = [5, 5, 4, 3, 4]
        
        fig, ax = plt.subplots(facecolor='#323232', figsize=(7, 5),dpi=(100))
        ax.clear()
        
        ax.axhline(y=1, color='gray', linestyle='--')
        ax.axhline(y=2, color='gray', linestyle='--')
        ax.axhline(y=3, color='gray', linestyle='--')
        ax.axhline(y=4, color='gray', linestyle='--')
        ax.axhline(y=5, color='gray', linestyle='--')
        ax.bar(metricas, valores, color="#66FFFF", width=0.3, align='center')
        ax.set_xlabel('', color="white")
        ax.set_ylabel('Valores', color="white")
        ax.set_title('Média de avaliação sobre time geral', color="white")
        ax.set_facecolor('#404040')
        ax.yaxis.set_tick_params(color='white')


        ytick_labels = ax.get_yticklabels()
        for label in ytick_labels:
            label.set_color('white')

        xtick_labels = ax.get_xticklabels()
        for label in xtick_labels:
            label.set_color('white')  # Cor dos textos 'Maturidade', 'Autonomia', 'Desempenho'

        canvas =  FigureCanvasTkAgg(fig, master=media_time_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=50, y=50)

      

    botaoQuantResp = ctk.CTkButton(master=janelaDash, text= "Quantidade Respostas", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=mostrar_total_respostas).place(x=1030, y =150)
    botaoMediaTime = ctk.CTkButton(master=janelaDash, text= "Média times", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=mostra_media_time ).place(x=1030, y =200)
    botaoAutoAv = ctk.CTkButton(master=janelaDash, text= "Autoavaliação", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=1030, y =250)
    botaoMediaInt = ctk.CTkButton(master=janelaDash, text= "Média sobre Você", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=telaDashMediaInt).place(x=1030, y =300)
    botaoAnalise = ctk.CTkButton(master=janelaDash, text= "Analise Comparativa", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=telaDashAnalise).place(x=1030, y =350)

nome_integrante = 'Jhony'
sprint_receb = '2'
turma_receb = 'bd'
time_receb = 'techorizon'
total_integ = 0

with open('data_json/users.json', 'r') as arquivou:
    dados_json_users = json.load(arquivou)

idturma = "123"
idtime = "3"
for idturmajson in dados_json_users['usuarios']:
    if idturmajson['idturma'] == idturma:
        if idturmajson['idtime'] == idtime:
            total_integ += 1

frame1 = ctk.CTkFrame(janelaDash, width=130, height=130, fg_color="dimgray")
frame1.place(x=20, y=20)
label = ctk.CTkLabel(master=frame1, text="Sprint\n"+sprint_receb, text_color=("white"), font=("roboto", 20, "bold")).place(x=30, y=30)

frame2 = ctk.CTkFrame(janelaDash, width=130, height=130, fg_color="dimgray")
frame2.place(x=20, y=180)
label = ctk.CTkLabel(master=frame2, text="Turma", text_color=("white"), font=("roboto", 20, "bold")).place(x=30, y=20)
label = ctk.CTkLabel(master=frame2, text="Time", text_color=("white"), font=("roboto", 20, "bold")).place(x=35, y=70)

frame3 = ctk.CTkFrame(janelaDash, width=130, height=130, fg_color="dimgray")
frame3.place(x=20, y=340)
label = ctk.CTkLabel(master=frame3, text="Total de\nintegrantes\n"+str(total_integ), text_color=("white"), font=("roboto", 20, "bold")).place(x=15, y=20)

frame4 = ctk.CTkFrame(janelaDash, width=130, height=130, fg_color="dimgray")
frame4.place(x=20, y=500)
label = ctk.CTkLabel(master=frame4, text="Legenda", text_color=("white"), font=("roboto", 20, "bold")).place(x=20, y=20)


tela_dashboard_operacional()