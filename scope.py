def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()


a_var = 1

def a_func():
    global  a_var
    a_var = a_var + 1
    print(a_var, '[ a_var inside a_func() ]')

print(a_var, '[ a_var outside a_func() ]')
a_func()

i = 1

def foo():
    i = 5
    print(i, 'in foo()')
    for j in range(2):
        i=i+j
        print(i, 'in foo() loop')
    print(i, 'in foo() after loop')
    def inner():
        i +=1
        print(i, 'in foo() inner()')


print(i, 'global')

foo()
print(i, 'global')