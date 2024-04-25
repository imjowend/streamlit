tipo_organizacion_trabajo_to_english = {
    "Fuerzas armadas": "Armed_forces",
    "Negocios": "Business",
    "Construcción": "Construction",
    "Educación": "Education",
    "Finanzas/Negocios": "Finance/Business",
    "Gobierno": "Government",
    "Industria": "Industry",
    "Medicina": "Medicine",
    "Otro": "Other",
    "Bienes raíces": "Real Estate",
    "Autoempleado": "Self-employed",
    "Comercio": "Trade",
    "Transporte": "Transport"
}
tipo_contrato_to_english = {
     "Préstamos de tesorería": "Cash loans",
      "Préstamos renovables": "Revolving loans",
}
estatus_laboral_to_english = {
    "Trabajador":"Working",
    "Pensionista":"Pensioner",
    "Desempleado":"Unemployed"
}
nivel_educacion_to_english = {
    "Secundaria / secundaria especial":"Secondary / secondary special",
    "Educación superior":"Higher education",
    "Superior incompleta":"Incomplete higher",
    "Secundaria inferior":"Lower secondary",
    "Titulación académica":"Academic degree"
}
estado_civil_to_english = {
    "Soltero / no casado":"Single / not married",
    "Casado":"Married",  
    "Viudo":"Widow", 
    "Separado":"Separated"
}
forma_habitar_to_english = {
    "Casa/apartamento":"House / apartment", 
    "Apartamento alquilado":"Rented apartment",
    "Con los padres":"With parents", 
    "Oficina/Apartamento comercial":"Office/Co-op apartment"   
    }
ocupacion_to_english = {
    "Obreros":"Laborers", 
    "Personal de base":"Core staff", 
    "Otros":"Other", 
    "Directivos":"Managers", 
    "Conductores":"Drivers", 
    "Personal de ventas":"Sales staff"
}
tipo_cuenta_trabajo_to_english={
    "Cuenta de empresa":"business_account",
    "No especifica":"not specified",
    "Cuenta personal":"personal_account"
}
dataset = {
    'auto_propio': False,
    'casa_depto_propio': False,
    'quien_acompano': False,
    'dia_inicio_proceso': 1,
    'telefono_trabajo': False,
    'telefono_casa': False,
    'telefono_casa2': False,
    'reg_residencia_diferente': False,
    'reg_trabajo_diferente': False,
    'city_residencia_diferente': False,
    'city_trabajo_diferente': False,
    'live_trabajo_diferente': False,
    # Tipo de credito al que postula
    'tipo_contrato_Cash loans': False,
    'tipo_contrato_Revolving loans': False,
    # Estatus laboral
    'estatus_laboral_Pensioner': False,
    'estatus_laboral_Unemployed': False,
    'estatus_laboral_Working': False,
    #  Nivel de educación
    'nivel_educacion_Academic  degree': False,
    'nivel_educacion_Higher education': False,
    'nivel_educacion_Incomplete higher': False,
    'nivel_educacion_Lower secondary': False,
    'nivel_educacion_Secondary / secondary special': False,
    #  Estado civil
    'estado_civil_Married': False,
    'estado_civil_Separated': False,
    'estado_civil_Single / not married': False,
    'estado_civil_Widow': False,
    # Tipo de vivienda donde habita
    'forma_habitar_House / apartment': False,
    'forma_habitar_Office/Co-op apartment': False,
    'forma_habitar_Rented apartment': False,
    'forma_habitar_With parents': False,
    # Tipo de ocupacion del postulante
    'ocupacion_Core staff': False,
    'ocupacion_Drivers': False,
    'ocupacion_Laborers': False,
    'ocupacion_Managers': False,
    'ocupacion_Other': False,
    'ocupacion_Sales staff': False,
    #Tipo de organizacion donde trabaja
    'tipo_organizacion_trabajo_Armed_forces': False,
    'tipo_organizacion_trabajo_Business': False,
    'tipo_organizacion_trabajo_Construction': False,
    'tipo_organizacion_trabajo_Education': False,
    'tipo_organizacion_trabajo_Finance/Business': False,
    'tipo_organizacion_trabajo_Government': False,
    'tipo_organizacion_trabajo_Industry': False,
    'tipo_organizacion_trabajo_Medicine': False,
    'tipo_organizacion_trabajo_Other': False,
    'tipo_organizacion_trabajo_Real Estate': False,
    'tipo_organizacion_trabajo_Self-employed': False,
    'tipo_organizacion_trabajo_Trade': False,
    'tipo_organizacion_trabajo_Transport': False,
    # Que tipo de cuenta bancaria tiene 
    'tipo_cuenta_bancaria_business_account': False,
    'tipo_cuenta_bancaria_not specified': False,
    'tipo_cuenta_bancaria_personal_account': False,
    # Inputs numericos
    "monto_credito": 1,
    "anios_edad": 1,
    "cant_miembros_fam": 1,
    "obs_30_cnt_circulo_social": 1,
    "monto_req_credito_anual": 1,
    "cant_hijos": 1,
    "monto_ingreso_total": 1,
    "anualidad_mensual": 1,
    "precio_bienes": 1,
    "anios_empleado": 1,    
}

#1
auto_propio = input("¿Cuenta con vehículo propio?")
auto_propio_valor = True if auto_propio == "Si" else False

#2
casa_depto_propio = input("¿Cuenta con vivienda propia?")
casa_depto_propio_valor = True if casa_depto_propio == "Si" else False

#3
quien_acompano = input("¿Vino acompañado?")
quien_acompano_valor = True if quien_acompano == "Si" else False

