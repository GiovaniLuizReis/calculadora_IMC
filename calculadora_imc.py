import streamlit as st

with st.sidebar:
    st.title("Calculadora de IMC")
    st.write("Esta calculadora permite calcular o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos pelo usuário.")


st.title("Calculadora de IMC")

peso = st.number_input("Digite seu peso em kg:", min_value=0.0, step=0.1)
altura = st.number_input("Digite sua altura em metros:", min_value=0.0, step=0.01)


if st.button("Calcular IMC"):
    if altura > 0:
        imc = peso / (altura ** 2)
        st.write(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            st.write("Classificação: Abaixo do peso")
        elif 18.5 <= imc < 24.9:
            st.write("Classificação: Peso normal")
        elif 25 <= imc < 29.9:
            st.write("Classificação: Sobrepeso")
        elif 30 <= imc < 34.9:
            st.write("Classificação: Obesidade de Grau I")
        elif 35 <= imc < 39.9:
            st.write("Classificação: Obesidade de Grau II")
        else:
            st.write("Classificação: Obesidade de Grau III")  
    else:
        st.error("A altura deve ser maior que zero.")

