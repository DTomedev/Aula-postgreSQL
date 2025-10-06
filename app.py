import streamlit as st
from crud import criar_aluno, atualizar_idade, listar_alunos, deletar_aluno

st.set_page_config(page_title="Gerenciamento de Alunos", page_icon="👨‍🎓")

st.title("Sistema de Alunos com PostgreSQL")

menu = st.sidebar.radio("Menu", ["Inserir","Listar", "Atualizar", "Deletar"])

#Inserindo alunos
if menu == "Inserir":
    st.subheader("➕ Inserir Alunos ")
    nome = st.text_input("Nome:", placeholder="Seu Nome")
    idade = st.number_input("Idade:", min_value=16, max_value=110, step=1)

    if st.button("Salvar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} inserido com sucesso!")
        else:
            st.warning("O campo nome não pode ser vazio.")

#Listar alunos
elif menu == "Listar":
    st.subheader("Listar Alunos")
    alunos = listar_alunos()
    if alunos:
       st.dataframe(alunos)
       alunos = alunos.rename(columns={"id":"ID","nome": "NOME","idade": "IDADE"})
    else:
        st.info("Nenhum Aluno Encontrado!")

#Atualizar idade
elif menu == "Atualizar":
    st.subheader("Atualizar Idade")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("Escolha o ID do Aluno para Atualizar:", [linha[0] for linha in alunos])
        nova_idade = st.number_input("Nova Idade:", max_value=110, min_value=16, step=1)
        if st.button("Atualizar"):
            atualizar_idade(id_aluno, nova_idade)
            st.success("Idade do aluno atualizada com sucesso!")
    else:
        st.info("Nenhum aluno disponível para atualizar")

