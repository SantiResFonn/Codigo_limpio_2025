#Exception personalizada para cada clase de error

class ErrorValorCompra(Exception):
    """"ERROR: El valor de la compra no puede ser un número menor o igual a cero """
class ErrorValorIVA(Exception):
    """"ERROR: El valor del IVA no puede ser un número menor a cero"""
class ErrorValorIC(Exception):
    """"ERROR: El valor del Impuesto al consumo no puede ser un número menor a cero"""
class ErrorImpuestoLicor(Exception):
    """"ERROR: El valor del Impuesto al licor no puede ser un número menor a cero  """
class ErrorParametroBolsa(Exception):
    """"ERROR: Parametro de impuesto de bolsa no valido (Si/No) """


def calcular_compra(valor_compra: float, valor_iva: float, valor_ic: float, impuesto_licor: float, impuesto_bolsa: str):
    #Asignacion de entradas y cambio a porcentajes
    valor_ib = 0
    valor_iva=valor_iva/100
    valor_ic=valor_ic/100
    impuesto_licor=impuesto_licor/100
    # Manejo de errores

    if valor_compra <= 0:
        raise ErrorValorCompra("ERROR: El valor de la compra no puede ser un número menor o igual a cero ")
    if valor_iva < 0:
        raise ErrorValorIVA("ERROR: El valor del IVA no puede ser un número menor a cero")
    if valor_ic < 0:
        raise ErrorValorIC("ERROR: El valor del Impuesto al consumo no puede ser un número menor a cero")
    if impuesto_licor < 0:
        raise ErrorImpuestoLicor("ERROR: El valor del Impuesto al licor no puede ser un número menor a cero  ")

    #Condicion para ver si se aplica o no el impuesto de bolsa
    if impuesto_bolsa.lower() == "si":
        valor_ib = 70
    elif impuesto_bolsa.lower() == "no":
        valor_ib = 0
    else:
        raise ErrorParametroBolsa("ERROR: Parametro de impuesto de bolsa no valido (Si/No) ")
    return valor_compra + (valor_compra*valor_iva) + (valor_compra*valor_ic) + (valor_compra*impuesto_licor) + valor_ib
