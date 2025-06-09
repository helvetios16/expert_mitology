# Descripción del Proyecto

<!--toc:start-->

- [Descripción del Proyecto](#descripción-del-proyecto)
  - [Componentes principales](#componentes-principales)
  <!--toc:end-->

Este proyecto implementa un sistema de procesamiento y validación de datos basado en reglas definidas por el usuario. El núcleo del sistema es el archivo `main.py`, que se encarga de cargar, interpretar y aplicar las reglas especificadas en el archivo `rules.yaml` sobre un conjunto de datos de entrada.

## Componentes principales

- **main.py**: Contiene la lógica principal del programa. Se encarga de:

  - Leer y cargar las reglas desde el archivo `rules.yaml`.
  - Procesar los datos de entrada.
  - Aplicar las reglas de validación y transformación sobre los datos.
  - Generar un reporte o salida con los resultados de la validación.

- **rules.yaml**: Archivo de configuración donde se definen las reglas que el sistema debe aplicar. Estas reglas pueden incluir validaciones de formato, restricciones de valores, transformaciones de datos, entre otras.
