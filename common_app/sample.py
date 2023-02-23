def division_decorator(func):
    def wrapper(x,y):
        if y>x:
            x,y = y,x
        return func(x,y)
    return wrapper

@division_decorator
def division(x,y):
    result = x/y
    return result

div = division(10,2)

print(div)