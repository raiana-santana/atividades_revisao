import tkinter as tk

root = tk.Tk()

#Definindo um título
root.title("Janela Tk")
root.geometry("500x400")

#Label é o rótulo
rotulo = tk.Label(root, text="Vou mudar quando você clicar no botão", font=("Arial", 12), fg="#000000")
rotulo.pack()

#Button
def button_click():
    rotulo.config(text="CLICOU NO BOTÃO!!!!!")

button = tk.Button(root, text="Clica aqui po", command=button_click)
button.pack()

#Label é o rótulo
rotulo_entry = tk.Label(root, text="Aí embaixo é o entry", font=("Arial", 9), fg="#000000")
rotulo_entry.pack()

#Entry é a entrada de texto de uma linha
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, bg="pink")
entry.pack()

#Label é o rótulo
rotulo_text = tk.Label(root, text="Aí embaixo é o text", font=("Arial", 9), fg="#000000")
rotulo_text.pack()

#Text é a entrada de texto de várias linhas
text = tk.Text(root, height=5, width=30, wrap="word")
text.pack()

#Frame é o quadro
frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=200)
frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor="center")
frame.pack()

#Canvas é a tela
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack

#Checkbutton é botão de verificação
check_var =  tk.BooleanVar()
check_button = tk.Checkbutton(root, text="Aceitar termos", variable=check_var)
check_button.pack()

#Radiobutton (Botão de ação)
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Opção 1", variable=radio_var, value="1")
radio2 = tk.Radiobutton(root, text="Opção 2", variable=radio_var, value="2")
radio1.pack()
radio2.pack()

#Scale é o controle deslizante
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

#Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="MENU", menu=file_menu)
file_menu.add_command(label="Novo")
file_menu.add_command(label="Abrir")
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit)



root.mainloop()