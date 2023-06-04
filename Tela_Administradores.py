# ---------------------------------------- Janela de Administradores -------------------------------------------- #
import tkinter as tk
import json
import customtkinter as ctk
import telaADM
from tkinter import *
import hashlib
import ast
from customtkinter import *

#Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Caracteristicas da Tela
janelaADM = ctk.CTk() #Nome
janelaADM.geometry("1200x650") #Tamanho
janelaADM.title("btspadrao/Insigth 360")
janelaADM.iconbitmap("btspadrao/logo_insight.ico")
janelaADM.resizable(False, False) #Limita o tamanho da tela
label = ctk.CTkLabel(master=janelaADM, text="Administradores", text_color=("white"), font=("roboto", 32, "bold")).place(x=500, y=5)

def open_menu():
    janelaADM.destroy()
    telaADM.abrir_tela_adm()
#Voltar para tela inicial
imgbeck = PhotoImage(file = "btspadrao/botaovoltar.png").subsample(18)
Button=ctk.CTkButton(master=janelaADM, image=imgbeck, text="Voltar", width=120, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14), command=open_menu).place(x=1000, y=612)


def janela_alert(titulo, mensagem, medida):
    janelaAlertadadosFaltando = ctk.CTk()
    janelaAlertadadosFaltando.title(titulo)
    janelaAlertadadosFaltando.resizable(False, False)
    larg_tela = janelaADM.winfo_screenwidth()
    alt_tela = janelaADM.winfo_screenheight()
    x = (larg_tela - medida) // 2
    y = (alt_tela - 100) // 2
    tamanho = (f"{medida}x100+{x}+{y}")
    janelaAlertadadosFaltando.geometry(tamanho)
    label_alerta = ctk.CTkLabel(master=janelaAlertadadosFaltando, text=mensagem, font=('Roboto', 15, 'bold')).pack()
    
    def destroy_alerta_Dados_faltando():
        janelaAlertadadosFaltando.destroy()

    button_ok = ctk.CTkButton(janelaAlertadadosFaltando, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta_Dados_faltando, fg_color='#5CE1E6', text_color='black').pack()
    janelaAlertadadosFaltando.mainloop()


    button_ok = ctk.CTkButton(janelaAlertadadosFaltando, text="Ok", font=('Roboto', 20, 'bold'), command=destroy_alerta_Dados_faltando, fg_color='#5CE1E6', text_color='black').pack()
    button_cancel = ctk.CTkButton(janelaAlertadadosFaltando, text="Cancel", font=('Roboto', 20, 'bold'), command=cancel, fg_color='#5CE1E6', text_color='black').pack()

    janelaAlertadadosFaltando.mainloop()

#Frame.01
frame = ctk.CTkFrame(master=janelaADM, width=1200, height=550)
frame.place(x=0, y=50)
label = ctk.CTkLabel(master=frame, text="Usuários e Administradores",  text_color="white", font=("Roboto", 20, "bold")).place(x=495, y=5)
label = ctk.CTkLabel(master=frame, text="Cadastro de Novos Administradores", text_color="white", font=("Roboto", 20, "bold")).place(x=450, y=260)

acesso_usuarios = json.load(open("data_json/users.json", "r"))
user = acesso_usuarios["usuarios"]

primeira_vez_admin = 0

def remocao():
    primeira_vez_admin = 1
    #Frame.02
    global frame_2
    frame_2 = ctk.CTkScrollableFrame(master=frame,fg_color='#c0c0c0',width=1000, height=200)
    scroll_1 = frame_2._scrollbar
    scroll_1.configure(height=0)
    frame_2.place(x=100, y=40)
    
    for x in range(len(user)):
        if(user[x]["aceito"] == True):

            def remove(indice):
                def plotar():
                    for z in range(len(user)):
                        if(user[z]["user"] == user[indice]["user"]):
                            #print(user[indice]["user"])
                            user.pop(indice)
                            insert_acesso = (json.dumps(acesso_usuarios, indent=4))

                            with open("data_json/users.json", "w") as arq_json:
                                arq_json.write(insert_acesso)
                            remocao()
                return plotar      
            
            label = ctk.CTkLabel(master=frame_2, text= user[x]["id"], text_color=('black'), font=("Roboto", 20, "bold")).grid(column=0, row=x, padx=100, pady=10)
            button_remove_adm=ctk.CTkButton(master=frame_2, text="Remover Usuário", width=10, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14), command=remove(x)).grid(column=1, row=x, padx=50, pady=5)

if(primeira_vez_admin == 0):
    remocao()

scroll_3 = frame_2._scrollbar
scroll_3.configure(height=0)

var_nome_adm = ctk.StringVar()
var_senha_adm = ctk.StringVar()
var_email_adm = ctk.StringVar()

frame_3 = ctk.CTkFrame(master=frame, fg_color='#2e2d2d',width=1020, height=200)
frame_3.place(x=100, y=300)

text_nome = ctk.CTkLabel(master=frame_3, text="Nome:", font = ('Roboto', 14)).place(x=250, y=20)
nome_adm = ctk.CTkEntry(master=frame_3, placeholder_text="Username", width=400, font = ('Roboto', 14), textvariable=var_nome_adm)
nome_adm.place(x=300, y=20)

text_email = ctk.CTkLabel(master=frame_3, text="Email:", font = ('Roboto', 14)).place(x=250, y=70)
email_adm = ctk.CTkEntry(master=frame_3, placeholder_text="E-mail do Administrador", width=400, font=("Roboto", 14), textvariable=var_email_adm)
email_adm.place(x=300, y=70)

text_senha = ctk.CTkLabel(master=frame_3, text="Senha:", font = ('Roboto', 14)).place(x=250, y=120)
senha_adm = ctk.CTkEntry(master=frame_3, placeholder_text="Senha do Administrador", width=400, font=("Roboto", 14), show="*", textvariable=var_senha_adm)
senha_adm.place(x=300, y=120)

def cadastro_adm():

    if((var_nome_adm.get() == "") or (var_email_adm.get() == "") or (var_senha_adm.get() == "")):
        janela_alert("ALERTA", "Por favor, complete todos os dados\n", 300)
    else:
        with open('data_json/users.json', 'r') as f:
            data = json.load(f)

        senha_nova = var_senha_adm.get()
        encript = hashlib.sha512(senha_nova.encode('utf-8')).hexdigest()
        
        novo_adm = {
            "user":var_nome_adm.get(),
            "id":var_email_adm.get(),
            "idturma": "",
            "idtime": "",
            "cargo":"adm",
            "senha": encript,
            "sprint_atual": 0,
            "isActive": False,
            "aceito": True,
            "resp": False
        }

        

        data['usuarios'].append(novo_adm)
        data = json.dumps(data, indent=4)

        with open('data_json/users.json', 'w') as arquivo:
            arquivo.write(data)
            var_nome_adm.set("")
            var_email_adm.set("")
            var_senha_adm.set("")
            janela_alert("CADASTRADO", "Novo Administrador cadastrado com sucesso!\n", 500)


btn_criar_adm = ctk.CTkButton(master= frame_3, text="Cadastrar", command=cadastro_adm, width=100, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14))
btn_criar_adm.place(x=450, y=170)

janelaADM.mainloop()