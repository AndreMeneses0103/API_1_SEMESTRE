
# Definir Dicionário Json

# --------------------------------------- Início Tkinter ------------------------------------------------ #

# ---------------------------------------- Janela Prinicipal -------------------------------------------- #
import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Janela é o nome dado a tela criada por CTK
janela = ctk.CTk()

# Tamanho 
janela.geometry("1200x650")

# Título
janela.title("Insigth 360")

# Imagem usada para icone
janela.iconbitmap("logo_insight.ico")

# Ajuste de dimensões da janela desativados
janela.resizable(False, False)


# Identificação do usuário
label = ctk.CTkLabel(master=janela, text="Administrador", text_color=("white"), font=("roboto", 16))
label.place(x=587, y=1)

# Botão
Button=ctk.CTkButton(master=janela, text="MENU INICIAL", width=100, cursor='hand2', text_color=('black'), fg_color='#00FFFF', hover_color='#2FCDCD', font=('Roboto', 16)).place(x=1000, y=600)

# ------------------------------------------------ Frame 1 --------------------------------------------- #
#Frame 1 = Frame Base (estética)

# Frame 1 - Dimensões
frame = ctk.CTkFrame(master=janela, width=1200, height=550)

#Frame 1 - Indica o principal que a frame ficará.
frame.pack(side=RIGHT)

#Criando um novo Frame
#fr_quadro1=frame(app,borderwidth=1,relief="solid")
#fr_quadro1.place(x=10,y=10,width=300,height=300)

# Frame Wigdets 
label = ctk.CTkLabel(master=frame, text="Solicitações de Novos Usuários",  text_color="white", font=('Roboto', 16))
label.place(x=537, y=5)

# ------------------------------------------------ Frame 2 ------------------------------------------- #
#Frame 2 = Aceite de usuários

# Frame 2 - Dimensões
frame_2 = ctk.CTkScrollableFrame(master=frame,fg_color='#00FFFF',width=1000, height=200)

#Recebe Scroll
scroll_1 = frame_2._scrollbar
scroll_1.configure(height=0)

# Frame 2 - Indica o principal que a frame ficará
frame_2.place(x=100, y=40)

# Nome do Usuário 1
label = ctk.CTkLabel(master=frame_2, text="Usuário 1",  text_color="black", font=('Roboto', 20))
label.pack(side=LEFT)

#Variavel capaz de não repetir
aceite_1= ctk.IntVar()
rejeitar_1= ctk.StringVar()

# Checkbox Usuário 1
Checkbutton = ctk.CTkRadioButton(master=frame_2, variable=aceite_1, value=1, text="Aceitar", text_color=('black'), font=('Roboto', 20)).pack()
Checkbutton = ctk.CTkRadioButton(master=frame_2, variable=rejeitar_1, value=2, text="Rejeitar", text_color=('black'), font=('Roboto', 20)).pack(side=RIGHT)

#Acrescentar uma função de adção para adicionar novos usuários nas linhas abaixo.

#Nome do Usuário 2 
#label = ctk.CTkLabel(master=frame_2, text="Usuário 2", text_color=('black'), font=('Roboto', 14))
#label.pack()

# Checkbox Usuário 2
#Checkbutton = ctk.CTkCheckBox(master=frame_2, text="Aceitar", text_color=('black'), font=('Roboto', 14)).pack(side=RIGHT)
#Checkbutton = ctk.CTkCheckBox(master=frame_2, text="Rejeitar", text_color=('black'), font=('Roboto', 14)).pack(side=RIGHT)

# ------------------------------------------------ Frame 3 ------------------------------------------- #
#Frame 3 = Redefinição de senha

# Frame 3 - Dimensões
frame_3 = ctk.CTkScrollableFrame(master=frame, fg_color='#00FFFF',width=1000, height=200)

#Recebe Scroll
scroll_3 = frame_2._scrollbar
scroll_3.configure(height=0)

# Frame 3 - Indica o principal que a frame ficará
frame_3.place(x=100, y=300)

# Redefinição de senha 
label = ctk.CTkLabel(master=frame, text="Redefinição de Senha", text_color="white", font=('Roboto', 16))
label.place(x=550, y=260)

# Integrar com Jason
label = ctk.CTkLabel(master=frame_3, text="Usuário x", text_color=('black'), font=('Roboto', 14))
label.pack()

label = ctk.CTkEntry(master=frame_3, placeholder_text="Nova Senha", width=200).pack()

# Integrar com Jason
label = ctk.CTkLabel(master=frame_3, text="Usuário y", text_color=('black'), font=('Roboto', 14))
label.pack()

label = ctk.CTkEntry(master=frame_3, placeholder_text="Nova Senha", width=200).pack()

# Logo Marca ***************************************************** Erro
#from PIL import Image, ImageTk

# Carrega a imagem usando a biblioteca PIL
#img = Image.open("logo 2.png")
#logo_img = ImageTk.PhotoImage(img)

# Cria um rótulo para exibir a imagem
#logo_label = ctk.CTkLabel(master=frame, image=logo_img)

# Armazena uma referência para evitar que a imagem seja coletada pelo coletor de lixo
#logo_label.image = logo_img  

# Define a posição do rótulo na janela
#logo_label.place(x=550, y=10)  

janela.mainloop()