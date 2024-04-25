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
