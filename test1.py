import requests
def elegirProductosPares():
    response = requests.get("https://fakestoreapi.com/products")
    productos = response.json()
    for producto in productos:
        if producto["id"] % 2 == 0:
            print(f"ID: {producto['id']}, Title: {producto['title']}, Price: ${producto['price']}")

def altaUsuarioNuevo():
    name = input("Ingrese el nombre del usuario: ")
    username = input("Ingrese el nombre de usuario: ")
    email = input("Ingrese el correo electrónico del usuario: ")
    
    payload = {
        "name": name,
        "username": username,
        "email": email
    }
    
    response = requests.post("https://fakestoreapi.com/users", json=payload)
    user_data = response.json()
    
    print("Respuesta del servidor:", user_data)

def imprimeCarrito():
    global UID
    global PID
    #Imprimir username, email (del cliente), title, price (del producto)
    response = requests.get("https://fakestoreapi.com/carts")
    carts = response.json()
    print(carts) #Todos los carritos
    for carrito in carts:
        UID = carrito['userId']
        print("checando el UserName e Email del UID: ...", UID)
        consultaNameEmail(UID)
        prodsArray = carrito['products']
        print(prodsArray)
        for prod in prodsArray:
            PID = prod['productId'] #Product ID de cada producto
            QTY = prod['quantity'] #cantidad de cada producto
            tituloPrecioProducto(PID,QTY)
        print("------------------------------------------\n")


def consultaNameEmail(userID):
    response = requests.get("https://fakestoreapi.com/users/"+str(userID))
    userObject = response.json()
    nombre = userObject['username']
    email = userObject['email']
    print("Nombre: "+ nombre,"| Email: ",email)

def tituloPrecioProducto(productID,QTY):
    response = requests.get("https://fakestoreapi.com/products/"+str(productID))
    prodObject = response.json()
    title = prodObject['title']
    price = prodObject['price']
    print("Producto:",title, " | Precio:", price, " | Cantidad: ",QTY)



#elegirProductosPares()
#altaUsuarioNuevo()
imprimeCarrito()

