from operator import truediv
import random


def juego_adivinanza():
    # Genera un numero del 1 al 100
    
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
    adivinado = False

    print("*" * 40)
    print("¡Bienvenido al juego de adivinanza de numero")
    print("Debes adivinar un numero entre el 1 y el 100")
    print("¡Intenta adivinarlo!")
    print("*" * 40)

    while not adivinado and intentos < max_intentos:
        # Solisitar un numero
        try:
            numero_ingresado = int(input("Introduzca un nemero del 1 al 100: "))

            if 1 <= numero_ingresado <= 100:
             intentos += 1
             
             
             if numero_ingresado < numero_secreto:
                 print(f"El numero secreto es mayor a {numero_ingresado}")
             elif numero_ingresado > numero_secreto:
                 print(f"El numero secreto es menor a {numero_ingresado}")
             else:
                 print(
                    f"¡Felicitaciones has ganado! El numero {numero_ingresado} es el secreto y lo has logrado en {intentos} intentos")
                 adivinado = True
            
            else:
                print("por favor introduzca un numero valido entre el 1 y el 100")
        
        except ValueError:
            print("Entrada inválida: debe ingresar un número entero.")        
    
    
    # Si terminó el bucle y no adivinó
    if not adivinado:
        print(f"Se acabaron los intentos. El número secreto era {numero_secreto}.")
    
    print("Gracias por jugar 😎")


juego_adivinanza()