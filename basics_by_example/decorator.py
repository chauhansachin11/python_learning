
def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b = b,a
        return(func(a,b))
    
    return(inner)

# Method No - 1 to use decorator
def div(a,b):
    print(a/b)

div(2,4)
div1 = smart_div(div)
div1(2,4)

# Method No - 2 to use decorator


@smart_div
def div(a,b):
    print(a/b)

div(2,4)
