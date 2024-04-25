import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="💻",
)

st.title('App de análisis de datos predictivo para calificación de riesgo')

st.write("El objetivo de este proyecto es realizar un MVP que muestre un reporte de análisis de datos predictivo para establecer la calificación de riesgo de potenciales clientes, al momento de otorgar préstamos.")

dataset = []

auto_propio = st.radio("Cuenta con auto propio?", ("Si", "No"))

#1
casa_depto_propio = st.radio("Cuenta con departamento propio?", ("Si", "No"))

quien_acompano = st.selectbox("Quien la acompaño al momento de pedir el credito", ['Sin compañia', 'Familia', 'Conyugue o Pareja', 'Niños', 'Grupo de personas'])

#2
dia_inicio_proceso = st.selectbox("Que dia de la semana pidió el credito?", ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"])
#3
telefono_trabajo = st.radio("Entregó telefono de trabajo cuando postuló?", ("Si", "No"))

telefono_casa = st.radio("Entregó telefono de casa cuando postuló?", ("Si", "No"))

#4
telefono_casa2 = st.radio("Entregó telefono de casa2 cuando postuló?", ("Si", "No"))
#5
reg_residencia_diferente = st.radio("Si la residencia indicada es distinta a la real", ("Si", "No") )
#6
reg_trabajo_diferente= st.radio("Si la direccion de trabajo indicada es distinta a la real", ("Si", "No") )
#7
city_residencia_diferente= st.radio("Si la ciudad de residencia indicada es distinta a la real", ("Si", "No") )

city_trabajo_diferente= st.radio("Si la ciudad de trabajo indicada es distinta a la real", ("Si", "No") )

live_trabajo_diferente= st.radio("Si la ciudad de trabajo indicada es distinta a donde vive", ("Si", "No") )
#8 Tiene: Cash loans y Revolving loans
tipo_contrato = st.selectbox("Que tipo de contrato tiene?", ["Préstamos de tesorería", "Préstamos renovables"])
#9 Tiene: Pensioner, Unemployed y Working
estatus_laboral = st.selectbox("Cual es su situacion laboral actual?", ['Trabajador', 'Pensionista', 'Desempleado'])
#10 Tiene: Academic degree, Higher education, Incomplete higher, Lower secondary, Secondary/ secondary special
nivel_educacion = st.selectbox("Cual es su nivel de educacion?", ['Secundaria / secundaria especial', 'Educación superior', 'Superior incompleta', 'Secundaria inferior', 'Titulación académica'])
#11
estado_civil = st.selectbox("Cual es su estado civil?", ['Soltero / no casado', 'Casado', 'Matrimonio civil', 'Viudo', 'Separado'])
#12
forma_habitar = st.selectbox("En que tipo de residencia habita?", ["Casa/apartamento", "Apartamento alquilado", "Con los padres", "Apartamento municipal", "Apartamento oficina", "Apartamento cooperativa"])
#13
ocupacion = st.selectbox("Que tipo de trabajo tiene?", ['Obreros', 'Personal de base', 'Otros', 'Directivos', 'Conductores', 'Personal de ventas'])
#14
tipo_organizacion_trabajo = st.selectbox("En que area trabaja",['Empresas', 'Educación', 'Administración', 'Otros', 'Construcción', 'Medicina', 'Autónomos', 'Transporte', 'Inmobiliario', 'Comercio', 'Industria', 'Fuerzas Armadas', 'Finanzas'])

#Inputs numericos
monto_credito = st.number_input("¿Cuál es el monto del crédito que solicita?")

anios_edad =  st.number_input("¿Cuál es su edad?")

cant_miembros_fam = st.number_input("¿Cuántas personas hay en su círculo familiar?")

obs_30_cnt_circulo_social = st.number_input("Cantidad de deudas impagas del cliente en un período de 30 días antes de la fecha de solicitud del crédito")

def_30_cnt_circulo_social = st.number_input("Cantidad de personas con las que el cliente tiene una deuda impaga en los últimos 30 días")

monto_req_credito_anual = st.number_input("Cantidad de solicitudes de crédito en el último año")

cant_hijos = st.number_input("Cuantos hijos tiene?")

monto_ingreso_total = st.number_input("Monto del ingreso total del cliente")

anualidad_mensual = st.number_input("Anualidad del crédito")

precio_bienes = st.number_input("Precio de los bienes para los cuales se otorga el crédito")

anios_empleado = st.number_input("Antigüedad en el empleo actual")


st.write("<iframe width='1000' height='600' src='https://app.powerbi.com/view?r=eyJrIjoiZTFlNDM1ZjctN2VjYS00ZDFhLTljZTItNWRhOTZmZDBmMjcxIiwidCI6ImI1ZDc4OTI3LTI1ZDAtNDRhOS04MzcwLWQ4NmU1N2M3YmE5NiIsImMiOjR9' style='display:block;margin:auto;'></iframe>", unsafe_allow_html=True)