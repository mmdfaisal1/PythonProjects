def check_name(method):
    def inner(self):
        if self.name == "Faisal":
            print("Hey my name is also the same")
        return method(self)
    return inner


class Person:
    def __init__(self, name):
        self.name = name

    @check_name
    def display(self):
        print("Entered user name is:", self.name)


# main
my_person = Person("Faisal")
my_person.display()









