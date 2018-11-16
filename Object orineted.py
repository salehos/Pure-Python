class Animal:
    type = "Animal"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def get_name(self):
        return "my name is %s and my age is %d" % (self._name, self._age)
    #property baes mishe tabe faqat returnesh kar kone va baghie dastresi behesh be soorate kamel nadashte bashan va be onvane tabe ba () nmiad

class Cat(Animal):
    def __init__(self, age):
        super(Cat, self).__init__("cat", age)



dog = Animal("dog", 10)
cat = Cat(15)

print(dog.get_name)
print(cat.get_name)
print(type(dog))
print(cat.__class__)
print("\n")
