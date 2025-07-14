productos ={'8475HD':['HP',15.6,'8GB','DD','1T','Intel Core i5','NvidiaGTX1050'],
            '275HD':['Lenovo',14.4,'4GB','SDD','512GB','Intel Core i5','NvidiaGTX1050'],
            'JjFHD':['Asus',14,'16GB','SDD','256GB','Intel Core i7','NvidiaRTX2080Ti'],
            'fgdxFHD':['HP',15.6,'8GB','DD','1T','Intel Core i3','Integrada'],
            'GF75HD':['Asus',15.6,'8GB','DD','1T','Intel Core i7','NvidiaGTX1050'],
            '123FHD':['Lenovo',14.6,'6GB','DD','1T','AMD Ryzen 5','Integrada'],
            '342FHD':['Lenovo',15.6,'8GB','DD','1T','AMD Ryzen 7','NvidiaGTX1050'],
            'UWU131HD':['Dell',15.6,'8GB','DD','1T','AMD Ryzen 3','NvidiaGTX1050']

}
stock = {'8475HD':[387990,10],'275HD':[327990,4],'JjFHD':[424990,1],
         'fgdxFHD':[664990,21],'123FHD':[290890,32],'342FHD':[444990,7],
         'GF75HD':[749990,2],'UWU131HD':[349990,1],'FS1230HD':[249990,0]
}

def buscar_stock_por_codigo(codigo_producto:str):
    for i in stock:
        if i.lower() == codigo_producto.lower():
            return  stock[i][1]

def disminuir_stock(codigo_producto:str,cantidad:int):
    stock_disponible = buscar_stock_por_codigo(codigo_producto)

    if stock_disponible >= cantidad:
       stock[codigo_producto.upper()[1]]-= cantidad
       return True
    else:
       return False

def Actualizar_precio(nombre_producto:str,P:int):
    producto_encontrado = buscar_computador_por_nombre (nombre_producto)
    if producto_encontrado != None:
        print(producto_encontrado)
        for i in stock:
            if i.upper() == producto_encontrado[0].upper():
                stock[i][0]=P
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")

def busqueda_precio(P_minimo:int,P_maximo:int):
    for i in productos:
        if productos[i][0]>= P_minimo and productos[i][5]<= P_maximo:
            print(productos[1])

def validar_texto(mensaje_input):
    while True:
        texto = input(mensaje_input)
        if len(texto.strip())==0:
            continue
        else:
            return texto
def validar_numero_entero_positivo(msg_input:str):
    while True:
        try:
            numero= int(input(msg_input))
            if numero <= 0:
                print("no puedo ingresar valores negativos o directamente 0")
                continue
            else: return numero

        except ValueError:
            print("solo se puede ingresar numeros enteros")
            continue


def buscar_computador_por_nombre(nombre_producto:str):
   for i in productos:
       if productos[i][0].lower() == nombre_producto.lower():
         print("Encontrado")
         producto_encontrado= productos[i]       
         producto_encontrado.insert(0,i)
         return producto_encontrado

def stock_marca():
    for i in productos:
        print(f"NOMBRE:{productos[i][0]} || Modelo:{productos[i][1]}")


def menu():
    while True:
        print("***MENU PRINCIPAL***")
        print("1.Stock marca")
        print("2.busqueda por precio")
        print("3.Actualizar precio")
        print("4.Salir")
        try:
            opcion = int(input("ingrese una opcion: "))
            print("")
        except ValueError:
            print("Debe Seleccionar una opcion Valida!!")
     
        if opcion == "1":
            stock_marca()
        elif opcion == "2":
            P_minimo = validar_numero_entero_positivo ("ingrese el precio minimo")
            P_maximo = validar_numero_entero_positivo ("ingrese el precio maximo")
            busqueda_precio(P_minimo,P_maximo)
        elif opcion == "3":
            nombre_producto = validar_texto("ingrese el nombre del Producto: ")
            nuevo_precio = validar_numero_entero_positivo("ingrese nuevo precio: ")
            Actualizar_precio(nombre_producto,nuevo_precio)
        elif opcion == "4":
            break
        else:
            print("opcion no valida!!!")


menu()
