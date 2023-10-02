import requests
def elegirProductosPares():
    response = requests.get("https://fakestoreapi.com/products")
    productos = response.json()
    for producto in productos:
        if producto["id"] % 2 == 0:
            print(f"ID: {producto['id']}, Title: {producto['title']}, Price: ${producto['price']}")

def altaUsuarioNuevo():
#Se piden las variables al usuario
    email = input("Ingrese el email del usuario: ")
    username = input("Ingrese el nombre del usuario: ")
    password = input("Ingrese un password: ")
    first_name = input("Ingrese el nombre de quien crea el usuario: ")
    last_name = input("Ingrese el apellido de quien crea el usuario: ")
    city = input("Ingrese su ciudad: ")
    street = input("Ingrese calle y numero: ")
    number = input("Ingrese el numero de interior: ")
    zipcode = input("Ingrese el codigo postal: ")
    lat = input("Ingrese una latitud: ")
    long = input("Ingrese una longitud: ")
    phone = input("Ingrese un telefono: ")

    #Se construye la estructura de datos del usuario
    payload = {
        "email": email,
        "username": username,
        "password": password,
        "name": {
            "firstname": first_name,
            "lastname": last_name
        },
        "address": {
            "city": city,
            "street": street,
            "number": number,
            "zipcode": zipcode,
            "geolocation": {
                "lat": lat,
                "long": long
            }
        },
        "phone": phone
    }
    response = requests.post("https://fakestoreapi.com/users", json=payload)    
    print("Respuesta del servidor:", response.json())

def imprimeCarrito():
#Imprimir username, email (del cliente), title, price (del producto)
    global UID
    global PID
    response = requests.get("https://fakestoreapi.com/carts")
    carts = response.json()
    #print(carts) #Todos los carritos
    for carrito in carts:
        UID = carrito['userId']
        id = carrito['id']
        print("Carrito con ID: ", id) #Para verificar que si se repite el usuario, sea diferente id de carrito
        consultaNameEmail(UID)
        prodsArray = carrito['products']
        #print(prodsArray)
        for prod in prodsArray:
            PID = prod['productId'] #Product ID de cada producto
            QTY = prod['quantity'] #cantidad de cada producto
            tituloPrecioProducto(PID,QTY)
        print("------------------------------------------\n")

def consultaNameEmail(userID):
    #Para extraer el nombre y el email de un usuario asociado a un carrito
    response = requests.get("https://fakestoreapi.com/users/"+str(userID))
    userObject = response.json() #Objeto respuesta usando el endpoint de un usuario especifico
    nombre = userObject['username']
    email = userObject['email']
    print("Nombre: "+ nombre,"| Email: ",email)

def tituloPrecioProducto(productID,QTY):
    #Para extraer el titulo y precio de un producto asociado a un carrito
    response = requests.get("https://fakestoreapi.com/products/"+str(productID))
    prodObject = response.json() #objeto respuesta usando el endpoint de un producto especifico
    title = prodObject['title']
    price = prodObject['price']
    print("Producto:",title, " | Precio:", price, " | Cantidad: ",QTY)

while True:
    print("\nMenu:")
    print("1. Imprimir productos pares")
    print("2. Dar de alta un usuario nuevo")
    print("3. Imprimir carritos y sus datos")
    print("4. Salir\n")

    opcion = input("Ingrese el número de la opción que desea ejecutar: ")

    if opcion == "1":
        elegirProductosPares()
    elif opcion == "2":
        altaUsuarioNuevo()
    elif opcion == "3":
        imprimeCarrito()
    elif opcion == "4":
        print("Adios ;) ")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida (1-4).")
