import customtkinter as ctk
import json
import matplotlib
import feedback
import TelaBV
import tkinter
from tkinter import *
from customtkinter import *

from colorama import Fore, Style
import matplotlib.pyplot as plt
matplotlib.use('TkAgg') #INFORMA QUAL BACK-END MAT.. USARÁ - INTEGRA O TK COM O MAT
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from PIL import Image

def abrir_dash_op(idturmaParametro, idtimeParametro, sprintSelecionadaParametro, user_id):

    global idturma, idtime, sprintSelecionada, idavaliado
    idturma = idturmaParametro
    idtime = idtimeParametro
    sprintSelecionada = sprintSelecionadaParametro
    idavaliado = user_id

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

            img= ctk.CTkImage(dark_image=Image.open("btspadrao/logo_insight.png"),size=(180,120))
            label_img = ctk.CTkLabel(master=janelaDash, image=img, text='')
            label_img.place(x=1000, y=30)
            
            janelaDash.title("Insight 360º")
            janelaDash.iconbitmap("btspadrao/logo_insight.ico")
            janelaDash.resizable(False, False) #defino que o usuário não pode redimensionar a tela  

        def todos_os_dashs():
            global idturma, idtime, sprintSelecionada, idavaliado
            frameTodos = ctk.CTkFrame(master=janelaDash, width=800, height=650, fg_color='#242424')
            frameTodos.place(x=200, y=50)
               
              
            comp_frame = ctk.CTkFrame(master=frameTodos, width=380, height=255, fg_color='#242424')
            comp_frame.place(x=400, y=280)
            
            with open ("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)

            #MÉDIA DO INTEGRANTE
        
            
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


            #VARIAVEIS TIME
            
            resposta1Time = 0
            resposta2Time = 0
            resposta3Time = 0
            resposta4Time = 0
            resposta5Time = 0
            controlerTime = 0

        
            #TIME
            for i in dados_json['avaliacao']:
                if i['idturma'] == idturma:
                    if i['idtime']==idtime:
                        if i['sprint'] == sprintSelecionada:
                            for x in i['respostas']:
                                controlerTime += 1
                                resposta1Time += x['resposta1']
                                resposta2Time += x['resposta2']
                                resposta3Time += x['resposta3']
                                resposta4Time += x['resposta4']
                                resposta5Time += x['resposta5']
            
                        
            #PROCESSAMENTO DE MÉDIAS TURMAS

            medResp1 = resposta1/controler
            medResp2 = resposta2/controler
            medResp3 = resposta3/controler
            medResp4 = resposta4/controler
            medResp5 = resposta5/controler

            #PROCESSAMENTO DE MÉDIAS TIME

            medResp1Time = resposta1Time/controlerTime
            medResp2Time = resposta2Time/controlerTime
            medResp3Time = resposta3Time/controlerTime
            medResp4Time = resposta4Time/controlerTime
            medResp5Time = resposta5Time/controlerTime

            #DADOS DA TURMA
            dados1 = {
                "Comunicação": medResp1,
                "Relação Interpessoal": medResp2,
                "Proatividade": medResp3,
                "Produtividade": medResp4, 
                "Prazos de entrega": medResp5
            }

            #DADOS DO TIME
            dados2 = {
                "Comunicação": medResp1Time,
                "Relação Interpessoal": medResp2Time,
                "Proatividade": medResp3Time,
                "Produtividade": medResp4Time, 
                "Prazos de entrega": medResp5Time
            }

            indicadores = dados1.keys()
            valores1 = dados1.values()
            valores2 = dados2.values()

            print(indicadores)
            print(valores1)
            print(valores2)
        
            figura = Figure(figsize=(4.5,3), dpi=100)
            eixo = figura.add_subplot(111)

            eixo.plot(indicadores, valores2, color="#c8c8c8", label = "Time")    
            eixo.plot(valores1, color="#00FFFF", label = "Você")
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
                label.set_size(8)

            xtick_labels = eixo.get_xticklabels()
            for label in xtick_labels:
                label.set_color('white') 
                label.set_size(8)

            canvas = FigureCanvasTkAgg(figura, master=comp_frame)
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=10)

            
            
            media_time_frame = ctk.CTkFrame(master=frameTodos, width=380, height=255, fg_color='#242424')
            media_time_frame.place(x=10, y=280)
            with open("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)
            
            
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
                "Relação\nInterpessoal": medResp2,
                "Proatividade": medResp3,
                "Produti-\nvidade": medResp4, 
                "Prazos\nde entrega": medResp5
            }

            indicadores = dados.keys()
            valores = dados.values()
        # Criação da figura e do eixo
            figura = Figure(figsize=(4.5, 3), dpi=100)
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
                label.set_size(8)

            xtick_labels = eixo.get_xticklabels()
            for label in xtick_labels:
                label.set_color('white') 
                label.set_size(8)
            
            canvas = FigureCanvasTkAgg(figura, master=media_time_frame)
            canvas.draw()

            eixo.set_title('Média do time sobre você', color=cor_texto)

            # Exibição do gráfico na janela do Tkinter
            canvas.get_tk_widget().place(x=10, y=10)
            pass

            comp_frame = ctk.CTkFrame(master=frameTodos, width=380, height=255, fg_color='#242424')
            comp_frame.place(x=400, y=10)
            
