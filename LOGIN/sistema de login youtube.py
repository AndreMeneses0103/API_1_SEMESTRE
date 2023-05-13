import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Sistema de login")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)

img = PhotoImage(file="log.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=5, y=65)

#frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

#frame widgets
label = customtkinter.CTkLabel(master=frame, text="Sistema de Login", text_font="Roboto")
label.place(x=25, y=5)


janela.mainloop()