import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as cTK
import sqlite3
from sqlite3 import Error
import datetime
from ttkthemes import ThemedTk
import math
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
data = datetime.datetime.now().date()
horario = datetime.datetime.now().time()

produtos_lista = []
produto_preco = []
produto_quantidade = []
lista_labels = []
produtos_id = []
def conecta():
    try:
        con = sqlite3.connect('/home/dimitriscalixto/Área de Trabalho/trabalho-tesi-final/database/banco')
        return con
    except Error as er:
        print('Erro durante a conexão.')
class Fechamento:
    def __init__(self,master):
        self.janela = master
        self.top_level = tk.Toplevel(self.janela)

        self.esquerda  = tk.Frame(self.top_level, width = 500, height = 700, bg='white')
        self.esquerda.pack(side=tk.LEFT)

        self.direita = tk.Frame(self.top_level, width=500, height=700, bg='lightblue')
        self.direita.pack(side=tk.RIGHT)

        self.heading = tk.Label(self.esquerda, text="Sistemas de Vendas/Estoque", font=('arial 26 bold'),bg='white')
        self.heading.place(x=0,y=0)

        self.produto_label = tk.Label(self.direita, text="Produto: ",font=('arial 15 bold'), bg = 'lightblue')
        self.produto_label.place(x=0,y=60)

        self.quantidade_label = tk.Label(self.direita, text="Quantidade: ", font=('arial 15 bold'), bg='lightblue')
        self.quantidade_label.place(x=200, y=60)

        self.valor_label = tk.Label(self.direita, text="Valor: ", font=('arial 15 bold'), bg='lightblue')
        self.valor_label.place(x=380, y=60)

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

        self.total_lbl = tk.Label(self.direita, text='Total Preço: ', font=("arial 25 bold"), bg='lightblue')
        self.total_lbl.place(x=0, y=450)


    def procurar_id(self):
        try:
            sql = "SELECT * FROM produtos WHERE id = ?"
            con = conecta()
            cursor = con.cursor()
            resultado = cursor.execute(sql,(self.id_entry.get(),))
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

            self.carrinho_btn = tk.Button(self.esquerda,text="Carrinho",width=15,height=1,bg='steelblue',fg='white',command=self.carrinho)
            self.carrinho_btn.place(x=290,y=415)

            self.fechamento_btn = tk.Button(self.direita, text='Finalizar Compra', font=('arial 12 bold'),
                                            bg='steelblue',fg='white',command=self.venda)
            self.fechamento_btn.place(x=10, y=620)

            con.commit()
            con.close()
        except:
            messagebox.showerror('Aviso','ID não consta no banco')
    def carrinho(self):
        self.quantidade_valor = int(self.quantidade_entry.get())
        if self.quantidade_valor > int(self.get_estoque):
            tk.messagebox.showinfo('Aviso','Quantidade indisponível!')
        else:
            self.total = (float(self.quantidade_valor)*float(self.get_preco))
            produtos_id.append(self.get_id)
            produtos_lista.append(self.get_nome)
            produto_preco.append(self.total)
            produto_quantidade.append(self.quantidade_valor)
        self.x_index = 0
        self.y_index = 100
        for i in range(len(produtos_lista)):
            self.nometemp = tk.Label(self.direita,text=f'{produtos_lista[i]}',font=('arial 12 bold'), bg='lightblue')
            self.nometemp.place(x=0,y=self.y_index)
            lista_labels.append(self.nometemp)

            self.quantidadetemp = tk.Label(self.direita, text=f'{produto_quantidade[i]}', font=('arial 12 bold'), bg='lightblue')
            self.quantidadetemp.place(x=300, y=self.y_index)
            lista_labels.append(self.quantidadetemp)

            self.precotemp = tk.Label(self.direita, text=f'{produto_preco[i]}', font=('arial 12 bold'),bg='lightblue')
            self.precotemp.place(x=380, y=self.y_index)
            lista_labels.append(self.precotemp)

            self.y_index += 40

            self.total_lbl.configure(text=f'Total: {sum(produto_preco)} R$')

    def limpar_labels(self):
        for label in lista_labels:
            label.destroy()
        produtos_lista.clear()
        produto_preco.clear()
        produto_quantidade.clear()
        produtos_id.clear()



    def venda(self):
            sql = "INSERT INTO venda(id,valor_total,data) VALUES (?,?,?)"
            con = conecta()
            cursor = con.cursor()
            cursor.execute(sql, (None, sum(produto_preco), str(data)))
            con.commit()
            con.close()

            self.venda_id = cursor.lastrowid
            doc = SimpleDocTemplate("nota_fiscal.pdf", pagesize=letter)
            story = []

            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name="Center", alignment=1))

            # Título
            title = "Nota Fiscal"
            story.append(Paragraph(title, styles["Title"]))
            story.append(Spacer(1, 12))
            item_data = []
            for i in range(len(produtos_lista)):
                descricao = produtos_lista[i]
                quantidade = produto_quantidade[i]
                preco_unitario = produto_preco[i]
                subtotal = quantidade * preco_unitario
                item_info = f"{descricao}: {quantidade} x R${preco_unitario:.2f} = R${subtotal:.2f}"
                item_data.append(item_info)
            story.append(Paragraph("Itens da Compra:", styles["Heading2"]))
            for item_info in item_data:
                story.append(Paragraph(item_info, styles["Normal"]))
            story.append(Spacer(1, 12))
            total_info = f"Total da Compra: R${sum(produto_preco):.2f}"
            story.append(Paragraph(total_info, styles["Heading2"]))
            doc.build(story)

            for i in range(len(produtos_lista)):
                self.produto_nome = produtos_lista[i]
                self.produto_preco = produto_preco[i]
                self.produto_quantidade = produto_quantidade[i]
                self.produto_id = produtos_id[i]
                sql = "INSERT INTO itens_venda (id,id_venda,quantidade,preco_unit,produto_id)  VALUES (?,?,?,?,?)"
                con = conecta()
                cursor = con.cursor()
                cursor.execute(sql, (None,self.venda_id,self.produto_quantidade,self.produto_preco,self.produto_id))
                con.commit()
                con.close()
                con = conecta()
                cursor = con.cursor()
                cursor.execute('''
                        UPDATE produtos
                        SET estoque = estoque - ?
                        WHERE id = ?''',(self.produto_quantidade, self.produto_id))
                con.commit()
                con.close()
            Fechamento.limpar_labels(self)
            self.total_lbl.configure(text=f'')
            self.quantidade_entry.delete(0,tk.END)
            self.id_entry.delete(0,tk.END)
            messagebox.showinfo("Aviso",'Compra realizada com sucesso, gerando nota fiscal...')
            self.top_level.destroy()