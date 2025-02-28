def calcular_compra(valor_compra: float, valor_iva: float, valor_ic: float, impuesto_licor: float, impuesto_bolsa: str):
    valor_ib = 0
    valor_iva=valor_iva/100
    valor_ic=valor_ic/100
    impuesto_licor=impuesto_licor/100
    #Condicion para ver si se aplica o no el impuesto de bolsa
    if impuesto_bolsa.lower() == "si":
        valor_ib = 70
    elif impuesto_bolsa.lower() == "no":
        valor_ib = 0
    return valor_compra + (valor_compra*valor_iva) + (valor_compra*valor_ic) + (valor_compra*impuesto_licor) + valor_ib
