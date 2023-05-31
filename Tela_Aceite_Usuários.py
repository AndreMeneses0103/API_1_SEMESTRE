# ---------------------------------------- Janela Prinicipal -------------------------------------------- #
import tkinter as tk
import json
import customtkinter as ctk
import hashlib
import telaADM
from tkinter import *
import ast



#Janela - Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Janela - Nomeando tela
janela = ctk.CTk()

#Janela - Tamanho 

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela - 1200) // 2
y = (altura_tela - 650) // 2

janela.geometry(f"1200x650+{x}+{y}")

#Janela - Título
janela.title("Insigth 360")

#Janela - Imagem usada para icone
janela.iconbitmap("logo_insight.ico")

#Janela - Ajuste de dimensões da janela desativados
janela.resizable(False, False)

#Janela - Identificação do usuário
label = ctk.CTkLabel(master=janela, text="Administrador", text_color=("white"), font=("roboto", 32, "bold")).place(x=500, y=1)

def open_menu():
    janela.destroy()
    telaADM.abrir_tela_adm()
        
#Janela - Botão
imgbeck = PhotoImage(file = "botaovoltar.png").subsample(18)
buttonVerificar = ctk.CTkButton(master=janela, text="Voltar", width=120, image=imgbeck, cursor='hand2', text_color=("black"), fg_color="#5CE1E6", font=('Roboto', 14), command=open_menu).place(x=1000, y=612)

def Close():
        acesso = json.load(open("data_json/users.json", "r"))

        for x in range(len(acesso["usuarios"])):
            acesso["usuarios"][x]["isActive"] = False

        insert_acesso = str(json.dumps(acesso, indent=4))

        with open("data_json/users.json", "w") as arq_json:
            arq_json.write(insert_acesso)

        janela.destroy()
        import Tela_Login_API
        #TLOGIN.abrir_login()

    #Imagem do botão logout
logout = PhotoImage(file = "logout.png").subsample(2)
Button = ctk.CTkButton(master=janela, width = 50, image=logout, text="", fg_color="#1a1a1a", command=Close)
Button.place(x=1070, y=7)

# ------------------------------------------------ Frame 1 --------------------------------------------- #
#Frame 1 - Frame Base (Estética)

#Frame 1 - Dimensões
frame = ctk.CTkFrame(master=janela, width=1200, height=550)

#Frame 1 - Indica o principal que a frame ficará
frame.place(x=0, y=50)

#Frame 1 - Solicitação de Novos Usuários 
label = ctk.CTkLabel(master=frame, text="Solicitações de Novos Usuários",  text_color="white", font=("Roboto", 20, "bold")).place(x=465, y=5)

#Frame 1 - Redefinição de Senha 
label = ctk.CTkLabel(master=frame, text="Redefinição de Senha", text_color="white", font=("Roboto", 20, "bold")).place(x=500, y=260)

# ------------------------------------------------ Frame 2 ------------------------------------------- #
# Frame 2 = Aceite de usuários

global frame_2
#Frame 2 - Dimensões
frame_2 = ctk.CTkScrollableFrame(master=frame,fg_color='#c0c0c0',width=1000, height=200)

#Frame 2 - Recebe Scroll
scroll_1 = frame_2._scrollbar
scroll_1.configure(height=0)

#Frame 2 - Indica o principal que a frame ficará
frame_2.place(x=100, y=40)

acesso = json.load(open("data_json/users.json", "r"))

ac_turmas = json.load(open("data_json/turmas.json", "r"))


user = acesso["usuarios"]
tur = ac_turmas["turmas"]

turma_certa = ""
time_certo = ""
posicao = ""
ninguem = 0
v_nome = []
v_opcao = []


