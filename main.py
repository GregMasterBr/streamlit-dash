import streamlit as st
import pandas as pd
import numpy as np
import datetime


def dashboard():
    st.header("Minha dashboard")
    st.write("## Hoje é ",datetime.datetime.now())
    st.text('Meu texto')
    st.sidebar.markdown('# MENU')
    st.markdown('# Meu texto')
    st.caption('Estou testando a lib streamlit para criar dashboards')
    st.write("# Seja bem-vindo", ['Gregorio', 'Queiroz'])

    st.markdown("~--------------------------------~")
    df = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])

    st.title('DADOS EM UMA TABELA')
    st.table(df)

    st.title('DADOS EM UM DATAFRAME')
    st.dataframe(df)    

    if st.sidebar.button('Exibir gráfico em Linhas'):
        st.title('GRÁFICOS EM LINHA')
        st.line_chart(df)

    if st.sidebar.button('Exibir gráfico em Barras'):
        st.title('GRÁFICOS EM BARRAS')
        st.bar_chart(df)

    if st.sidebar.checkbox('Aceitar'):
        st.sidebar.text('Aceito')

    st.title('SELECIONE UMA OPÇÃO')
    opcao = st.radio(
    "Selecione uma opção",
    ('Opção 1', 'Opção 2'))

    if opcao == 'Opção 1':
        st.write('1')
    else:
        st.write("2")

    option = st.selectbox(
        'Selecione',
        ('Op 1', 'Op 2', 'Op 3'))

    st.write('Você selecionou:', option)        

    options = st.multiselect(
        'Cor favorita',
        ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
        ['Vermelho', 'Verde'])

    st.sidebar.title("Selecione o intervalo")
    values = st.sidebar.slider(
    'Intervalo',
    0.0, 100.0, (25.0, 75.0))    
    
    st.sidebar.title("Adicionar o nome")
    nome_ = st.sidebar.text_input('Nome', 'GreMaster')   
    pessoas_ = ['Gregorio'] 
    btn_add = st.sidebar.button('Adicionar')
    if btn_add:
        pessoas_.append(nome_)
    st.sidebar.write("## Pessoas", pessoas_)
    
    numero_ = st.sidebar.number_input('Número')
    st.sidebar.write("## Número", numero_)
    
    d = st.sidebar.date_input(
    "Digite uma data",
    datetime.date(2022, 9, 9))

if __name__ == "__main__":
    dashboard()