#             with open ("data_json/questions.json", "r") as arquivo:
#                 dados_json = json.load(arquivo)

# #MÉDIA DO INTEGRANTE
            
#             resposta1 = 0
#             resposta2 = 0
#             resposta3 = 0
#             resposta4 = 0
#             resposta5 = 0
#             controler = 0

#             for i in dados_json['avaliacao']:
#                 if i['idturma'] == idturma:
#                     if i['idtime']==idtime:
#                         controler += 1
#                         for x in i['respostas']:
#                             if x['idavaliado']== idavaliado:
#                                 resposta1 += x['resposta1']
#                                 resposta2 += x['resposta2']
#                                 resposta3 += x['resposta3']
#                                 resposta4 += x['resposta4']
#                                 resposta5 += x['resposta5']


#             #VARIAVEIS TIME
            
#             resposta1Time = 0
#             resposta2Time = 0
#             resposta3Time = 0
#             resposta4Time = 0
#             resposta5Time = 0
#             controlerTime = 0

        
#             #TIME
#             for i in dados_json['avaliacao']:
#                 if i['idturma'] == idturma:
#                     if i['idtime']==idtime:
#                         if i['sprint'] == sprintSelecionada:
#                             for x in i['respostas']:
#                                 controlerTime += 1
#                                 resposta1Time += x['resposta1']
#                                 resposta2Time += x['resposta2']
#                                 resposta3Time += x['resposta3']
#                                 resposta4Time += x['resposta4']
#                                 resposta5Time += x['resposta5']
            
                        
#             #PROCESSAMENTO DE MÉDIAS TURMAS

#             medResp1 = resposta1/controler
#             medResp2 = resposta2/controler
#             medResp3 = resposta3/controler
#             medResp4 = resposta4/controler
#             medResp5 = resposta5/controler

#             #PROCESSAMENTO DE MÉDIAS TIME

#             medResp1Time = resposta1Time/controlerTime
#             medResp2Time = resposta2Time/controlerTime
#             medResp3Time = resposta3Time/controlerTime
#             medResp4Time = resposta4Time/controlerTime
#             medResp5Time = resposta5Time/controlerTime

#             #DADOS DA TURMA
#             dados1 = {
#                 "Comunicação": medResp1,
#                 "Relação Interpessoal": medResp2,
#                 "Proatividade": medResp3,
#                 "Produtividade": medResp4, 
#                 "Prazos de entrega": medResp5
#             }

#             #DADOS DO TIME
#             dados2 = {
#                 "Comunicação": medResp1Time,
#                 "Relação Interpessoal": medResp2Time,
#                 "Proatividade": medResp3Time,
#                 "Produtividade": medResp4Time, 
#                 "Prazos de entrega": medResp5Time
#             }


#             indicadores = dados1.keys()
#             valores1 = dados1.values()
#             valores2 = dados2.values()

#             print(indicadores)
#             print(valores1)
#             print(valores2)
        
#             figura = Figure(figsize=(4.5,3), dpi=100)
#             eixo = figura.add_subplot(111)

