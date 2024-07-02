from tkinter import *
from tkinter import ttk
def cadastrar():
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    print("Cadastro concluído!")
    print(f"CPF: {cpf}/ Nome: {nome}/ Data de nascimento: {data_nascimento}")
def cancelar():
    entry_cpf.delete(0, END)
    entry_nome.delete(0, END)
    entry_data_nascimento.delete(0, END)

janela = Tk()
janela.title("Cadastro de Clientes")

label_cpf = Label(janela, text="CPF:")
label_cpf.grid(column=0, row=0, padx=10, pady=5)
entry_cpf = Entry(janela)
entry_cpf.grid(column=1, row=0, padx=10, pady=5)

label_nome = Label(janela, text="Nome:")
label_nome.grid(column=0, row=1, padx=10, pady=5)
entry_nome = Entry(janela)
entry_nome.grid(column=1, row=1, padx=10, pady=5)

label_data_nascimento = Label(janela, text="Data de nascimento:")
label_data_nascimento.grid(column=0, row=2, padx=10, pady=5)
entry_data_nascimento = Entry(janela)
entry_data_nascimento.grid(column=1, row=2, padx=10, pady=5)

botao_cadastrar = Button(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.grid(column=0, row=3, padx=10, pady=10)

botao_cancelar = Button(janela, text="Cancelar", command=cancelar)
botao_cancelar.grid(column=1, row=3, padx=10, pady=10)

janela.mainloop()
