import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image
import sqlite3

conexao = sqlite3.connect('/home/dimitriscalixto/Área de Trabalho/trabalho-tesi-final/database/banco')
cursor = conexao.cursor()
cursor.execute('''SELECT SUM(iv.quantidade * (p.preco_venda - p.preco_custo)) AS lucro_total
FROM produtos AS p
INNER JOIN itens_venda AS iv ON p.id = iv.produto_id''')
vendas = cursor.fetchall()
total_lucro = sum(venda[0] for venda in vendas)
conexao.close()



Image.CUBIC = Image.BICUBIC
janela = ttk.Window(themename = 'litera')

frame_resumo_mes = ttk.LabelFrame(janela, text="Resumo do Mês", padding=(10, 10))
frame_resumo_mes.grid(row=0, column=2, rowspan=5, columnspan=2)

mtr1 = ttk.Meter(frame_resumo_mes, subtext='Lucro', bootstyle='success',amountused=total_lucro,amounttotal=50000)
mtr1.grid(row=0, column=0, sticky='e', padx=10, pady=10)
janela.mainloop()