#4
dia_inicio_proceso = input("¿Qué día de la semana es hoy?")
dias_dict = {"Lunes": "1", "Martes": "2", "Miércoles": "3", "Jueves": "4", "Viernes": "5", "Sábado": "6", "Domingo": "7"}
dia_valor = dias_dict.get(dia_inicio_proceso)

#5
telefono_trabajo = input("¿Brindó teléfono de trabajo cuando postuló?")
telefono_trabajo_valor = True if telefono_trabajo == "Si" else False

#6
telefono_casa = input("¿Brindó teléfono particular cuando postuló?")
telefono_casa_valor = True if telefono_casa == "Si" else False

#7
telefono_casa2 = input("¿Brindó otro teléfono cuando postuló?")
telefono_casa2_valor = True if telefono_casa2 == "Si" else False

#8
reg_residencia_diferente = input("El domicilio real, ¿es diferente al domicilio legal?" )
reg_residencia_diferente_valor = True if reg_residencia_diferente == "Si" else False

#9
reg_trabajo_diferente= input("El domicilio laboral real, ¿es diferente al domicilio legal?" )
reg_trabajo_diferente_valor = True if reg_trabajo_diferente == "Si" else False

#10
city_residencia_diferente= input("La ciudad de residencia real, ¿es diferente a la legal?" )
city_residencia_diferente_valor = True if city_residencia_diferente == "Si" else False

#11
city_trabajo_diferente= input("La ciudad de trabajo real, ¿es diferente a la legal?" )
city_trabajo_diferente_valor = True if city_trabajo_diferente == "Si" else False

#12
live_trabajo_diferente= input("La ciudad de trabajo indicada, ¿es distinta a donde vive?" )
live_trabajo_diferente_valor = True if live_trabajo_diferente == "Si" else False

#13 y 14
# Tiene: Cash loans y Revolving loans
tipo_contrato = input("¿Qué tipo de contrato tiene?")
tipo_contrato_true = tipo_contrato_to_english[tipo_contrato]
clave = f'tipo_contrato_{tipo_contrato_true}'
dataset[clave] = True
#15, 16 y 17
# Tiene: Pensioner, Unemployed y Working
estatus_laboral = input("¿Cuál es su situación laboral actual?")
estatus_laboral_true = estatus_laboral_to_english[estatus_laboral]
clave = f'estatus_laboral_{estatus_laboral_true}'
dataset[clave] = True

#18, 19, 20, 21 y 22
# Tiene: Academic degree, Higher education, Incomplete higher, Lower secondary, Secondary/ secondary special
nivel_educacion = input("Cual es su nivel de educacion?")
nivel_educacion_true = nivel_educacion_to_english[nivel_educacion]
clave = f'nivel_educacion_{nivel_educacion_true}'
dataset[clave] = True

#23, 24, 25 y 26
estado_civil = input("Cual es su estado civil?")
estado_civil_true = estado_civil_to_english[estado_civil]
clave = f'estado_civil_{estado_civil_true}'
dataset[clave] = True

#27, 28, 29 y 30
forma_habitar = input("En que tipo de residencia habita?")
forma_habitar_true = forma_habitar_to_english[forma_habitar]
clave = f'forma_habitar_{forma_habitar_true}'
dataset[clave] = True

#31, 32, 33, 34, 35 y 36
ocupacion = input("Que tipo de trabajo tiene?")
ocupacion_true = ocupacion_to_english[ocupacion]
clave = f'ocupacion_{ocupacion_true}'
dataset[clave] = True

#37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 y 49
tipo_organizacion_trabajo = input("En que area trabaja")
tipo_organizacion_trabajo_true = tipo_organizacion_trabajo_to_english[tipo_organizacion_trabajo]
clave = f'tipo_organizacion_trabajo_{tipo_organizacion_trabajo_true}'
dataset[clave] = True

#50, 51 y 52
tipo_cuenta = input("¿Qué tipo de cuenta bancaria tiene el solicitante?")
tipo_cuenta_trabajo_true = tipo_cuenta_trabajo_to_english[tipo_cuenta]
clave = f'tipo_cuenta_trabajo_{tipo_cuenta_trabajo_true}'
dataset[clave] = True

#Inputs numericos
#53
monto_credito = int(input("¿Cuál es el monto del crédito que solicita?"))
dataset["monto_credito"] = monto_credito

#54
anios_edad =  int(input("¿Cuál es su edad?"))
dataset["anios_edad"] = anios_edad

#55
cant_miembros_fam = int(input("¿Cuántas personas hay en su círculo familiar?"))
dataset["cant_miembros_fam"] = cant_miembros_fam

#56
obs_30_cnt_circulo_social = int(input("Cantidad de deudas impagas del cliente en un período de 30 días antes de la fecha de solicitud del crédito"))
dataset["obs_30_cnt_circulo_social"] = obs_30_cnt_circulo_social

#57
monto_req_credito_anual = int(input("Cantidad de solicitudes de crédito en el último año"))
dataset["monto_req_credito_anual"] = monto_req_credito_anual

#58
cant_hijos = input("Cuantos hijos tiene?")
dataset["cant_hijos"] = cant_hijos

#59
monto_ingreso_total = int(input("Monto del ingreso total del cliente"))
dataset["monto_ingreso_total"] = monto_ingreso_total

#60
anualidad_mensual = int(input("Anualidad del crédito"))
dataset["anualidad_mensual"] = anualidad_mensual

#61
precio_bienes = int(input("Precio de los bienes para los cuales se otorga el crédito"))
dataset["precio_bienes"] = precio_bienes

#62
anios_empleado = int(input("Antigüedad en el empleo actual"))
dataset["anios_empleado"] = anios_empleado
