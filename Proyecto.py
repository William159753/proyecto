from datetime import datetime

def pedir_fecha(texto):
    while True:
        try:
            return datetime.strptime(input(texto), "%d/%m/%Y")
        except:
            print("Error: use formato dd/mm/yyyy")

tabla = []           
datos_cargados = False

while True:

    print("\n====== MENU ======")
    print("1. Ingresar datos y registrar pagos")
    print("2. Ver tabla de amortización")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        tabla.clear()  

        monto = float(input("Monto del préstamo: "))
        cuotas = int(input("Cantidad de meses: "))

        fecha_inicio = pedir_fecha("Fecha inicio (dd/mm/yyyy): ")
        hoy = datetime.today()

        tasa_anual = 0.04
        tasa_mensual = tasa_anual / 12
        multa_diaria = tasa_anual / 360

        cuota = monto * tasa_mensual / (1 - (1 + tasa_mensual) ** -cuotas)

        meses_pasados = (hoy.year - fecha_inicio.year) * 12 + (hoy.month - fecha_inicio.month)
        if meses_pasados < 0:
            meses_pasados = 0
        if meses_pasados > cuotas:
            meses_pasados = cuotas

        saldo = monto
        fecha_pago = fecha_inicio

        print("\nSe deben registrar", meses_pasados, "cuotas hasta hoy\n")

        for i in range(1, cuotas + 1):

            mes = fecha_pago.month + 1
            año = fecha_pago.year
            if mes > 12:
                mes = 1
                año += 1
            fecha_pago = datetime(año, mes, fecha_pago.day)

            interes = saldo * tasa_mensual
            capital = cuota - interes
            saldo = saldo - capital

            if i <= meses_pasados:
                fecha_real = pedir_fecha("Fecha real de pago: ")
                dias_atraso = (fecha_real - fecha_pago).days
                if dias_atraso > 0:
                    multa = dias_atraso * cuota * multa_diaria
                else:
                    multa = 0
            else:
                fecha_real = "-"
                multa = 0

            tabla.append([
                i,
                fecha_pago.strftime("%d/%m/%Y"),
                round(cuota, 2),
                round(interes, 2),
                round(capital, 2),
                round(saldo, 2),
                fecha_real if fecha_real == "-" else fecha_real.strftime("%d/%m/%Y"),
                round(multa, 2)
            ])

        datos_cargados = True
        print("\n Datos registrados correctamente")

    elif opcion == "2":

        if not datos_cargados:
            print("\n No hay datos registrados")
        else:
            print("\nTABLA DE AMORTIZACIÓN\n")
            print("N° | Fecha Pago | Cuota | Interés | Capital | Saldo | Fecha Real | Multa")
            print("-" * 85)

            for fila in tabla:
                print(fila[0], "|", fila[1], "|", fila[2], "|",
                      fila[3], "|", fila[4], "|",
                      fila[5], "|", fila[6], "|", fila[7])

    elif opcion == "3":
        print("Saliendo del programa")
        break

    else:
        print("Opción inválida")
    monto_total = monto_pagado - Monto
    print ("El cliente tiene un capital cancelado de : ", monto_total)
elif opcion == 3:
    print ("Bye")
