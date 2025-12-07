Usuario = input("ingresar el nombre del usuario: ")
Monto = input("Ingrese el monto a cobrar: ")
from datetime import date
from dateutil import relativedelta
Fecha_prestamo = (input("Ingrese la fecha del prestamo(DD-MM-YYYY): "))
Fecha = date.strftime(Fecha_prestamo, "%d-%m-%Y")
Numero_pagos = input ("Cuantos pagos va a realizar: ")
Tnominal_anual = 0.04
#Gastos_administrativos =float (Monto * 0.005)
Multa= float (Tnominal_anual/360)
Tnominal_mensual =float (Tnominal_anual/12)

#Pago 1
Fecha_pagar= (Fecha + relativedelta(months=1))
print(Fecha_pagar) 