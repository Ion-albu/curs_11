"""
Task: Sistem de Management al unei Biblioteci

Timp alocat: 15-20 minute

Creați următoarele clase pentru a gestiona o bibliotecă:

1. Clasa Book:
   - Atribute: title, author, year, isbn
   - Metodele __str__ și __repr__
   - O staticmethod care validează ISBN-ul (trebuie să aibă 13 cifre)
   """
class Book:
   def __init__(self, title, author,year, isbn):
      self.title = title
      self.author = author
      self.year = year
      self.isbn = isbn
      
   def __str__(self):
       return f" Cartea : {self.title}, autorul: {self.author}, scrisa in anu; {self.year}"
   def __repr__(self):
      return f"Book=(title= '{self.title}, autor='{self.author}, isbn='{self.isbn})"
   
   @staticmethod
   def validate_isbn(isbn):
        nr = int("1" + "0"*12)
        return isbn > nr

      
      


"""
2. Clasa Library:
   - Moștenește o clasă de bază Building (cu atribute: address, floors)
   - Atribute adiționale: books (listă), staff (listă)
   - Metode pentru:
     * adăugare carte
     * căutare carte după ISBN
     * afișare toate cărțile unui autor
"""
class Building:
   def __init__(self,adress, floors):
      self.adress = adress
      self.floors = floors

class Library(Building):
   def __init__(self, adress, floors, books=None, staff=None):
      super().__init__(adress, floors)
      self.books = books if books is not None else []
      self.staff = staff if staff is not None else []

   def adauga_carte(self, carte):
        # Validarea carte, isinstance(carte, Book)
        if isinstance(carte, Book):
            # Validare dupa isbn
            if Book.validate_isbn(carte.isbn):
                for carte_in_library in self.books:
                    if carte.isbn == carte_in_library.isbn:
                        return "Acest isbn deja exista in librarie!"
                self.books.append(carte)
                print(f"Cartea {carte.title} a fost adaugata cu succes!")

   def cauta_carte_dupa_isbn(self, isbn):
        # Iteram prin carti
        for carte in self.books:
        # carte.isbn == isbn
            if carte.isbn == isbn:
                return carte.__str__()
        # un mesaj cartea nu a fost gasita
        return f"Cartea cu sibn: {isbn} nu a fost gasita"
   
   def afisare_carti_a_unui_autor(self, autor):
        # o lista cu carti
        lista_de_carti = []
        # iteram prin carti
        for carte in self.books:
        # verificam daca carte.autor == autor --> facem .append(carte)
            if carte.author == autor:
                lista_de_carti.append(carte)
        return lista_de_carti
   
carte = Book("Luceafarul", "Mihai Eminescu", 1850, 1200000000000000)
librarie = Library("Stefan cel Mare", 4)
librarie.adauga_carte(carte)
print(librarie.cauta_carte_dupa_isbn(carte.isbn))
print(librarie.afisare_carti_a_unui_autor("Mihai Eminescu"))

"""

#Bonus:
- Implementați o metodă de sortare a cărților după anul publicării
- Adăugați management al erorilor pentru ISBN invalid

#Test data:
"""
book1 = Book("Amintiri din copilărie", "Ion Creangă", 1892, "1234567890123")
book2 = Book("Luceafărul", "Mihai Eminescu", 1883, "9876543210123")

