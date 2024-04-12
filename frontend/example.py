import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="💻",
)

st.title('App de análisis de datos predictivo para calificación de riesgo')

st.write("El objetivo de este proyecto es realizar un MVP que muestre un reporte de análisis de datos predictivo para establecer la calificación de riesgo de potenciales clientes, al momento de otorgar préstamos.")


tipo_contrato = st.radio("Que tipo de contrato tiene?", ("Préstamos de tesorería", "Préstamos renovables"))

auto_propio = st.radio("Cuenta con auto propio?", ("Si", "No"))

casa_depto_propio = st.radio("Cuenta con departamento propio?", ("Si", "No"))

quien_acompano = st.radio("Quien la acompaño al momento de pedir el credito", ('Sin compañia', 'Familia', 'Conyugue o Pareja', 'Niños', 'Grupo de personas'))

estatus_laboral = st.radio("Cual es su situacion laboral actual?", ('Trabajador', 'Funcionario', 'Socio comercial', 'Pensionista', 'Desempleado', 'Estudiante', 'Empresario', 'Baja por maternidad'))

nivel_educacion = st.radio("Cual es su nivel de educacion?", ('Secundaria / secundaria especial', 'Educación superior', 'Superior incompleta', 'Secundaria inferior', 'Titulación académica'))

estado_civil = st.radio("Cual es su estado civil?", ('Soltero / no casado', 'Casado', 'Matrimonio civil', 'Viudo', 'Separado'))

forma_habitar = st.radio("En que tipo de residenciadonde habita?", ("Casa/apartamento", "Apartamento alquilado", "Con los padres", "Apartamento municipal", "Apartamento oficina", "Apartamento cooperativa"))

ocupacion = st.radio("Que tipo de trabajo tiene?", ('Obreros', 'Personal de base', 'Otros', 'Directivos', 'Conductores', 'Personal de ventas'))

dia_inicio_proceso = st.radio("Que dia de la semana pidió el credito?", ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"))