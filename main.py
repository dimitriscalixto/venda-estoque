import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from cadastro import Tela as cadastro
from atualizar import Tela as atualizar
from fechamento import Fechamento as fechamento
from listar_produtos import Listar as listamento
import sqlite3
Image.CUBIC = Image.BICUBIC
class Main:
    def __init__(self, master):
        self.janela = master


        self.janela.geometry('500x525')

        self.btn_cadastro = ttk.Button(self.janela, command=self.abre_cadastro, text="Cadastrar Produtos", width=20)
        self.btn_cadastro.place(x=50, y=50)

        self.btn_atualizar = ttk.Button(self.janela, command=self.abre_atualizar, text="Atualizar Produtos", width=20)
        self.btn_atualizar.place(x=50, y=160)

        self.btn_listar = ttk.Button(self.janela, command=self.abre_listar, text="Listar Produtos", width=20)
        self.btn_listar.place(x=50, y=260)

        self.btn_fechamento = ttk.Button(self.janela, command=self.abre_fechamento, text="Venda Produtos", width=20)
        self.btn_fechamento.place(x=50, y=360)


        frame_resumo_mes = ttk.LabelFrame(self.janela, text="Resumo do Mês", padding=(10, 10))
        frame_resumo_mes.place(x= 250,y= 10)

        self.mtr1 = ttk.Meter(frame_resumo_mes, subtext='Lucro', bootstyle='default', interactive=False,amountused=self.lucro(),amounttotal=100000)
        self.mtr1.grid(row=0, column=0, sticky='e', padx=10, pady=10)

        self.mtr2 = ttk.Meter(frame_resumo_mes, subtext='Vendas', bootstyle='default',amountused=self.vendas())
        self.mtr2.grid(row=1, column=0, sticky='e', padx=10, pady=10)

        self.btn_att = ttk.Button(frame_resumo_mes, command=self.atualizar_medidores, text="Atualizar Dados", width=20)
        self.btn_att.grid(row=2,column=0)

    def lucro(self):
        conexao = sqlite3.connect('/home/dimitriscalixto/Área de Trabalho/trabalho-tesi-final/database/banco')
        cursor = conexao.cursor()

        cursor.execute('''
        SELECT SUM(iv.quantidade * (p.preco_venda - p.preco_custo)) AS lucro_total
        FROM produtos AS p
        INNER JOIN itens_venda AS iv ON p.id = iv.produto_id
        ''')
        lucros = cursor.fetchall()

        self.total_lucro = sum(lucro[0] for lucro in lucros)

        conexao.close()
        return self.total_lucro
    def vendas(self):
        conexao = sqlite3.connect('/home/dimitriscalixto/Área de Trabalho/trabalho-tesi-final/database/banco')
        cursor = conexao.cursor()

        cursor.execute("SELECT COUNT(*) FROM venda")
        lucros = cursor.fetchall()

        self.total_vendas = sum(lucro[0] for lucro in lucros)

        conexao.close()
        return self.total_vendas

    def atualizar_medidores(self):
        self.mtr1.configure(amountused= self.lucro())
        self.mtr2.configure(amountused= self.vendas())
    def abre_cadastro(self):
        cadastro(self.janela)

    def abre_atualizar(self):
        atualizar(self.janela)

    def abre_fechamento(self):
        fechamento(self.janela)

    def abre_listar(self):
        listamento(self.janela)

master = ThemedTk(theme="breeze")
app = Main(master)
master.mainloop()