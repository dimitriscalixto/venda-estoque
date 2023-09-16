import tkinter as tk
from tkinter import ttk
import sqlite3


def listar_produtos():
    # Conectar ao banco de dados
    conexao = sqlite3.connect('/home/dimitriscalixto/Área de Trabalho/trabalho-tesi-final/database/banco')
    cursor = conexao.cursor()

    # Executar a consulta SQL para obter os produtos
    cursor.execute("SELECT id, nome, estoque, fornecedor, fornecedor_numero FROM produtos")
    produtos = cursor.fetchall()

    # Fechar a conexão com o banco de dados
    conexao.close()

    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Lista de Produtos")

    # Criar uma tabela para exibir os produtos com as colunas desejadas
    tabela = ttk.Treeview(janela, columns=('ID', 'Nome', 'Estoque', 'Fornecedor', 'Numero Fornecedor'))

    # Configurar a Treeview para não mostrar o cabeçalho da primeira coluna
    tabela['show'] = 'headings'

    tabela.heading('ID', text='ID')
    tabela.heading('Nome', text='Nome')
    tabela.heading('Estoque', text='Estoque')
    tabela.heading('Fornecedor', text='Fornecedor')
    tabela.heading('Numero Fornecedor', text='Numero Fornecedor')

    # Adicionar os produtos à tabela
    for produto in produtos:
        tabela.insert('', 'end', values=produto)

    # Configurar a geometria da tabela
    tabela.pack(padx=10, pady=10, fill='both', expand=True)

    janela.mainloop()


# Chamar a função para listar os produtos
listar_produtos()
