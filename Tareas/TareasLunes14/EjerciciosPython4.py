def comprobador(variable1):
    color = variable1
    color = color.lower()

    if color == "verde":
        print("Usted puede pasar sin problema")

    elif color == "amarillo":
        print("Usted puede pasar con dificultades")
    
    elif color == "rojo":
        print("Usted no puede pasar bajo ningún concepto")

    else:
        print("Ha introducido un color no válido")

colorescribir = input("Introduzca el color de su tarjeta: ")

comprobador(colorescribir)
