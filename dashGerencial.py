import customtkinter as ctk
import json
import matplotlib
import TelaBV
import tkinter

from colorama import Fore, Style
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

from PIL import Image, ImageTk

def abrir_dash_ge(idturmaParametro, idtimeParametro, sprintSelecionada,turmaSelecionada, timeSelecionado):
    janelaDashGerencial = ctk.CTk()

    global idturma, idtime, sprint
    idturma = idturmaParametro
    idtime = idtimeParametro
    sprint = sprintSelecionada

    class tela_dashboard_gerencial:
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
            x = (screen_width - 1200) // 2
            y = (screen_height - 650) // 2
            janelaDashGerencial.geometry("1200x650+{}+{}".format(x, y))


            img= ctk.CTkImage(dark_image=Image.open("logo_insight.png"),size=(200,140))
            label_img = ctk.CTkLabel(master=janelaDashGerencial, image=img, text='')
            label_img.place(x=980, y=10)
            
            janelaDashGerencial.title("Insight 360º")
            janelaDashGerencial.iconbitmap("logo_insight.ico")
            janelaDashGerencial.resizable(False, False) #defino que o usuário não pode redimensionar a tela  

        def telaDashAnalise():
            global idturma, idtime, sprint
            comp_frame = ctk.CTkFrame(master=janelaDashGerencial, width=800, height=650)
            comp_frame.place(x=200, y=50)
            
            with open("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)
            
            
            resposta1 = 0
            resposta2 = 0
            resposta3 = 0
            resposta4 = 0
            resposta5 = 0
            controler = 0


            #VARIAVEIS TIME
            
            resposta1Time = 0
            resposta2Time = 0
            resposta3Time = 0
            resposta4Time = 0
            resposta5Time = 0
            controlerTime = 0

            #TURMA
            for i in dados_json['avaliacao']:
                if i['idturma'] == idturma:
                    for x in i['respostas']:
                        controler += 1
                        resposta1 += x['resposta1']
                        resposta2 += x['resposta2']
                        resposta3 += x['resposta3']
                        resposta4 += x['resposta4']
                        resposta5 += x['resposta5']
        
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

            #DADOS DA TURMA
            dados2 = {
                "Comunicação": medResp1,
                "Relação Interpessoal": medResp2,
                "Proatividade": medResp3,
                "Produtividade": medResp4, 
                "Prazos de entrega": medResp5
            }

            #PROCESSAMENTO DE MÉDIAS TIME

            medResp1Time = resposta1Time/controlerTime
            medResp2Time = resposta2Time/controlerTime
            medResp3Time = resposta3Time/controlerTime
            medResp4Time = resposta4Time/controlerTime
            medResp5Time = resposta5Time/controlerTime

            #DADOS DA TURMA
            dados2 = {
                "Comunicação": medResp1,
                "Relação Interpessoal": medResp2,
                "Proatividade": medResp3,
                "Produtividade": medResp4, 
                "Prazos de entrega": medResp5
            }

            #DADOS DO TIME
            dados1 = {
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

            eixo.plot(valores1, color="#00FFFF", label = "Time")
            eixo.plot(indicadores, valores2, color="#c8c8c8", label = "Turma")    
            
            eixo.set_title("Análise comparativa entre a turma e o time", color="white")
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
            canvas.get_tk_widget().place(x=10, y=10)

        def mostrar_total_respostas():
            with open('data_json/questions.json', 'r') as arquivo:
                dados_json_questions = json.load(arquivo)

            with open('data_json/users.json', 'r') as arquivou:
                dados_json_users = json.load(arquivou)

            global idturma, idtime, sprint
            
            qnt_turma = 0
            qnt_resp = 0 
            for idturmajson in dados_json_users['usuarios']:
                if idturmajson['idturma'] == idturma:
                    if idturmajson['idtime'] == idtime:
                        qnt_turma += 1 

            for idturmajson in dados_json_questions['avaliacao']:
                if idturmajson['idturma'] == idturma:
                    if idturmajson['idtime'] == idtime:
                         if idturmajson['sprint'] == sprintSelecionada:
                            qnt_resp += 1 

            #Processamento de dados
            qnt_n_resp = qnt_turma - qnt_resp
                
            #Frame
            mostrar_total_resposta = ctk.CTkFrame(master=janelaDashGerencial, width=800, height=650)
            mostrar_total_resposta.place(x=200, y=50)
            
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

# Definir cor dos rótulos
            for text in texts:
                text.set_color('white')
                text.set_fontsize(12)
            ax.axis('equal')

            # Círculo no centro
            centre_circle = plt.Circle((0, 0), 0.45, fc='#404040')
            ax.add_artist(centre_circle)

            # Propriedades estéticas
            plt.title("Total de Respostas", color="white", size=15)
            
            canvas =  FigureCanvasTkAgg(fig, master=mostrar_total_resposta)
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=10)

        def mostra_media_time():
            with open("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)
        
            global idturma, idtime, sprint
            
            resposta1 = 0
            resposta2 = 0
            resposta3 = 0
            resposta4 = 0
            resposta5 = 0
            controler = 0

            for i in dados_json['avaliacao']:
                if i['idturma'] == idturma:
                    if i['idtime']==idtime:
                         if i['sprint'] == sprintSelecionada:
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
            media_time_frame = ctk.CTkFrame(master=janelaDashGerencial, width=800, height=650)
            media_time_frame.place(x=200, y=50)
            #Labels
            metricas = indicadores
            valores = valores
            
            fig, ax = plt.subplots(facecolor='#323232', figsize=(8, 6),dpi=(100))
            ax.clear()
            
            ax.axhline(y=1, color='gray', linestyle='--')
            ax.axhline(y=2, color='gray', linestyle='--')
            ax.axhline(y=3, color='gray', linestyle='--')
            ax.axhline(y=4, color='gray', linestyle='--')
            ax.axhline(y=5, color='gray', linestyle='--')
            ax.bar(metricas, valores, color="#66FFFF", width=0.3, align='center')
            ax.set_xlabel('', color="white")
            ax.set_ylabel('Valores', color="white")
            ax.set_title('Média de avaliação do time', color="white")
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
            canvas.get_tk_widget().place(x=10, y=10)

        def mediaTurma():
            media_turma_frame = ctk.CTkFrame(master=janelaDashGerencial, width=800, height=650)
            media_turma_frame.place(x=200, y=50)

            with open("data_json/questions.json", "r") as arquivo:
                dados_json = json.load(arquivo)
            
            global idturma, idtime, sprint
            resposta1 = 0
            resposta2 = 0
            resposta3 = 0
            resposta4 = 0
            resposta5 = 0
            controler = 0

            for i in dados_json['avaliacao']:
                if i['idturma'] == idturma:
                    if i['sprint'] == sprintSelecionada:
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
            
            canvas = FigureCanvasTkAgg(figura, master=media_turma_frame)
            canvas.draw()

            eixo.set_title('Média de respostas da turma', color=cor_texto)

            # Exibição do gráfico na janela do Tkinter
            canvas.get_tk_widget().place(x=10, y=10)
            pass
        


        
        def mostrar_todos_dash():
                frameTodos = ctk.CTkFrame(master=janelaDashGerencial, width=800, height=650, fg_color='#242424')
                frameTodos.place(x=200, y=50)
                
                with open('data_json/questions.json', 'r') as arquivo:
                    dados_json_questions = json.load(arquivo)

                with open('data_json/users.json', 'r') as arquivou:
                    dados_json_users = json.load(arquivou)

                global idturma, idtime, sprint
                
                qnt_turma = 0
                qnt_resp = 0 
                for idturmajson in dados_json_users['usuarios']:
                    if idturmajson['idturma'] == idturma:
                        if idturmajson['idtime'] == idtime:
                            qnt_turma += 1 

                for idturmajson in dados_json_questions['avaliacao']:
                    if idturmajson['idturma'] == idturma:
                        if idturmajson['idtime'] == idtime:
                            if idturmajson['sprint'] == sprintSelecionada:
                                qnt_resp += 1 

                #Processamento de dados
                qnt_n_resp = qnt_turma - qnt_resp
                    
                #Frame
                mostrar_total_resposta = ctk.CTkFrame(master=frameTodos, width=380, height=255)
                mostrar_total_resposta.place(x=10, y=10)
                
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

        # Definir cor dos rótulos
                for text in texts:
                    text.set_color('white')
                ax.axis('equal')

                # Círculo no centro
                centre_circle = plt.Circle((0, 0), 0.45, fc='#404040')
                ax.add_artist(centre_circle)

                # Propriedades estéticas
                plt.title("Total de Respostas", color="white")
                
                canvas =  FigureCanvasTkAgg(fig, master=mostrar_total_resposta)
                canvas.draw()
                canvas.get_tk_widget().place(x=10, y=10)

                #GRAFICO MEDIA TURMA


                media_turma_frame = ctk.CTkFrame(master=frameTodos, width=380, height=255)
                media_turma_frame.place(x=400, y=10)
                
                resposta1 = 0
                resposta2 = 0
                resposta3 = 0
                resposta4 = 0
                resposta5 = 0
                controler = 0

                for i in dados_json_questions['avaliacao']:
                    if i['idturma'] == idturma:
                        if i['sprint'] == sprintSelecionada:
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
                
                canvas = FigureCanvasTkAgg(figura, master=media_turma_frame)
                canvas.draw()

                eixo.set_title('Média de respostas da turma', color=cor_texto)

                # Exibição do gráfico na janela do Tkinter
                canvas.get_tk_widget().place(x=10, y=10)

                #dash media time



                resposta1 = 0
                resposta2 = 0
                resposta3 = 0
                resposta4 = 0
                resposta5 = 0
                controler = 0

                for i in dados_json_questions['avaliacao']:
                    if i['idturma'] == idturma:
                        if i['idtime']==idtime:
                            if i['sprint'] == sprintSelecionada:
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
                #Frame 
                media_time_frame = ctk.CTkFrame(master=frameTodos, width=380, height=255)
                media_time_frame.place(x=10, y=280)
                #Labels
                metricas = indicadores
                valores = valores
                
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
                ax.set_title('Média de avaliação do time', color="white")
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



                #DASH ANALISE COMPARATIVA

                comp_frame = ctk.CTkFrame(master=frameTodos, width=380, height=255)
                comp_frame.place(x=400, y=280)
                
                with open("data_json/questions.json", "r") as arquivo:
                    dados_json = json.load(arquivo)
             
                resposta1 = 0
                resposta2 = 0
                resposta3 = 0
                resposta4 = 0
                resposta5 = 0
                controler = 0


                #VARIAVEIS TIME
       
                resposta1Time = 0
                resposta2Time = 0
                resposta3Time = 0
                resposta4Time = 0
                resposta5Time = 0
                controlerTime = 0

                #TURMA
                for i in dados_json['avaliacao']:
                    if i['idturma'] == idturma:
                        if i['sprint'] == sprintSelecionada:
                            for x in i['respostas']:
                                controler += 1
                                resposta1 += x['resposta1']
                                resposta2 += x['resposta2']
                                resposta3 += x['resposta3']
                                resposta4 += x['resposta4']
                                resposta5 += x['resposta5']
            
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

                #DADOS DA TURMA
                dados2 = {
                    "Comunicação": medResp1,
                    "Relação Interpessoal": medResp2,
                    "Proatividade": medResp3,
                    "Produtividade": medResp4, 
                    "Prazos de entrega": medResp5
                }

                #PROCESSAMENTO DE MÉDIAS TIME

                medResp1Time = resposta1Time/controlerTime
                medResp2Time = resposta2Time/controlerTime
                medResp3Time = resposta3Time/controlerTime
                medResp4Time = resposta4Time/controlerTime
                medResp5Time = resposta5Time/controlerTime

                #DADOS DA TURMA
                dados2 = {
                    "Comunicação": medResp1,
                    "Relação Interpessoal": medResp2,
                    "Proatividade": medResp3,
                    "Produtividade": medResp4, 
                    "Prazos de entrega": medResp5
                }

                #DADOS DO TIME
                dados1 = {
                    "Comunicação": medResp1Time,
                    "Relação\nInterpessoal": medResp2Time,
                    "Proatividade": medResp3Time,
                    "Produti-\nvidade": medResp4Time, 
                    "Prazos\nde entrega": medResp5Time
                }

                indicadores = dados1.keys()
                valores1 = dados1.values()
                valores2 = dados2.values()

                print(indicadores)
                print(valores1)
                print(valores2)
            
                figura = Figure(figsize=(4.5,3), dpi=100)
                eixo = figura.add_subplot(111)

                eixo.plot(valores1, color="#00FFFF", label = "Time")
                eixo.plot(indicadores, valores2, color="#c8c8c8", label = "Turma")    
                
                eixo.set_title("Análise comparativa entre a turma e o time", color="white")
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

       
        mostrar_todos_dash()
        botaoQuantResp = ctk.CTkButton(master=janelaDashGerencial, text= "Total de Respostas", border_spacing=4, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=mostrar_total_respostas).place(x=1030, y =150)
        botaoMediaTime = ctk.CTkButton(master=janelaDashGerencial, text= "Média turma", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=mediaTurma).place(x=1030, y =200)
        botaoAutoAv = ctk.CTkButton(master=janelaDashGerencial, text= "Média time", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=mostra_media_time).place(x=1030, y =250)
        #botaoMediaInt = ctk.CTkButton(master=janelaDashGerencial, text= "Média sobre Você", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=1030, y =300)
        botaoAnalise = ctk.CTkButton(master=janelaDashGerencial, text= "Analise Comparativa", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=telaDashAnalise).place(x=1030, y =300)
        botaoGeral = ctk.CTkButton(master=janelaDashGerencial, text= "Todos Dashboards", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=mostrar_todos_dash).place(x=1030, y =350)
        botaoMenuInicial = ctk.CTkButton(master=janelaDashGerencial, text= "Menu Inicial", text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=1030, y =400)
    
    nome_integrante = 'Dashboard Gerencial'
    sprint_receb = sprint
    
    total_integ = 0

    with open('data_json/users.json', 'r') as arquivou:
        dados_json_users = json.load(arquivou)

    
    for idturmajson in dados_json_users['usuarios']:
        if idturmajson['idturma'] == idturma:
            if idturmajson['idtime'] == idtime:
                total_integ += 1




    turma_receb = turmaSelecionada
    time_receb = timeSelecionado


    label = ctk.CTkLabel(master=janelaDashGerencial, text=nome_integrante, text_color=("#00FFFF"), font=("roboto", 20, "bold")).place(x=40, y=20)

    frame2 = ctk.CTkFrame(janelaDashGerencial, width=150, height=70, fg_color="gray26", border_width=2)
    frame2.place(x=30, y=170)
    label = ctk.CTkLabel(master=frame2, text="Sprint\n"+sprint_receb, text_color=("white"), font=("roboto", 20, "bold")).place(x=45, y=10)

    frame3 = ctk.CTkFrame(janelaDashGerencial, width=150, height=70, fg_color="gray26", border_width=2)
    frame3.place(x=30, y=250)   
    label = ctk.CTkLabel(master=frame3, text="Turma\n"+turma_receb, text_color=("white"), font=("roboto", 20, "bold")).place(x=45, y=10)

    frame4 = ctk.CTkFrame(janelaDashGerencial, width=150, height=70, fg_color="gray26", border_width=2)
    frame4.place(x=30, y=330)
    label = ctk.CTkLabel(master=frame4, text="Time\n"+time_receb, text_color=("white"), font=("roboto", 20, "bold")).place(x=20, y=10)

    frame5 = ctk.CTkFrame(janelaDashGerencial, width=150, height=70, fg_color="gray26", border_width=2)
    frame5.place(x=30, y=410)
    label = ctk.CTkLabel(master=frame5, text="Membros\n"+str(total_integ), text_color=("white"), font=("roboto", 20, 'bold')).place(x=28, y=10)

    frame6 = ctk.CTkFrame(janelaDashGerencial, width=140, height=140, fg_color="gray26", border_width=2)
    frame6.place(x=1030, y =450)
    label = ctk.CTkLabel(master=frame6, text="Legenda", text_color=("white"), font=("roboto", 20, "bold")).place(x=30, y=10)
    label = ctk.CTkLabel(master=frame6, text="1- Muito Bom\n2- Bom\n3- Regular\n4- Ruim\n5- Muito Ruim", text_color=("white"), font=("roboto", 15)).place(x=25, y=40)

    tela_dashboard_gerencial()
