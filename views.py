import streamlit as st
import time
# from service import Service

class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir Conta")
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Cadastrar"):
            try:
                Service.cliente_inserir(nome, email, senha)
                st.success("Conta criada com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

class ManterClienteUI:
    @staticmethod
    def inserir():
        st.subheader("Inserir Cliente")
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Inserir"):
            try:
                Service.cliente_inserir(nome, email, senha)
                st.success("Cliente inserido com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

    @staticmethod
    def atualizar(op):
        st.subheader("Atualizar Cliente")
        id = op.get_id()
        nome = st.text_input("Novo Nome", op.get_nome())
        email = st.text_input("Novo E-mail", op.get_email())
        senha = st.text_input("Nova Senha", op.get_senha(), type="password")
        if st.button("Atualizar"):
            try:
                Service.cliente_atualizar(id, nome, email, senha)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

    @staticmethod
    def excluir(op):
        st.subheader("Excluir Cliente")
        if st.button("Excluir"):
            try:
                Service.cliente_excluir(op.get_id())
                st.success("Cliente excluído com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

class ManterProfissionalUI:
    @staticmethod
    def inserir():
        st.subheader("Inserir Profissional")
        nome = st.text_input("Nome Profissional")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Inserir Profissional"):
            try:
                Service.profissional_inserir(nome, email, senha)
                st.success("Profissional cadastrado com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

    @staticmethod
    def atualizar(op):
        st.subheader("Atualizar Profissional")
        id = op.get_id()
        nome = st.text_input("Nome Profissional", op.get_nome())
        email = st.text_input("E-mail", op.get_email())
        senha = st.text_input("Senha", op.get_senha(), type="password")
        if st.button("Atualizar Profissional"):
            try:
                Service.profissional_atualizar(id, nome, email, senha)
                st.success("Profissional atualizado com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

    @staticmethod
    def excluir(op):
        st.subheader("Excluir Profissional")
        if st.button("Excluir Profissional"):
            try:
                Service.profissional_excluir(op.get_id())
                st.success("Profissional excluído com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

class ManterHorarioUI:
    @staticmethod
    def inserir(id_prof_logado):
        st.subheader("Abrir Agenda / Inserir Horário")
        data_texto = st.text_input("Data e Hora (dd/mm/aaaa HH:MM)")
        if st.button("Abrir Horário"):
            try:
                Service.horario_inserir(data_texto, id_prof_logado)
                st.success("Horário disponibilizado com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

    @staticmethod
    def excluir(op):
        st.subheader("Excluir Horário")
        if st.button("Excluir Horário"):
            try:
                Service.horario_excluir(op.get_id())
                st.success("Horário removido com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))