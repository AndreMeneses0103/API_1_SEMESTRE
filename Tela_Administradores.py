# ---------------------------------------- Janela de Administradores -------------------------------------------- #
import tkinter as tk
import json
import customtkinter as ctk
import telaADM
from tkinter import *
import ast

#Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Caracteristicas da Tela
janelaADM = ctk.CTk() #Nome
janelaADM.geometry("1200x650") #Tamanho
janelaADM.title("Insigth 360")
janelaADM.iconbitmap("logo_insight.ico")
janelaADM.resizable(False, False) #Limita o tamanho da tela
label = ctk.CTkLabel(master=janelaADM, text="Administradores", text_color=("white"), font=("roboto", 32, "bold")).place(x=500, y=5)

def open_menu():
    janelaADM.destroy()
    telaADM.abrir_tela_adm()
#Voltar para tela inicial
Button=ctk.CTkButton(master=janelaADM, text="Voltar", width=120, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14), command=open_menu).place(x=1000, y=612)


with open("data_json/users.json", "r") as file:
    acesso_usuarios = json.load(file)

usuarios = acesso_usuarios["usuarios"]

frame_3 = ctk.CTkScrollableFrame(master=janelaADM, fg_color='#c0c0c0', width=1000, height=200)
frame_3.place(x=100, y=300)

for x in range (len(usuarios)):
    if usuarios[x]["cargo"] == "user" and usuarios[x]["aceito"]:
        label = ctk.CTkLabel(master=frame_3, text=usuarios[x]["id"], text_color=('black'), font=("Roboto", 20, "bold")).grid(column=0, row=x, padx=25, pady=10)
        button_promote = ctk.CTkButton(master=frame_3, text="Tornar Administrador", width=10, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14)).grid(column=1, row=x, padx=50, pady=5)
            
        def deletar_usuarios(delete):
            def selecao():
                print ("1")

            return selecao
            print(delete)

        button_remove = ctk.CTkButton(master=frame_3, text="Remover Usuário", width=10, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14), command=deletar_usuarios(x)).grid(column=2, row=x, padx=10, pady=5)

    #usuario_remover = usuarios.pop(index)

    with open("data_json/users.json", "w") as file:
        json.dump(acesso_usuarios, file, indent=4)

#Frame.01
frame = ctk.CTkFrame(master=janelaADM, width=1200, height=550)
frame.place(x=0, y=50)
label = ctk.CTkLabel(master=frame, text="Usuários Administradores",  text_color="white", font=("Roboto", 20, "bold")).place(x=495, y=5)
label = ctk.CTkLabel(master=frame, text="Fornecer Acesso Administrativo ou Remover Usuário", text_color="white", font=("Roboto", 20, "bold")).place(x=355, y=260)

#Frame.02
global frame_2
frame_2 = ctk.CTkScrollableFrame(master=frame,fg_color='#c0c0c0',width=1000, height=200)
scroll_1 = frame_2._scrollbar
scroll_1.configure(height=0)
frame_2.place(x=100, y=40)
acesso_usuarios = json.load(open("data_json/users.json", "r"))

user = acesso_usuarios["usuarios"]
for x in range(len(user)):
    if(user[x]["cargo"] == "adm"):
        if(user[x]["aceito"] == True):
            label = ctk.CTkLabel(master=frame_2, text= user[x]["id"], text_color=('black'), font=("Roboto", 20, "bold")).grid(column=0, row=x, padx=100, pady=10)
            button_downgrade=ctk.CTkButton(master=frame_2, text="Remover ADM", width=10, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14)).grid(column=1, row=x, padx=50, pady=5)
            button_save=ctk.CTkButton(master=frame_2, text="Salvar", width=10, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14)).grid(column=2, row=x, padx=50, pady=5)

#Frame.03
frame_3 = ctk.CTkScrollableFrame(master=frame, fg_color='#c0c0c0',width=1000, height=200)
scroll_3 = frame_2._scrollbar
scroll_3.configure(height=0)
frame_3.place(x=100, y=300)

for x in range(len(user)):
    if(user[x]["cargo"] == "user"):
        if(user[x]["aceito"] == True):
            label = ctk.CTkLabel(master=frame_3, text= user[x]["id"], text_color=('black'), font=("Roboto", 20, "bold")).grid(column=0, row=x, padx=25, pady=10)
            button_promote=ctk.CTkButton(master=frame_3, text="Tornar Administrador", width=10, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14)).grid(column=1, row=x, padx=50, pady=5)
            button_remove=ctk.CTkButton(master=frame_3, text="Remover Usuário", width=10, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14)).grid(column=2, row=x, padx=10, pady=5)
            button_save=ctk.CTkButton(master=frame_3, text="Salvar", width=10, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14)).grid(column=3, row=x, padx=50, pady=5)



janelaADM.mainloop()