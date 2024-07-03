import csv

pedidos=[]

def Registrar_pedido():
    print("REGISTRAR UN PEDIDO: ")
    rut=validar_rut()
    nombre=validar_nombre()
    direccion=validar_direccion()
    comuna=validar_comuna()
 
    
    pedido=[rut, nombre, direccion, comuna,]

    pedidos.append(pedido)

    print("RESUMEN DEL PEDIDO:")

    for vicho in pedidos:
        print(f"RUT:{vicho[0]} NOMBRE:{vicho[1]} DIRECCION:{vicho[2]} COMUNA:{vicho[3]}  ")



def listar_pedidos():
    if not pedidos:
        print("DEBE REGISTRAR PEDIDO EN OPCIÓN 1!")
    else:
        for vicho in pedidos:
            print(f"RUT:{vicho[0]} NOMBRE:{vicho[1]} DIRECCION:{vicho[2]} COMUNA:{vicho[3]} ")
        

def Buscar_pedido_rut():
    if not pedidos[0]:
        print("BEDE INGRESAR UN RUT VALIDO! ")
    else:
        pedidos[0]=input("ingrese rut a buscar: ")
        pedidos[0].index()
        if pedidos[0]:
            return pedidos[0]
        else:
            print("rut no encontrado!")

def imprimir_hoja_ruta_csv():
    if not pedidos:
        print("error! debe ingresar datos en opción 1!")
    else:
      print("archivo creado con exito!")
    with open("nombre_archivo.csv","w", newline="")as archivo:
        escritor=csv.writer(archivo) 
        for vicho in pedidos:
            escritor.writerow(pedidos)


def salir_programa():
    print("saliendo...")
    print("hasta luego!")


#validaciones:

def validar_rut():
    while True:
        try:
            ru=int(input("ingrese un rut (sin guión, ni puntos!):  "))
            if len(str(ru))==9:
                return ru
            else:
                print("ingrese un rut valido!")
        except:
            print("error! ingrese solo números!")

def validar_nombre():
    while True:
        nom=input("ingrese su nombre: ")
        if len(nom)>=3 and nom.isalpha():
            return nom
        else:
            print("ERROR INGRESE SOLO LETRAS!")
        
def validar_direccion():
        while True:
            di=input("ingrese su dirección: ")
            if len(di)>=3:
                    return di
            else:
                print("error! la dirección debe tener al menos 3 letras!")

def validar_comuna():
    while True:
        co=input("ingrese comuna:")
        if len(co)>=3:
            return co
        else:
            print("error! debe tener al menos 3 letras!")

        #det_pedido=print("ingrese detalle del pedido: ")
        #print("SELECCIONA SU DETALLE DEL PEDIDO:")
        #print("1. CILINDRO 5KG:  $12500 ")
        #print("2. CILINDRO 15KG: $25000 ")
        #opc2=int("ingrese una opción (1,2): ")

        #if opc2==1:
            #ass
        #elif opc2==2:
            #pass



