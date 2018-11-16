class Animal:
    type = "Animal"

    def __init__(self, age):
        self._age = age

    @classmethod
    def get_class_name(cls):
        print("class name is " + cls.__name__)
    # ba @classmethod mishe in tabe ha nro overwrite kard

    @property
    def get_name(self):
        return "my name is %s and my age is %d" % (self.type, self._age)
    # property baes mishe tabe faqat returnesh kar kone va baghie dastresi behesh be soorate kamel nadashte bashan va
    #  be onvane tabe ba () nmiad


class Cat(Animal):
    type = "Cat"

    def __init__(self, age):
        super(Cat, self).__init__(age)


Cat.type = "DOG!!"
dog = Animal(10)
cat = Cat(15)

print(dog.get_class_name())
print(dog.get_name)
print(cat.get_name)
print(type(dog))
print(cat.__class__)
print("\n")
