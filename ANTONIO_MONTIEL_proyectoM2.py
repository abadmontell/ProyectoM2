#Ejercicio 1

# iniciamos un ciclo
while True:  
    # solicitamos al usuario que ingrese una palabra
    palabra = input("Ingrese una palabra con al menos cuatro letras: ")  
    # calculamos la longitud de la palabra ingresada
    longitud = len(palabra)  
# si la longitud es menor que 4
    while longitud < 4:  
        # solicitamos al usuario que ingrese otra palabra
        palabra = input("La palabra debe tener al menos cuatro letras. Ingrese una palabra: ")  
        # calculamos la longitud de la nueva palabra ingresada
        longitud = len(palabra)  
# si la longitud está entre 4 y 8
    if longitud <= 8:  
        # imprimimos un mensaje indicando que la palabra es correcta
        print("La palabra es correcta.")  
         # si la longitud es mayor que 8
    else: 
         # imprimimos un mensaje indicando que sobran letras
        print("Sobran letras. Tiene", longitud, "letras.") 
# preguntamos al usuario si desea ingresar otra palabra
    respuesta = input("¿Desea ingresar otra palabra? (S/N) ")  
    # si la respuesta no es "S" (no desea ingresar otra palabra)
    if respuesta.upper() != "S":  
        # rompemos el ciclo 
        break  

#Ejercicio 2

# Iniciamos un ciclo para que el usuario pueda ingresar múltiples conjuntos de coordenadas
while True:
    # Solicitamos al usuario que ingrese las coordenadas
    x = float(input("Ingrese X: "))
    y = float(input("Ingrese Y: "))

    # Verificamos en qué cuadrante se encuentra el punto y mostramos el resultado al usuario
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    elif x == 0 and y == 0:
        print("El punto se encuentra en el origen.")
    elif x == 0:
        print("El punto se encuentra sobre el eje Y.")
    elif y == 0:
        print("El punto se encuentra sobre el eje X.")
    else:
        print("El punto se encuentra en el cuadrante IV.")

    # Preguntamos al usuario si desea ingresar otro conjunto de coordenadas
    respuesta = input("¿Desea ingresar otro punto? (S/N) ")

    # Si la respuesta no es "S" (es decir, si el usuario no desea ingresar otro punto), detenemos el ciclo infinito y finalizamos el programa
    if respuesta.upper() != "S":
        break