import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO = "cadastros.json"

def carregar():
    if os.path.exists(ARQUIVO):
        return json.load(open(ARQUIVO, "r"))
    return []

def salvar():
    json.dump(cadastros, open(ARQUIVO, "w"), indent=4)

def cadastrar():
    if entry_nome.get() == "":
        messagebox.showwarning("Erro", "Nome obrigatório")
        return

    cadastros.append({
        "nome": entry_nome.get(),
        "idade": entry_idade.get(),
        "email": entry_email.get()
    })

    salvar()
    atualizar()

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def atualizar():
    lista.delete(0, tk.END)
    for p in cadastros:
        lista.insert(tk.END, f"{p['nome']} | {p['idade']} | {p['email']}")

def remover():
    if lista.curselection():
        cadastros.pop(lista.curselection()[0])
        salvar()
        atualizar()

cadastros = carregar()

# ===== JANELA =====
janela = tk.Tk()
janela.title("Sistema de Gestão")
janela.geometry("700x520")
janela.config(bg="#121826")

# ===== HEADER =====
header = tk.Frame(janela, bg="#1f2937", height=60)
header.pack(fill="x")

tk.Label(
    header,
    text="📊 Sistema de Cadastro Profissional",
    bg="#1f2937",
    fg="white",
    font=("Arial", 16, "bold")
).pack(pady=15)

# ===== FORM =====
form = tk.Frame(janela, bg="#121826")
form.pack(pady=20)

tk.Label(form, text="Nome", fg="white", bg="#121826").grid(row=0, column=0)
entry_nome = tk.Entry(form, width=30)
entry_nome.grid(row=0, column=1, padx=5)

tk.Label(form, text="Idade", fg="white", bg="#121826").grid(row=1, column=0)
entry_idade = tk.Entry(form, width=30)
entry_idade.grid(row=1, column=1, padx=5)

tk.Label(form, text="Email", fg="white", bg="#121826").grid(row=2, column=0)
entry_email = tk.Entry(form, width=30)
entry_email.grid(row=2, column=1, padx=5)

# ===== BOTÕES =====
btn_frame = tk.Frame(janela, bg="#121826")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="➕ Cadastrar", bg="#22c55e", fg="white", width=15, command=cadastrar).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="🗑 Remover", bg="#ef4444", fg="white", width=15, command=remover).grid(row=0, column=1, padx=5)

# ===== LISTA =====
lista = tk.Listbox(janela, width=80, height=15, bg="#1e293b", fg="white")
lista.pack(pady=20)

atualizar()

janela.mainloop()