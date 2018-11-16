class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return "my name is %s and my age is %d" % (self._name, self._age)

dog = Animal("dog" , 10)
cat = Animal("cat" , 15)
print(dog.get_name())
print(cat.get_name())
