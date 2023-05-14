# ---------------------------------------- Janela Prinicipal -------------------------------------------- #
import json
import customtkinter as ctk
from tkinter import *
from subprocess import run


#Janela - Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Janela - Nomeando tela
janela = ctk.CTk()

#Janela - Tamanho 
janela.geometry("1200x650")

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
    import telaADM
    

    

         
#Janela - Botão
Button=ctk.CTkButton(master=janela, text="Voltar", width=120, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14)).place(x=1000, y=612)

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

#Frame 2 - Dimensões
frame_2 = ctk.CTkScrollableFrame(master=frame,fg_color='#c0c0c0',width=1000, height=200)

#Frame 2 - Recebe Scroll
scroll_1 = frame_2._scrollbar
scroll_1.configure(height=0)

#Frame 2 - Indica o principal que a frame ficará
frame_2.place(x=100, y=40)

for x in range(0,10):
    label = ctk.CTkLabel(master=frame_2, text=f"Usuário {x}",  text_color="black", font=('Roboto', 20, "bold")).grid(column=1, row=x, padx=20, pady=10)
    #Frame 2 - Time do Usuário
    label = ctk.CTkLabel(master=frame_2, text="Time 1",  text_color="black", font=('Roboto', 20, "bold")).grid(column=2, row=x, padx=20, pady=10)
    #Frame 2 - Turma do Usuário
    label = ctk.CTkLabel(master=frame_2, text="Turma 1",  text_color="black", font=('Roboto', 20, "bold")).grid(column=3, row=x, padx=50, pady=10)
    #Frame 2 - Inibir dupla seleção no checkbox
    opcao= ctk.IntVar()
    #Frame 2 - Checkbox Usuário
    Checkbutton = ctk.CTkRadioButton(master=frame_2, variable=opcao, value=1, text="Aceitar", text_color=('black'), font=('Roboto', 20, "bold")).grid(column=4, row=x, padx=20, pady=10)
    Checkbutton = ctk.CTkRadioButton(master=frame_2, variable=opcao, value=2, text="Rejeitar", text_color=('black'), font=('Roboto', 20, "bold")).grid(column=5, row=x, padx=20, pady=10)
    #Frame 2 - Botão para salvar seleção
    Button=ctk.CTkButton(master=frame_2, text="Salvar", width=100, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14)).grid(column=6, row=x, padx=80, pady=10)

#Acrescentar uma função de adição para adicionar novos usuários nas linhas abaixo.

# ------------------------------------------------ Frame 3 ------------------------------------------- #
# Frame 3 = Redefinição de senha

#Frame 3 - Dimensões
frame_3 = ctk.CTkScrollableFrame(master=frame, fg_color='#c0c0c0',width=1000, height=200)

#Frame 3 - Recebe Scroll
scroll_3 = frame_2._scrollbar
scroll_3.configure(height=0)

# Frame 3 - Indica o principal que a frame ficará
frame_3.place(x=100, y=300)

for x in range(0,10):
    label = ctk.CTkLabel(master=frame_3, text=f"Usuário {x}", text_color=('black'), font=("Roboto", 20, "bold")).grid(column=0, row=x, padx=100, pady=10)

    #Frame 3 - Barra de entrada "Nova Senha"
    label = ctk.CTkEntry(master=frame_3, placeholder_text="Nova Senha", width=400, font=("Roboto", 14, "bold")).grid(column=1, row=x, pady=10)

    #Frame 3 - Botão para salvar seleção
    Button=ctk.CTkButton(master=frame_3, text="Salvar", width=100, cursor='hand2', text_color=('black'), fg_color="#5CE1E6", hover_color='#2FCDCD', font=('Roboto', 14)).grid(column=4, row=x, padx=100, pady=5)

# ------------------------------------------------ Janela Total ------------------------------------------- #

# Janela Total - Permite exibir todos os componetes contidos na tela. 
janela.mainloop()