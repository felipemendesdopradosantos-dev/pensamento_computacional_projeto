import tkinter as tk
from tkinter import messagebox, simpledialog

# ====================================================
# CONFIGURAÇÃO E VARIÁVEIS DO SISTEMA
# ====================================================
janela = tk.Tk()
janela.title("Sistema de Agendamento - Barbearia")
janela.geometry("800x650")
janela.configure(bg="#2c3e50")  # Cor de fundo elegante (azul escuro/cinza)

# Variáveis Tkinter para armazenar os dados dos 3 clientes
c1_nome = tk.StringVar(value="")
c1_servico = tk.StringVar(value="")
c1_horario = tk.StringVar(value="")

c2_nome = tk.StringVar(value="")
c2_servico = tk.StringVar(value="")
c2_horario = tk.StringVar(value="")

c3_nome = tk.StringVar(value="")
c3_servico = tk.StringVar(value="")
c3_horario = tk.StringVar(value="")


# ====================================================
# FUNÇÕES DAS OPÇÕES DO MENU
# ====================================================

def realizar_agendamento():
    # Identifica o primeiro cadastro livre
    if c1_nome.get() == "":
        cadastro = 1
    elif c2_nome.get() == "":
        cadastro = 2
    elif c3_nome.get() == "":
        cadastro = 3
    else:
        messagebox.showwarning("Aviso", "Agenda lotada! Limite de 3 clientes atingido.")
        return

    # Janela customizada para capturar o serviço e dados de forma limpa
    janela_agendar = tk.Toplevel(janela)
    janela_agendar.title(f"Realizar Cadastro {cadastro}")
    janela_agendar.geometry("400x350")
    janela_agendar.configure(bg="#34495e")
    janela_agendar.grab_set()  # Bloqueia a janela principal até fechar esta

    tk.Label(janela_agendar, text="Nome do Cliente:", fg="white", bg="#34495e", font=("Arial", 11, "bold")).pack(pady=5)
    ent_nome = tk.Entry(janela_agendar, font=("Arial", 11), width=30)
    ent_nome.pack(pady=5)

    tk.Label(janela_agendar, text="Selecione o Serviço:", fg="white", bg="#34495e", font=("Arial", 11, "bold")).pack(pady=5)
    
    var_servico = tk.StringVar(value="Corte")
    servicos = ["Corte", "Barba", "Sobrancelha", "Corte + Barba"]
    menu_servico = tk.OptionMenu(janela_agendar, var_servico, *servicos)
    menu_servico.config(font=("Arial", 10), width=20)
    menu_servico.pack(pady=5)

    tk.Label(janela_agendar, text="Horário:", fg="white", bg="#34495e", font=("Arial", 11, "bold")).pack(pady=5)
    ent_horario = tk.Entry(janela_agendar, font=("Arial", 11), width=15)
    ent_horario.pack(pady=5)

    def salvar_cadastro():
        nome = ent_nome.get().strip()
        serv = var_servico.get()
        horario = ent_horario.get().strip()

        if nome == "" or horario == "":
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        if cadastro == 1:
            c1_nome.set(nome)
            c1_servico.set(serv)
            c1_horario.set(horario)
        elif cadastro == 2:
            c2_nome.set(nome)
            c2_servico.set(serv)
            c2_horario.set(horario)
        elif cadastro == 3:
            c3_nome.set(nome)
            c3_servico.set(serv)
            c3_horario.set(horario)

        messagebox.showinfo("Sucesso", "Agendamento realizado com sucesso!")
        janela_agendar.destroy()

    tk.Button(janela_agendar, text="Confirmar Agendamento", bg="#2ecc71", fg="white", 
              font=("Arial", 11, "bold"), command=salvar_cadastro).pack(pady=20)


def listar_agendamentos():
    lista = ""
    if c1_nome.get() != "":
        lista += f"Cliente 1: {c1_nome.get()} - {c1_servico.get()} - {c1_horario.get()}\n"
    if c2_nome.get() != "":
        lista += f"Cliente 2: {c2_nome.get()} - {c2_servico.get()} - {c2_horario.get()}\n"
    if c3_nome.get() != "":
        lista += f"Cliente 3: {c3_nome.get()} - {c3_servico.get()} - {c3_horario.get()}\n"
    
    if lista == "":
        lista = "Nenhum agendamento marcado."
        
    messagebox.showinfo("Agendamentos do Dia", lista)


