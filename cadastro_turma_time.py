import json
import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import random

janela = ctk.CTk()

class tela_cadastro_time:
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_nova_turma()
        janela.mainloop()
    
    def tema(self):
        ctk.set_appearance_mode("dark") #modo dark
        ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
    

    def tela(self):    
        janela.geometry("1200x800") #DEFINO O TAMANHO DA JANELA
        janela.title("Cadastro novas turmas")
        janela.iconbitmap("logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela  


    def tela_nova_turma(self):
        #trabalhando com a imagem da tela
        img = PhotoImage(file="logo_insight.png").subsample(3) # reduzindo o tamanho em 50%
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=10, y=10)
        label_tt = ctk.CTkLabel(master=janela, text='Administrador', font=('Roboto',18, 'bold'), text_color="#00FFFF").place(x=50, y=130)

        #frame a direita
        tela_cadastro_frame = ctk.CTkFrame(master=janela, width=900, height=1000)
        tela_cadastro_frame.pack(side=RIGHT)

        #frame widgets
        label = ctk.CTkLabel(master=tela_cadastro_frame, text="Cadastro de nova turma", font = ('Roboto', 25, 'bold'), text_color= ('white') ).place(x=45, y=40)
        
        #entrada de dados
        user_name_label1 = ctk.CTkLabel(master=tela_cadastro_frame, text="Nome da turma: ", text_color="white", font=('Roboto', 14)).place(x=45,y=100)
        novaturma = tk.StringVar()#criação da variavel 
        novaturma_entry = ctk.CTkEntry(master=tela_cadastro_frame, placeholder_text="Nova turma",placeholder_text_color="gray", width=600, font = ('Roboto', 14), textvariable=novaturma).place(x=45, y=125)

        quantidade_sprints_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Número de sprints: ", text_color="white", font=('Roboto', 14)).place(x=45,y=175)
        quantidade_sprints = tk.IntVar()
        quantidade_sprints_entry = ctk.CTkEntry(master=tela_cadastro_frame, placeholder_text="Número de sprints:",placeholder_text_color="gray", width=60, font = ('Roboto', 14), textvariable=quantidade_sprints).place(x=45,y=200)
        
        global sprint
        sprint = dict()
        #LISTA QUE ARMAZENA OS DADOS DA SPRINT PARA GRAVAR EM JSON
        sprints = []
        def define_numero_sprints():

            # Frame onde vai aparecer sprints criadas
            frame_sprints = ctk.CTkFrame(master=tela_cadastro_frame, width=400, height=250, fg_color='gray')
            frame_sprints.place(x= 45, y= 500)

            sprint['turma'] = novaturma.get()
            label_turma = ctk.CTkLabel(master=frame_sprints, text=sprint['turma'], text_color="white", font=('Roboto', 30, 'bold')).place(x=10, y=20)


            #Cria um menu variável de acordo com o numero de sprints
            num_valores = int(quantidade_sprints.get())
            sprints = [str(i) for i in range(1, num_valores+1)]
            sprintSelecionada = IntVar()
            sprintSelecionada.set(sprints[0])
            opcoes_time = ctk.CTkOptionMenu(master=tela_cadastro_frame, fg_color='gray',values=sprints, variable=sprintSelecionada).place(x=50,y=380)
            
            #titulo periodos
            titulo_periodo_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Período das sprints", text_color="white", font=('Roboto', 25, 'bold')).place(x=45,y=270)
            numero_sprints_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Escolha a sprint", text_color="white", font=('Roboto', 14)).place(x=45,y=320)
         
            global fim_sprint, data_seleciona_fim, data_seleciona_inicio, inicio_sprint
            inicio_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Início da sprint", text_color="white", font=('Roboto', 14)).place(x=350,y=320)
            inicio_sprint = DateEntry(master=tela_cadastro_frame, width=10, font=("Roboto", 8), background='#00FFFF', foreground='black', borderwidth=2)
            inicio_sprint.place(x= 350, y= 380)
            data_seleciona_inicio = inicio_sprint.get_date()

            fim_sprint_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Fim da sprint", text_color="white", font=('Roboto', 14)).place(x=550,y=320)
            fim_sprint = DateEntry(master=tela_cadastro_frame,width=10, font=("Roboto", 8), background='#00FFFF', foreground='black', borderwidth=2)
            fim_sprint.place(x=550, y=380)
            data_seleciona_fim = fim_sprint.get_date()
            global hor,alt
            hor = 10
            alt = 10
            #LISTA QUE IRÁ ARMAZENAR TEMPORARIAMENTE AS SPRINTS 
            sprintsSelecionada = []
            #Essa botão vai salvar em JSOn
            def guardaInformacoes():

                global hor,alt
                
                #Salva o nome da turma
                data_seleciona_inicio = inicio_sprint.get_date()
                data_seleciona_fim = fim_sprint.get_date()
                data_sprint = sprintSelecionada.get()

                data_final = "Inicio: " + str(data_seleciona_inicio) + " // Final: " + str(data_seleciona_fim)
                sprint_select = "Sprint: " + str(data_sprint)


                #label das sprints criadas
                alt = alt + 50
                label_sprint = ctk.CTkLabel(master=frame_sprints, text=sprint_select, text_color="white", font=('Roboto', 20, 'bold')).place(x=hor, y=alt)
                alt = alt + 30
                label_data = ctk.CTkLabel(master=frame_sprints, text=data_final, text_color="white", font=('Roboto', 20, 'bold')).place(x=hor, y=alt)


                
                print(f'Inicio da sprint {data_sprint} é {data_seleciona_inicio} e o final é {data_seleciona_fim}')
                #VARIAVEIS E LISTA QUE ARMAZENARAM DADOS PARA GRAVAR EM JSON - JHONY
                global idturma, nometurma
                idturma = sprint['turma'].replace(" ", "").strip()
                numeroaleatorio = random.randint(500, 10000)
                idturma = idturma+str(numeroaleatorio)
                nometurma = sprint['turma']
                
                sprintsSelecionada.append({
                                "indice":str(data_sprint), 
                                "inicioSprint": str(data_seleciona_inicio),
                                "fimSprint":str(data_seleciona_fim)
                                })
                print(sprintsSelecionada)
                
            ''' with open ('data_json/turmas.json', "r") as turmas:
                    data_turma = json.load(turmas)

                novos_dados = data_turma
                dados_novos ={
                        "idturma": idturma,
                        "nometurma": nometurma,
                        "sprints": sprints,
                        "times": "teste"   
                }

                novos_dados['turmas'].append(dados_novos)
                novos_dados = json.dumps(novos_dados, indent=4)


                with open ("data_json/turmas.json" , "w") as escrevendo:
                    escrevendo.write(novos_dados)
'''         
            botao = ctk.CTkButton(master=tela_cadastro_frame,command=guardaInformacoes, text="OK", text_color=('black'),cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=450)
            botao_proxima_etapa = ctk.CTkButton(master=tela_cadastro_frame, text="Próxima etapa", command=tela_cadastro_time, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=600)
            
               
        botao_define_sprint = ctk.CTkButton(master=tela_cadastro_frame, text="Confirmar", font = ('Roboto', 14), command = define_numero_sprints, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=200)
    

        def tela_cadastro_time():
            #Apaga o frame de cadastro de turmas
            tela_cadastro_frame.pack_forget()

            # frame a direita
            tela_times_frame = ctk.CTkFrame(master=janela, width=900, height=1000)
            tela_times_frame.pack(side=RIGHT)

            # criar novos times
            label_novos_times = ctk.CTkLabel(master=tela_times_frame, text="Cadastro de novos times", font=('Roboto', 25, 'bold'), text_color=('white')).place(x=45, y=40)
            label_num_times = ctk.CTkLabel(master=tela_times_frame, text="Defina o número de times", font=('Roboto', 14), text_color=('white')).place(x=45, y=100)

            # define quantidade de times
            num_times = tk.IntVar()
            num_times_entry = ctk.CTkEntry(master=tela_times_frame, placeholder_text="Número de times:",placeholder_text_color="gray", width=60, font=('Roboto', 14), textvariable=num_times).place(x=45, y=130)
            
            def cria_novos_times():
                numero_times = int(num_times.get())
                lista_times = [str(i) for i in range(1, numero_times+1)]
                print(lista_times)

                
                label_nome_times = ctk.CTkLabel(master=tela_times_frame, text="Nomeie cada um dos times", font=('Roboto', 14),text_color=('white')).place(x=45, y= 200)
                time_nome_entry = ctk.CTkEntry(master=tela_times_frame,placeholder_text="Nome do time", placeholder_text_color="gray", width=480, font=('Roboto', 14), text_color=('white')).place(x= 200, y=230)
                qtos_time = ctk.CTkOptionMenu(master=tela_times_frame, fg_color='gray',values=lista_times).place(x=45,y=230)

                #frame que vai listar os times criados
                times_frame = ctk.CTkFrame(master=tela_times_frame, width=650, height=200).place(x=45, y= 300)
                nome_times_botao = ctk.CTkButton(master=tela_times_frame, text="Adicionar",command= salvatimes, font=('Roboto', 14), text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=690, y=230)
                
            def salvatimes():
                pass


            num_times_botao = ctk.CTkButton(master=tela_times_frame, text="OK",command= cria_novos_times, font=('Roboto', 14), text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=150, y=130)




tela_cadastro_time()