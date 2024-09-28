def menu():
    while True:
        print("")
        print("\t\tBIENVENIDO A BILLIFY")
        print("")
        print("\t\t* Menú de Opciones *")
        print("")
        print("\t1. Copia de una factura")
        print("\t2. Resumen de las facturas de un cliente en un mes")
        print("\t3. Diagrama de barras")
        print("\t4. Productos comunes comprados entre dos clientes")
        print("\t5. Salida del sistema")
        print("\nIngrese el número correspondiente a la función\n",end="> ")
        try:
            option=int(input())
            if 1<=option<=5:
                return option
            else:
                raise ValueError
        except ValueError:
            print("\n\tERROR. Opción no válida.")
            input("\nPresione cualquier letra para volver al menu...\n> ")