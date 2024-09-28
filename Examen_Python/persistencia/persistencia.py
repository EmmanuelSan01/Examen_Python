productsFile="Examen_Python/persistencia/productos.dat"
customersFile="Examen_Python/persistencia/clientes.dat"
salesFile="Examen_Python/persistencia/ventas.dat"

def leerCodProd():
    fd=open(productsFile,"r")
    for line in fd:
        string=line.split(";")
        code=string[0]
        # print(code)
        return code
    fd.close()

def leerDescProd():
    fd=open(productsFile,"r")
    for line in fd:
        string=line.split(";")
        desc=string[1]
        # print(desc)
        return desc
    fd.close()

def leerValuProd():
    fd=open(productsFile,"r")
    for line in fd:
        string=line.split(";")
        price=string[2]
        # print(price)
        return price
    fd.close()

def leerCodCli():
    fd=open(customersFile,"r")
    for line in fd:
        string=line.split(";")
        code=string[0]
        # print(code)
        return code
    fd.close()

def leerNomCli():
    fd=open(customersFile,"r")
    for line in fd:
        string=line.split(";")
        name=string[1]
        # print(name)
        return name
    fd.close()

def leerTelCli():
    fd=open(customersFile,"r")
    for line in fd:
        string=line.split(";")
        phone=string[2]
        # print(phone)
        return phone
    fd.close()

def leerCodFact(input):
    fd=open(salesFile,"r")
    for line in fd:
        string=line.split(";")
        code=string[0]
        if code in salesFile:
            if code==input:
                print("\nCODFACT\tAÑO\tMES\tDIA\tCODCLI\tCODPROD\tUNIDADESPROD\tVALOR\tVALORFACT\n")
                print(string[0],"\t",string[1],"\t",string[2],"\t",string[3],"\t",string[4],"\t",string[5],"\t",string[6],"\t\t",string[7],"\t",string[8])
        else:
            print(f"\nNo existe factura con código '{input}'")
            break
    fd.close()

def leerCliMes(inputCode,inputMonth):
    fd=open(customersFile,"r")
    for line in fd:
        stringC=line.split(";")
        codecc=stringC[0]
        name=stringC[1]
    fd=open(salesFile,"r")
    for line in fd:
        stringS=line.split(";")
        codecf=stringS[4]
        month=stringS[2]
        if inputCode in customersFile:
            if codecc==inputCode:
                if codecc in codecf:
                    match month:
                        case "01":
                            output="Enero"
                        case "02":
                            output="Febrero"
                        case "03":
                            output="Marzo"
                        case "04":
                            output="Abril"
                        case "05":
                            output="Mayo"
                        case "06":
                            output="Junio"
                        case "07":
                            output="Julio"
                        case "08":
                            output="Agosto"
                        case "09":
                            output="Septiembre"
                        case "10":
                            output="Octubre"
                        case "11":
                            output="Noviembre"
                        case "12":
                            output="Diciembre"
                    if month in salesFile:
                        if month==inputMonth:
                            print("Código:\t",inputCode)
                            print("Nombre:\t",name)
                            print(f"Mes:\t{inputMonth} {output}")
                            print("\nCODFACT\tAÑO\tMES\tDIA\tCODCLI\tCODPROD\tUNIDADESPROD\tVALOR\tVALORFACT\n")
                            print(stringS[0],"\t",stringS[1],"\t",stringS[2],"\t",stringS[3],"\t",stringS[4],"\t",stringS[5],"\t",stringS[6],"\t\t",stringS[7],"\t",stringS[8])
                    else:
                        print(f"\nEl cliente con código '{inputCode}' no tiene facturas en el mes '{inputMonth}'")
                        break    
                else:
                    print(f"\nNo hay facturas para el cliente con código '{inputCode}'")
                    break
        else:
            print(f"\nNo existe cliente con código '{inputCode}'")
            break
    fd.close()

def leerYear():
    fd=open(salesFile,"r")
    for line in fd:
        string=line.split(";")
        year=string[1]
        # print(year)
        return year
    fd.close()

def leerMes():
    fd=open(salesFile,"r")
    for line in fd:
        string=line.split(";")
        month=string[2]
        # print(month)
        return month
    fd.close()

def leerDia():
    fd=open(salesFile,"r")
    for line in fd:
        string=line.split(";")
        day=string[3]
        # print(day)
        return day
    fd.close()

def leerCodCliFact():
    fd=open(salesFile,"r")
    for line in fd:
        string=line.split(";")
        code=string[4]
        # print(code)
        return code
    fd.close()

def leerCodCliProdFact():
    fd=open(salesFile,"r")
    for line in fd:
        string=line.split(";")
        code=string[5]
        # print(code)
        return code
    fd.close()

def leerUnidProd():
    fd=open(salesFile,"r")
    for line in fd:
        string=line.split(";")
        units=string[6]
        # print(units)
        return units
    fd.close()

def leerValor():
    fd=open(salesFile,"r")
    for line in fd:
        string=line.split(";")
        price=string[7]
        # print(price)
        return price
    fd.close()

def leerValorFact():
    fd=open(salesFile,"r")
    for line in fd:
        string=line.split(";")
        total=string[8]
        # print(total)
        return total
    fd.close()
