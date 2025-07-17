"""
### 🧪 **Exercițiu de evaluare: Relația dintre Mașină, Motor și Șofer**

#### Cerință:

Creează următoarele clase:

1. **Clasa `Motor`**

   * Atribut **privat**: `putere` (în cai putere)
   * Metodă **publică**: `descrie_motor()` → returnează un string cu puterea motorului
   """
class Motor:
   def __init__(self, putere):
      self.__putere = putere

   def descrie_motor(self):
      return f"puterea motorului este: {self.__putere}"
"""
2. **Clasa `Sofer`**

   * Atribut **public**: `nume`
   * Metodă **privată**: `__verifica_permis()` → returnează `True`
   * Metodă **publică**: `poate_conduce()` → folosește metoda `__verifica_permis()`
"""
class Sofer:
   def __init__(self, nume):
      self.nume = nume

   def __verifica_permis(self):
      return True
   def poate_conduce(self):
      return self.__verifica_permis()

"""
3. **Clasa `Masina`**

   * **Agregare**: primește un obiect de tip `Sofer` ca parametru în constructor
   * **Compoziție**: creează în constructor un obiect de tip `Motor`
   * Atribut **privat**: `__marca`
   * Metodă **publică**: `porneste()` → verifică dacă șoferul poate conduce și afișează un mesaj cu marca și puterea motorului

   """
class Masina:
   def __init__(self,marca,putere_motor,sofer):
      self.__marca = marca
      self.motor = Motor(putere_motor)
      self.sofer = sofer

   def porneste(self):
      if self.sofer.poate_conduce():
            print(f"Mașina {self.__marca} a pornit cu {self.motor.descrie_motor()}.")
      else:
            print(f"{self.sofer.nume} nu poate conduce mașina {self.__marca}.")


#### Exemplu de utilizare:


sofer = Sofer("Maria")
masina = Masina("Dacia", sofer)
masina.porneste()

### ✅ Ce trebuie să conțină testul:
"""
* Folosirea **atributelor private** (`__marca`, `__verifica_permis`)
* Utilizarea **metodelor publice/private**
* Demonstrarea **compoziției** (`Masina` creează `Motor`)
* Demonstrarea **agregării** (`Masina` primește un `Sofer`)
* Verificare logică simplă în metoda `porneste()`
"""
