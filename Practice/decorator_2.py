def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner


@str_upper
def greeting():
    return "Hello, how are you?"


# new_string = str_upper(greeting) is equivalent to @str_upper
# print(new_string())
# print(str_upper(greeting)())

print(greeting())





