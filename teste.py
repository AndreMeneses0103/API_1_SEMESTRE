<<<<<<< HEAD
import customtkinter as ctk
import json
import matplotlib
import tkinter
from colorama import Fore, Style
import matplotlib.pyplot as plt
matplotlib.use('TkAgg') #INFORMA QUAL BACK-END MAT.. USARÁ - INTEGRA O TK COM O MAT
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import teste as tela

from PIL import Image

def mostrar_todos_dash(nometela):
        
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
        mostrar_total_resposta = ctk.CTkFrame(master=nometela, width=380, height=255)
        mostrar_total_resposta.place(x=200, y=50)
        
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


        media_turma_frame = ctk.CTkFrame(master=nometela, width=380, height=255)
        media_turma_frame.place(x=600, y=50)
        idturma = "123"
        resposta1 = 0
        resposta2 = 0
        resposta3 = 0
        resposta4 = 0
        resposta5 = 0
        controler = 0

        for i in dados_json_questions['avaliacao']:
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



        idturma = "123"
        idtime = "3"
        resposta1 = 0
        resposta2 = 0
        resposta3 = 0
        resposta4 = 0
        resposta5 = 0
        controler = 0

        for i in dados_json_questions['avaliacao']:
            if i['idturma'] == idturma:
                if i['idtime']==idtime:
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
        media_time_frame = ctk.CTkFrame(master=nometela, width=380, height=255)
        media_time_frame.place(x=200, y=330)
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

        comp_frame = ctk.CTkFrame(master=nometela, width=380, height=255)
        comp_frame.place(x=600, y=330)
        
        with open("data_json/questions.json", "r") as arquivo:
            dados_json = json.load(arquivo)
        
        idturma = "123"
        resposta1 = 0
        resposta2 = 0
        resposta3 = 0
        resposta4 = 0
        resposta5 = 0
        controler = 0


        #VARIAVEIS TIME
        idtime = "3"
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

       
=======
import matplotlib.pyplot as plt

# Dados para o eixo x e y
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotar a linha
plt.plot(x, y, 'r-')  # 'r-' define a cor e o estilo da linha (vermelho)

# Plotar os pontos
plt.scatter(x, y, c='b')  # 'c' define a cor dos pontos (azul)

# Adicionar rótulos aos pontos
for i, j in zip(x, y):
    plt.text(i, j, f'({i}, {j})')

# Exibir o gráfico
plt.show()
>>>>>>> 34adbae4923dbb91094adb7ab8252057ad239893
