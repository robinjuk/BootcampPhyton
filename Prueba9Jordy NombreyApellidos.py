#cadenas de texto

nombre = "Rodrigo Medina"
#print(nombre[2:4])

print(nombre[8:14])

#Base de datos existiran dos columnas, una que se llame nombre y la otra que se llame apellido

def nombrecapital():
    print("Introduce un nombre")
    nombre = input()
    #Funciones para formatear texto
    #Existe una funcion que permite unicamente poner la primera letra en mayuscula
    nombreactualizado = nombre.capitalize()
    print(nombreactualizado)



def nombreminus():
    print("Introduce un nombre")
    nombre = input()
    
    nombreactualizado = nombre.lower()
    print(nombreactualizado)

#----------------------------------------MVP ZONE------------------------------------------------------------------
def nombremayus():
    print("Introduce un nombre")
    nombre = input()
    
    nomUsuario = nombre[0:7]
    apellido = nombre[8:14]

    nomUsuarioActualizado = nomUsuario.lower()
    apellidoactualizado = apellido.upper()

    print(nomUsuarioActualizado)
    print(apellidoactualizado)



#Para invertir letras. Si esta en mayusculas, se pone en minusculas y al contrario.

def inversorletras():
    print("Introduce un nombre")
    nombre = input()
    
    nomUsuario = nombre[0:6]
    apellido = nombre[7:14]

    #nomUsuarioActualizado = nomUsuario.lower()
    #apellidoactualizado = apellido.upper()

    #print(nomUsuarioActualizado)
    #print(apellidoactualizado)
    nombreActualizado = nombre.swapcase()
    print(nombreActualizado)


#Se quiere localizar en el apellido la estructura "Ave"
def buscadorletras():
    print("Introduce un nombre")
    nombre = input()
    
    if nombre.find("ave") != -1:
        print("Contiene 'ave'")
    else:
        print("No contiene 'ave'")

#Transorma una cadena en una lista
def separadorletras():
    print("Introduce un nombre")
    nombre = input()
    
    print(nombre.split(" "))

separadorletras()