import pandas as pd
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
import getpass
import os

arquivo_csv = ""
df = pd.DataFrame()


# Selecionar arquivo
def selecionar_arquivo():

    global arquivo_csv

    arquivo_csv = filedialog.askopenfilename(
        title="Selecionar arquivo CSV",
        filetypes=[("Arquivos CSV", "*.csv")]
    )

    if arquivo_csv:

        label_arquivo.config(
            text=f"Arquivo: {os.path.basename(arquivo_csv)}"
        )

        status_label.config(
            text="Arquivo selecionado com sucesso!"
        )


# Importar dados
def importar_dados():

    global arquivo_csv
    global df

    if not arquivo_csv:

        messagebox.showerror(
            "Erro",
            "Selecione um arquivo CSV primeiro!"
        )

        return

    try:

        status_label.config(
            text="Importando dados..."
        )

        # Ler CSV
        df_original = pd.read_csv(
            arquivo_csv,
            sep=';'
        )

        # Remover espaços extras
        df_original.columns = df_original.columns.str.strip()

        # Criar DataFrame dos processadores
        df_proc = pd.DataFrame({
            'produto': df_original['produtos'],
            'quantidade': df_original['quantidade'],
            'preco': df_original['preco']
        })

        

        # Unir tudo em uma única coluna produto
        df = pd.concat(
            [df_proc],
            ignore_index=True
        )

        # Informações extras
        df['data_importacao'] = datetime.now().strftime(
            '%d/%m/%Y %H:%M:%S'
        )

        df['usuario_responsavel'] = getpass.getuser()

        df['status_importacao'] = 'Sucesso'

        df['origem_arquivo'] = os.path.basename(
            arquivo_csv
        )

        # Salvar no SQLite
        conn = sqlite3.connect('banco.db')

        df.to_sql(
            'produtos',
            conn,
            if_exists='replace',
            index=False
        )

        conn.close()

        # Limpar tabela
        tabela.delete(*tabela.get_children())

        # Exibir dados
        for _, row in df.iterrows():

            tabela.insert(
                "",
                "end",
                values=(
                    row['produto'],
                    row['quantidade'],
                    row['preco']
                )
            )

        quantidade = len(df)

        status_label.config(
            text=f"{quantidade} registros importados!"
        )

        messagebox.showinfo(
            "Sucesso",
            f"{quantidade} registros importados com sucesso!"
        )

    except Exception as e:

        status_label.config(
            text="Erro na importação!"
        )

        messagebox.showerror(
            "Erro",
            str(e)
        )


# Pesquisa
def pesquisar():

    pesquisa = campo_pesquisa.get().lower()

    tabela.delete(*tabela.get_children())

    for _, row in df.iterrows():

        if (
            pesquisa in str(row['produto']).lower()
            or pesquisa in str(row['preco']).lower()
        ):

            tabela.insert(
                "",
                "end",
                values=(
                    row['produto'],
                    row['quantidade'],
                    row['preco']
                )
            )


# Criar janela
janela = tk.Tk()

janela.title("Sistema de Importação de Dados")
janela.geometry("900x500")
janela.configure(bg="#1e1e1e")


# Título
titulo = tk.Label(
    janela,
    text="SISTEMA DE IMPORTAÇÃO DE DADOS",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
)

titulo.pack(pady=15)


# Botão selecionar
botao_selecionar = tk.Button(
    janela,
    text="Selecionar CSV",
    command=selecionar_arquivo,
    width=20,
    height=2,
    bg="#3a3a3a",
    fg="white"
)

botao_selecionar.pack(pady=5)


# Nome arquivo
label_arquivo = tk.Label(
    janela,
    text="Nenhum arquivo selecionado",
    bg="#1e1e1e",
    fg="white"
)

label_arquivo.pack()


# Botão importar
botao_importar = tk.Button(
    janela,
    text="Importar Dados",
    command=importar_dados,
    width=20,
    height=2,
    bg="#0078D7",
    fg="white"
)

botao_importar.pack(pady=15)


# Campo pesquisa
campo_pesquisa = tk.Entry(
    janela,
    width=40,
    font=("Arial", 10)
)

campo_pesquisa.pack(pady=5)


# Botão pesquisa
botao_pesquisa = tk.Button(
    janela,
    text="Pesquisar",
    command=pesquisar,
    width=20,
    bg="#444",
    fg="white"
)

botao_pesquisa.pack(pady=5)


# Tabela
tabela = ttk.Treeview(
    janela,
    columns=(
        "produto",
        "quantidade",
        "preco"
    ),
    show="headings",
    height=12
)

# Cabeçalhos
tabela.heading(
    "produto",
    text="Produto"
)

tabela.heading(
    "quantidade",
    text="Quantidade"
)

tabela.heading(
    "preco",
    text="Preço"
)

# Largura das colunas
tabela.column(
    "produto",
    width=350
)

tabela.column(
    "quantidade",
    width=120
)

tabela.column(
    "preco",
    width=120
)

tabela.pack(
    pady=10,
    fill="both",
    expand=True
)


# Status
status_label = tk.Label(
    janela,
    text="Sistema pronto",
    bg="#1e1e1e",
    fg="#00FF7F",
    font=("Arial", 10, "bold")
)

status_label.pack(
    side="bottom",
    pady=15
)


# Executar
janela.mainloop()