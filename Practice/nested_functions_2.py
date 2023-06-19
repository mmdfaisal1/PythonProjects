def outer():
    x = 3

    def inner():
        return x + 3
    return inner()


a = outer()
print(a)
