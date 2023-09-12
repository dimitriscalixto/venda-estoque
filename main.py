import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as cTK
import sqlite3
from sqlite3 import Error
import datetime
from ttkthemes import ThemedTk

data = datetime.datetime.now().date()
horario = datetime.datetime.now().time()
def conecta():
    try:
        con = sqlite3.connect('/home/dimitriscalixto/Área de Trabalho/trabalho-tesi-final/database/banco')
        return con
    except Error as er:
        print('Erro durante a conexão.')
class Main:
    def __init__(self,master):
        self.janela = master

        self.esquerda  = tk.Frame(self.janela, width = 500, height = 700, bg='white')
        self.esquerda.pack(side=tk.LEFT)

        self.direita = tk.Frame(self.janela, width=500, height=700, bg='lightblue')
        self.direita.pack(side=tk.RIGHT)

        self.heading = tk.Label(self.esquerda, text="Sistemas de Vendas/Estoque", font=('arial 26 bold'),bg='white')
        self.heading.place(x=0,y=0)

        self.produto_label = tk.Label(self.direita, text="Produto: ",font=('arial 18 bold'), bg = 'lightblue')
        self.produto_label.place(x=0,y=60)

        self.quantidade_label = tk.Label(self.direita, text="Quantidade: ", font=('arial 18 bold'), bg='lightblue')
        self.quantidade_label.place(x=300, y=60)

        self.valor_label = tk.Label(self.direita, text="Valor: ", font=('arial 18 bold'), bg='lightblue')
        self.valor_label.place(x=300, y=90)

        self.id_label = tk.Label(self.esquerda, text="Digite o ID: ", font=('arial 12 bold'),bg='white')
        self.id_label.place(x=0, y=80)

        self.id_entry = tk.Entry(self.esquerda, width=25,font=('arial 12 bold'))
        self.id_entry.place(x=190, y=80)

        self.btn_procurar = tk.Button(self.esquerda,text="Pesquisar",width=15,height=1,bg='steelblue',fg='white',command=self.procurar_id)
        self.btn_procurar.place(x=290,y=110)

        self.nome_produto = tk.Label(self.esquerda,text='', font=("arial 23 bold"), bg='white')
        self.nome_produto.place(x=0,y=250)

        self.preco_produto = tk.Label(self.esquerda, text='', font=("arial 23 bold"), bg='white')
        self.preco_produto.place(x=0, y=300)

        self.total = tk.Label(self.direita, text='Total Preço: ', font=("arial 25 bold"), bg='lightblue')
        self.total.place(x=0, y=450)

    def procurar_id(self):
        sql = "SELECT * FROM inventario WHERE id = ?"
        con = conecta()
        cursor = con.cursor()
        resultado = cursor.execute(sql,(self.id_entry.get()))

        for r in resultado:
            self.get_id = r[0]
            self.get_nome = r[1]
            self.get_preco = r[4]
            self.get_estoque = r[2]

        self.nome_produto.configure(text=f'Nome Produto :{self.get_nome}')
        self.preco_produto.configure(text=f'Preço: {self.get_preco} R$')

        self.quantidade = tk.Label(self.esquerda, text="Quantidade: ", font=('arial 18 bold'),bg='white')
        self.quantidade.place(x=0,y=370)

        self.quantidade_entry = tk.Entry(self.esquerda, width=25,font=('arial 12 bold'),bg='white')
        self.quantidade_entry.place(x=190,y=375)

        self.carrinho_btn = tk.Button(self.esquerda,text="Carrinho",width=15,height=1,bg='steelblue',fg='white')
        self.carrinho_btn.place(x=290,y=415)



        con.commit()
        con.close()

master = ThemedTk(theme="breeze")
app = Main(master)
master.mainloop()