for x in range(len(user)):

    for y in range(len(tur)):
        if(user[x]["idturma"] == tur[y]["idturma"]):
            turma_certa = tur[y]["nometurma"]
            posicao = tur[y]["ordem"]


    for z in range(len(tur[posicao]["times"])):
        if(user[x]["idtime"] == tur[posicao]["times"][z]["idtime"]):
            time_certo = tur[posicao]["times"][z]["nometime"]


    if(user[x]["aceito"] == False):

        label = ctk.CTkLabel(master=frame_2, text=user[x]["user"],  text_color="black", font=('Roboto', 16)).grid(column=1, row=x, padx=40, pady=10, sticky=W)
        #Frame 2 - Time do Usuário
        label = ctk.CTkLabel(master=frame_2, text=time_certo,  text_color="black", font=('Roboto', 16)).grid(column=2, row=x, padx=40, pady=10, sticky=W)
        #Frame 2 - Turma do Usuário
        label = ctk.CTkLabel(master=frame_2, text=turma_certa,  text_color="black", font=('Roboto', 16)).grid(column=3, row=x, padx=60, pady=10, sticky=W)
        #Frame 2 - Inibir dupla seleção no checkbox
        opcao = tk.StringVar()
        opcao.set("")
        v_opcao.append(opcao)
        #Frame 2 - Checkbox Usuário
        Checkbuttons = ctk.CTkRadioButton(master=frame_2, variable=opcao, value={"nome":user[x]["user"], "status":'1'}, text="Aceitar", text_color=('black'), font=('Roboto', 16)).grid(column=6, row=x, padx=60, pady=10, sticky=W)
        Checkbuttons = ctk.CTkRadioButton(master=frame_2, variable=opcao, value={"nome":user[x]["user"], "status":'2'}, text="Negar", text_color=('black'), font=('Roboto', 16)).grid(column=7, row=x, padx=60, pady=10, sticky=W)

        #Frame 2 - Botão para salvar seleção
    else:
        ninguem = ninguem + 1

if(ninguem != len(user)):
    Button=ctk.CTkButton(master=frame_2, text="Salvar", width=100, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14), command= (lambda v_nome = user[x]["user"]: mudanca(v_nome))).grid(columnspan=6)

def mudanca(nome):
    global frame_2

    ativos = []
    dict_ativos = []
    vazio = 0
    for opcao in v_opcao:
        if(opcao.get() == ""):
            vazio = 1
        else:
            ativos.append(opcao.get())


    if(vazio == 0):
        for item in ativos:
            dicionario = ast.literal_eval(item)
            dict_ativos.append(dicionario)

        for x in range(len(user)):
            for z in range(len(dict_ativos)):
                if(dict_ativos[z]["nome"] == user[x]["user"]):
                    if(dict_ativos[z]["status"] == "1"):
                        user[x]["aceito"] = True
                        insert_acesso = (json.dumps(acesso, indent=4))
                        with open("data_json/users.json", "w") as arq_json:
                            arq_json.write(insert_acesso)


        frame_2.destroy()
        frame_2 = ctk.CTkScrollableFrame(master=frame,fg_color='#c0c0c0',width=1000, height=200)
        frame_2.place(x=100, y=40)

# ------------------------------------------------ Frame 3 ------------------------------------------- #
# Frame 3 = Redefinição de senha

#Frame 3 - Dimensões
frame_3 = ctk.CTkScrollableFrame(master=frame, fg_color='#c0c0c0',width=1000, height=200)

#Frame 3 - Recebe Scroll
scroll_3 = frame_2._scrollbar
scroll_3.configure(height=0)

# Frame 3 - Indica o principal que a frame ficará
frame_3.place(x=100, y=300)

s_opcao = []

for x in range(len(user)):
    if(user[x]["aceito"] == True):
        label = ctk.CTkLabel(master=frame_3, text= user[x]["user"], text_color=('black'), font=("Roboto", 20, "bold")).grid(column=0, row=x, padx=100, pady=10)

        nova_senha = ctk.StringVar()
        nova_senha.set("")
        s_opcao.append(nova_senha)
        #Frame 3 - Barra de entrada "Nova Senha"
        label = ctk.CTkEntry(master=frame_3, placeholder_text="Nova Senha", width=400, font=("Roboto", 14, "bold"), textvariable=nova_senha).grid(column=1, row=x, pady=10)

        def criar_imprimir(indice):
            def imprimir():
                # print(f'TEXTO VINDO = {s_opcao[indice].get()}')
                # print(f'PESSOA SELECIONADA: {user[indice]["user"]}')

                for z in range(len(user[x]["user"])):
                    if(user[z]["user"] == user[indice]["user"]):
                        user[z]["senha"] = (hashlib.sha512((s_opcao[indice].get()).encode('utf-8')).hexdigest())
                        insert_acesso = (json.dumps(acesso, indent=4))
                        with open("data_json/users.json", "w") as arq_json:
                            arq_json.write(insert_acesso)

            return imprimir 
        #Frame 3 - Botão para salvar seleção
        Button=ctk.CTkButton(master=frame_3, text="Salvar", width=100, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14), command= criar_imprimir(x)).grid(column=4, row=x, padx=100, pady=5)




# ------------------------------------------------ Janela Total ------------------------------------------- #

# Janela Total - Permite exibir todos os componetes contidos na tela. 
janela.mainloop()