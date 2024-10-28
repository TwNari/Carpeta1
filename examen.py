print ("SIMULADOR DE CAJERO")
nombre = input ("Para comenzar, ¿A qué nombre esta la cuenta de banco?")
cco = (input ("Favor de ingresar tu nip"))
while True:
    cc1 = (input ("Favor de confirmar el nip"))
    if cc1 == cco:
     print ("Perfecto, prosigamos entonces.")
     break
    else:
        print ("Haz escrito mal tu nip, vuelve a intentarlo")
num1 = float (input ( "Por favor da una cantidad inicial para tu cuenta de banco") )
print ( "La cantidad de dinero en tu cuenta es $" , num1 )
#Empezar movimientos en la cuenta
print ( "-----------------------------------------")
print ( "Ahora hagamos algunas transacciones")
while True:
    d = input ( "¿Deseas hacer alguna operación en tu cuenta? (sí) (no)")
    print ("Respuesta no reconocida. Por favor, responde con 'sí' o 'no'(con acento en la i)")
    #Respuesta positiva
    if d == "sí":
        print("Empecemos entonces")
        print("-----------------------------------------")
        while True:
            r = input("Para checar tu estado de cuenta escribe (1), para depositar dinero escribe (2), para retirar dinero (3) se te cobrara un impuesto de $16 y para finalizar tu sesión en el cajero (4): ")
            if r == "1":
                print("La cantidad de dinero en tu cuenta es de $", num1)
            elif r == "2":
                s = float(input("¿Cuánto dinero quieres depositar? "))
                num1 += s
                print("Has depositado $", s, ". Tu nuevo saldo es $", num1)
                print("-----------------------------------------")
            elif r == "3":
                s = float(input("¿Cuánto dinero quieres retirar? "))
                if s > num1 - 16:
                    print("No tienes suficiente saldo para retirar esa cantidad.")
                else:
                    num1 -= s - 16
                    print("Has retirado $", s, ". Tu nuevo saldo es $", num1)
                    print("-----------------------------------------")
            elif r == "4":
                print("Entonces hemos terminado tu consulta en este cajero. Tu estado de cuenta final es de $", num1)
                break 
            else:
                print("Opción no reconocida. Por favor, elige una opción del menú.")
        break
#Si no quieren
    elif d == "no":
        print("seria todo por hoy")
        break
#En caso de que escribiera mal
    else:
        print("se acabo")
print ( "Muy bien, hemos terminado. Tu estado de cuenta ha terminado con $" , num1 )
print ( "-----------------------------------------")
