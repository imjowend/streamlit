import streamlit as st
#Definir el título
st.title('App de análisis de datos predictivo para calificación de riesgo')

st.write("Esta aplicación tiene el objetivo de elevar cualquier número al cuadrado:")

x = st.number_input('Introduzca un número:')  
st.write('El número al cuadrado es:', x**2)