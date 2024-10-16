import tkinter as tk

janela = tk.Tk()
janela.title("Interface Gráfica com Tkinter")
janela.geometry("300x200")
rotulo = tk.Label(janela, text="Bem-vindo à sua primeira interface gráfica!")
rotulo.pack()
janela.mainloop()
