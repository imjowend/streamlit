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
dia_inicio_proceso_to_number = {
    "Lunes": 1,
    "Martes": 2,
    "Miercoles": 3,
    "Jueves": 4,
    "Viernes": 5,
    "Sabado": 6,
    "Domingo": 7,
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

dataset = {
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
    'tipo_organizacion_trabajo_Transport': False
}

tipo_organizacion = input("¿Qué tipo de organización de trabajo es? ")
tipo_organizacion_trabajo_true = tipo_organizacion_trabajo_to_english[tipo_organizacion]
clave = f'tipo_organizacion_trabajo_{tipo_organizacion_trabajo_true}'
dataset[clave] = True
print("Dataset resultante:", dataset)


dia_inicio_proceso = input("Que dia de la semana pidió el credito?")
dia_inicio_proceso_number = dia_inicio_proceso_to_number[dia_inicio_proceso]
dataset['dia_inicio_proceso'] = dia_inicio_proceso_number

tipo_contrato = print("Quien la acompaño al momento de pedir el credito")
tipo_contrato_true = tipo_contrato_to_english[tipo_contrato]
clave = f'tipo_contrato_{tipo_contrato_true}'
dataset[clave] = True

estatus_laboral = print("Cual es su situacion laboral actual?")
estatus_laboral_true = estatus_laboral_to_english[estatus_laboral]
clave = f'estatus_laboral_{estatus_laboral_true}'
dataset[clave] = True