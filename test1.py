import requests
def elegirProductosPares():
    response = requests.get("https://fakestoreapi.com/products")
    productos = response.json()
    for producto in productos:
        if producto["id"] % 2 == 0:
            print(f"ID: {producto['id']}, Title: {producto['title']}, Price: ${producto['price']}")

def altaUsuarioNuevo():
    email = input("Ingrese su correo electronico: ")
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese un password: ")
    firstname = input ("Ingrese su nombre sin apellido")
    lastname = input ("Ingrese su apellido")

    
    payload = {
        "email": email,
        "username": username,
        "password": password

    }
    
    response = requests.post("https://fakestoreapi.com/users", json=payload)
    user_data = response.json()
    
    print("Respuesta del servidor:", user_data)

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



#elegirProductosPares()
altaUsuarioNuevo()
#imprimeCarrito()

