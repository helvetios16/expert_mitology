from arta import RulesEngine

# Inicializar el motor de reglas con la configuración en el directorio actual
eng = RulesEngine(config_path="")

# Datos de entrada del paciente
data = {"fever": True, "cough": True, "sneezing": False}

# Aplicar las reglas al conjunto de datos
result = eng.apply_rules(input_data=data)

print(result)
