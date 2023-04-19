import tkinter as tk
import customtkinter as ctk
from tkinter import *
import json



global avaliado
avaliado = 0
avaliador = input("Digite o nome do avaliador: ")
avaliados = []
avaliados.append(avaliador)
r = "S"
while r == "S":
    avaliados.append(input("Digite o nome do integrante do grupo: "))
    r = input("Deseja adicionar mais um participante S - SIM N - NÃO: ")

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
        janela.geometry("1500x700") #DEFINO O TAMANHO DA JANELA
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

        nome = avaliador
        sprint = "Sprint 1"
        label_nome_usuario = ctk.CTkLabel(master=janela, text='Avaliador: '+nome, font=('Roboto', 20, 'bold')).place(x=50, y=150)
        label_sprint = ctk.CTkLabel(master=janela, text=sprint, font=('Roboto', 20, 'bold')).place(x=50, y=190)



        label_autoavaliacao = ctk.CTkLabel(master=janela, text='Avaliado: ', font=('Roboto', 25, 'bold')).place(x=50, y=260)
        y_direcao_tela = 300
        
        for i in range(len(avaliados)):
            if avaliados[i] == avaliados[avaliado]:  # Substitua "João" pelo nome do avaliado que deseja destacar
                print(avaliados[avaliado])
                label_integrantes = ctk.CTkLabel(master=janela, text=avaliados[i], font=('Roboto', 20, 'bold'), text_color='white').place(x=50, y=y_direcao_tela)

            else:
                label_integrantes = ctk.CTkLabel(master=janela, text=avaliados[i], font=('Roboto', 20, 'bold'), text_color='gray').place(x=50, y=y_direcao_tela)

        
            y_direcao_tela += 30




        button_voltar = ctk.CTkButton(janela, width=200, fg_color='#5CE1E6', text_color='black', hover_color='#00FFFF', text='Tela Inicial', font = ('Roboto', 20), cursor="hand2").place(x=90, y=600)

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
         

            label_pergunta1 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua comunicação com o grupo durante essa Sprint?', font=('Roboto', 18)).place(x=50, y=90)
            checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta1, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=160)
            checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta1, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=160)
            checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta1, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=160)
            checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta1, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=160)
            checkbutton_respostas1 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta1, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=160)
            


            label_pergunta2 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia o seu trabalho em equipe durante essa Sprint?', font=('Roboto', 18)).place(x=50, y=200)
            checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta2, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=290)
            checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta2, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=290)
            checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta2, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=290)
            checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta2, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=290)
            checkbutton_respostas2 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta2, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=290)
        

            label_pergunta3 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua proatividade durante essa Sprint?', font=('Roboto', 18)).place(x=50, y=310)
            checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta3, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=430)
            checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta3, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=430)
            checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta3, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=430)
            checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta3, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=430)
            checkbutton_respostas3 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta3, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=430)
        

            label_pergunta4 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua proatividade durante essa Sprint?', font=('Roboto', 18)).place(x=50, y=420)
            checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta4, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=570)
            checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta4, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=570)
            checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta4, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=570)
            checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta4, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=570)
            checkbutton_respostas4 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta4, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=570)
        

            label_pergunta5 = ctk.CTkLabel(master=perguntas_frame, text='Como você avalia sua entrega com relação ao prazo do projeto nessa Sprint?', font=('Roboto', 18)).place(x=50, y=530)
            checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Muito Ruim',variable=resposta5, value=1,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2",activeforeground='black').place(x=80, y=710)
            checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Ruim', variable=resposta5, value=2,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=280, y=710)
            checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Regular', variable=resposta5, value=3,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=480, y=710)
            checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Bom', variable=resposta5, value=4,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=680, y=710)
            checkbutton_respostas5 = tk.Radiobutton(perguntas_frame, text='Muito Bom', variable=resposta5, value=5,font=('Roboto', 18), background='#212121', foreground='white',selectcolor="#4F4F4F",indicatoron=False, cursor="hand2").place(x=880, y=710)
            

            def proximo_integrante():
            
                global avaliado
                respostas = {}
                
                #gravação de respostas
                respostas["nome: "] = avaliados[avaliado]
                respostas["resposta1"] = resposta1.get()
                respostas["resposta2"] = resposta2.get()
                respostas["resposta3"] = resposta3.get()
                respostas["resposta4"] = resposta4.get()
                respostas["resposta5"] = resposta5.get()
                
                #MÉTRICAS EM NÚMEROS
                # 1 - MUITO RUIM / 2 - RUIM / 3 - REGULAR / 4 - BOM / 5 - MUITO BOM

                #zera os valores das variaveis
                resposta1.set("")
                resposta2.set("")
                resposta3.set("")
                resposta4.set("")
                resposta5.set("")
                


                avaliado +=1
                print(respostas)
                
                #JANELA ALERTA DE CONFIRMAÇÃO DE AVALIAÇÃO REALIZADA
                janelaAlertaAvaliacao = ctk.CTk()
                janelaAlertaAvaliacao.title("ALERTA!")
                janelaAlertaAvaliacao.geometry('300x100')
                label_alerta = ctk.CTkLabel(master=janelaAlertaAvaliacao, text="Avaliação registrada com sucesso!\n", font=('Roboto', 15, 'bold')).pack()
                def destroy_alerta_Avaliacao():
                    janelaAlertaAvaliacao.destroy()
                    
                button_ok = ctk.CTkButton(janelaAlertaAvaliacao, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta_Avaliacao, fg_color='#5CE1E6', text_color='black').pack()
                    
                janelaAlertaAvaliacao.mainloop()      
                pass


            #FUNÇÃO QUE VERIFICA SE O USUÁRIO PREENCHEU CORRETAMENTE A AVALIAÇÃO
            def verificacaoPreenchimento():
                if (resposta1.get() != 0 and resposta2.get() != 0 and resposta3.get() != 0 and resposta4.get() != 0 and resposta5.get() != 0):
                    proximo_integrante()
                else:
                    janelaAlerta = ctk.CTk()
                    janelaAlerta.title("ALERTA!")
                    janelaAlerta.geometry('300x130')
                    label_alerta = ctk.CTkLabel(master=janelaAlerta, text="ATENÇÃO!\nO preenchimento de todos\nos campos é obrigatório!\n", font=('Roboto', 15, 'bold')).pack()
                    def destroy_alerta():
                        janelaAlerta.destroy()
                    button_ok = ctk.CTkButton(janelaAlerta, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta, fg_color='#5CE1E6', text_color='black').pack()
                    
                    janelaAlerta.mainloop()
                pass

            button_proximo = ctk.CTkButton(perguntas_frame, text='Próximo', font=('Roboto', 20, 'bold'), fg_color='#5CE1E6', text_color='black', cursor="hand2", width=230, command=verificacaoPreenchimento).place(x=700, y=640)
        questionario()
                    
                 
        pass
       

#INSTANCIEI (CHAMEI) A CLASSE AVALIAÇÃO
Avaliação()