def cancelar_agendamento():
    nome = simpledialog.askstring("Cancelar", "Digite o nome do cliente para cancelar:")
    if not nome:
        return
        
    nome = nome.strip()
    if nome == c1_nome.get():
        c1_nome.set(""), c1_servico.set(""), c1_horario.set("")
        messagebox.showinfo("Cancelado", "Agendamento do Cliente 1 cancelado.")
    elif nome == c2_nome.get():
        c2_nome.set(""), c2_servico.set(""), c2_horario.set("")
        messagebox.showinfo("Cancelado", "Agendamento do Cliente 2 cancelado.")
    elif nome == c3_nome.get():
        c3_nome.set(""), c3_servico.set(""), c3_horario.set("")
        messagebox.showinfo("Cancelado", "Agendamento do Cliente 3 cancelado.")
    else:
        messagebox.showerror("Erro", "Cliente não encontrado.")


def consultar_cliente():
    nome = simpledialog.askstring("Consultar", "Digite o nome do cliente:")
    if not nome:
        return
        
    nome = nome.strip()
    if nome == c1_nome.get():
        info = f"Nome: {c1_nome.get()}\nServiço: {c1_servico.get()}\nHorário: {c1_horario.get()}"
        messagebox.showinfo("Dados do Cliente", info)
    elif nome == c2_nome.get():
        info = f"Nome: {c2_nome.get()}\nServiço: {c2_servico.get()}\nHorário: {c2_horario.get()}"
        messagebox.showinfo("Dados do Cliente", info)
    elif nome == c3_nome.get():
        info = f"Nome: {c3_nome.get()}\nServiço: {c3_servico.get()}\nHorário: {c3_horario.get()}"
        messagebox.showinfo("Dados do Cliente", info)
    else:
        messagebox.showerror("Erro", "Cliente não encontrado.")


def mostrar_horarios():
    horarios = "Horários padrão de atendimento:\n\n08:00 | 09:00 | 10:00 | 11:00\n13:00 | 14:00 | 15:00 | 16:00 | 17:00"
    messagebox.showinfo("Horários Disponíveis", horarios)


