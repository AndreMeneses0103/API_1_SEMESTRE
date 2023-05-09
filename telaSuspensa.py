import customtkinter as ctk
import tkinter as tk


def janelaSuspensa():
    janelaSuspensa = ctk.CTk()
    janelaSuspensa.title("ALERTA!")
    screen_width = janelaSuspensa.winfo_screenwidth()
    screen_height = janelaSuspensa.winfo_screenheight()
    x = (screen_width - 300) // 2
    y = (screen_height - 100) // 2
    janelaSuspensa.geometry("450x230+{}+{}".format(x, y))
    janelaSuspensa.resizable(False, False)

    testando = tk.StringVar()
    label = ctk.CTkLabel(master=janelaSuspensa, text="Justifique sua escolha: ", font=('Roboto', 15)).pack()
    entry = ctk.CTkEntry(master=janelaSuspensa, width=300, textvariable=testando).pack()

    def destroy():
        
        if testando.get()== "":
            labelAlerta = ctk.CTkLabel(master=janelaSuspensa, text="O preenchimento é obrigatório!").pack()
        else:
            janelaSuspensa.destroy()

    buttonDestroy = ctk.CTkButton(janelaSuspensa, text='Ok', command=destroy).pack()

    janelaSuspensa.mainloop()

janelaSuspensa()