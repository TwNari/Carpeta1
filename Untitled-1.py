print("Bienvenido a nuestra tienda de línea blanca")
nn = input("Para saber a nombre de quien está la cuenta, inserta tu nombre: ")
print("Perfecto,", nn, "te mostraremos nuestros productos y tú nos dirás qué te interesa ver.")
y = 0
total_productos = 0
historial = {
    "Refrigerador": 0,
    "Lavadora": 0,
    "Secadora": 0,
    "Estufa": 0,
    "Horno microondas": 0,
    "Lavavajillas": 0,
    "Horno de gas o eléctrico": 0
} # LISTADO PARA RESPETAR MI CANTIDAD DE STOCK
print("---------------------")
print("O(∩_∩)O ... LOADING")
print("---------------------")
print("Antes", nn, "ten en cuenta que tu estado de cuenta actual es de: $", y)
print("---------------------")
print("CATALOGO:")
# PRODUCTOS
pu = "Refrigerador $1,500 USD"
pd = "Lavadora $1,000 USD"
pt = "Secadora $1,000 USD"
pc = "Estufa $1,200 USD"
pcc = "Horno microondas $300 USD"
ps = "Lavavajillas $1,000 USD"
pss = "Horno de gas o eléctrico $1,000 USD"
print("---------------------")
while True:
    print("Constamos de", pu, " (1), ", pd, " (2), ", pt, " (3), ", pc, " (4), ", pcc, " (5), ", ps, " (6) y ", pss, " (7)")
    print("Antes de que nos digas qué producto te interesa, debes saber que solo constamos con 10 en existencia de cada uno.")
    rr = input("¿De qué producto quieres información? ")
    if rr in ["1", "2", "3", "4", "5", "6", "7"]: # LISTADO PARA NO HACER TANTA LINEA
        if rr == "1":
            producto = "Refrigerador"
            precio = 1500
        elif rr == "2":
            producto = "Lavadora"
            precio = 1000
        elif rr == "3":
            producto = "Secadora"
            precio = 1000
        elif rr == "4":
            producto = "Estufa"
            precio = 1200
        elif rr == "5":
            producto = "Horno microondas"
            precio = 300
        elif rr == "6":
            producto = "Lavavajillas"
            precio = 1000
        elif rr == "7":
            producto = "Horno de gas o eléctrico"
            precio = 1000
        print("---------------------")
        print("(•ˋ _ ˊ•) ... LOADING")
        print("---------------------")
        while True:
            rr_cantidad = int(input("Dinos qué tanta cantidad de este producto quieres comprar: "))
            if historial[producto] + rr_cantidad > 10: #LOS CORCHETES ME AYUDAN A SABER QUE PRODUCTO DEL HISTORIAL ME AGARRARON Y LLEVA EL CONTEO
                print("Has elegido una cantidad que excede el límite de 10 para ese producto, inténtalo de nuevo.")
            else:
                historial[producto] += rr_cantidad 
                y += precio * rr_cantidad  
                total_productos += rr_cantidad  
                print("Bien, tu total ahora es de:", y, "USD")
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
print("---------------------")
print("(👉ﾟヮﾟ)👉... LOADING")
print("Entonces", nn, "la cantidad que debes de pagar es de $", y, "USD")
descuento = 0.30 * y 
precio_final = y - descuento
while True:
    pp = input("¡Pero antes!, ¿Cuentas con una tarjeta de membresía con nosotros? Tener una te aplicaría un 30 porciento de descuento (sí) (no): ")
    if pp == "sí":
        print("Excelente, entonces tu precio sería de $", precio_final, "USD")
        break
    elif pp == "no":
        tarjeta = input("¿Deseas que te demos una? Cuestan $10 USD extras. (sí) (no): ")
        while True:
            if tarjeta == "no":
                print("De acuerdo, entonces tu precio final es de $", y, "USD")
                break
            elif tarjeta == "sí":
                otroprecio = precio_final + 10
                print("Muy bien! ╰(*°▽°*)╯, entonces tu precio es $", otroprecio, "USD")
                break
            else:
                print("Respuesta no reconocida, intenta de nuevo -recuerda que sí lleva acento en la i-")
        break
    else:
        print("Respuesta no reconocida, intenta de nuevo -recuerda que sí lleva acento en la i-")
print("------------")
print("Aceptando tu método de pago en el sistema...")
print("------------")
print("Muchas gracias por usar nuestra tienda!!, vuelve pronto ヾ(⌐■-■)ノ♪")
