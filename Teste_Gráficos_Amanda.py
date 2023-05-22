import tkinter as tk

# Janela - Aparência
root = tk.Tk()
root.configure(bg='black')

# Janela - Tamanho
root.geometry("1200x650")

# Janela - Título
root.title("Insight 360")

# Janela - Ícone
#root.iconbitmap("logo_insight.ico")

# Janela - Ajuste de dimensões da janela desativados
root.resizable(False, False)

# Frames
frame0 = tk.Frame(root, bg='aquamarine', width=600, height=400)
#frame0 = tk.Scrollbar(root, fg_color='#c0c0c0',width=1000, height=200)
frame0.place(relx=0.5, rely=0.3, anchor='center')

#Frame 2 - Recebe Scroll
#scroll_1 = frame0._scrollbar
#scroll_1.configure(height=0)

frame1 = tk.Frame(frame0, bg='gray', width=100, height=100)
frame1.grid(column=1, row=0, padx=20, pady=10)

frame2 = tk.Frame(frame0, bg='gray', width=100, height=100)
frame2.grid(column=2, row=0, padx=20, pady=10)

frame3 = tk.Frame(frame0, bg='gray', width=100, height=100)
frame3.grid(column=1, row=1, padx=20, pady=10)

frame4 = tk.Frame(frame0, bg='gray', width=100, height=100)
frame4.grid(column=2, row=1, padx=20, pady=10)

frame5 = tk.Frame(root, bg='aquamarine', width=280, height=240)
#frame0 = tk.Scrollbar(root, fg_color='#c0c0c0',width=1000, height=200)
frame5.place(relx=0.5, rely=0.7, anchor='center')

# Iniciar loop da janela
root.mainloop()