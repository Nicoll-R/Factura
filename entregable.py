import os
import time
os.system("cls")
import sys
class pedido_prueba:
    valor = []    
    precio = []
    nombre = ""
    direccion = ""
    fecha = ""
    def menucompleto():
        print("""
====================================              
|       PRODUCTOS EN VENTA         |
====================================
| A |Casco                 |S/14.50|
| B |Protector auricular   |S/10.50|
| C |Macarillas            |S/09.50|
| D |Cinturón de seguridad |S/15.50|
====================================
              """)

    def menu_opciones(self, opcion, cantidad):
        if opcion.lower() == "a":
            preci = 14.5
            pedido_prueba.precio.append(14.5)
            prod = ("| A |Casco                  |S/14.50|")    
        elif opcion.lower() == "b":
            preci = 10.5
            pedido_prueba.precio.append(10.5)
            prod = ("| B |Protector auricular    |S/10.50|")            
        elif opcion.lower() == "c":
            preci = 9.5
            pedido_prueba.precio.append(9.5)
            prod = ("| C |Macarillas             |S/09.50|")       
        elif opcion.lower() == "d":
            preci = 15.5
            pedido_prueba.precio.append(15.5)
            prod = ("| D |Cinturón de seguridad  |S/15.50|")       
        else:
            pedido_prueba.precio.append(0)
            preci = 0
            print("Opcion no valida")
        if (cantidad>10):
            os.system("cls")
            print("Cantidad máxima de productos: 10")
            pedido_prueba.valor.clear()
            pedido_prueba.precio.clear()
            os.system("Pause")
            os.system("cls")
        else: 
            for _ in range(cantidad):
                pedido_prueba.valor.append(prod)
                pedido_prueba.precio.append(preci)
                
            print(prod)
            os.system("Pause")
            os.system("cls")
        elem = len(pedido_prueba.valor)
        if elem > 10:
            os.system("Pause")
            os.system("cls")
            print("Hola, {0}.\nHas alcanzado la cantidad máxima de elementos".format(pedido_prueba.nombre))
            num = 0
            for elemento in pedido_prueba.valor:
                num += 1
                print("{0}.{1}".format(num, elemento))
            print("Se iniciará una nueva orden")
            pedido_prueba.valor.clear()  
            pedido_prueba.precio.clear()
   
 
    def agregar(self, accion):
        if (accion == "1"):
            pedido_prueba.menucompleto()
        elif (accion =="2"):
            pedido_prueba.valor.clear()
            pedido_prueba.menucompleto()
        elif (accion =="3"):
            print("Finalizando el programa...")
            sys.exit() 
        else: 
            print("Ingrese opción valida")


print("""
====================================
|           BIENVENIDO A           |
|           PERU DELIVERY          |
====================================
""")


pedido_prueba.nombre = input("|        INGRESE NOMBRE             |\n")
pedido_prueba.direccion = input("|        INGRESE DIRECCION         |\n")
pedido_prueba.fecha = input("|        INGRESE FECHA             |\n")
obj = pedido_prueba()
os.system("Pause")
os.system("cls")


print("""
====================================           
|       MENU PRINCIPAL             |      
====================================           
| 1 |MENU DE SELECCION             |
| 2 |NUEVA ORDEN                   |
| 3 |SALIR                         |
====================================
""")
opc= input("Ingrese Acción: ")
if (opc == "3"):
    sys.exit() 
 #obj.agregar(opc)

while True:
    print("""
====================================           
|      MENU DE SELECCION           |            
====================================          
| 1 |AGREGAR PRODUCTOS             |
| 2 |VER PRODUCTOS AGREGADOS       |
| 3 |SOLICITAR FACTURA             |
| 4 |REGRESAR AL MENU ANTERIOR     |
====================================
    """)
    op = input("Siguiente accion: ")

    if op == "1":
        pedido_prueba.menucompleto()
        opcion = input("Ingrese la opcion: ")
        cantidad = int(input("Ingrese cantidad a elegir: "))
        obj.menu_opciones(opcion, cantidad)
        
    elif (op == "2"):
        print("Hola, {0}.\nLos productos en lista son:".format(pedido_prueba.nombre))
        num = 0
        for elemento in pedido_prueba.valor:
            num += 1
            print("{0}.{1}".format(num, elemento))
        os.system("Pause")
        os.system("cls")
    elif (op == "3"):
        for i in range(1):
            total = sum(pedido_prueba.precio)
            IGV = round(total * 0.18, 2)
            pagofinal = round(total * 0.18 + total , 2)
            print("""
============================================  
|     BOLETA DE VENTAS                     |
============================================  
|  DIRECCION:  {0}                         
|  NOMBRE:     {1}                         
|  FECHA:      {2}                         """.format(pedido_prueba.direccion, pedido_prueba.nombre, pedido_prueba.fecha))
            num = 0
            for elemento in pedido_prueba.valor:
                num += 1
                print("|{0}.{1}".format(num, elemento))
            print("""| Subtotal : """, total, """           |         
| Igv :""", IGV, """|                
| Total a pagar:""", pagofinal, """    |      
| Gracias por tu compra, {0}               
========================================     """.format(pedido_prueba.nombre))
            pedido_prueba.valor.clear()  
            pedido_prueba.precio.clear()
            os.system("Pause")
            os.system("cls")
    elif (op =="4"):
        print("""
====================================                     
| 1 |MENU DE SELECCION             |
| 2 |NUEVA ORDEN                   |
| 3 |SALIR                         |
====================================
        """) 
        selec= input("Ingrese Acción: ")
        obj.agregar(selec)
        os.system("Pause")
        os.system("cls")
    else:
        print("Ingrese opcion valida")
    
    
    
   
    
    

    







