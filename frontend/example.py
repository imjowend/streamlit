import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="💻",
)

st.title('App de análisis de datos predictivo para calificación de riesgo')

st.write("El objetivo de este proyecto es realizar un MVP que muestre un reporte de análisis de datos predictivo para establecer la calificación de riesgo de potenciales clientes, al momento de otorgar préstamos.")

dataset = []
#1
casa_depto_propio = st.radio("Cuenta con departamento propio?", ("Si", "No"))
#2
dia_inicio_proceso = st.radio("Que dia de la semana pidió el credito?", ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"))
#3
telefono_trabajo = st.radio("Entregó telefono de trabajo cuando postuló?", ("Si", "No"))
#4
telefono_casa2 = st.radio("Entregó telefono de casa2 cuando postuló?", ("Si", "No"))
#5
reg_residencia_diferente = st.radio("Si la residencia indicada es distinta a la real", ("Si", "No") )
#6
reg_trabajo_diferente= st.radio("Si la direccion de trabajo indicada es distinta a la real", ("Si", "No") )
#7
city_residencia_diferente= st.radio("Si la ciudad de residencia indicada es distinta a la real", ("Si", "No") )
#8 Tiene: Cash loans y Revolving loans
tipo_contrato = st.radio("Que tipo de contrato tiene?", ("Préstamos de tesorería", "Préstamos renovables"))
#9 Tiene: Pensioner, Unemployed y Working
estatus_laboral = st.radio("Cual es su situacion laboral actual?", ('Trabajador', 'Funcionario', 'Socio comercial', 'Pensionista', 'Desempleado', 'Estudiante', 'Empresario', 'Baja por maternidad'))
#10 Tiene: Academic degree, Higher education, Incomplete higher, Lower secondary, Secondary/ secondary special
nivel_educacion = st.radio("Cual es su nivel de educacion?", ('Secundaria / secundaria especial', 'Educación superior', 'Superior incompleta', 'Secundaria inferior', 'Titulación académica'))
#11
estado_civil = st.radio("Cual es su estado civil?", ('Soltero / no casado', 'Casado', 'Matrimonio civil', 'Viudo', 'Separado'))
#12
forma_habitar = st.radio("En que tipo de residencia habita?", ("Casa/apartamento", "Apartamento alquilado", "Con los padres", "Apartamento municipal", "Apartamento oficina", "Apartamento cooperativa"))
#13
ocupacion = st.radio("Que tipo de trabajo tiene?", ('Obreros', 'Personal de base', 'Otros', 'Directivos', 'Conductores', 'Personal de ventas'))
#14
tipo_organizacion_trabajo = st.radio("En que area trabaja",('Empresas', 'Educación', 'Administración', 'Otros', 'Construcción', 'Medicina', 'Autónomos', 'Transporte', 'Inmobiliario', 'Comercio', 'Industria', 'Fuerzas Armadas', 'Finanzas'))

#De aca para abajo no salen en el Array
auto_propio = st.radio("Cuenta con auto propio?", ("Si", "No"))

quien_acompano = st.radio("Quien la acompaño al momento de pedir el credito", ('Sin compañia', 'Familia', 'Conyugue o Pareja', 'Niños', 'Grupo de personas'))

telefono_casa = st.radio("Entregó telefono de casa cuando postuló?", ("Si", "No"))

city_trabajo_diferente= st.radio("Si la ciudad de trabajo indicada es distinta a la real", ("Si", "No") )

live_trabajo_diferente= st.radio("Si la ciudad de trabajo indicada es distinta a donde vive", ("Si", "No") )