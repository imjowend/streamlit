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

forma_habitar = st.radio("En que tipo de residencia habita?", ("Casa/apartamento", "Apartamento alquilado", "Con los padres", "Apartamento municipal", "Apartamento oficina", "Apartamento cooperativa"))

ocupacion = st.radio("Que tipo de trabajo tiene?", ('Obreros', 'Personal de base', 'Otros', 'Directivos', 'Conductores', 'Personal de ventas'))

dia_inicio_proceso = st.radio("Que dia de la semana pidió el credito?", ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"))

tipo_organizacion_trabajo = st.radio("En que area trabaja",('Empresas', 'Educación', 'Administración', 'Otros', 'Construcción', 'Medicina', 'Autónomos', 'Transporte', 'Inmobiliario', 'Comercio', 'Industria', 'Fuerzas Armadas', 'Finanzas'))

telefono_trabajo = st.radio("Entregó telefono de trabajo cuando postuló?", ("Si", "No"))

telefono_casa = st.radio("Entregó telefono de casa cuando postuló?", ("Si", "No"))

telefono_casa2 = st.radio("Entregó telefono de casa2 cuando postuló?", ("Si", "No"))

reg_residencia_diferente = st.radio("Si la residencia indicada es distinta a la real", ("Si", "No") )

reg_trabajo_diferente= st.radio("Si la direccion de trabajo indicada es distinta a la real", ("Si", "No") )

city_residencia_diferente= st.radio("Si la ciudad de residencia indicada es distinta a la real", ("Si", "No") )

city_trabajo_diferente= st.radio("Si la ciudad de trabajo indicada es distinta a la real", ("Si", "No") )

live_trabajo_diferente= st.radio("Si la ciudad de trabajo indicada es distinta a donde vive", ("Si", "No") )