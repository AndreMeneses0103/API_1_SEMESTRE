import tkinter as tk
import customtkinter as ctk
from tkinter import *
import json
import TelaBV


global avaliado
avaliado = 0

def abrir_avaliacao(sprintAvaliacao, timeAvaliacao, turmaAvaliacao, idturma, idtime):
   
    #IMPORTAÇÃO DO JSON DE USUÁRIOS PRÉ DEFINIDOS
    with open('data_json/users.json', 'r') as usuarios:
            data = json.load(usuarios)

    #BUSCANDO AVALIADOS DO TIME e ids
    usuarios = data["usuarios"]
    #PEGAR O ID DA PESSOA QUE ESTIVER LOGADA
    global idavaliador
    for usuario in usuarios:
        if usuario['isActive'] == True:
            idavaliador = usuario['id']

    avaliados = []
    idavaliados = []
    
    #PEGAR DA TELA DO VINICIUS
    for usuario in usuarios:
        if usuario["idturma"] == idturma and usuario["idtime"] == idtime:
            avaliados.append(usuario['user'])
            idavaliados.append(usuario["id"])
    
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
            y = (screen_height - 650) // 2
            janela.geometry("1200x650+{}+{}".format(x, y))
            
            janela.title("Insight 360º")
            janela.iconbitmap("logo_insight.ico")
            janela.resizable(False, False) #defino que o usuário não pode redimensionar a tela
            pass

        #definição do modo dark
        def tema(self):
            ctk.set_appearance_mode("dark") #modo dark
            ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
            pass

        def tela_avaliação(self):
            img = PhotoImage(file="logo_insight.png").subsample(3) # reduzindo o tamanho em 50%
            label_img = ctk.CTkLabel(master=janela, image=img, text='')
            label_img.place(x=43, y=15)

            for x in range(len(data["usuarios"])):
                if((data["usuarios"][x]["isActive"]) == True):
                    logado = data["usuarios"][x]["user"]
            global nome, sprint, turma, time

            #vincular as variaveis com os dados reais 
           
            nome = logado
            sprint = sprintAvaliacao
            turma = turmaAvaliacao
            time = timeAvaliacao

            label_sprint = ctk.CTkLabel(master=janela, text='Sprint: '+sprint, font=('Roboto', 12, 'bold'), text_color='white').place(x=50, y=150)
            label_turma = ctk.CTkLabel(master=janela, text='Turma: '+turma, font=('Roboto', 12, 'bold'), text_color='white').place(x=50, y=180)
            label_time = ctk.CTkLabel(master=janela, text='Time: '+time, font=('Roboto', 12, 'bold'), text_color='white').place(x=50, y=205)
            label_nome_usuario = ctk.CTkLabel(master=janela, text='Avaliador: '+nome, font=('Roboto', 12, 'bold'), text_color='white').place(x=50, y=235)
            
            janela.protocol("WM_DELETE_WINDOW", Close)


            #FUNÇÃO QUE DEFINE QUEM É O AVALIADO
            def avaliadoFuncao():
                print(avaliados[avaliado])
               
                button_ok = ctk.CTkButton(janela, text='Avaliado: '+avaliados[avaliado], font=('Roboto', 12, 'bold'), text_color='white',width=250,anchor='w', hover_color='#1a1a1a', fg_color='#1a1a1a').place(x=45, y=260)

                pass

            avaliadoFuncao()

            label_autoavaliacao = ctk.CTkLabel(master=janela, text='Integrantes do time: ', font=('Roboto', 12, 'bold')).place(x=50, y=310)
            
            #CONTROLADOR DE POSICIONAMENTO DE TELA
            y_direcao_tela = 340

            for i in range(len(avaliados)):
                label_integrantes = ctk.CTkLabel(master=janela, text=avaliados[i], font=('Roboto', 13, 'bold'), text_color='gray').place(x=50, y=y_direcao_tela)
                y_direcao_tela += 20

           
            #CRIAÇÃO DO FRAME PERGUNTAS
            perguntas_frame = ctk.CTkFrame(master=janela, width=900, height=700)
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
                feedback1 = tk.StringVar()
                feedback2 = tk.StringVar()
                feedback3 = tk.StringVar()
                feedback4 = tk.StringVar()
                feedback5 = tk.StringVar()

                titulo_questionario = ctk.CTkLabel(master=perguntas_frame, text='Questionário Avaliativo', font=('Roboto', 23, 'bold'), text_color='#5CE1E6').place(x=300, y=20)
            
                ypergunta1 = 105
                label_pergunta1 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia a comunicação com o grupo durante essa Sprint?', font=('Roboto', 14)).place(x=70, y=70)
                checkbutton_respostas1 = ctk.CTkRadioButton(master=perguntas_frame, text='Muito Ruim',variable=resposta1, value=1,font=('Roboto', 14), fg_color='#5CE1E6').place(x=70, y=ypergunta1)
                checkbutton_respostas1 = ctk.CTkRadioButton(perguntas_frame, text='Ruim', variable=resposta1, value=2,font=('Roboto', 14), fg_color='#5CE1E6').place(x=220, y=ypergunta1)
                checkbutton_respostas1 = ctk.CTkRadioButton(perguntas_frame, text='Regular', variable=resposta1, value=3,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=330, y=ypergunta1)
                checkbutton_respostas1 = ctk.CTkRadioButton(perguntas_frame, text='Bom', variable=resposta1, value=4,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=460, y=ypergunta1)
                checkbutton_respostas1 = ctk.CTkRadioButton(perguntas_frame, text='Muito Bom', variable=resposta1, value=5,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=570, y=ypergunta1)
                label_pergunta1 = ctk.CTkLabel(master=perguntas_frame, text='Feedback:', font=('Roboto', 14)).place(x=70, y=140)
                entryFeedback = ctk.CTkEntry(master=perguntas_frame, textvariable=feedback1, width=300, font=('Roboto', 14), placeholder_text="Seu feedback").place(x=150, y=140)
               
                ypergunta2 = 215
                label_pergunta2 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia o trabalho em equipe durante essa Sprint?', font=('Roboto', 14)).place(x= 70, y=180)
                checkbutton_respostas2 = ctk.CTkRadioButton(perguntas_frame, text='Muito Ruim',variable=resposta2, value=1,font=('Roboto', 14), fg_color='#5CE1E6').place(x=70, y=ypergunta2)
                checkbutton_respostas2 = ctk.CTkRadioButton(perguntas_frame, text='Ruim', variable=resposta2, value=2,font=('Roboto', 14), fg_color='#5CE1E6' ).place(x=220, y=ypergunta2)
                checkbutton_respostas2 = ctk.CTkRadioButton(perguntas_frame, text='Regular', variable=resposta2, value=3,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=330, y=ypergunta2)
                checkbutton_respostas2 = ctk.CTkRadioButton(perguntas_frame, text='Bom', variable=resposta2, value=4,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=460, y=ypergunta2)
                checkbutton_respostas2 = ctk.CTkRadioButton(perguntas_frame, text='Muito Bom', variable=resposta2, value=5,font=('Roboto', 14), fg_color='#5CE1E6' ).place(x=570, y=ypergunta2)
                label_pergunta2 = ctk.CTkLabel(master=perguntas_frame, text='Feedback:', font=('Roboto', 14)).place(x=70, y=250)
                entryFeedback2 = ctk.CTkEntry(master=perguntas_frame, textvariable=feedback2, width=300, font=('Roboto', 14), placeholder_text="Seu feedback").place(x=150, y=250)
                
                ypergunta3 = 325
                label_pergunta3 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua proatividade durante essa Sprint?', font=('Roboto', 14)).place(x= 70, y=290)
                checkbutton_respostas3 = ctk.CTkRadioButton(perguntas_frame, text='Muito Ruim',variable=resposta3, value=1,font=('Roboto', 14), fg_color='#5CE1E6').place(x=70, y=ypergunta3)
                checkbutton_respostas3 = ctk.CTkRadioButton(perguntas_frame, text='Ruim', variable=resposta3, value=2,font=('Roboto', 14), fg_color='#5CE1E6' ).place(x=220, y=ypergunta3)
                checkbutton_respostas3 = ctk.CTkRadioButton(perguntas_frame, text='Regular', variable=resposta3, value=3,font=('Roboto', 14), fg_color='#5CE1E6' ).place(x=330, y=ypergunta3)
                checkbutton_respostas3 = ctk.CTkRadioButton(perguntas_frame, text='Bom', variable=resposta3, value=4,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=460, y=ypergunta3)
                checkbutton_respostas3 = ctk.CTkRadioButton(perguntas_frame, text='Muito Bom', variable=resposta3, value=5,font=('Roboto', 14), fg_color='#5CE1E6' ).place(x=570, y=ypergunta3)
                label_pergunta3 = ctk.CTkLabel(master=perguntas_frame, text='Feedback:', font=('Roboto', 14)).place(x=70, y=360)
                entryFeedback3 = ctk.CTkEntry(master=perguntas_frame, textvariable=feedback3, width=300, font=('Roboto', 14), placeholder_text="Seu feedback").place(x=150, y=360)
                

                ypergunta4 = 435
                label_pergunta4 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua produtividade durante essa Sprint?', font=('Roboto', 14)).place(x= 70, y=400)
                checkbutton_respostas4 = ctk.CTkRadioButton(perguntas_frame, text='Muito Ruim',variable=resposta4, value=1,font=('Roboto', 14), fg_color='#5CE1E6').place(x=70, y=ypergunta4)
                checkbutton_respostas4 = ctk.CTkRadioButton(perguntas_frame, text='Ruim', variable=resposta4, value=2,font=('Roboto', 14), fg_color='#5CE1E6' ).place(x=220, y=ypergunta4)
                checkbutton_respostas4 = ctk.CTkRadioButton(perguntas_frame, text='Regular', variable=resposta4, value=3,font=('Roboto', 14), fg_color='#5CE1E6' ).place(x=330, y=ypergunta4)
                checkbutton_respostas4 = ctk.CTkRadioButton(perguntas_frame, text='Bom', variable=resposta4, value=4,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=460, y=ypergunta4)
                checkbutton_respostas4 = ctk.CTkRadioButton(perguntas_frame, text='Muito Bom', variable=resposta4, value=5,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=570, y=ypergunta4)
                label_pergunta4 = ctk.CTkLabel(master=perguntas_frame, text='Feedback:', font=('Roboto', 14)).place(x=70, y=470)
                entryFeedback4 = ctk.CTkEntry(master=perguntas_frame, textvariable=feedback4, width=300, font=('Roboto', 14), placeholder_text="Seu feedback").place(x=150, y=470)
                
                ypergunta5 = 545
                label_pergunta5 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua entrega com relação ao prazo do projeto nessa Sprint?', font=('Roboto', 14)).place(x=70, y=510)
                checkbutton_respostas5 = ctk.CTkRadioButton(perguntas_frame, text='Muito Ruim',variable=resposta5, value=1,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=70, y=ypergunta5)
                checkbutton_respostas5 = ctk.CTkRadioButton(perguntas_frame, text='Ruim', variable=resposta5, value=2,font=('Roboto', 14) , fg_color='#5CE1E6').place(x=220, y=ypergunta5)
                checkbutton_respostas5 = ctk.CTkRadioButton(perguntas_frame, text='Regular', variable=resposta5, value=3,font=('Roboto', 14), fg_color='#5CE1E6' ).place(x=330, y=ypergunta5)
                checkbutton_respostas5 = ctk.CTkRadioButton(perguntas_frame, text='Bom', variable=resposta5, value=4,font=('Roboto', 14), fg_color='#5CE1E6' ).place(x=460, y=ypergunta5)
                checkbutton_respostas5 = ctk.CTkRadioButton(perguntas_frame, text='Muito Bom', variable=resposta5, value=5,font=('Roboto', 14), fg_color='#5CE1E6').place(x=570, y=ypergunta5)
                label_pergunta5 = ctk.CTkLabel(master=perguntas_frame, text='Feedback:', font=('Roboto', 14)).place(x=70, y=580)
                entryFeedback5 = ctk.CTkEntry(master=perguntas_frame, textvariable=feedback5, width=300, font=('Roboto', 14), placeholder_text="Seu feedback").place(x=150, y=580)
                
                respostaLista = []
                def proximo_integrante():
                    global avaliado
                    respostas = {}
                    
                    #gravação de respostas
                    respostas["idavaliado"] = idavaliados[avaliado]
                    respostas["resposta1"] = resposta1.get()
                    respostas["feedback1"] = feedback1.get()
                    respostas["resposta2"] = resposta2.get()
                    respostas["feedback2"] = feedback2.get()
                    respostas["resposta3"] = resposta3.get()
                    respostas["feedback3"] = feedback3.get()
                    respostas["resposta4"] = resposta4.get()
                    respostas["feedback4"] = feedback4.get()
                    respostas["resposta5"] = resposta5.get()
                    respostas["feedback5"] = feedback5.get()

                    respostaLista.append(respostas)
                    
                    
                    #MÉTRICAS EM NÚMEROS
                    # 1 - MUITO RUIM / 2 - RUIM / 3 - REGULAR / 4 - BOM / 5 - MUITO BOM

                    #zera os valores das variaveis
                    resposta1.set(0)
                    resposta2.set(0)
                    resposta3.set(0)
                    resposta4.set(0)
                    resposta5.set(0)
                    feedback1.set("")
                    feedback2.set("")
                    feedback3.set("")
                    feedback4.set("")
                    feedback5.set("")

                    
                    #CONTROLADOR
                    avaliado+=1

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
                                

                                novos_dados_respostas['avaliacao'].append(dados_respostas)
                                novos_dados_respostas = json.dumps(novos_dados_respostas, indent=4)

                                with open("data_json/questions.json", "w") as arquivo:
                                   arquivo.write(novos_dados_respostas)


                                with open("data_json/users.json", "r") as arquivo:
                                    data = json.load(arquivo)
                                

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
                    
                    print(respostas) 
                    
                    janelaAlertaAvaliacao.mainloop()      
                 
                    
                #FUNÇÃO QUE VERIFICA SE O USUÁRIO PREENCHEU CORRETAMENTE A AVALIAÇÃO
                def verificacaoPreenchimento():
                    if (resposta1.get() != 0 and resposta2.get() != 0 and resposta3.get() != 0 and resposta4.get() != 0 and resposta5.get() != 0):
                        #CONDICIONAL QUE VERIFICA SE A RESPOSTA DO USUÁRIO FOR ABAIXO DE REGULAR É OBRIGATÓRIO O PREENCHIMENTO DO FEEDBACK
                        if((feedback1.get() == "" and resposta1.get()<4) or (feedback2.get() == "" and resposta2.get()<4) or (feedback3.get() == "" and resposta3.get()<4) or (feedback4.get() == "" and resposta4.get()<4) or (feedback5.get() == "" and resposta5.get()<4)):
                            
                            #JANELA PARA ALERTA DE FEEDBACK OBRIGATORIO P/ RESPOSTAS ABAIXO DE REGULAR
                            janelaFeedbackObrigatorio = ctk.CTk()
                            janelaFeedbackObrigatorio.title("ALERTA!")
                            screen_width = janelaFeedbackObrigatorio.winfo_screenwidth()
                            screen_height = janelaFeedbackObrigatorio.winfo_screenheight()
                            x = (screen_width - 330) // 2
                            y = (screen_height - 180) // 2
                            janelaFeedbackObrigatorio.geometry("330x180+{}+{}".format(x, y))
                            janelaFeedbackObrigatorio.resizable(False, False)
                            label_alerta = ctk.CTkLabel(master=janelaFeedbackObrigatorio, text="\nATENÇÃO!\n\nO preenchimento do feedback\né obrigatório para respostas:\nRegular, Ruim e Muito Ruim\n", font=('Roboto', 15, 'bold')).pack()
                            def destroy_alerta():
                                janelaFeedbackObrigatorio.destroy()
                            button_ok = ctk.CTkButton(janelaFeedbackObrigatorio, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()
                            
                            janelaFeedbackObrigatorio.mainloop()
                        else:
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
            
                button_proximo = ctk.CTkButton(perguntas_frame, text="Próximo", font=('Roboto', 15), fg_color='#5CE1E6', text_color='black', cursor="hand2", width=180, command=verificacaoPreenchimento).place(x=660, y=600)

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

#INSTANCIAMENTO DA CLASSE AVALIAÇÃO
    Avaliação()
# abrir_avaliacao()
