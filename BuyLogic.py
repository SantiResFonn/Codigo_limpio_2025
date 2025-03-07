#Exception personalizada para cada clase de error

class ErrorValorCompra(Exception):
    """"ERROR: El valor de la compra no puede ser un número menor o igual a cero """
class ErrorValorIVA(Exception):
    """"ERROR: El valor del IVA no puede ser un número menor a cero"""
class ErrorValorImpuestoConsumo(Exception):
    """"ERROR: El valor del Impuesto al consumo no puede ser un número menor a cero"""
class ErrorImpuestoLicor(Exception):
    """"ERROR: El valor del Impuesto al licor no puede ser un número menor a cero  """
class ErrorParametroBolsa(Exception):
    """"ERROR: Parametro de impuesto de bolsa no valido (Si/No) """


def calcular_total_compra(valor_compra: float, valor_iva: float, valor_impuesto_consumo: float, impuesto_licor: float, impuesto_bolsa: str):
    #Asignacion de entradas y cambio a porcentajes
    valor_impuesto_bolsa = 0
    valor_iva_porcentaje = valor_iva/100
    valor_impuesto_consumo_porcentaje = valor_impuesto_consumo/100
    impuesto_licor_porcentaje = impuesto_licor/100
    # Manejo de errores

    if valor_compra <= 0:
        raise ErrorValorCompra("ERROR: El valor de la compra no puede ser un número menor o igual a cero ")
    if valor_iva_porcentaje < 0:
        raise ErrorValorIVA("ERROR: El valor del IVA no puede ser un número menor a cero")
    if valor_impuesto_consumo_porcentaje < 0:
        raise ErrorValorImpuestoConsumo("ERROR: El valor del Impuesto al consumo no puede ser un número menor a cero")
    if impuesto_licor_porcentaje < 0:
        raise ErrorImpuestoLicor("ERROR: El valor del Impuesto al licor no puede ser un número menor a cero  ")

    #Condicion para ver si se aplica o no el impuesto de bolsa
    if impuesto_bolsa.lower() == "si":
        valor_impuesto_bolsa = 70
    elif impuesto_bolsa.lower() == "no":
        valor_impuesto_bolsa = 0
    else:
        raise ErrorParametroBolsa("ERROR: Parametro de impuesto de bolsa no valido (Si/No) ")
    return valor_compra + (valor_compra*valor_iva_porcentaje) + (valor_compra*valor_impuesto_consumo_porcentaje) + (valor_compra*impuesto_licor_porcentaje) + valor_impuesto_bolsa
