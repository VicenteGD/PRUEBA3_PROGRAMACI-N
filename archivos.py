import os, time, csv
from funciones import *

os.system("cls")

while True:
    os.system("cls")


    print("""MENÚ
    1). Registrar pedido
    2). Listar todos los pedidos
    3). Buscar pedido por rut
    4). Imprimir hoja de ruta
    5). Salir del programa""")
  
    while True:
        try:
            opc = int(input("ingrese una opción disponible: (1,2,3,4):  "))
            if opc in (1,2,3,4,5):
                break
            else: 
                print("ingrese una opción (1,2,3,4)")
        except:
            print("ingrese un NÚMERO ENTERO!")
    if opc==1:
        Registrar_pedido()
    elif opc==2:
        listar_pedidos()
    elif opc==3:
        Buscar_pedido_rut()
    elif opc==4:
        imprimir_hoja_ruta_csv()
    elif opc==5:
        salir_programa()
    else:
        print("error! debe ingresar una opción disponible!")
    time.sleep(3)