def alterar_agendamento():
    nome = simpledialog.askstring("Alterar", "Digite o nome do cliente que deseja alterar:")
    if not nome:
        return
        
    nome = nome.strip()
    alvo = 0
    if nome == c1_nome.get() and c1_nome.get() != "": alvo = 1
    elif nome == c2_nome.get() and c2_nome.get() != "": alvo = 2
    elif nome == c3_nome.get() and c3_nome.get() != "": alvo = 3

    if alvo > 0:
        janela_alterar = tk.Toplevel(janela)
        janela_alterar.title("Alterar Informações")
        janela_alterar.geometry("350x250")
        janela_alterar.configure(bg="#34495e")
        janela_alterar.grab_set()

        tk.Label(janela_alterar, text="Escolha o que deseja alterar:", fg="white", bg="#34495e", font=("Arial", 11, "bold")).pack(pady=15)

        def mudar_horario():
            novo_h = simpledialog.askstring("Novo Horário", "Digite o novo horário:")
            if novo_h:
                if alvo == 1: c1_horario.set(novo_h)
                elif alvo == 2: c2_horario.set(novo_h)
                elif alvo == 3: c3_horario.set(novo_h)
                messagebox.showinfo("Sucesso", "Horário atualizado!")
                janela_alterar.destroy()

        def mudar_servico():
            janela_serv = tk.Toplevel(janela_alterar)
            janela_serv.title("Novo Serviço")
            janela_serv.geometry("250x150")
            janela_serv.configure(bg="#2c3e50")
            
            var_s = tk.StringVar(value="Corte")
            tk.OptionMenu(janela_serv, var_s, "Corte", "Barba", "Sobrancelha", "Corte + Barba").pack(pady=20)
            
            def confirmar_s():
                if alvo == 1: c1_servico.set(var_s.get())
                elif alvo == 2: c2_servico.set(var_s.get())
                elif alvo == 3: c3_servico.set(var_s.get())
                messagebox.showinfo("Sucesso", "Serviço atualizado!")
                janela_serv.destroy()
                janela_alterar.destroy()
                
            tk.Button(janela_serv, text="Confirmar", command=confirmar_s).pack()

        tk.Button(janela_alterar, text="Alterar apenas Horário", width=22, command=mudar_horario, bg="#3498db", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
        tk.Button(janela_alterar, text="Alterar apenas Serviço", width=22, command=mudar_servico, bg="#3498db", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
    else:
        messagebox.showerror("Erro", "Cliente não encontrado ou nome inválido.")


def relatorio_faturamento():
    faturamento = 0
    # Junta os serviços ativos para calcular
    servicos_ativos = [c1_servico.get(), c2_servico.get(), c3_servico.get()]
    
    # Valida apenas se o cliente correspondente estiver preenchido
    nomes_ativos = [c1_nome.get(), c2_nome.get(), c3_nome.get()]
    
    for i in range(3):
        if nomes_ativos[i] != "":
            if servicos_ativos[i] == "Corte": faturamento += 30
            elif servicos_ativos[i] == "Barba": faturamento += 25
            elif servicos_ativos[i] == "Sobrancelha": faturamento += 15
            elif servicos_ativos[i] == "Corte + Barba": faturamento += 50

    messagebox.showinfo("Relatório Financeiro", f"Faturamento Total Estimado para Hoje:\n\nR$ {faturamento},00")


def limpar_agenda():
    confirmar = messagebox.askyesno("Confirmar Limpeza", "Tem certeza que deseja apagar TODOS os agendamentos?")
    if confirmar:
        c1_nome.set(""), c1_servico.set(""), c1_horario.set("")
        c2_nome.set(""), c2_servico.set(""), c2_horario.set("")
        c3_nome.set(""), c3_servico.set(""), c3_horario.set("")
        messagebox.showinfo("Limpeza", "Agenda totalmente limpa!")


def estatisticas_dia():
    ocupados = 0
    if c1_nome.get() != "": ocupados += 1
    if c2_nome.get() != "": ocupados += 1
    if c3_nome.get() != "": ocupados += 1
    
    vagas_livres = 3 - ocupados
    msg = f"Agendamentos Marcados: {ocupados}\nVagas Restantes: {vagas_livres}"
    messagebox.showinfo("Estatísticas da Agenda", msg)


# ====================================================
# INTERFACE GRÁFICA (LAYOUT DA JANELA PRINCIPAL)
# ====================================================

# Título Principal do Menu Visual
lbl_titulo = tk.Label(janela, text="BEM-VINDO À BARBEARIA", font=("Arial", 22, "bold"), fg="#f1c40f", bg="#2c3e50")
lbl_titulo.pack(pady=30)

lbl_sub = tk.Label(janela, text="Escolha a opção desejada no painel abaixo:", font=("Arial", 12), fg="#ecf0f1", bg="#2c3e50")
lbl_sub.pack(pady=5)

# Container para organizar os botões organizadamente
frame_botoes = tk.Frame(janela, bg="#2c3e50")
frame_botoes.pack(pady=20)

# Configurações de estilo padrão para os botões do Menu
estilo_botao = {
    "font": ("Arial", 11, "bold"),
    "width": 32,
    "height": 2,
    "fg": "white",
    "bd": 0,
    "cursor": "hand2"
}

# Criando e empacotando os botões na ordem correta (1 a 9 e Sair)
tk.Button(frame_botoes, text="1 - Realizar agendamento", bg="#2980b9", command=realizar_agendamento, **estilo_botao).grid(row=0, column=0, padx=10, pady=8)
tk.Button(frame_botoes, text="2 - Listar agendamentos", bg="#2980b9", command=listar_agendamentos, **estilo_botao).grid(row=0, column=1, padx=10, pady=8)

tk.Button(frame_botoes, text="3 - Cancelar agendamento", bg="#2980b9", command=cancelar_agendamento, **estilo_botao).grid(row=1, column=0, padx=10, pady=8)
tk.Button(frame_botoes, text="4 - Consultar cliente", bg="#2980b9", command=consultar_cliente, **estilo_botao).grid(row=1, column=1, padx=10, pady=8)

tk.Button(frame_botoes, text="5 - Mostrar horários disponíveis", bg="#2980b9", command=mostrar_horarios, **estilo_botao).grid(row=2, column=0, padx=10, pady=8)
tk.Button(frame_botoes, text="6 - Alterar agendamento", bg="#2980b9", command=alterar_agendamento, **estilo_botao).grid(row=2, column=1, padx=10, pady=8)

tk.Button(frame_botoes, text="7 - Relatório de faturamento", bg="#27ae60", command=relatorio_faturamento, **estilo_botao).grid(row=3, column=0, padx=10, pady=8)
tk.Button(frame_botoes, text="8 - Limpar toda a agenda", bg="#c0392b", command=limpar_agenda, **estilo_botao).grid(row=3, column=1, padx=10, pady=8)

tk.Button(frame_botoes, text="9 - Estatísticas do dia", bg="#8e44ad", command=estatisticas_dia, **estilo_botao).grid(row=4, column=0, columnspan=2, pady=8)

# Linha divisória
tk.Label(janela, text="-" * 85, fg="#7f8c8d", bg="#2c3e50").pack(pady=15)

# Botão Sair integrado de forma limpa na parte inferior
tk.Button(janela, text="0 - Sair do Sistema", font=("Arial", 12, "bold"), bg="#7f8c8d", fg="white", 
          width=20, height=2, bd=0, cursor="hand2", command=janela.quit).pack(pady=10)

# Inicia o laço contínuo da interface gráfica (Substitui o while True)
janela.mainloop()