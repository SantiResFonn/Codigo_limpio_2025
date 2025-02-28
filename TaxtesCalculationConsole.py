import BuyLogic

#Entradas
try:
        valor_compra=float(input("Ingrese el valor de la compra: "))
        valor_iva=float(input("Ingrese el porcentaje del IVA aplicable a la compra: "))
        valor_ic=float(input("Ingrese el porcentaje del Impuesto al consumo aplicable a la compra: "))
        impuesto_licor=float(input("Ingrese el porcentaje del Impuesto al licor aplicable a la compra: "))
        impuesto_bolsa=input("¿A su compra se le aplica impuesto de bolsa?(Si/No)")

        #Proceso
        total = BuyLogic.calcular_compra(valor_compra,valor_iva,valor_ic,impuesto_licor,impuesto_bolsa)

        #Salidas

        print(f"El valor total de la compra es {total}")
except Exception as ex:
    print(f"ALERTA: Ocurrio un Error {ex}")