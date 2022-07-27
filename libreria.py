# Clase Library y sus metodos --- Comienzo

class Library:

    def __init__(self, bookslist, name): # Aquí, el nombre de la libreria
        self.bookslist = bookslist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'Hemos encontrado los libros en nuestra libreria: {self.name} \n')
        for book in self.bookslist:
            print(book)

    def addBook(self, book):
        if book in bookslist:
            print('El libro ya existe')
        else:
            self.bookslist.append(book)
            bookDatabase = open(databaseName, 'a')
            bookDatabase.write('\n')
            bookDatabase.write(book)
            print('Libro añadido')

    def lendBook(self, book, user):
        if book in bookslist:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print('El libro ha sido prestado. Base de datos actualizada.')
            else:
                print(f'El libro esta siendo usado por {self.lendDict[book]}')
        else:
            print('¡Disculpas! No tenemos ese libro en nuestra libreria')

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('El libro se devolvio exitosamente!')
        else:
            print('El libro no existe en la base de datos de libros prestados')

# Clase Library y sus metodos --- Fin


# Función Main - Aceptando los input de los usuarios --- Comienzo

def main():
    while(True):
        print(f'Bienvenido a la libreria {library.name}. Las siguientes son sus opciones,')
        choice = '''
        1. Mostar libros
        2. Prestar libro
        3. Agregar libro
        4. Devolver un libro
        '''
        print(choice)

        userInput = input('Presiona Q para salir y C para continuar: ')
        if userInput == 'C':
            userChoice = int(input('Seleccione una opción para continuar: '))
            if userChoice == 1:
                library.displayBooks()
            
            elif userChoice == 2:
                book = input('Ingrese el nombre del libro que desea prestar: ')
                user = input('Ingrese el nombre del usuario: ')
                library.lendBook(book, user)
            
            elif userChoice == 3:
                book = input('Ingrese el nombre del libro que desea agregar: ')
                library.addBook(book)

            elif userChoice == 4:
                book = input('Ingrese el nombre del libro que desea devolver: ')
                library.returnBook(book)

            else:
                print('Por favor ingrese una opción válida!')
        
        elif userInput == 'Q':
            break

        else:
            print('Por favor ingrese una opción válida!')

# Función Main - Aceptando los input de los usuarios --- Final

# La ejecución del programa comienza aquí usando la condición __name__

if __name__ == '__main__':
    bookslist = []
    databaseName = input('Ingrese el archivo de la base de datos con su extensión: ')
    bookDatabase = open(databaseName, 'r')
    for book in bookDatabase:
        bookslist.append(book)
    library = Library(bookslist, 'PythonX')
    main() 
    # Salta a la función Main para aceptar los input de los usuarios
