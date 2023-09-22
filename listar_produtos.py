import tkinter as tk
from tkinter import ttk
import sqlite3

class Listar:
    def __init__(self, master):
        self.janela = master
        self.top_level = tk.Toplevel(self.janela)
        self.top_level.title("Lista de Produtos")
        self.conexao = sqlite3.connect('/home/dimitriscalixto/Área de Trabalho/trabalho-tesi-final/database/banco')
        self.cursor = self.conexao.cursor()

        self.criar_tabela()
        self.criar_botao_deletar()

    def criar_tabela(self):
        self.tabela = ttk.Treeview(self.top_level, columns=('ID', 'Nome', 'Estoque', 'Fornecedor', 'Numero Fornecedor'))
        self.tabela['show'] = 'headings'

        self.tabela.heading('ID', text='ID')
        self.tabela.heading('Nome', text='Nome')
        self.tabela.heading('Estoque', text='Estoque')
        self.tabela.heading('Fornecedor', text='Fornecedor')
        self.tabela.heading('Numero Fornecedor', text='Numero Fornecedor')

        self.tabela.pack(padx=10, pady=10, fill='both', expand=True)

        self.carregar_produtos()

    def carregar_produtos(self):
        self.cursor.execute("SELECT id, nome, estoque, fornecedor, fornecedor_numero FROM produtos")
        produtos = self.cursor.fetchall()

        for produto in produtos:
            self.tabela.insert('', 'end', values=produto)

    def criar_botao_deletar(self):
        self.botao_deletar = ttk.Button(self.top_level, text="Deletar", command=self.deletar_produto)
        self.botao_deletar.pack(pady=10)

    def deletar_produto(self):
        selecionado = self.tabela.focus()

        if selecionado:
            valores = self.tabela.item(selecionado, 'values')
            produto_id = valores[0]

            self.cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
            self.conexao.commit()
            self.tabela.delete(selecionado)



