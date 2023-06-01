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
remocao()

frame_3 = ctk.CTkScrollableFrame(master=frame, fg_color='#c0c0c0',width=1000, height=200)
scroll_3 = frame_2._scrollbar
scroll_3.configure(height=0)
frame_3.place(x=100, y=300)

janelaADM.mainloop()