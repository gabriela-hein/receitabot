from tkinter import Image

import streamlit as st
from PIL import Image
import inteligencia

##inteligencia.py

st.set_page_config(layout='wide')
chave = st.secrets["GEMINI_CHAVE"]

##adicionar imagens

head1, head2, head2 = st.columns([3, 2, 11], vertical_alignment="bottom")
with head1:
    st.image("arquivos/onomedaimagem", width=250)

with head2:
    st.image("arquivos/onomedaimagem2", width=120)

with head3:
    st.title(":violet[RECEITA BOT]")
    st.subheader("O seu assistente virtual para gerar receitas!")

col1, col2 = st.columns([2,2])

with col1:
    st.header('Faça o upload da foto com os ingredientes')
    arquivo_foto = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if arquivo_foto is not None:
        imagem = Image.open(arquivo_foto)
        st.image(imagem)
        with st.spinner ("O receita Bot está dando uma olhada..."):
            if st.button("Detectar Possíveis Receitas"):
                st.session_state.ingredientes=inteligencia.detectar_ingredientes(chave, imagem)
                st.session_state.receitas=inteligencia.possiveis_receitas(chave,st.session_state.ingredientes)


    if 'ingredientes' in st.session_state:
        st.write(f":violet[Ingredientes detectados:] {st.session_state.ingredientes}")
        st.write(':violet[Possíveis Receitas:]')
        for id, receita in enumerate(st.session_state.receitas, start=1):
            st.write(f"{id}.{receita}")



with col2:
    if 'receitas' in st.session_state:
        st.header("Escolha uma receita")
        receita_selecionada = st.selectbox("",st.session_state.receitas)
        with st.spinner("O receita Bot está criando a receita..."):
            if st.button("Ver receita"):
                st.session_state.receita_completa=inteligencia.receita_completa(chave,
                                                                                st.session_state.ingredientes,
                                                                                receita_selecionada)
                st.write(st.session_state.receita_completa)






