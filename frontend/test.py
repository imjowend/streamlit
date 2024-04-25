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
    "Secundaria / secundaria especial":"Secondary/ secondary special",
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
    "Con los padres":"With parents", "Oficina/Apartamento comercial":"Office/Co-op apartment"   
    }
ocupacion_to_english = {
    "Obreros":"Laborers", 
    "Personal de base":"Core staff", 
    "Otros":"Others", 
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
    'quien_acompañó': 0,
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
}


tipo_contrato = input("Quien la acompaño al momento de pedir el credito")
tipo_contrato_true = tipo_contrato_to_english[tipo_contrato]
clave = f'tipo_contrato_{tipo_contrato_true}'
dataset[clave] = True

estatus_laboral = input("Cual es su situacion laboral actual?")
estatus_laboral_true = estatus_laboral_to_english[estatus_laboral]
clave = f'estatus_laboral_{estatus_laboral_true}'
dataset[clave] = True

nivel_educacion = input("Cual es su nivel de educacion?")
nivel_educacion_true = nivel_educacion_to_english[nivel_educacion]
clave = f'nivel_educacion_{nivel_educacion_true}'
dataset[clave] = True

estado_civil = input("Cual es su estado civil?")
estado_civil_true = estado_civil_to_english[estado_civil]
clave = f'estado_civil_{estado_civil_true}'
dataset[clave] = True

forma_habitar = input("En que tipo de residencia habita?")
forma_habitar_true = forma_habitar_to_english[forma_habitar]
clave = f'forma_habitar_{forma_habitar_true}'
dataset[clave] = True

ocupacion = input("Que tipo de trabajo tiene?")
ocupacion_true = ocupacion_to_english[ocupacion]
clave = f'ocupacion_{ocupacion_true}'
dataset[clave] = True


tipo_organizacion = input("¿Qué tipo de organización de trabajo es? ")
tipo_organizacion_trabajo_true = tipo_organizacion_trabajo_to_english[tipo_organizacion]
clave = f'tipo_organizacion_trabajo_{tipo_organizacion_trabajo_true}'
dataset[clave] = True

tipo_cuenta = input("¿Qué tipo de cuenta bancaria tiene el solicitante?")
tipo_cuenta_trabajo_true = tipo_cuenta_trabajo_to_english[tipo_cuenta]
clave = f'tipo_cuenta_trabajo_{tipo_cuenta_trabajo_true}'
dataset[clave] = True


print("Dataset resultante:", dataset)
