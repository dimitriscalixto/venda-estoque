import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import sqlite3
from sqlite3 import Error

def conecta():
    try:
        con = sqlite3.connect('/home/dimitriscalixto/Área de Trabalho/trabalho-tesi-final/database/banco')
        return con
    except Error as er:
        print('Erro durante a conexão.')
class  Tela:
    def __init__(self,master):

        self.janela = master
        self.top_level = tk.Toplevel(self.janela)
        self.top_level.geometry('500x500')
        self.heading = ttk.Label(self.top_level,text="Cadastro de Produtos",font=('arial 20 bold'))
        self.heading.place(x=115,y=0)

        self.nome_produto = ttk.Label(self.top_level,text="Nome do Produto:",font=('arial 10'))
        self.nome_produto.place(x=15,y=70)

        self.estoque = ttk.Label(self.top_level, text="Estoque:", font=('arial 10'))
        self.estoque.place(x=15, y=120)

        self.preco_custo = ttk.Label(self.top_level, text="Preco de Custo:", font=('arial 10'))
        self.preco_custo.place(x=15, y=170)

        self.preco_venda = ttk.Label(self.top_level, text="Preco de Venda:", font=('arial 10'))
        self.preco_venda.place(x=15, y=220)

        self.nome_fornecedor = ttk.Label(self.top_level, text="Nome do Fornecedor:", font=('arial 10'))
        self.nome_fornecedor.place(x=15, y=270)

        self.tel_fornecedor = ttk.Label(self.top_level, text="Telefone do Fornecedor:", font=('arial 10'))
        self.tel_fornecedor.place(x=15, y=320)

        self.id = ttk.Label(self.top_level, text="ID:", font=('arial 10'))
        self.id.place(x=15, y=370)

        self.nome_entry = ttk.Entry(self.top_level, width=20, font=('arial 10'))
        self.nome_entry.place(x=150,y=70)

        self.estoque_entry = ttk.Entry(self.top_level, width=20, font=('arial 10'))
        self.estoque_entry.place(x=150, y=120)

        self.preco_custo_entry = ttk.Entry(self.top_level, width=20, font=('arial 10'))
        self.preco_custo_entry.place(x=150, y=170)

        self.preco_venda_entry = ttk.Entry(self.top_level, width=20, font=('arial 10'))
        self.preco_venda_entry.place(x=150, y=220)

        self.nome_fornecedor_entry = ttk.Entry(self.top_level, width=20, font=('arial 10'))
        self.nome_fornecedor_entry.place(x=150, y=270)

        self.telefone_fornecedor_entry = ttk.Entry(self.top_level, width=20, font=('arial 10'))
        self.telefone_fornecedor_entry.place(x=160, y=320)

        self.id_entry = ttk.Entry(self.top_level, width=20, font=('arial 10'))
        self.id_entry.place(x=35, y=370)

        self.btn_add = ttk.Button(self.top_level, width= 25, text="Cadastrar",command=self.get_items)
        self.btn_add.place(x=120, y=420)

    def get_items(self):
        self.nomeproduto = self.nome_entry.get()
        self.estoque = self.estoque_entry.get()
        self.precocusto = self.preco_custo_entry.get()
        self.precovenda = self.preco_venda_entry.get()
        self.nomefornecedor = self.nome_fornecedor_entry.get()
        self.telefornecedor = self.telefone_fornecedor_entry.get()

        self.totalcusto = float(self.precocusto) * float(self.estoque)
        self.totalvenda = float(self.precovenda) * float(self.estoque)

        self.lucro = float(self.totalvenda - self.totalcusto)

        if self.nomeproduto == "" or self.estoque == "" or self.precocusto == "" or self.precovenda == "":
            tk.messagebox.showinfo("Preencha todos os campos")
        else:
            sql =   ("INSERT INTO produtos(nome,estoque,preco_custo,preco_venda,fornecedor,total_custo,total_preco_venda,lucro,fornecedor_numero) VALUES(?,?,?,?,?,?,?,?,?)")
            con = conecta()
            cursor = con.cursor()
            cursor.execute(sql,(self.nomeproduto,self.estoque,self.precocusto,self.precovenda,self.nomefornecedor,self.totalcusto,self.totalvenda,self.lucro,self.telefornecedor))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Aviso",message="Cadastro do Produto Realizado")


