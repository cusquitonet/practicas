def enterProducts(): # Funcion 1
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Presiona A para añadir un producto y Q para salir: ')
        if details == 'a':
            product = input('Ingrese el producto: ')
            quantity = int(input('Ingrese la cantidad: '))
            buyingData.update({product: quantity})
        elif details == 'q':
            enterDetails = False
        else:
            print('Por favor elige la opción correcta')
    return buyingData


def getPrice(product, quantity): # Funcion 2
    priceData = {
        'Biscocho': 3,
        'Pollo': 5,
        'Huevos': 1,
        'Pescado': 3,
        'Torta': 2,
        'Peras': 2,
        'Manzanas': 3,
        'Cebollas': 3
    }
    subtotal = priceData[product] * quantity
    print(product + ': $' + str(priceData[product]) + ' x ' + str(quantity) + ' unidades = $' + str(subtotal))
    return subtotal

def getDiscount(billAmount, membership): # Funcion 3
    discount = 0
    if billAmount >= 25:
        if membership == 'Gold':
            billAmount = billAmount * 0.80
            discount = 20
        elif membership == 'Silver':
            billAmount = billAmount * 0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) + ' % descuento por ' + membership + ' '+ 'membresia en total a pagar: $' + str(billAmount))
    else:
        print('No hay descuento en un monto menor a $25')
    return billAmount


def makeBill(buyingData, membership): # Funcion 4
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print('El monto a pagar es $ ' + str(billAmount))


buyingData = enterProducts() # Llama a la funcion 1
membership = input('Ingrese su membresia: ')
makeBill(buyingData, membership) # Llama a la funcion 4
