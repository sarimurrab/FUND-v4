class Parent():
    def __init__(self, last_name, property):
        self.last_name = last_name
        self.property = property

class Child(Parent):
    def __init__(self, last_name, property, modern_rituals):
        Parent.__init__(self,last_name,property)
        self.modern_rituals = modern_rituals

obj1 = Child("Sinha",20000,"yes")
print(obj1.last_name)