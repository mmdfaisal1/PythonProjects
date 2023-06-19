def div_decorator(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


@div_decorator
def div(a, b):
    print(a / b)

# div = div_decorator(div)
# div(2, 4)


div(1, 4)

