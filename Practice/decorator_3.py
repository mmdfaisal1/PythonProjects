def check_divide_by_zero(func):
    def inner(x, y):
        if y == 0:
            return "The denominator is zero"
        return func(x, y)
    return inner


@check_divide_by_zero
def div(a, b):
    return a / b


print(div(4, 0))








