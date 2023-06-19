class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Hello", self.name)

    @staticmethod
    def display2():
        print("Hello!")


# main
my_person = Person("Faisal")
my_person.display()


# The above is equivalent to
Person("Faisal").display()





