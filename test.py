
class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # representation en string de l'objet
    def __str__(self): 
        return f"{self.name} {self.age}"
    
p1 = Person("Dominique", 29)

print(p1)