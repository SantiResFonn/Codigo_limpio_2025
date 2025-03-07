Santiago Restrepo Fonnegra

El git contiene un Excel con el resultado de los diferentes casos de prueba más la entrevista del experto del tema
El archivo TaxtesCalculatioConsole corresponde a la interfaz del usuario que recibe las varibles de entradas que son: el valor de la compra, el valor del IVA(El programa lo convierte a porcentaje), el valor del Impuesto al consumo(El programa lo convierte a porcentaje),
el valor del impuesto al licor(El programa lo convierte a porcentaje) y un parametro de Si/No para verificar si se le aplica el impuesto de bolsa que es de 70 pesos en caso de ser aplicado

El Archivo BuyLogic corresponde a la logica del codigo para calcular el valor final de la compra sumando cada impuesto luego de ser calculado, además contiene el manejo de errores que puede dar el sistema, como la introducción de valores negativos o un parametro
indebido para el impuesto de las bolsas arrojando su respectiva excepcion

El Archivo TaxestTest pone en prueba todos los casos de prueba, exitosos, excepciones y errores que estan en el archivo de Excel Casos de prueba.


