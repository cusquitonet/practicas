class Library:

    def __init__(self, bookslist, name):
        self.bookslist = bookslist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'Estamos buscando los libros en nuestra libreria:{self.name}')
        for book in self.bookslist:
            print(book)

    def addBook(self, book):
        if book in bookslist:
            print('El libro ya existe')
        else:
            self.bookslist.append(book)
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
            print('El libro no existe en la la base de datos de ibros prestados')