#             eixo.plot(indicadores, valores2, color="#c8c8c8", label = "Time")    
#             eixo.plot(valores1, color="#00FFFF", label = "Você")
#             eixo.set_title("Análise comparativa entre você e o time", color="white")
#             eixo.set_facecolor("#404040")
#             figura.set_facecolor("#323232")
#             eixo.legend()
#             eixo.axhline(y=1, color='gray', linestyle='--')
#             eixo.axhline(y=2, color='gray', linestyle='--')
#             eixo.axhline(y=3, color='gray', linestyle='--')
#             eixo.axhline(y=4, color='gray', linestyle='--')
#             eixo.axhline(y=5, color='gray', linestyle='--')

#             ytick_labels = eixo.get_yticklabels()
#             for label in ytick_labels:
#                 label.set_color('white')
#                 label.set_size(8)

#             xtick_labels = eixo.get_xticklabels()
#             for label in xtick_labels:
#                 label.set_color('white') 
#                 label.set_size(8)

#             canvas = FigureCanvasTkAgg(figura, master=comp_frame)
#             canvas.draw()
#             canvas.get_tk_widget().place(x=10, y=10)

            with open('data_json/questions.json', 'r') as arquivo:
                dados_json_questions = json.load(arquivo)

            with open('data_json/users.json', 'r') as arquivou:
                dados_json_users = json.load(arquivou)

            
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
            mostrar_total_resposta = ctk.CTkFrame(master=frameTodos, width=380, height=255, fg_color='#242424')
            mostrar_total_resposta.place(x=10, y=10)
            ProcessLookupError
            #Labels
            metricas = ['Respondidos', 'Não\nRespondidos']
            valores = [qnt_resp, qnt_n_resp]
            cores= ['#00ffff', 'white']
            
            fig, ax = plt.subplots(facecolor='#323232', figsize=(4.5, 3),dpi=(100))
            ax.clear()

            # Exibição das listas com cores usando o ctk e colorama
            janela = ctk.CTk()

            
            # Gráfico de pizza
            patches, texts, autotexts = ax.pie(valores, labels=metricas, startangle=90, autopct='%1.1f%%', colors=cores)
            ax.axis('equal')

            for text in texts:
                text.set_color('white')
                text.set_fontsize(10)

            # Círculo no centro
            centre_circle = plt.Circle((0, 0), 0.45, fc='#404040')
            ax.add_artist(centre_circle)

            # Propriedades estéticas
            plt.title("Total de Respostas", color="white")
            
            canvas =  FigureCanvasTkAgg(fig, master=mostrar_total_resposta)
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=10)
            
            with open("data_json/questions.json", "r") as arquivo:
                            dados_json = json.load(arquivo)
                    
            
            sprint = sprintSelecionada
            
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
                "Relação\nInterpessoal": medResp2,
                "Proatividade": medResp3,
                "Produti-\nvidade": medResp4, 
                "Prazos\nde entrega": medResp5
            }

            indicadores = dados.keys()
            valores = dados.values()


            # GRAFICO GIL
            #Frame 
            media_time_frame = ctk.CTkFrame(master=frameTodos, width=380, height=255, fg_color='#242424')
            media_time_frame.place(x=400, y=10)
            #Labels
            metricas = indicadores
           
            
            fig, ax = plt.subplots(facecolor='#323232', figsize=(4.5, 3),dpi=(100))
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
                label.set_size(8)

            xtick_labels = ax.get_xticklabels()
            for label in xtick_labels:
                label.set_color('white')  # Cor dos textos 'Maturidade', 'Autonomia', 'Desempenho'
                label.set_size(8)

            canvas =  FigureCanvasTkAgg(fig, master=media_time_frame)
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=10)
              
            #aqui acaba a frame1
        todos_os_dashs()

        def telaDashMediaInt():
            
            global idturma, idtime, sprintSelecionada, idavaliado

            media_time_frame = ctk.CTkFrame(master=janelaDash, width=800, height=650, fg_color='#242424')
            media_time_frame.place(x=200, y=50)
            with open("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)
            
            
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

            eixo.set_title('Média do time sobre você', color=cor_texto)

            # Exibição do gráfico na janela do Tkinter
            canvas.get_tk_widget().place(x=100, y=80)
            pass



        def telaDashAnalise():
            comp_frame = ctk.CTkFrame(master=janelaDash, width=800, height=650, fg_color='#242424')
            comp_frame.place(x=200, y=50)
            global idturma, idtime, sprintSelecionada, idavaliado

            with open ("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)

            #MÉDIA DO INTEGRANTE
            
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


            #VARIAVEIS TIME
            
            resposta1Time = 0
            resposta2Time = 0
            resposta3Time = 0
            resposta4Time = 0
            resposta5Time = 0
            controlerTime = 0

        
            #TIME
            for i in dados_json['avaliacao']:
                if i['idturma'] == idturma:
                    if i['idtime']==idtime:
                        if i['sprint'] == sprintSelecionada:
                            for x in i['respostas']:
                                controlerTime += 1
                                resposta1Time += x['resposta1']
                                resposta2Time += x['resposta2']
                                resposta3Time += x['resposta3']
                                resposta4Time += x['resposta4']
                                resposta5Time += x['resposta5']
            
                        
            #PROCESSAMENTO DE MÉDIAS TURMAS

            medResp1 = resposta1/controler
            medResp2 = resposta2/controler
            medResp3 = resposta3/controler
            medResp4 = resposta4/controler
            medResp5 = resposta5/controler

            #PROCESSAMENTO DE MÉDIAS TIME

            medResp1Time = resposta1Time/controlerTime
            medResp2Time = resposta2Time/controlerTime
            medResp3Time = resposta3Time/controlerTime
            medResp4Time = resposta4Time/controlerTime
            medResp5Time = resposta5Time/controlerTime

            #DADOS DA TURMA
            dados1 = {
                "Comunicação": medResp1,
                "Relação Interpessoal": medResp2,
                "Proatividade": medResp3,
                "Produtividade": medResp4, 
                "Prazos de entrega": medResp5
            }

            #DADOS DO TIME
            dados2 = {
                "Comunicação": medResp1Time,
                "Relação Interpessoal": medResp2Time,
                "Proatividade": medResp3Time,
                "Produtividade": medResp4Time, 
                "Prazos de entrega": medResp5Time
            }

            indicadores = dados1.keys()
            valores1 = dados1.values()
            valores2 = dados2.values()

            print(indicadores)
            print(valores1)
            print(valores2)
        
            figura = Figure(figsize=(8,6), dpi=100)
            eixo = figura.add_subplot(111)

            eixo.plot(indicadores, valores2, color="#c8c8c8", label = "Time")    
            eixo.plot(valores1, color="#00FFFF", label = "Você")
            eixo.set_title("Análise comparativa entre você e o time", color="white")
            eixo.set_facecolor("#404040")
            figura.set_facecolor("#323232")
            eixo.legend()
            eixo.axhline(y=1, color='gray', linestyle='--')
            eixo.axhline(y=2, color='gray', linestyle='--')
            eixo.axhline(y=3, color='gray', linestyle='--')
            eixo.axhline(y=4, color='gray', linestyle='--')
            eixo.axhline(y=5, color='gray', linestyle='--')
            eixo.scatter(range(len(indicadores)), valores2, color='#c8c8c8')

            for i, valor in enumerate(valores1):
                eixo.text(i, valor, f'{valor:.2f}', color='#00FFFF', ha='center', va='bottom')

            # Adicionar os valores na ponta de cada ponto da turma
            for i, valor in enumerate(valores2):
                eixo.text(i, valor, f'{valor:.2f}', color='#c8c8c8', ha='center', va='bottom')

            ytick_labels = eixo.get_yticklabels()
            for label in ytick_labels:
                label.set_color('white')

            xtick_labels = eixo.get_xticklabels()
            for label in xtick_labels:
                label.set_color('white') 

            canvas = FigureCanvasTkAgg(figura, master=comp_frame)
            canvas.draw()
            canvas.get_tk_widget().place(x=100, y=80)

        def mostrar_total_respostas():
            with open('data_json/questions.json', 'r') as arquivo:
                dados_json_questions = json.load(arquivo)
            global idturma, idtime, sprintSelecionada, idavaliado
            with open('data_json/users.json', 'r') as arquivou:
                dados_json_users = json.load(arquivou)

            
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
            mostrar_total_resposta = ctk.CTkFrame(master=janelaDash, width=800, height=650, fg_color='#242424')
            mostrar_total_resposta.place(x=200, y=50)
            ProcessLookupError
            #Labels
            metricas = ['Respondidos', 'Não Respondidos']
            valores = [qnt_resp, qnt_n_resp]
            cores= ['#00ffff', 'white']
            
            fig, ax = plt.subplots(facecolor='#323232', figsize=(8, 6),dpi=(100))
            ax.clear()

            # Exibição das listas com cores usando o ctk e colorama
            janela = ctk.CTk()

            
            # Gráfico de pizza
            patches, texts, autotexts = ax.pie(valores, labels=metricas, startangle=90, autopct='%1.1f%%', colors=cores)
            ax.axis('equal')
            for text in texts:
                text.set_color('white')
                text.set_fontsize(12)

            # Círculo no centro
            centre_circle = plt.Circle((0, 0), 0.45, fc='#404040')
            ax.add_artist(centre_circle)

            # Propriedades estéticas
            plt.title("Total de Respostas", color="white")
            
            canvas =  FigureCanvasTkAgg(fig, master=mostrar_total_resposta)
            canvas.draw()
            canvas.get_tk_widget().place(x=100, y=80)
                
            
        def mostra_media_time():
            #Frame 
            
            with open("data_json/questions.json", "r") as arquivo:
                    dados_json = json.load(arquivo)
            
            global idturma, idtime, sprintSelecionada, idavaliado
            
            sprint =sprintSelecionada
            
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
            media_time_frame = ctk.CTkFrame(master=janelaDash, width=800, height=650)
            media_time_frame.place(x=200, y=50)
            #Labels
            #label_nome = ctk.CTkLabel(master=media_time_frame, text='Dashboards: Vinicius Domingues Mangaba', font=('Roboto',18, 'bold'), text_color="#00FFFF",).place(x= 300, y= 50)
            metricas = indicadores
            valores = valores
            
            with open ("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)        
            
            
            fig, ax = plt.subplots(facecolor='#323232', figsize=(8, 6))
            ax.clear()
            ax.bar(metricas, valores, color="#66FFFF", width=0.3, align='center')
            ax.set_xlabel('', color="white")
            ax.set_ylabel('Valores', color="white")
            ax.set_title('Média de avaliação sobre o time', color="white")
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
            canvas.get_tk_widget().place(x=100, y=80)


        def mostra_autoavaliacao():
            #Frame 
            global idturma, idtime, sprintSelecionada, idavaliado
            idavaliador = idavaliado
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

                    
            autoavaliacao_frame = ctk.CTkFrame(master=janelaDash, width=800, height=650)
            autoavaliacao_frame.place(x=200, y=50)

            #label_nome = ctk.CTkLabel(master=autoavaliacao_frame, text='Dashboards: Vinicius Domingues Mangaba', font=('Roboto',18, 'bold'), text_color="#00FFFF",).place(x= 300, y= 50)
            metricas = ['Comunicação', 'Relacionamento', 'Proatividade', 'Produtividade','Entregas']
            valores = respostas
            
            fig, ax = plt.subplots(facecolor='#323232', figsize=(8, 6))
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
            canvas.get_tk_widget().place(x=100, y=80)    

        def open_feedback():
            janelaDash.destroy()
            feedback.abrir_feedback(idturmaParametro, idtimeParametro, sprintSelecionadaParametro, user_id)

        def open_BV():
            janelaDash.destroy()
            TelaBV.abrir()
            
        botaoQuantResp = ctk.CTkButton(master=janelaDash, text= "Total de Respostas", border_spacing=4, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=mostrar_total_respostas).place(x=1030, y =170)
        botaoMediaTime = ctk.CTkButton(master=janelaDash, text= "Média times", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=mostra_media_time ).place(x=1030, y =220)
        botaoAutoAv = ctk.CTkButton(master=janelaDash, text= "Autoavaliação", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=mostra_autoavaliacao).place(x=1030, y =270)
        botaoMediaInt = ctk.CTkButton(master=janelaDash, text= "Média sobre Você", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=telaDashMediaInt).place(x=1030, y =320)
        botaoAnalise = ctk.CTkButton(master=janelaDash, text= "Analise Comparativa", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=telaDashAnalise).place(x=1030, y =370)
        botaoFeedback = ctk.CTkButton(master=janelaDash, text= "Feedbacks Recebidos", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=open_feedback).place(x=1030, y =470)
        botaoMenuInicial = ctk.CTkButton(master=janelaDash, text= "Menu Inicial", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=open_BV).place(x=1030, y =520)
        botaoTodosGraficos = ctk.CTkButton(master=janelaDash, text= "Todos os Gráficos", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=todos_os_dashs).place(x=1030, y=420)

        


    with open('data_json/turmas.json', "r") as arquivoNomes:
        dados_nomes = json.load(arquivoNomes)

    for i in dados_nomes['turmas']:
        if idturma == i['idturma']:
            nome_turma = i['nometurma']
            for x in i['times']:
                if idtime == x['idtime']:
                    nome_time = x['nometime']

    sprint_receb = sprintSelecionada
    turma_receb = nome_turma
    time_receb = nome_time
    total_integ = 0

    with open('data_json/users.json', 'r') as arquivou:
        dados_json_users = json.load(arquivou)

    for idturmajson in dados_json_users['usuarios']:
        if idturmajson['idturma'] == idturma:
            if idturmajson['idtime'] == idtime:
                total_integ += 1
    
    for i in dados_json_users['usuarios']:
        if idavaliado == i['id']:
            nome_integrante = i['user']

    nova_turma = turma_receb
    palavras = nova_turma.split()
    if len(palavras) > 2:
        # Pegar apenas as iniciais das palavras
        iniciais = [palavra[0] for palavra in palavras if palavra[0].isupper()]
        nova_turma = ''.join(iniciais)
    

    nova_time = time_receb

# Verificar se o time possui mais de duas palavras
    palavras_time = nova_time.split()
    if len(palavras_time) > 2:
        # Pegar apenas as iniciais maiúsculas das palavras do time
        iniciais_time = [palavra[0] for palavra in palavras_time if palavra[0].isupper()]
        nova_time = ''.join(iniciais_time)


    
    
    label = ctk.CTkLabel(master=janelaDash, text=nome_integrante, text_color=("#00FFFF"), font=("roboto", 20, "bold")).place(x=30, y=15)

    frame2 = ctk.CTkFrame(janelaDash, width=150, height=70, fg_color="gray26", border_width=2)
    frame2.place(x=30, y=70)
    label = ctk.CTkLabel(master=frame2, text="Sprint\n"+sprint_receb, text_color=("white"), font=("roboto", 20, "bold")).place(x=45, y=10)

    frame3 = ctk.CTkFrame(janelaDash, width=150, height=70, fg_color="gray26", border_width=2)
    frame3.place(x=30, y=160)   
    label = ctk.CTkLabel(master=frame3, text="Turma\n"+nova_turma, text_color=("white"), font=("roboto", 20, "bold")).place(x=45, y=10)

    frame4 = ctk.CTkFrame(janelaDash, width=150, height=70, fg_color="gray26", border_width=2)
    frame4.place(x=30, y=250)
    label = ctk.CTkLabel(master=frame4, text="Time\n"+nova_time, text_color=("white"), font=("roboto", 20, "bold")).place(x=20, y=10)

    frame5 = ctk.CTkFrame(janelaDash, width=150, height=70, fg_color="gray26", border_width=2)
    frame5.place(x=30, y=340)
    label = ctk.CTkLabel(master=frame5, text="Membros\n"+str(total_integ), text_color=("white"), font=("roboto", 20, 'bold')).place(x=28, y=10)

    frame6 = ctk.CTkFrame(janelaDash, width=150, height=140, fg_color="gray26", border_width=2)
    frame6.place(x=30, y=430)
    label = ctk.CTkLabel(master=frame6, text="Legenda", text_color=("white"), font=("roboto", 20, "bold")).place(x=30, y=10)
    label = ctk.CTkLabel(master=frame6, text="1- Muito Bom\n2- Bom\n3- Regular\n4- Ruim\n5- Muito Ruim", text_color=("white"), font=("roboto", 15)).place(x=25, y=40)

    tela_dashboard_operacional()
