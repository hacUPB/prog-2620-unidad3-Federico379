Promedio = float(input("ingrese su promedio:" ))

nivel_socioeconomico = int(input("ingrese su estrato:" ))

otorgado = (Promedio > 9.0) or (Promedio >= 8.0 and nivel_socioeconomico == 1)

print("beca otorgada:", otorgado)