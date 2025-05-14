# Calculadora de Impuestos de Compras

## Editores:

- Valery Monsalve
- Santiago Alcaraz

## Autor

- Santiago Restrepo Fonnegra

## ¿Qué es y para qué es?

Este proyecto es una calculadora de impuestos de compras que, al ingresar ciertos porcentajes aplicables a un producto, calcula el valor total a pagar. Los impuestos considerados son:

- IVA
- Impuesto al consumo
- Impuesto a los licores
- Impuesto de bolsa

## ¿Cómo lo hago funcionar?

### Prerrequisitos

- Python 3.x instalado en el sistema.

### Ejecución

1. Clona el repositorio:

   ```bash
   gh repo clone SantiResFonn/Codigo_limpio_2025
   ```

2. Navega a la carpeta raíz del proyecto:

   ```bash
   cd Codigo_limpio_2025
   ```

3. Ejecuta el programa desde la línea de comandos:

   ```bash
   python src/view/console/TaxtesCalculationConsole.py
   ```

## ¿Cómo está hecho?

El proyecto sigue una arquitectura modular y está organizado de la siguiente manera:

- **Carpeta `src`**: Contiene el código fuente de la lógica de la aplicación, estructurado en subcarpetas por cada capa de la aplicación.

  - **`src/view/console`**: Incluye la interfaz de consola para interactuar con la calculadora.
  - **`src/model`**: Contiene la lógica de negocio para el cálculo de impuestos.

- **Carpeta `tests`**: Contiene las pruebas unitarias para asegurar el correcto funcionamiento de la aplicación.

Cada carpeta de código fuente incluye un archivo `__init__.py` para que Python la reconozca como un módulo y permita realizar importaciones adecuadas.

## Uso

Primero se debe introducir el valor de la compra.

- Luego el programa preguntara por el porcentaje del impuesto de IVA que se aplica, a la fecha de este README es 19%, 5%, 0. Introducir numeros enteros, ya que el programa se encarga de pasarlos a porcentajes.
- Luego preguntara si aplica el impuesto al consumo, como dicho anteriormente introducir solo enteros, los valores pueden ser hasta la creación de este README 4%, 8% y 0%
- Luego preguntara si aplica impuesto al licor, introducir tambien un entero.
- Luego preguntara si se le aplica el impuesto de bolsa, este valor es un "Si" o un "No", si es un si se aplicara al final, si es un no, no sumara nada al valor final
  Al introducir estos datos, se totalizara el valor de la compra.

Para ejecutar las pruebas unitarias desde la carpeta raíz, utiliza el siguiente comando:

```bash
python tests/TaxesTest.py
```

Para que las pruebas se ejecuten correctamente desde la carpeta raíz, asegúrate de indicar la ruta de búsqueda donde se encuentran los módulos, añadiendo las siguientes líneas al inicio del módulo de pruebas:

```python
import sys
sys.path.append("src")
```

## ¿Cómo ejecuto la interfaz gráfica (GUI)?

Este proyecto también cuenta con una interfaz gráfica hecha con Kivy, que permite interactuar con la calculadora de impuestos de forma visual.

Prerequisitos:

- Tener instalado Python 3.x
- Instalar la librería Kivy, si no la tienes aún:

```bash
pip install kivy

```

Ejecución:

- Desde la carpeta raíz del proyecto, ejecuta el siguiente archivo:

```bash
python GUI.py

```

- Aparecerá una ventana donde puedes introducir los datos de la compra y los impuestos correspondientes. Al presionar el botón "Calcular total", verás el valor total con todos los impuestos aplicados.

## 📦 Ejecutable

Puedes descargar la última versión del ejecutable desde la carpeta [`dist/`](dist/main.exe).

## 🚀 Cómo usarlo

1. Descarga el archivo `main.exe`.
2. Haz doble clic para ejecutarlo. _(No requiere instalar Python)_

> ⚠️ Si Windows bloquea la app, haz clic derecho → Propiedades → "Desbloquear".

## 🛠️ Construcción del ejecutable

Este proyecto usa [PyInstaller](https://www.pyinstaller.org/) para empaquetar el archivo `main.py`.  
Puedes generar el ejecutable con:

```bash
pyinstaller main.spec
```
