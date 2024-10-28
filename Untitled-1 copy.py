print ("Bienvenido a nuestra tienda en línea")
nn = input ("Para saber a nombre de quien esta la cuenta inserta tu nombre")
print ("perfecto ", nn, " Te mostraremos nuestro catalogo y tu nos diras que te interesa ver")
x = 0
print ("Tu estado de cuenta actual es de: $" , x)
#Sección de precios
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
    ac = input ("¿Qué buscas? prendas superiores (1) prendas inferiores (2) vestidos (3) ropa deportiva (4)")
    if ac == "1":
        while True:
         act = input ("Tenemos las siguientes opciones: camisetas (1), camisas (2), blusas (3), suéteres (4), chalecos (5), abrigos (6)")
         if act == "1":
            actt = input ("Tenemos las siguientes opciones: Básica de algodón, cuello redondo: $ ", q ," (1), Gráfica con estampado abstracto: $ " , we, " (2), Camiseta de rayas estilo marinero: $ " , e , " (3), Camiseta deportiva de poliéster: $ ", r , " (4)")
         if actt == "1":
              x += q
              print ("Bien ahora tu cuenta es de $ ", x)
              break
         elif actt == "2":
              x += we
              print ("Bien ahora tu cuenta es de $ ", x)
              break
         elif actt == "3":
              x += e
              print ("Bien ahora tu cuenta es de $ ", x)
              break
         elif actt == "3":
              x += r
              print ("Bien ahora tu cuenta es de $ ", x)
              break
         else: 
              print ("Elegiste una opción no valida.")
    break
    if act == "2":
            acty = input ("Tenemos las siguientes opciones:")
            break
    elif act == "3":
            actu = input ("Tenemos las siguientes opciones:")
            break
    elif act == "4":
            acti = input ("Tenemos las siguientes opciones:")
            break
    else:
            print ("Elegiste una opción no valida, intentalo de nuevo")
    if ac == "2":
        acg = input ("Tenemos las siguientes opciones de prendas inferiores: pantalones (1), shorts (2), faldas (3), leggins (4), jeans (5), para niños (6)")
        break
    if ac == "3":
        ach = input ("Tenemos las siguientes opciones en vestidos: con short (1), vestidos casuales (2), vestidos de fiesta (3), vestidos de cóctel (4), para niños (5)")
        break
    if ac == "4":
        acj = input ("Esto es lo que tenemos de ropa deportiva: sudaderas (1), pantalones deportivos (2), leggings deportivos (3), ropa de yoga (4)")
        break
    else:
        print ("Parece que elegiste una opción no válida, vuelve a intentarlo.")
