import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import random
import json
import telaADM
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
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        x = (screen_width - 1500) // 2
        y = (screen_height - 650) // 2
        janela.geometry("1200x650+{}+{}".format(x, y))


        janela.title("Insight 360º")
        janela.iconbitmap("logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela  


    def tela_nova_turma(self):
        #trabalhando com a imagem da tela
        img = PhotoImage(file="logo_insight.png").subsample(3) # reduzindo o tamanho em 50%
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=10, y=10)
        label_tt = ctk.CTkLabel(master=janela, text='Administrador', font=('Roboto',18, 'bold'), text_color="#00FFFF").place(x=50, y=130)
        def voltar():
            janela.destroy()
            telaADM.abrir_tela_adm()
        botao_fim = ctk.CTkButton(master=janela, text="Voltar", font=('Roboto', 14), text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=voltar).place(x=50, y=170)


        #frame a direita
        tela_cadastro_frame = ctk.CTkFrame(master=janela, width=900, height=1000)
        tela_cadastro_frame.pack(side=RIGHT)

        #frame widgets
        label = ctk.CTkLabel(master=tela_cadastro_frame, text="Cadastro de nova turma", font = ('Roboto', 25, 'bold'), text_color= ('white') ).place(x=45, y=40)
        
        #entrada de dados
        user_name_label1 = ctk.CTkLabel(master=tela_cadastro_frame, text="Nome da turma: ", text_color="white", font=('Roboto', 14)).place(x=45,y=100)
        novaturma = tk.StringVar()#criação da variavel 
        novaturma_entry = ctk.CTkEntry(master=tela_cadastro_frame, placeholder_text="Nova turma",placeholder_text_color="gray", width=600, font = ('Roboto', 14), textvariable=novaturma).place(x=45, y=125)

        # Entrada da quantidade de sprints
        quantidade_sprints_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Número de sprints: ", text_color="white", font=('Roboto', 14)).place(x=45,y=175)
        quantidade_sprints = tk.IntVar()
        quantidade_sprints_entry = ctk.CTkEntry(master=tela_cadastro_frame, placeholder_text="Número de sprints:",placeholder_text_color="gray", width=60, font = ('Roboto', 14), textvariable=quantidade_sprints).place(x=45,y=200)
        
        global sprint
        sprint = dict()
        #LISTA QUE ARMAZENA OS DADOS DA SPRINT PARA GRAVAR EM JSON
        sprints = []

        #Funcao que cria labels em scrollableFrames
        def cria_label(titulo, frame, posicaoX, posicaoY, coluna):
            label = ctk.CTkLabel(master=frame, text=titulo, text_color="white", font=('Roboto', 12, 'bold'))
            label.grid(row=posicaoX, column=coluna, pady = posicaoY,sticky=W)

        def armazena_json(idturma='teste', nometurma='teste', opcao=1,sprintsSelecionada='padrao',times='padrao'):
            with open ('data_json/turmas.json', "r") as turmas:
                data_turma = json.load(turmas)

            novos_dados = data_turma

            if (opcao==1):
                dados_novos ={
                        "idturma": idturma,
                        "nometurma": nometurma,
                        "sprints": sprintsSelecionada 
                }
                novos_dados['turmas'].append(dados_novos)
                novos_dados = json.dumps(novos_dados, indent=4)
            else:
                for i in novos_dados:
                    novos_dados["turmas"][0]["times"].append(times)
                    novos_dados = json.dumps(novos_dados, indent=4)
                
            with open ("data_json/turmas.json" , "w") as escrevendo:
                escrevendo.write(novos_dados)


        def define_numero_sprints():
            sprint['turma'] = novaturma.get()
            # Frame onde vai aparecer sprints criadas
            frame_sprints = ctk.CTkScrollableFrame(master=tela_cadastro_frame, width=400, height=200, corner_radius=0, fg_color="transparent",label_text=sprint['turma'] )
            frame_sprints.place(x= 45, y= 390)
            
            #Cria um menu variável de acordo com o numero de sprints
            num_valores = int(quantidade_sprints.get())
            sprints = [str(i) for i in range(1, num_valores+1)]
            sprintSelecionada = ctk.IntVar()
            sprintSelecionada.set(sprints[0])
            opcoes_time = ctk.CTkOptionMenu(master=tela_cadastro_frame, fg_color='gray',values=sprints, variable=sprintSelecionada).place(x=50,y=350)
            
            #titulo periodos
            titulo_periodo_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Período das sprints", text_color="white", font=('Roboto', 25, 'bold')).place(x=45,y=270)
            numero_sprints_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Escolha a sprint", text_color="white", font=('Roboto', 14)).place(x=45,y=320)

            #Entrada da data inicio sprint 
            global fim_sprint, data_seleciona_fim, data_seleciona_inicio, inicio_sprint
            inicio_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Início da sprint", text_color="white", font=('Roboto', 14)).place(x=350,y=320)
            inicio_sprint = DateEntry(master=tela_cadastro_frame, width=10, font=("Roboto", 8), background='#00FFFF', foreground='black', borderwidth=2,locale='pt_BR',date_pattern='dd/mm/yyyy')
            inicio_sprint.place(x= 350, y= 380)

            #Entrada da data final da sprint
            fim_sprint_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Fim da sprint", text_color="white", font=('Roboto', 14)).place(x=550,y=320)
            fim_sprint = DateEntry(master=tela_cadastro_frame,width=10, font=("Roboto", 8), background='#00FFFF', foreground='black', borderwidth=2,locale='pt_BR',date_pattern='dd/mm/yyyy')
            fim_sprint.place(x=550, y=380)
            global hor,alt
            hor = 1
            alt = 1
            #LISTA QUE IRÁ ARMAZENAR TEMPORARIAMENTE AS SPRINTS 
            global sprintsSelecionada
            sprintsSelecionada = []

            def guardaInformacoes():
                global hor,alt
                
                #Puxa as informações de datas e número da sprint
                data_seleciona_inicio = inicio_sprint.get_date()
                data_seleciona_fim = fim_sprint.get_date()
                data_sprint = sprintSelecionada.get()

                data_inicio = str(data_seleciona_inicio)
                mes, dia, ano = data_inicio.split('-')
                nova_data = f"{ano}/{dia}/{mes}"
                
                data_fim = str(data_seleciona_fim)
                mesf, diaf, anof = data_fim.split('-')
                nova_dataf = f"{anof}/{diaf}/{mesf}"

                data_final = "  Inicio: " + str(nova_data) + " // Final: " + str(nova_dataf)
                sprint_select = "  Sprint: " + str(data_sprint)

                #label das sprints criadas
                cria_label(sprint_select, frame_sprints, hor+1, alt, 0)
                cria_label(data_final, frame_sprints, hor+1, alt, 1)
                hor = hor + 1
                
                #VARIAVEIS E LISTA QUE ARMAZENARAM DADOS PARA GRAVAR EM JSON - JHONY
                global idturma, nometurma, sprintsSelecionada
                idturma = sprint['turma'].replace(" ", "").strip()
                numeroaleatorio = random.randint(500, 10000)
                idturma = idturma+str(numeroaleatorio)
                nometurma = sprint['turma']
                
                sprintsSelecionada.append({
                                "indice":str(data_sprint), 
                                "inicioSprint": str(nova_data),
                                "fimSprint":str(nova_dataf)
                                })
                print(sprintsSelecionada)
                
                #armazena_json(idturma=idturma, nometurma=nometurma, sprintsSelecionada=sprintsSelecionada,opcao=1)



            #Botão de OK que vai rodar a função para guardar informações
            botao = ctk.CTkButton(master=tela_cadastro_frame,command=guardaInformacoes, text="OK", text_color=('black'),cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=450)
            botao_proxima_etapa = ctk.CTkButton(master=tela_cadastro_frame, text="Próxima etapa", command=tela_cadastro_time, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=600)
            
        #Botao que confirma o numero de sprints
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
            
            #função que vai definir numero e nome de times de uma turma
            def cria_novos_times():
                numero_times = int(num_times.get())
                lista_times = [str(i) for i in range(1, numero_times+1)]
                timeSelecionado = ctk.IntVar()
                timeSelecionado.set(lista_times[0])
                nomeTime = tk.StringVar()

                global x, y, times
                times = dict()
                y = x = 1
                label_nome_times = ctk.CTkLabel(master=tela_times_frame, text="Nomeie cada um dos times", font=('Roboto', 14),text_color=('white')).place(x=45, y= 200)
                time_nome_entry = ctk.CTkEntry(master=tela_times_frame,placeholder_text="Nome do time", placeholder_text_color="gray", width=480, font=('Roboto', 14), text_color=('white'), textvariable=nomeTime).place(x= 200, y=230)
                qtos_time = ctk.CTkOptionMenu(master=tela_times_frame, fg_color='gray',values=lista_times, variable=timeSelecionado).place(x=45,y=230)

                #frame que vai listar os times criados
                times_frame = ctk.CTkScrollableFrame(master=tela_times_frame, width=650, height=200, corner_radius=0, fg_color="transparent",label_text='Nome dos times')
                times_frame.place(x=45, y= 300)
                timesList = []
                #Funcao que salva os times os times em JSON e cria labels para mostrar o que foi cadastrado
                def salvatimes():
                    global x, y
                    #def cria_label(titulo, frame, posicaoX, posicaoY, coluna):
                    
                    idtime = nomeTime.get().replace(" ", "").strip()
                    numeroaleatorio = random.randint(500, 10000)
                    idtime = idtime+str(numeroaleatorio)

                    time = timeSelecionado.get()
                    team_name = nomeTime.get()
                    team_select = "Time " + str(time)+ ": "
                                        
                    cria_label(team_select, times_frame,y,0,0)
                    cria_label(team_name, times_frame,y,0,1)
                    y+=1
                    print(team_select+ " -> " + team_name)
                    
                    timesList.append({
                            "idtime": idtime,
                            "nometime": nomeTime.get()    
                    })
                    nomeTime.set("")
                    '''
                    time = {"nometime": team_name,
                            "idtime": time
                            }
                    armazena_json(opcao=2, times=time)
                    print(time)'''
                    

                def concluir():
                    print(timesList)
                    print(idturma,"\n", nometurma, "\n",sprintsSelecionada)
                    with open("data_json/turmas.json", "r") as arquivo:
                        dados = json.load(arquivo)


                    for x in range(len(dados['turmas'])):
                        print(x)
                        ordem = x

                    ordem +=1

                    novosdados = dados

                    data_turmas = {
                        "idturma": idturma,
                        "nometurma": nometurma,
                        "ordem": ordem,
                        "sprints": sprintsSelecionada, 
                        "times": timesList
                    }

                    novosdados['turmas'].append(data_turmas)
                    novosdados = json.dumps(novosdados, indent=4)

                    with open('data_json/turmas.json', 'w') as arquivoEscrevendo:
                        arquivoEscrevendo.write(novosdados)
            
                    janela.destroy()
                    import telaADM
                    pass 
                botao_fim = ctk.CTkButton(master=tela_times_frame, text="Concluir", font=('Roboto', 14), text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=concluir).place(x=650, y=600)
                nome_times_botao = ctk.CTkButton(master=tela_times_frame, text="Adicionar",command= salvatimes, font=('Roboto', 14), text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=690, y=230)
            
            num_times_botao = ctk.CTkButton(master=tela_times_frame, text="OK",command= cria_novos_times, font=('Roboto', 14), text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=150, y=130)



tela_cadastro_time()