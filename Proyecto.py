Usuario = input("ingresar el nombre del usuario: ").lower()
Monto = float(input("Ingrese el monto a cobrar: "))
from datetime import datetime
fecha = input("Ingrese la fecha inicial: ")
fecha_inicial = datetime.strptime(fecha, "%d/%m/%Y")
dia_paga = fecha_inicial.day
mes_paga = fecha_inicial.month + 1
año_paga = fecha_inicial.year
if mes_paga > 12:
    mes_paga = 1
    año_paga += 1
Gastos_administrativos =float (Monto * 0.005)
Numero_pagos = int(input ("Cuantos pagos va a realizar: "))
Tnominal_anual = 0.04
Multa= float (Tnominal_anual/360)   
Tnominal_mensual =float (Tnominal_anual/12)

#Pago 1
for i in range (Numero_pagos):
    
    try:
        print (dia_paga,"/",mes_paga,"/",año_paga)
        
        mes_paga += 1  
        
        if mes_paga > 12:
            mes_paga = 1      
            año_paga += 1     

    except NameError:
        print("Escribir la fecha como (dd/mm/yyyy)")
Factor_descuento = (1 + Tnominal_mensual) ** (-Numero_pagos)
Cuota_fija = (Tnominal_mensual * Monto) / (1 - Factor_descuento)
DIVIDENDO = Cuota_fija

for i in range(Numero_pagos):
    fecha_pagar = datetime(año_paga, mes_paga, dia_paga)
    fecha_rea = input("Ingrese la fecha en que pagó (dd/mm/yyyy): ")
    fecha_real = datetime.strptime(fecha_rea, "%d/%m/%Y")
    dia_real = fecha_real.day
    mes_real = fecha_real.month
    año_real = fecha_real.year
    monto_pagado = float(input("Ingrese cuánto pagó este mes: "))
    monto_total = monto_pagado - Monto
    if Monto != monto_total:
        while monto_pagado != (Numero_pagos):
            fecha_pagar = datetime(año_paga, mes_paga, dia_paga)
            fecha_real = input("Ingrese la fecha en que pagó (dd/mm/yyyy): ")
            days=0
            monto_pagado = float(input("Ingrese cuánto pagó este mes: "))
    else:
        print ("Usted ha saldado su deuda con la sociedad")
            
