def comprobador():
    colorescribir = input("Introduzca el color de su tarjeta: ")
    colorescribir = colorescribir.lower()

    if colorescribir == "verde":
        print("Usted puede pasar sin problema")

    elif colorescribir == "amarillo":
        print("Usted puede pasar con dificultades")
    
    elif colorescribir == "rojo":
        print("Usted no puede pasar bajo ningún concepto")

    else:
        print("Ha introducido un color no válido")


comprobador()
