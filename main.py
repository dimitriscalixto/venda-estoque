import tkinter as tk
from ttkthemes import ThemedTk
from cadastro import Tela as cadastro
from atualizar import  Tela as atualizar
from fechamento import Main as fechamento
class Main:
    def __init__(self,master):
        self.janela = master
        self.janela.geometry('500x500')

        self.btn_cadastro = tk.Button(self.janela,command=self.abre_cadastro,text="Cadastrar Produtos")
        self.btn_cadastro.place(x=50,y=0)

        self.btn_atualizar = tk.Button(self.janela, command=self.abre_atualizar, text="Atualizar Produtos")
        self.btn_atualizar.place(x=50, y=50)

        self.btn_fechamento = tk.Button(self.janela, command=self.abre_fechamento, text="Venda Produtos")
        self.btn_fechamento.place(x=50, y=100)
    def abre_cadastro(self):
        cadastro(self.janela)
    def abre_atualizar(self):
        atualizar(self.janela)

    def abre_fechamento(self):
        fechamento(self.janela)
master = ThemedTk(theme="breeze")
app = Main(master)
master.mainloop()