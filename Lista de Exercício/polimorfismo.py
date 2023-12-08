class Cachorro: 
   def fazer_som(self):
        return "Au Au"

class Gato: 
   def fazer_som(self):
        return "Miau!"

animais = [Cachorro(), Gato()] 

for animal in animais: 
  print(animal.fazer_som())