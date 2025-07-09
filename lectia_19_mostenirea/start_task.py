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
      self.isbn = isbn
    
      
    def __str__(self):
       return f"titlu: {self.title}, autorul: {self.author}, isbn{self.isbn}"
    def __repr__(self):
      return f"Book=(title= '{self.title}, autor='{self.author}, isbn='{self.isbn})"

      
      


"""
2. Clasa Library:
   - Moștenește o clasă de bază Building (cu atribute: address, floors)
   - Atribute adiționale: books (listă), staff (listă)
   - Metode pentru:
     * adăugare carte
     * căutare carte după ISBN
     * afișare toate cărțile unui autor
"""
class Library(Book):
   def 
"""

#Bonus:
- Implementați o metodă de sortare a cărților după anul publicării
- Adăugați management al erorilor pentru ISBN invalid

#Test data:
"""
book1 = Book("Amintiri din copilărie", "Ion Creangă", 1892, "1234567890123")
book2 = Book("Luceafărul", "Mihai Eminescu", 1883, "9876543210123")

