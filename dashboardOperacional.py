import customtkinter as ctk
import json


janelaDashOp = ctk.CTk()

class tela_dashboard_operacional:
    def __init__(self):
        self.janela=janelaDashOp
        self.tema()
        self.tela()
        janelaDashOp.mainloop()
    

    def tema(self):
        ctk.set_appearance_mode("dark") #modo dark
        ctk.set_default_color_theme("dark-blue") #defino a cor do modo dark 
    

    def tela(self):    
        screen_width = janelaDashOp.winfo_screenwidth()
        screen_height = janelaDashOp.winfo_screenheight()
        x = (screen_width - 1500) // 2
        y = (screen_height - 650) // 2
        janelaDashOp.geometry("1200x650+{}+{}".format(x, y))


        janelaDashOp.title("btspadrao/Insight 360º")
        janelaDashOp.iconbitmap("btspadrao/logo_insight.ico")
        janelaDashOp.resizable(False, False) #defino que o usuário não pode redimensionar a tela  

tela_dashboard_operacional()