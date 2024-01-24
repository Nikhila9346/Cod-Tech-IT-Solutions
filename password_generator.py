import random
import string
import customtkinter as tk
import pyperclip

janela = tk.CTk()
janela.geometry('479x403+370+164')

janela.grid_columnconfigure(0, weight=0)
janela.grid_columnconfigure(1, weight=0)
janela.grid_rowconfigure(0, weight=0)
janela.grid_rowconfigure(1, weight=0)

label_titulo = tk.CTkLabel(janela, text='Password Generator')
label_titulo.configure(font=('',20))
label_titulo.grid(column=1, row=0, columnspan=2, padx=10, pady=10)

frame = tk.CTkFrame(janela)
frame.grid_columnconfigure(0, weight=0)
frame.grid_rowconfigure(0, weight=0)
frame.grid_rowconfigure(1, weight=0)
frame.grid_rowconfigure(2, weight=0)
frame.grid_rowconfigure(3, weight=0)
frame.grid_rowconfigure(4, weight=0)
frame.grid_rowconfigure(5, weight=0)
frame.grid_rowconfigure(6, weight=0)
frame.grid(column=0, row=1)

check_minusculas_var = tk.StringVar()
check_maiusculas_var = tk.StringVar()
check_especial_var = tk.StringVar()
check_numeros_var = tk.StringVar()

check_letras_minusculas = tk.CTkCheckBox(frame, text='Lowercase letters', variable=check_minusculas_var, onvalue='on', offvalue='off')
check_letras_minusculas.grid(row=0, column=0, padx=10, pady=10)
check_letras_maiusculas = tk.CTkCheckBox(frame, text='Uppercase letters', variable=check_maiusculas_var, onvalue='on', offvalue='off')
check_letras_maiusculas.grid(row=1, column=0, padx=10, pady=10)
check_caracter_especial = tk.CTkCheckBox(frame, text='Special characters', variable=check_especial_var, onvalue='on', offvalue='off')
check_caracter_especial.grid(row=2, column=0, padx=10, pady=10)
check_numeros = tk.CTkCheckBox(frame, text='Numbers', variable=check_numeros_var, onvalue='on', offvalue='off')
check_numeros.grid(row=3, column=0, padx=10, pady=10)
label_tamanho = tk.CTkLabel(frame, text='Number of characters:')
label_tamanho.grid(column=0, row=4, padx=10, pady=10)

def gerar_senha():
    tamanho = int(tamanho_da_senha.get())
    global senha
    caracteres = ''
    senha = ''
    if check_minusculas_var.get() == 'on':
        caracteres += string.ascii_lowercase
    if check_maiusculas_var.get() == 'on':
        caracteres += string.ascii_uppercase
    if check_especial_var.get() == 'on':
        caracteres += string.punctuation
    if check_numeros_var.get() == 'on':
        caracteres += string.digits
    if not caracteres:
        pass
    else:
        for i in range(tamanho):
            senha += random.choice(caracteres)
        senha += '\n'
        output.configure(state='normal')
        output.insert('0.0', senha)
        output.configure(state='disabled')

tamanho_da_senha = tk.CTkEntry(frame, height=5, width=30)
tamanho_da_senha.grid(column=0, row=5, padx=10, pady=10)
btn_gerar = tk.CTkButton(frame, text='Generate', command=gerar_senha)
btn_gerar.grid(column=0, row=6, padx=10, pady=10)
output = tk.CTkTextbox(janela, width=300, height=300)
output.configure(state='disabled')
output.grid(column=1, row=1, padx=10, pady=10)

def copiar():
    pyperclip.copy(senha)

copiar = tk.CTkButton(janela, text='Copy', command=copiar)
copiar.grid(column=1, row=2)

janela.mainloop()