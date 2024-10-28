print("Bienvenido a nuestra tienda en línea")
nn = input("Para saber a nombre de quien está la cuenta, inserta tu nombre: ")
print("Perfecto,", nn, "te mostraremos nuestro catálogo y tú nos dirás qué te interesa ver.")
x = 0
print("Tu estado de cuenta actual es de: $", x)
# Sección de precios
q = 15
we = 20
e = 18
r = 22
t = 35
y = 40
u = 30
i = 38
o = 50
p = 45
a = 55
s = 60
d = 25
while True:
    ac = input("¿Qué buscas? prendas superiores (1) prendas inferiores (2) vestidos (3) ropa deportiva (4): ")
    if ac == "1":
        while True:
            act = input("Tenemos las siguientes opciones: camisetas (1), camisas (2), blusas (3), suéteres (4), chalecos (5), abrigos (6): ")
            if act == "1":
                actt = input("Opciones de camisetas: Básica de algodón, cuello redondo: $", q, ", Gráfica con estampado abstracto: $", we, ", Camiseta de rayas estilo marinero: $", e, ", Camiseta deportiva de poliéster: $", r, ": ")
                if actt == "1":
                    x += q
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif actt == "2":
                    x += we
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif actt == "3":
                    x += e
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif actt == "4":
                    x += r
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                else:
                    print("Elegiste una opción no válida.")
            elif act == "2":
                acty = input("Opciones de camisas: Camisa de lino casual: $", t, ", Camisa formal de algodón con botones: $", y, ", Camisa de cuadros estilo leñador: $", u, ", Camisa con estampado tropical: $", i, ": ")
                if acty == "1":
                    x += t
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif acty == "2":
                    x += y
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif acty == "3":
                    x += u
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif acty == "4":
                    x += i
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                else:
                    print("Elegiste una opción no válida.")
    elif ac == "2":
        while True:
            acg = input("Tenemos las siguientes opciones de prendas inferiores: pantalones (1), shorts (2), faldas (3), leggins (4), jeans (5), para niños (6): ")
            if acg == "1":
                actp = input("Opciones de pantalones: Pantalón clásico: $", t, "(1), Pantalón de tela: $", y, "(2), Pantalón de mezclilla: $", u, ": ")
                if actp == "1":
                    x += t
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif actp == "2":
                    x += y
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                else:
                    print("Elegiste una opción no válida.")
            elif acg == "2":
                actsh = input("Opciones de shorts: Cortos: $", d, ", Largo: $", p, ": ")
                if actsh == "1":
                    x += d
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif actsh == "2":
                    x += p
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                else:
                    print("Elegiste una opción no válida.")
            elif acg == "3":
                actf = input("Opciones de faldas: Larga: $", we, ", Corta: $", e, ": ")
                if actf == "1":
                    x += we
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif actf == "2":
                    x += e
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                else:
                    print("Elegiste una opción no válida.")
            elif acg == "4":
                actl = input("Opciones de leggins: De deporte: $", e, ", De algodón: $", d, ": ")
                if actl == "1":
                    x += e
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif actl == "2":
                    x += d
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                else:
                    print("Elegiste una opción no válida.")
            elif acg == "5":
                actj = input("Opciones de jeans: Clásico: $", y, ", Slim: $", o, ": ")
                if actj == "1":
                    x += y
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                elif actj == "2":
                    x += o
                    print("Bien, ahora tu cuenta es de $", x)
                    break
                else:
                    print("Elegiste una opción no válida.")
            elif acg == "6":
                print("Opciones para niños: (A definir precios y opciones)")
                break
            else:
                print("Elegiste una opción no válida.")
    elif ac == "3":
        while True:
            ach = input("Tenemos las siguientes opciones en vestidos: Con short: $", a, "(1), Vestido casual: $", s, "(2), Vestido de fiesta: $", o, "(3), Vestido de cóctel: $", p, "(4), Para niños: $", d, "(5): ")
            if ach == "1":
                x += a
                print("Bien, ahora tu cuenta es de $", x)
                break
            elif ach == "2":
                x += s
                print("Bien, ahora tu cuenta es de $", x)
                break
            elif ach == "3":
                x += o
                print("Bien, ahora tu cuenta es de $", x)
                break
            elif ach == "4":
                x += p
                print("Bien, ahora tu cuenta es de $", x)
                break
            elif ach == "5":
                x += d
                print("Bien, ahora tu cuenta es de $", x)
                break
            else:
                print("Elegiste una opción no válida.")
    elif ac == "4":
        while True:
            acti = input("Esto es lo que tenemos de ropa deportiva: Sudadera deportiva con capucha: $", o, "(1), Pantalones deportivos ajustados: $", p, "(2), Leggings deportivos de compresión: $", a, "(3), Camiseta deportiva de secado rápido: $", d, "(4): ")
            if acti == "1":
                x += o
                print("Bien, ahora tu cuenta es de $", x)
                break
            elif acti == "2":
                x += p
                print("Bien, ahora tu cuenta es de $", x)
                break
            elif acti == "3":
                x += a
                print("Bien, ahora tu cuenta es de $", x)
                break
            elif acti == "4":
                x += d
                print("Bien, ahora tu cuenta es de $", x)
                break
            else:
                print("Elegiste una opción no válida.")
    break
