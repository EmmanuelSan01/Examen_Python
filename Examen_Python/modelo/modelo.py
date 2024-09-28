from persistencia.persistencia import *

def CopiaFact():
    print("\nCOPIA DE UNA FACTURA")
    print("\nIngrese el código de la factura")
    code=input("> ")
    leerCodFact(code)

def resumenFactCliMes():
    print("\nResumen de las facturas de un cliente en un mes")
    print("\nIngrese el código del cliente")
    code=input("> ")
    print("\nIngrese el mes")
    month=input("> ")
    leerCliMes(code,month)