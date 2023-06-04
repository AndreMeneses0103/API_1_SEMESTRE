import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import random
import json
import telaADM
from PIL import Image
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
        x = (screen_width - 1200) // 2
        y = (screen_height - 650) // 2
        janela.geometry(f"1200x650+{x}+{y}")
        janela.title("Insight 360º")
        janela.iconbitmap("btspadrao/logo_insight.ico")
        janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela  


    def tela_nova_turma(self):
        #trabalhando com a imagem da tela
        img = ctk.CTkImage(dark_image=Image.open("btspadrao/logo_insight.png"),size=(230,140)) # reduzindo o tamanho em 50%
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=10, y=10)
        label_tt = ctk.CTkLabel(master=janela, text='Administrador', font=('Roboto',18, 'bold'), text_color="#00FFFF").place(x=50, y=130)

        def voltar():
            janela.destroy()
            telaADM.abrir_tela_adm()
        imgbeck = PhotoImage(file = "btspadrao/botaovoltar.png").subsample(18)    
        buttonVerificar = ctk.CTkButton(master=janela, text="Voltar", width=120, image=imgbeck, cursor='hand2', text_color=("black"), fg_color="#5CE1E6", font=('Roboto', 14), command=voltar).place(x=50, y=170)

        #frame a direita
        tela_cadastro_frame = ctk.CTkFrame(master=janela, width=900, height=1000)
        tela_cadastro_frame.pack(side=RIGHT)

        #frame widgets
        label = ctk.CTkLabel(master=tela_cadastro_frame, text="Cadastro de nova turma", font = ('Roboto', 25, 'bold'), text_color= ('white') ).place(x=45, y=25)
        
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


        def define_numero_sprints():
            if novaturma.get() == "" or quantidade_sprints.get()==0:
                janelaPreenchimentoObrigatorio = ctk.CTk()
                janelaPreenchimentoObrigatorio.title("ALERTA!")
                screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                x = (screen_width - 330) // 2
                y = (screen_height - 180) // 2
                janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                janelaPreenchimentoObrigatorio.resizable(False, False)
                label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nO preenchimento de todos\nos campos é obrigatório\n", font=('Roboto', 15, 'bold')).pack()
                
                
                def destroy_alerta():
                        janelaPreenchimentoObrigatorio.destroy()
                button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                janelaPreenchimentoObrigatorio.mainloop()
            else:
                with open('data_json/turmas.json', "r") as arquivoTurmas:
                    dados_turmas = json.load(arquivoTurmas)

                for nometurmaJson in dados_turmas['turmas']:
                    if nometurmaJson['nometurma'] == novaturma.get():
                        janelaPreenchimentoObrigatorio = ctk.CTk()
                        janelaPreenchimentoObrigatorio.title("ALERTA!")
                        screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                        screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                        x = (screen_width - 330) // 2
                        y = (screen_height - 180) // 2
                        janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                        janelaPreenchimentoObrigatorio.resizable(False, False)
                        label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nEsta turma já está\ncadastrada\n", font=('Roboto', 15, 'bold')).pack()
                        def destroy_alerta():
                                janelaPreenchimentoObrigatorio.destroy()
                        button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                        janelaPreenchimentoObrigatorio.mainloop()
                    else:
                        sprint['turma'] = novaturma.get()
                        # Frame onde vai aparecer sprints criadas
                        frame_sprints = ctk.CTkScrollableFrame(master=tela_cadastro_frame, width=400, height=200, corner_radius=0, fg_color="transparent",label_text=sprint['turma'] )
                        frame_sprints.place(x= 45, y= 390)
                        
                        #Cria um menu variável de acordo com o numero de sprints
                        num_valores = int(quantidade_sprints.get())
                        global sprints
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
                        inicio_sprint.place(x= 450, y= 450)

                        #Entrada da data final da sprint
                        fim_sprint_label = ctk.CTkLabel(master=tela_cadastro_frame, text="Fim da sprint", text_color="white", font=('Roboto', 14)).place(x=550,y=320)
                        fim_sprint = DateEntry(master=tela_cadastro_frame,width=10, font=("Roboto", 8), background='#00FFFF', foreground='black', borderwidth=2,locale='pt_BR',date_pattern='dd/mm/yyyy')
                        fim_sprint.place(x=700, y=450)
                        global hor,alt
                        hor = 1
                        alt = 1
                        #LISTA QUE IRÁ ARMAZENAR TEMPORARIAMENTE AS SPRINTS 
                        global sprintsSelecionada
                        sprintsSelecionada = []

            def guardaInformacoes():
                global idturma, nometurma, sprintsSelecionada
                if sprintsSelecionada != []:
                    for i in sprintsSelecionada:
                        if i['indice'] == str(sprintSelecionada.get()):
                            validador = False
                            janelaPreenchimentoObrigatorio = ctk.CTk()
                            janelaPreenchimentoObrigatorio.title("ALERTA!")
                            screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                            screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                            x = (screen_width - 330) // 2
                            y = (screen_height - 180) // 2
                            janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                            janelaPreenchimentoObrigatorio.resizable(False, False)
                            label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nA sprint já foi cadastrada.\n", font=('Roboto', 15, 'bold')).pack()
                            def destroy_alerta():
                                    janelaPreenchimentoObrigatorio.destroy()
                            button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                            janelaPreenchimentoObrigatorio.mainloop()

                        else:
                            validador = True
                else:
                    validador = True
                
                if validador == True:

                    if inicio_sprint.get_date() < fim_sprint.get_date():
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
                    else: 
                        janelaPreenchimentoObrigatorio = ctk.CTk()
                        janelaPreenchimentoObrigatorio.title("ALERTA!")
                        screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                        screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                        x = (screen_width - 330) // 2
                        y = (screen_height - 180) // 2
                        janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                        janelaPreenchimentoObrigatorio.resizable(False, False)
                        label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nA data de início é maior ou\nigual a data final.\n", font=('Roboto', 15, 'bold')).pack()
                        def destroy_alerta():
                                janelaPreenchimentoObrigatorio.destroy()
                        button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                        janelaPreenchimentoObrigatorio.mainloop()


            #Botão de OK que vai rodar a função para guardar informações
            botao = ctk.CTkButton(master=tela_cadastro_frame,command=guardaInformacoes, text="OK", text_color=('black'),cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=450)
            botao_proxima_etapa = ctk.CTkButton(master=tela_cadastro_frame, text="Próxima etapa", command=tela_cadastro_time, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=600)
            

        #Botao que confirma o numero de sprints
        botao_define_sprint = ctk.CTkButton(master=tela_cadastro_frame, text="Confirmar", font = ('Roboto', 14), command = define_numero_sprints, text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=500, y=200)
    

        def tela_cadastro_time():
            global sprintsSelecionada, sprints, y
            y= 0
            print(sprints)
            validadorTamanho = False
          
            for listQuantidadeSprints in sprints:
                for listSprintSelecionada in sprintsSelecionada:
                    if listSprintSelecionada['indice'] == listQuantidadeSprints:
                         validadorTamanho = True
                    else:
                         validadorTamanho = False
             
            
            if validadorTamanho == False:
                janelaPreenchimentoObrigatorio = ctk.CTk()
                janelaPreenchimentoObrigatorio.title("ALERTA!")
                screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                x = (screen_width - 330) // 2
                y = (screen_height - 180) // 2
                janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                janelaPreenchimentoObrigatorio.resizable(False, False)
                label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nAs sprints não foram totalmente\npreenchidas.\n", font=('Roboto', 15, 'bold')).pack()
                
                
                def destroy_alerta():
                        janelaPreenchimentoObrigatorio.destroy()
                button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                janelaPreenchimentoObrigatorio.mainloop()
            else:

                #Apaga o frame de cadastro de turmas
                tela_cadastro_frame.pack_forget()

                # frame a direita
                tela_times_frame = ctk.CTkFrame(master=janela, width=900, height=1000)
                tela_times_frame.pack(side=RIGHT)

                # criar novos times
                label_novos_times = ctk.CTkLabel(master=tela_times_frame, text="Cadastro de novos times", font=('Roboto', 25, 'bold'), text_color=('white')).place(x=45, y=25)
                nomeTime = tk.StringVar()

                times = dict()
                y = x = 1
                label_nome_times = ctk.CTkLabel(master=tela_times_frame, text="Adicionar times", font=('Roboto', 14),text_color=('white')).place(x=45, y= 70)
                time_nome_entry = ctk.CTkEntry(master=tela_times_frame,placeholder_text="Nome do time", placeholder_text_color="gray", width=550, font=('Roboto', 14), text_color=('white'), textvariable=nomeTime).place(x= 45, y=110)

                #frame que vai listar os times criados
                times_frame = ctk.CTkScrollableFrame(master=tela_times_frame, width=550, height=350, corner_radius=0, fg_color="transparent",label_text='Nome dos times')
                times_frame.place(x=45, y= 200)
                timesList = []
               

                #Funcao que salva os times os times em JSON e cria labels para mostrar o que foi cadastrado
                def salvatimes():
                    global x, y
                    
                    if nomeTime.get() == "":
                        janelaPreenchimentoObrigatorio = ctk.CTk()
                        janelaPreenchimentoObrigatorio.title("ALERTA!")
                        screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                        screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                        x = (screen_width - 330) // 2
                        y = (screen_height - 180) // 2
                        janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                        janelaPreenchimentoObrigatorio.resizable(False, False)
                        label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nO preenchimento de todos os\ncampos é obrigatório.\n", font=('Roboto', 15, 'bold')).pack()
                        def destroy_alerta():
                                janelaPreenchimentoObrigatorio.destroy()
                        button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                        janelaPreenchimentoObrigatorio.mainloop()
                    else:
                        if timesList != []:
                             for i in timesList:
                                  if i['nometime']==nomeTime.get():
                                       validadorTime = False
                                  else:
                                       validadorTime = True
                        else:  
                             validadorTime = True 


                        if validadorTime == True:  
                            idtime = nomeTime.get().replace(" ", "").strip()
                            numeroaleatorio = random.randint(500, 10000)
                            idtime = idtime+str(numeroaleatorio)

                            #time = timeSelecionado.get()
                            team_name = nomeTime.get()
                            team_select = "Time: "
                                                
                            cria_label(team_select, times_frame,y,0,0)
                            cria_label(team_name, times_frame,y,0,1)
                            y+=1
                            print(team_select+ " -> " + team_name)
                            
                            timesList.append({
                                    "idtime": idtime,
                                    "nometime": nomeTime.get()    
                            })
                            nomeTime.set("")
                        else:
                            janelaPreenchimentoObrigatorio = ctk.CTk()
                            janelaPreenchimentoObrigatorio.title("ALERTA!")
                            screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                            screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                            x = (screen_width - 330) // 2
                            y = (screen_height - 180) // 2
                            janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                            janelaPreenchimentoObrigatorio.resizable(False, False)
                            label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nTime já cadastrado.\n", font=('Roboto', 15, 'bold')).pack()
                            def destroy_alerta():
                                    janelaPreenchimentoObrigatorio.destroy()
                            button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                            janelaPreenchimentoObrigatorio.mainloop()
                            

                def concluir():
                    if timesList == []:
                        janelaPreenchimentoObrigatorio = ctk.CTk()
                        janelaPreenchimentoObrigatorio.title("ALERTA!")
                        screen_width = janelaPreenchimentoObrigatorio.winfo_screenwidth()
                        screen_height = janelaPreenchimentoObrigatorio.winfo_screenheight()
                        x = (screen_width - 330) // 2
                        y = (screen_height - 180) // 2
                        janelaPreenchimentoObrigatorio.geometry("330x180+{}+{}".format(x, y))
                        janelaPreenchimentoObrigatorio.resizable(False, False)
                        label_alerta = ctk.CTkLabel(master=janelaPreenchimentoObrigatorio, text="\nATENÇÃO!\n\nÉ necessária a entrada \nde pelo menos um time.\n", font=('Roboto', 15, 'bold')).pack()
                        def destroy_alerta():
                                janelaPreenchimentoObrigatorio.destroy()
                        button_ok = ctk.CTkButton(janelaPreenchimentoObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()   
                        janelaPreenchimentoObrigatorio.mainloop()

                    else:
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
                        telaADM.abrir_tela_adm()
                     

                botao_fim = ctk.CTkButton(master=tela_times_frame, text="Concluir", font=('Roboto', 14), text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD', command=concluir).place(x=650, y=600)
                nome_times_botao = ctk.CTkButton(master=tela_times_frame, text="Adicionar",command= salvatimes, font=('Roboto', 14), text_color=('black'), cursor='hand2', fg_color='#00FFFF', hover_color='#2FCDCD').place(x=650, y=110)
           

tela_cadastro_time()
