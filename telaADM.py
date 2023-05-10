import customtkinter as ctk
import tkinter as tk
from tkinter import *
import TelaBV as TBV
# import Tela_Login_API as TLOGIN
import json

#Padrão temas da tela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#padrão da tela
janela = ctk.CTk()
janela.geometry("1080x540") 
janela.title("Tela Administrador")
janela.iconbitmap("logo_insight.ico")
janela.resizable(False, False)

#imagem logo 360
img = PhotoImage(file = "logo_insight.png").subsample(2)
label_img = ctk.CTkLabel(master=janela, image=img, text="")
label_img.place(x=15, y=20)
#titulo ADM
label_tt = ctk.CTkLabel(master=janela, text='Administrador', font=('Roboto',32, 'bold'), text_color="white").place(x=400, y=80)

def Close():
    acesso = json.load(open("data_json/users.json", "r"))

    for x in range(len(acesso["usuarios"])):
        acesso["usuarios"][x]["isActive"] = False

    insert_acesso = str(json.dumps(acesso, indent=4))

    with open("data_json/users.json", "w") as arq_json:
        arq_json.write(insert_acesso)

    janela.destroy()
    # TBV.abrir()
    TLOGIN.abrir_login()

#Imagem do botão logout
logout = PhotoImage(file = "logout.png").subsample(2)
Button = ctk.CTkButton(master=janela, image=logout, text="", fg_color="#1a1a1a", command=Close)
Button.place(x=900, y=40)




#logout_button = ctk.CTkButton("logout.JPG", text="", width=300, text_color='blue', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command="s").place(x=45, y=250)

#frame esquerda
frame1 = ctk.CTkFrame(master=janela, width=250, height=350)
frame1.place(x=15, y=180)

#lado direito


def abre_turmas():
    horizonte = 0
    vertical = 0
    frame = ctk.CTkFrame(master=janela, width=750, height=350)
    acesso = json.load(open("data_json/users.json", "r"))
    for x in range(len(acesso["usuarios"])):
        user_nome = acesso["usuarios"][x]["user"]
        btn_user = ctk.CTkButton(master=frame, text=user_nome, fg_color="#1a1a1a")
        btn_user.place(x=horizonte, y= vertical)
        horizonte = horizonte + 205
        if(horizonte > 750):
            vertical = vertical + 100
            horizonte = 0


    frame.place(x=300, y=180)







def abre_times():
    frame = ctk.CTkFrame(master=janela, width=750, height=350)
    texto =ctk.CTkLabel(master=frame, text="TIMES ABERTO", font=("Roboto",25),text_color='white').place(x=420, y=214)
    frame.place(x=300, y=180)

# frame3 = ctk.CTkFrame(master=janela, width=100, height=60)
# frame3.place(x=420, y=190)
# frame4 = ctk.CTkFrame(master=janela, width=100, height=100)
# frame4.place(x=300, y=260)
# frame5 = ctk.CTkFrame(master=janela, width=100, height=100)
# frame5.place(x=420, y=260)
# frame6 = ctk.CTkFrame(master=janela, width=245, height=150)
# frame6.place(x=290, y=375)
# frame7 = ctk.CTkFrame(master=janela, width=245, height=150)
# frame7.place(x=550, y=200)
# frame8 = ctk.CTkFrame(master=janela, width=245, height=150)
# frame8.place(x=810, y=200)
# frame9 = ctk.CTkFrame(master=janela, width=245, height=150)
# frame9.place(x=550, y=360)
# frame10 = ctk.CTkFrame(master=janela, width=245, height=150)
# frame10.place(x=810, y=360)

#botoes widgets
Button = ctk.CTkButton(master=frame1,width=180, fg_color="#5CE1E6", text="CADASTROS", font = ('Roboto', 18, 'bold'), text_color= ('black'))
Button.place(x=35, y=20)
Button = ctk.CTkButton(master=frame1, width=180, fg_color="#5CE1E6", text="USUÁRIO", font = ('Roboto', 18, 'bold'), text_color= ('black'))
Button.place(x=35, y=65)
Button = ctk.CTkButton(master=frame1, width=180, fg_color="#5CE1E6", text="TURMAS", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=abre_turmas)
Button.place(x=35, y=155)
Button = ctk.CTkButton(master=frame1, width=180, text="TIMES", fg_color="#5CE1E6", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=abre_times)
Button.place(x=35, y=200)
Button = ctk.CTkButton(master=frame1, width=180, text="SPRINTS", fg_color="#5CE1E6", font = ('Roboto', 18, 'bold'), text_color= ('black'))
Button.place(x=35, y=245)
Button = ctk.CTkButton(master=frame1, width=180, text="INTEGRANTES", fg_color="#5CE1E6", font = ('Roboto', 18, 'bold'), text_color= ('black'))
Button.place(x=35, y=295)

janela.mainloop()