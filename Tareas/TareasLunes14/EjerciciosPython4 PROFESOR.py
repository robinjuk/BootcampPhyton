def comprobador():
    texto = input("Introduzca el color de su tarjeta (rojo, amarillo o verde): ")
    if isinstance(texto, str):
        color = texto.lower()

        match color:
            case "verde":
                print("Usted puede pasar sin problema")

            case "amarillo":
                print("Usted puede pasar con dificultades")

            case "rojo":
                print("Usted no puede pasar bajo ningún concepto")

            case _:
                print("Ha introducido un color no válido")

# Ejemplo de uso
comprobador()
