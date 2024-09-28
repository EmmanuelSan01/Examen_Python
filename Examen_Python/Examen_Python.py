from persistencia.persistencia import *
from modelo.modelo import *
from interfaz.interfaz import menu

while True:
    op=menu()
    match op:
        case 1:
            CopiaFact()
        case 2:
            resumenFactCliMes()
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("\n\tGracias por usar el software.\n")
            break

# leerCodProd()
# leerDescProd()
# leerValuProd()
# leerCodCli()
# leerNomCli
# leerTelCli()
# leerCodFact()
# leerYear()
# leerMes()
# leerDia()
# leerCodCliFact()
# leerUnidProd()
# leerValor()
# leerValorFact()