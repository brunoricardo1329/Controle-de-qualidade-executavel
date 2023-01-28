import tkinter as tk
from tkinter import ttk
import pandas as pd

def cadastrar():
    # ler valores dos campos de entrada
    posto = posto_entry.get()
    sku = sku_entry.get()
    tipo_avaria = tipo_avaria_entry.get()
    saldo = saldo_entry.get()

    # adicionar valores ao arquivo Excel
    df = pd.read_excel('dados.xlsx')
    df = df.append({'POSTO': posto, 'SKU': sku, 'TIPO DE AVARIA': tipo_avaria, 'SALDO': saldo}, ignore_index=True)
    df.to_excel('dados.xlsx', index=False)

    # limpar campos de entrada

    posto_entry.delete(0, tk.END)
    sku_entry.delete(0, tk.END)
    tipo_avaria_entry.delete(0, tk.END)
    saldo_entry.delete(0, tk.END)

# criar janela
root = tk.Tk()
root.title("CONTROLE DE QUALIDADE")
# criar campos de entrada
posto_label = ttk.Label(root, text="POSTO:")
posto_label.grid(column=0, row=1)
posto_entry = ttk.Entry(root)
posto_entry.grid(column=1, row=1)

sku_label = ttk.Label(root, text="SKU:")
sku_label.grid(column=0, row=2)
sku_entry = ttk.Entry(root)
sku_entry.grid(column=1, row=2)

tipo_avaria_label = ttk.Label(root, text="TIPO DE AVARIA:")
tipo_avaria_label.grid(column=0, row=3)
tipo_avaria_entry = ttk.Entry(root)
tipo_avaria_entry.grid(column=1, row=3)

saldo_label = ttk.Label(root, text="SALDO:")
saldo_label.grid(column=0, row=4)
saldo_entry = ttk.Entry(root)
saldo_entry.grid(column=1, row=4)

#criar botão de cadastrar
cadastrar_button = ttk.Button(root, text="Cadastrar", command=cadastrar)
cadastrar_button.grid(column=1, row=5)
posto_label.config(font=("Arial", 18))
posto_entry.config(font=("Arial", 18))
sku_label.config(font=("Arial", 18))
sku_entry.config(font=("Arial", 18))
tipo_avaria_label.config(font=("Arial", 18))
tipo_avaria_entry.config(font=("Arial", 18))
saldo_label.config(font=("Arial", 18))
saldo_entry.config(font=("Arial", 18))
root.mainloop()
