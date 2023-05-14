# site inspiração: https://www.youtube.com/watch?v=gwP4nC5LLZY&t=520s

import customtkinter as ctk
import tkinter as tk
from tkinter import *
import tkcalendar as cal
from calendar import *
#import TelaBV as TBV
import cadastro_turma_time as cadt
# import Tela_Login_API as TLOGIN
import json

janela = ctk.CTk()

class telaAMD_oficial():
   def __init__(self):
      self.janela = janela
      self.tema()
      self.tela()
      self.logo()
      self.titulo()
      self.logout()
      self.tela_atalho()
      janela.mainloop()

#Padrão temas da tela
   def tema(self):
      ctk.set_appearance_mode("dark")
      ctk.set_default_color_theme("blue")
      pass

#padrão da tela
   def tela(self):
      screen_width = janela.winfo_screenwidth()
      screen_height = janela.winfo_screenheight()
      x = (screen_width - 1200) // 2
      y = (screen_height - 650) // 2
      janela.geometry("1200x650+{}+{}".format(x, y))
      janela.geometry("1200x650") 
      janela.title("Tela Administrador")
      janela.iconbitmap("logo_insight.ico")
      janela.resizable(False, False)
      pass

#imagem logo 360
   def logo(self):
      img = PhotoImage(file = "logo_insight.png").subsample(2)
      label_img = ctk.CTkLabel(master=janela, image=img, text="")
      label_img.place(x=35, y=20)

#titulo ADM
   def titulo(self):
      label_tt = ctk.CTkLabel(master=janela, text='Administrador', font=('Roboto',32, 'bold'), text_color="white").place(x=630, y=80)

#Imagem do botão logout
   def logout(self):
      logout = PhotoImage(file = "logout.png").subsample(2)
      Button = ctk.CTkButton(master=janela, image=logout, text="", fg_color="#242424", command=Close, width=40, height=25)
      Button.place(x=1120, y=30)

#logout_button = ctk.CTkButton("logout.JPG", text="", width=300, text_color='blue', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command="s").place(x=45, y=250)

   #frame esquerda
   def tela_atalho(self):
      frame1 = ctk.CTkFrame(master=janela, width=290, height=400, fg_color="#242424")
      frame1.place(x=15, y=180)
      
      # Janela times/turmas
      frame = ctk.CTkFrame(master=janela, width=800, height=370)
      texto =ctk.CTkLabel(master=frame, text="Olá administrador! ;)", font=("Roboto",40),text_color='white').place(x=230, y=150)
      # frame = ctk.CTkScrollableFrame(self, orientation=VERTICAL, Exception=False)
      frame.place(x=330, y=200)
      
      acesso = json.load(open("data_json/users.json", "r"))

      ac_turmas = json.load(open("data_json/turmas.json", "r"))

      for x in range(len(acesso["usuarios"])):
                if(acesso["usuarios"][x]["isActive"] == True):
                    user_nome = acesso["usuarios"][x]["user"]
                    jaResp = acesso["usuarios"][x]["resp"]

      times = []
      turmas = []

      for nome in ac_turmas["turmas"]:
                # times = acesso["usuarios"][x]["times"]
                turmas.append(nome["nometurma"])

      print(turmas)
      timeSelecionado = StringVar()
      turmaSelecionada = StringVar()

      turmaSelecionada.set(turmas[0])

      #Button = ctk.CTkButton(master=frame1,width=180, fg_color="#5CE1E6", text="CADASTROS", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=abre_cadt)
      #Button.place(x=55, y=65)
      #Button = ctk.CTkButton(master=frame1, width=180, fg_color="#5CE1E6", text="USUÁRIO", font = ('Roboto', 18, 'bold'), text_color= ('black'))
      #Button.place(x=55, y=115)
      turmas_label = ctk.CTkLabel(master=janela, text="Turma:", font=("Roboto", 18), text_color='black').place(x=65, y=315)
      turmas_option_menu = ctk.CTkOptionMenu(master=janela, values=turmas, variable=turmaSelecionada, fg_color="#5CE1E6", width=200, text_color='black', text="Turma:", font=("Roboto", 18)).place(x=65, y=315)
     # times_label = ctk.CTkLabel(master=janela, text="Time:", font=("Roboto", 18), text_color='blak').place(x=55, y=335)
      #times_option_menu = ctk.CTkOptionMenu(master=janela, values=times, variable=timeSelecionado, fg_color="#5CE1E6", width=180).place(x=65, y=335)
      #Button = ctk.CTkButton(master=frame1, width=180, text="SPRINTS", fg_color="#5CE1E6", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=abre_sprints)
      #Button.place(x=55, y=315)
      #Button = ctk.CTkButton(master=frame1, width=180, text="SPRINTS", fg_color="#5CE1E6", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=abre_sprints)
      #Button.place(x=55, y=335)
      #Button = ctk.CTkButton(master=frame1, width=180, text="SPRINTS", fg_color="#5CE1E6", font = ('Roboto', 18, 'bold'), text_color= ('black'), command=abre_sprints)
      #Button.place(x=55, y=365)

def abre_cadt():
   janela.destroy()
   cadt.abrir_cadastro()

#botoes widgets

def abre_turmas():
   horizonte = 0
   vertical = 0
   frame2 = ctk.CTkScrollableFrame(master=janela, width=800, height=370, orientation='vertical')
   acesso = json.load(open("data_json/turmas.json", "r"))
   for x in range(len(acesso["turmas"])):
      user_nome = acesso["turmas"][x]["nometurma"]
      btn_user = ctk.CTkButton(master=frame2, text=user_nome, fg_color="#1a1a1a")
      btn_user.pack(fill='x', padx=5, pady=10)
            
      #if(horizonte > 800):
       #  vertical = vertical + 70
        # horizonte = 0


   frame2.place(x=330, y=200)

# OLHAR TELA BV e LOGGIN
# Adicionar integrantes e Dashbords
def abre_times():
   horizonte = 0
   vertical = 0
   frame3 = ctk.CTkScrollableFrame(master=janela, width=800, height=370, orientation='vertical')
   acesso = json.load(open("data_json/turmas.json", "r"))
   for x in range(len(acesso["turmas"])):
      user_nome = acesso["turmas"][x]["times"][x]["nometime"]
      btn_user = ctk.CTkButton(master=frame3, text=user_nome, fg_color="#1a1a1a")
      btn_user.pack(fill='x', padx=5, pady=10)
            
      #if(horizonte > 800):
       #  vertical = vertical + 70
        # horizonte = 0  
  
  
   frame3.place(x=330, y=200)

def abre_sprints():
   horizonte = 0
   vertical = 0
   frame4 = ctk.CTkScrollableFrame(master=janela, width=800, height=370, orientation='vertical')
   acesso = json.load(open("data_json/turmas.json", "r"))
   for x in range(len(acesso["turmas"])):
      user_nome = acesso["turmas"][x]["sprints"][x]["indice"]
      btn_user = ctk.CTkButton(master=frame4, text=user_nome, fg_color="#1a1a1a")
      btn_user.pack(fill='x', padx=5, pady=10)
            
  
   frame4.place(x=330, y=200)

# Opção da tela de logout ir para tela de login
def Close():
    acesso = json.load(open("data_json/users.json", "r"))

    for x in range(len(acesso["usuarios"])):
        acesso["usuarios"][x]["isActive"] = False

    insert_acesso = str(json.dumps(acesso, indent=4))

    with open("data_json/users.json", "w") as arq_json:
        arq_json.write(insert_acesso)

    janela.destroy()
    # TBV.abrir()
    #TLOGIN.abrir_login()

telaAMD_oficial()