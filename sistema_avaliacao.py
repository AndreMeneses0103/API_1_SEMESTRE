import tkinter as tk
import customtkinter as ctk
from tkinter import *
import json
import TelaBV


global avaliado
avaliado = 0


def abrir_avaliacao():
    #IMPORTAÇÃO DO JSON DE USUÁRIOS PRÉ DEFINIDOS
    with open('data_json/users.json', 'r') as usuarios:
            data = json.load(usuarios)

   


    #for xr in range(len(data["usuarios"])):
    
    #BUSCANDO AVALIADOS DO TIME e ids
    usuarios = data["usuarios"]
    #PEGAR O ID DA PESSOA QUE ESTIVER LOGADA
    global idavaliador
    for usuario in usuarios:
        if usuario['isActive'] == True:
            idavaliador = usuario['id']

    avaliados = []
    idavaliados = []
    global idturma, idtime
    idturma = "123"
    idtime = "1234"
    for usuario in usuarios:
        if usuario["idturma"] == idturma and usuario["idtime"] == idtime:
            avaliados.append(usuario['user'])
            idavaliados.append(usuario["id"])
    
        #avaliados.append(data["usuarios"][xr]["user"])
    print(avaliados)


    janela = ctk.CTk()

    #CRIEI CLASSE AVALIAÇÃO
    class Avaliação:
        #função principal que chama todas as outras
        def __init__(self):
            self.tela()
            self.tema()
            self.tela_avaliação()
            janela.mainloop()  
            pass

        #configarações de tela
        def tela(self):   
            
            #ELEMENTOS QUE FAZEM COM QUE A TELA AO INICIAR POSICIONE AO MEIO
            screen_width = janela.winfo_screenwidth()
            screen_height = janela.winfo_screenheight()
            x = (screen_width - 1500) // 2
            y = (screen_height - 700) // 2
            janela.geometry("1500x700+{}+{}".format(x, y))
            
            janela.title("Sistema de login")
            janela.iconbitmap("logo_insight.ico")
            janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
            pass

        #definição do modo dark
        def tema(self):
            ctk.set_appearance_mode("dark") #modo dark
            ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
            pass

        def tela_avaliação(self):
            img = PhotoImage(file="logo_insight.png").subsample(2) # reduzindo o tamanho em 50%
            label_img = ctk.CTkLabel(master=janela, image=img, text='')
            label_img.place(x=20, y=20)

            for x in range(len(data["usuarios"])):
                if((data["usuarios"][x]["isActive"]) == True):
                    logado = data["usuarios"][x]["user"]
            global nome, sprint, turma, time

            nome = "logado"#tirar as aspas quando rodar com a aa
            sprint = "1"
            turma = "Banco de Dados"
            time = "TechHorizon"

            label_sprint = ctk.CTkLabel(master=janela, text='Sprint: '+sprint, font=('Roboto', 17, 'bold'), text_color='white').place(x=50, y=150)
            label_turma = ctk.CTkLabel(master=janela, text='Turma: '+turma, font=('Roboto', 17, 'bold'), text_color='white').place(x=50, y=180)
            label_time = ctk.CTkLabel(master=janela, text='Time: '+time, font=('Roboto', 17, 'bold'), text_color='white').place(x=50, y=205)
            label_nome_usuario = ctk.CTkLabel(master=janela, text='Avaliador: '+nome, font=('Roboto', 17, 'bold'), text_color='white').place(x=50, y=235)
            
            janela.protocol("WM_DELETE_WINDOW", Close)


            #FUNÇÃO QUE DEFINE QUEM É O AVALIADO
            def avaliadoFuncao():
                print(avaliados[avaliado])
                #if label_nome_usuario.winfo_exists():
                #   label_nome_usuario.destroy()
                #else:

                button_ok = ctk.CTkButton(janela, text='Avaliado: '+avaliados[avaliado], font=('Roboto', 17, 'bold'), fg_color='#242424', text_color='white',width=400,anchor='w', hover_color='#242424').place(x=45, y=260)

                #label_nome_usuario = ctk.CTkLabel(master=janela, text='Avaliado: '+avaliados[avaliado], font=('Roboto', 17, 'bold')).place(x=50, y=230)  
                pass

            avaliadoFuncao()

            label_autoavaliacao = ctk.CTkLabel(master=janela, text='Integrantes do time: ', font=('Roboto', 25, 'bold')).place(x=50, y=310)
            #CONTROLADOR DE POSICIONAMENTO DE TELA
            y_direcao_tela = 350

            for i in range(len(avaliados)):
                label_integrantes = ctk.CTkLabel(master=janela, text=avaliados[i], font=('Roboto', 15, 'bold'), text_color='gray').place(x=50, y=y_direcao_tela)
                y_direcao_tela += 30

            #button_voltar = ctk.CTkButton(janela, width=200, fg_color='#5CE1E6', text_color='black', hover_color='#00FFFF', text='Tela Inicial', font = ('Roboto', 20), cursor="hand2").place(x=90, y=600)

            #CRIAÇÃO DO FRAME PERGUNTAS
            perguntas_frame = ctk.CTkFrame(master=janela, width=1100, height=700)
            perguntas_frame.pack(side=RIGHT)

            global avaliadolabel 
            avaliadolabel = 0

            def questionario():
                #VARIAVEIS QUE ARMAZENARAM AS RESPOSTAS DO USUÁRIO   
                resposta1 = tk.IntVar()
                resposta2 = tk.IntVar()
                resposta3 = tk.IntVar()
                resposta4 = tk.IntVar()
                resposta5 = tk.IntVar()


                titulo_pergunta = ctk.CTkLabel(master=perguntas_frame, text='Questionário', font=('Roboto', 30, 'bold'), text_color='#5CE1E6').place(x=300, y=20)
            
                label_pergunta1 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia a comunicação com o grupo durante essa Sprint?', font=('Roboto', 18)).place(x=50, y=90)
                
                
                #JANELAS SUSPENSAS DE FEEDBACKS, CASO A RESPOSTA ESCOLHIDA SEJA INFERIOR A REGULAR
                '''def janelaSuspensa1():
                    janelaSuspensa = ctk.CTk()
                    janelaSuspensa.title("ALERTA!")
                    screen_width = janelaSuspensa.winfo_screenwidth()
                    screen_height = janelaSuspensa.winfo_screenheight()
                    x = (screen_width - 450) // 2
                    y = (screen_height - 230) // 2
                    janelaSuspensa.geometry("450x230+{}+{}".format(x, y))
                    janelaSuspensa.resizable(False, False)
                    
                    feedback1 = tk.IntVar()
                    label = ctk.CTkLabel(master=janelaSuspensa, text="Justifique sua escolha: ", font=('Roboto', 15)).pack()
                    entryTexto = ctk.CTkEntry(master=janelaSuspensa,textvariable=feedback1, width=300).pack()
                    
                    def destroyTeste():
                        
                        print(feedback1.get())
                        print(a, "---")
                        janelaSuspensa.destroy()
                        pass
                    

                    buttonDestroy = ctk.CTkButton(janelaSuspensa, text='Ok', command=destroyTeste).pack()
                    
                    janelaSuspensa.mainloop()
                   
                '''
                checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta1, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=165)
                checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta1, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=165)
                checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta1, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=165)
                checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta1, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=165)
                checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta1, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=165)
                #button = ctk.CTkButton(perguntas_frame, text="testando", command=cs.janelaSuspensa).place(x=80, y=90)

                label_pergunta2 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia o trabalho em equipe durante essa Sprint?', font=('Roboto', 18)).place(x=50, y=180)
                checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta2, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=278)
                checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta2, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=278)
                checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta2, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=278)
                checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta2, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=278)
                checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta2, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=278)
            

                label_pergunta3 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua proatividade durante essa Sprint?', font=('Roboto', 18)).place(x=50, y=270)
                checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta3, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=390)
                checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta3, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=390)
                checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta3, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=390)
                checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta3, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=390)
                checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta3, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=390)
            

                label_pergunta4 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua proatividade durante essa Sprint?', font=('Roboto', 18)).place(x=50, y=360)
                checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta4, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=500)
                checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta4, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=500)
                checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta4, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=500)
                checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta4, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=500)
                checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta4, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=500)
            

                label_pergunta5 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua entrega com relação ao prazo do projeto nessa Sprint?', font=('Roboto', 18)).place(x=50, y=450)
                checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta5, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=615)
                checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta5, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=615)
                checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta5, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=615)
                checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta5, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=615)
                checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta5, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=615)
                
                respostaLista = []
                def proximo_integrante():
                    global avaliado
                    respostas = {}
                    
                    #gravação de respostas
                    respostas["idavaliado"] = idavaliados[avaliado]
                    respostas["resposta1"] = resposta1.get()
                    respostas["resposta2"] = resposta2.get()
                    respostas["resposta3"] = resposta3.get()
                    respostas["resposta4"] = resposta4.get()
                    respostas["resposta5"] = resposta5.get()
                    
                    respostaLista.append(respostas)
                    
                    
                    #MÉTRICAS EM NÚMEROS
                    # 1 - MUITO RUIM / 2 - RUIM / 3 - REGULAR / 4 - BOM / 5 - MUITO BOM

                    #zera os valores das variaveis
                    resposta1.set(0)
                    resposta2.set(0)
                    resposta3.set(0)
                    resposta4.set(0)
                    resposta5.set(0)
                    
                    #CONTROLADOR
                    avaliado+=1
                    #tk.Label.destroy(label_nome_usuario)

                    #JANELA ALERTA DE CONFIRMAÇÃO DE AVALIAÇÃO REALIZADA
                    janelaAlertaAvaliacao = ctk.CTk()
                    janelaAlertaAvaliacao.title("ALERTA!")
                    janelaAlertaAvaliacao.resizable(False, False)
                    screen_width = janelaAlertaAvaliacao.winfo_screenwidth()
                    screen_height = janelaAlertaAvaliacao.winfo_screenheight()
                    x = (screen_width - 300) // 2
                    y = (screen_height - 100) // 2
                    janelaAlertaAvaliacao.geometry("300x100+{}+{}".format(x, y))
                    label_alerta = ctk.CTkLabel(master=janelaAlertaAvaliacao, text="Avaliação registrada com sucesso!\n", font=('Roboto', 15, 'bold')).pack()
                    
                    
                    def destroy_alerta_Avaliacao():
                        janelaAlertaAvaliacao.destroy()

                        #JANELA DE FINALIZAÇÃO DA AVALIAÇÃO
                        def finalizar():
                            controlador = (avaliado - 1)
                            
                            if (avaliados[(controlador)] == avaliados[-1]):
                                print("Respostas listas: ", respostaLista)
                                #  GRAVAÇÃO DAS RESPOSTAS EM JSON
                                dados_respostas = {
                                    "idAvaliador": idavaliador,
                                    "sprint": sprint,
                                    "idturma": idturma,
                                    "idtime": idtime,
                                    "respostas":respostaLista
                                }

                                with open("data_json/questions.json", "r") as arquivo:
                                    data = json.load(arquivo)
                            
                                novos_dados_respostas = data
                                #print("Novos dados já gravado: ", novos_dados_respostas)

                                novos_dados_respostas['avaliacao'].append(dados_respostas)
                                novos_dados_respostas = json.dumps(novos_dados_respostas, indent=4)
                                print(json.dumps(dados_respostas, indent=4))
                                with open("data_json/questions.json", "w") as arquivo:
                                   #  json.dump(json.dumps(novos_dados_respostas, indent=4), arquivo)
                                   arquivo.write(novos_dados_respostas)
                                janelaAlertaFinalizado = ctk.CTk()
                                janelaAlertaFinalizado.title("ALERTA!")
                                janelaAlertaFinalizado.resizable(False, False)
                                screen_width = janelaAlertaFinalizado.winfo_screenwidth()
                                screen_height = janelaAlertaFinalizado.winfo_screenheight()
                                x = (screen_width - 300) // 2
                                y = (screen_height - 100) // 2
                                janelaAlertaFinalizado.geometry("300x100+{}+{}".format(x, y))
                                label_alerta = ctk.CTkLabel(master=janelaAlertaFinalizado, text="Avaliação finalizada!\n", font=('Roboto', 15, 'bold')).pack()
                                def destroy_alerta_Finalizado():
                                    janela.destroy()
                                    janelaAlertaFinalizado.destroy()
                                    TelaBV.abrir()
                                button_ok = ctk.CTkButton(janelaAlertaFinalizado, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta_Finalizado, fg_color='#5CE1E6', text_color='black').pack()   
                                janelaAlertaFinalizado.mainloop()
                            else:
                                avaliadoFuncao()
                                
                        finalizar()
                        
                    button_ok = ctk.CTkButton(janelaAlertaAvaliacao, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta_Avaliacao, fg_color='#5CE1E6', text_color='black').pack()
                    
                    #avaliado +=1
                    print(respostas) 
                    
                    janelaAlertaAvaliacao.mainloop()      
                 
                    
                #FUNÇÃO QUE VERIFICA SE O USUÁRIO PREENCHEU CORRETAMENTE A AVALIAÇÃO
                def verificacaoPreenchimento():
                    if (resposta1.get() != 0 and resposta2.get() != 0 and resposta3.get() != 0 and resposta4.get() != 0 and resposta5.get() != 0):
                        proximo_integrante()
                    elif (resposta1.get() == 0 or resposta2.get() == 0 or resposta3.get() == 0 or resposta4.get() == 0 or resposta5.get() == 0):
                        #TELA ALERTA - NÃO PREENCHIMENTO DAS RESPOSTAS CORRETAMENTE
                        janelaAlerta = ctk.CTk()
                        janelaAlerta.title("ALERTA!")
                        screen_width = janelaAlerta.winfo_screenwidth()
                        screen_height = janelaAlerta.winfo_screenheight()
                        x = (screen_width - 300) // 2
                        y = (screen_height - 100) // 2
                        janelaAlerta.geometry("300x100+{}+{}".format(x, y))
                        janelaAlerta.resizable(False, False)
                        label_alerta = ctk.CTkLabel(master=janelaAlerta, text="ATENÇÃO!\nO preenchimento de todos\nos campos é obrigatório!\n", font=('Roboto', 15, 'bold')).pack()
                        def destroy_alerta():
                            janelaAlerta.destroy()
                        button_ok = ctk.CTkButton(janelaAlerta, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()
                        
                        janelaAlerta.mainloop()
                    pass
            
                button_proximo = ctk.CTkButton(perguntas_frame, text="Próximo", font=('Roboto', 20, 'bold'), fg_color='#5CE1E6', text_color='black', cursor="hand2", width=230, command=verificacaoPreenchimento).place(x=700, y=640)

            questionario()

    def Close():
        acesso = json.load(open("data_json/users.json", "r"))

        for x in range(len(acesso["usuarios"])):
            acesso["usuarios"][x]["isActive"] = False

        insert_acesso = str(json.dumps(acesso, indent=4))

        with open("data_json/users.json", "w") as arq_json:
            arq_json.write(insert_acesso)

        janela.destroy()
        janela.mainloop()

#INSTANCIEI (CHAMEI) A CLASSE AVALIAÇÃO
    Avaliação()
