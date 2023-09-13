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
def listar(sql):
        sql_mostra_cliente = 'SELECT * FROM produtos;'
        con = conecta()
        cursor = con.cursor()  # Objeto que permite executar SQL
        cursor.execute(sql)
        resultado = cursor.fetchall()  # carrega todos os dados em resultado
        # for i in resultado:
        #    print(i)
        con.close()
        return resultado

class  Tela:
    def __init__(self,master):

        self.janela = master
        self.janela.title("Formulário Cadastro")
        self.janela.geometry('500x500')
        self.heading = ttk.Label(self.janela,text="Atualizar Produtos",font=('arial 20 bold'))
        self.heading.place(x=115,y=0)

        self.nome_produto = ttk.Label(self.janela,text="Nome do Produto:",font=('arial 10'))
        self.nome_produto.place(x=15,y=70)

        self.estoque = ttk.Label(self.janela, text="Estoque:", font=('arial 10'))
        self.estoque.place(x=15, y=120)

        self.preco_custo = ttk.Label(self.janela, text="Preco de Custo:", font=('arial 10'))
        self.preco_custo.place(x=15, y=170)

        self.preco_venda = ttk.Label(self.janela, text="Preco de Venda:", font=('arial 10'))
        self.preco_venda.place(x=15, y=220)

        self.nome_fornecedor = ttk.Label(self.janela, text="Nome do Fornecedor:", font=('arial 10'))
        self.nome_fornecedor.place(x=15, y=270)

        self.tel_fornecedor = ttk.Label(self.janela, text="Telefone do Fornecedor:", font=('arial 10'))
        self.tel_fornecedor.place(x=15, y=320)

        self.id = ttk.Label(self.janela, text="Digite o ID:", font=('arial 10'))
        self.id.place(x=15, y=370)

        self.nome_entry = ttk.Entry(self.janela, width=20, font=('arial 10'))
        self.nome_entry.place(x=150,y=70)

        self.estoque_entry = ttk.Entry(self.janela, width=20, font=('arial 10'))
        self.estoque_entry.place(x=150, y=120)

        self.preco_custo_entry = ttk.Entry(self.janela, width=20, font=('arial 10'))
        self.preco_custo_entry.place(x=150, y=170)

        self.preco_venda_entry = ttk.Entry(self.janela, width=20, font=('arial 10'))
        self.preco_venda_entry.place(x=150, y=220)

        self.nome_fornecedor_entry = ttk.Entry(self.janela, width=20, font=('arial 10'))
        self.nome_fornecedor_entry.place(x=150, y=270)

        self.telefone_fornecedor_entry = ttk.Entry(self.janela, width=20, font=('arial 10'))
        self.telefone_fornecedor_entry.place(x=160, y=320)

        self.id_entry = ttk.Entry(self.janela, width=20, font=('arial 10'))
        self.id_entry.place(x=100, y=370)

        self.btn_procura = ttk.Button(self.janela, text="Pesquisar",width=15,command=self.procurar_id)
        self.btn_procura.place(x=270,y=370)
        self.btn_add = ttk.Button(self.janela, width= 25, text="Atualizar",command=self.atualizar)
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
            sql =   ("INSERT INTO produtos (nome,estoque,preco_custo,preco_venda,fornecedor,total_custo,total_preco_venda,lucro,fornecedor_numero) VALUES(?,?,?,?,?,?,?,?,?)")
            con = conecta()
            cursor = con.cursor()
            cursor.execute(sql,(self.nomeproduto,self.estoque,self.precocusto,self.precovenda,self.nomefornecedor,self.totalcusto,self.totalvenda,self.lucro,self.telefornecedor))
            con.commit()
            con.close()
            tk.messagebox.showinfo("Aviso",message="Cadastro do Produto Realizado")

    def procurar_id(self):
        sql = "SELECT * FROM produtos WHERE id = ?"
        con = conecta()
        cursor = con.cursor()
        resultado = cursor.execute(sql,(self.id_entry.get()))

        for r in resultado:
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
        con.commit()
        con.close()
        try:
            self.nome_entry.delete(0,tk.END)
            self.nome_entry.insert(0,str(self.n1))
            self.estoque_entry.delete(0, tk.END)
            self.estoque_entry.insert(0, str(self.n2))
            self.preco_custo_entry.delete(0, tk.END)
            self.preco_custo_entry.insert(0, str(self.n3))
            self.preco_venda_entry.delete(0, tk.END)
            self.preco_venda_entry.insert(0, str(self.n4))
            self.nome_fornecedor_entry.delete(0, tk.END)
            self.nome_fornecedor_entry.insert(0, str(self.n5))
            self.telefone_fornecedor_entry.delete(0, tk.END)
            self.telefone_fornecedor_entry.insert(0, str(self.n9))
        except:
            tk.messagebox.showerror("Erro", message="ID não encontrado")
    def atualizar(self):
        self.u1 = self.nome_entry.get()
        self.u2 = self.estoque_entry.get()
        self.u3 = self.preco_custo_entry.get()
        self.u4 = self.preco_venda_entry.get()
        self.u5 = self.nome_fornecedor_entry.get()
        self.u6 = self.telefone_fornecedor_entry.get()
        sql = "UPDATE produtos SET nome = ?,estoque=?,preco_custo=?,preco_venda=?,fornecedor=?,fornecedor_numero=? WHERE ID = ?"
        con = conecta()
        cursor = con.cursor()
        cursor.execute(sql,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.id_entry.get()))
        con.commit()
        con.close()
        tk.messagebox.showinfo("Aviso", message="Produto atualizado com sucesso")
master = ThemedTk(theme="breeze")
app = Tela(master)
master.mainloop()

