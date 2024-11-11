print("Bienvenido a Volaris, ¡Tu tienda de boletos de avión!")
nn = input("Para saber a nombre de quien está la cuenta, inserta tu nombre: ")
print("Perfecto,", nn, "te mostraremos nuestros destinos disponibles y tú nos dirás qué te interesa ver. Podemos venderte un maximo de 5 boletos")
total_boletos = 0
y=0
historial = {
    "Cancún (Nacional)": 0,
    "Guadalajara (Nacional)": 0,
    "Tijuana (Nacional)": 0,
    "Monterrey (Nacional)": 0,
    "CDMX (Nacional)": 0,
    "Puerto Vallarta (Nacional)": 0,
    "Mazatlán (Nacional)": 0,
    "Acapulco (Nacional)": 0,
    "Cozumel (Nacional)": 0,
    "La Paz (Nacional)": 0,
    "Los Angeles (Internacional)": 0,
    "Miami (Internacional)": 0,
    "Nueva York (Internacional)": 0,
    "Chicago (Internacional)": 0,
    "Houston (Internacional)": 0,
    "San Francisco (Internacional)": 0,
    "Dallas (Internacional)": 0,
    "Las Vegas (Internacional)": 0,
    "Toronto (Internacional)": 0,
    "Londres (Internacional)": 0,
}
#PRECIOS DE BOLETOS
cancun = "Cancún (Nacional) $150 USD"
gdl = "Guadalajara (Nacional) $100 USD"
tij = "Tijuana (Nacional) $80 USD"
mon = "Monterrey (Nacional) $90 USD"
cdmx = "CDMX (Nacional) $70 USD"
pvr = "Puerto Vallarta (Nacional) $120 USD"
maz = "Mazatlán (Nacional) $110 USD"
aca = "Acapulco (Nacional) $95 USD"
coz = "Cozumel (Nacional) $130 USD"
lpz = "La Paz (Nacional) $140 USD"
la = "Los Angeles (Internacional) $300 USD"
mia = "Miami (Internacional) $350 USD"
ny = "Nueva York (Internacional) $400 USD"
chi = "Chicago (Internacional) $370 USD"
hou = "Houston (Internacional) $320 USD"
sf = "San Francisco (Internacional) $330 USD"
dal = "Dallas (Internacional) $310 USD"
lv = "Las Vegas (Internacional) $280 USD"
tor = "Toronto (Internacional) $450 USD"
lon = "Londres (Internacional) $600 USD"
#VALORES DE TUA
tua = 20 
print("---------------------")
print("O(∩_∩)O ... LOADING")
print("---------------------")
print("Antes", nn, "ten en cuenta que tu estado de cuenta actual es de: $", y)
print("---------------------")
print("CATÁLOGO DE DESTINOS DISPONIBLES:")
print("---------------------")
while True:
    print(f"{cancun} (1), {gdl} (2), {tij} (3), {mon} (4), {cdmx} (5), {pvr} (6), {maz} (7), {aca} (8), {coz} (9), {lpz} (10), {la} (11), {mia} (12), {ny} (13), {chi} (14), {hou} (15), {sf} (16), {dal} (17), {lv} (18), {tor} (19), {lon} (20)")
    print("Antes de que nos digas qué destino te interesa, debes saber que solo constamos con 5 boletos en existencia de cada uno.")
    rr = input("¿De qué destino quieres información? ")
    if rr in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
        if rr == "1":
            destino = "Cancún (Nacional)"
            precio = 150 
        elif rr == "2":
            destino = "Guadalajara (Nacional)"
            precio = 100 
        elif rr == "3":
            destino = "Tijuana (Nacional)"
            precio = 80  
        elif rr == "4":
            destino = "Monterrey (Nacional)"
            precio = 90
        elif rr == "5":
            destino = "CDMX (Nacional)"
            precio = 70
        elif rr == "6":
            destino = "Puerto Vallarta (Nacional)"
            precio = 120
        elif rr == "7":
            destino = "Mazatlán (Nacional)"
            precio = 110 
        elif rr == "8":
            destino = "Acapulco (Nacional)"
            precio = 95
        elif rr == "9":
            destino = "Cozumel (Nacional)"
            precio = 130
        elif rr == "10":
            destino = "La Paz (Nacional)"
            precio = 140 
        elif rr == "11":
            destino = "Los Angeles (Internacional)"
            precio = 300 
        elif rr == "12":
            destino = "Miami (Internacional)"
            precio = 350
        elif rr == "13":
            destino = "Nueva York (Internacional)"
            precio = 400
        elif rr == "14":
            destino = "Chicago (Internacional)"
            precio = 370
        elif rr == "15":
            destino = "Houston (Internacional)"
            precio = 320
        elif rr == "16":
            destino = "San Francisco (Internacional)"
            precio = 330
        elif rr == "17":
            destino = "Dallas (Internacional)"
            precio = 310
        elif rr == "18":
            destino = "Las Vegas (Internacional)"
            precio = 280
        elif rr == "19":
            destino = "Toronto (Internacional)"
            precio = 450
        elif rr == "20":
            destino = "Londres (Internacional)"
            precio = 600
        print("---------------------")
        print("(•ˋ _ ˊ•) ... LOADING")
        print("---------------------")
        while True:
            rr_cantidad = int(input(f"Dinos cuántos boletos quieres para {destino}: "))
            if historial[destino] + rr_cantidad > 5: # LÍMITE DE 5 BOLETOS
                print("Has elegido una cantidad que excede el límite de 5 boletos por destino, inténtalo de nuevo.")
            else:
                historial[destino] += rr_cantidad 
                total_precio = precio * rr_cantidad 
                y += total_precio
                total_boletos += rr_cantidad  
                print("Bien, tu total ahora es de: $", y, "USD (sin incluir la TUA)")
                break
        while True:
            elc1 = input("¿Quieres seguir comprando? (sí) (no) ")
            if elc1 == "sí":
                print("Bien, sigamos comprando.")
                break 
            elif elc1 == "no":
                print("Pasemos a tu cuenta final entonces.")
                break
            else:
                print("Parece que has escrito una respuesta no válida.")
        if elc1 == "no":
            break 
    else:
        print("Opción no válida, intenta de nuevo.")  
#AÑADO TUA
print("---------------------")
pppf = y + tua
print("Tu total final es de: $", pppf, "USD (incluyendo TUA).")
print("------------")
print("Aceptando tu método de pago en el sistema...")
print("------------")
print("Muchas gracias por usar nuestra tienda!!, vuelve pronto ヾ(⌐■-■)ノ♪")