
# what if you wanted to carribianize all responses?
# enter the heymon decorator


def heymon(fun):
    def f(*args, **kwargs):
        res =fun(*args ,**kwargs)
        print(f"hey mon, the answer is {str(res)}")
        return res
    return f



def add(a ,b):
    return a+ b


# without decorator
print(str(add(1, 2)))

# redefine add
add_i = heymon(add)
add_i(2, 3)


# or this
@heymon
def add1(a, b):
    return a + b

add1(3,4)


def add2(a, b):
    return a + b

def multiheymon(n):
    def inner(fun):
        def f(*args, **kwargs):
            for _ in range(n):
                res =fun(*args ,**kwargs)
                print(f"multiheymon, the answer is {str(res)}")
            return res
        return f
    return inner

#redefine 2 level decorator
f=multiheymon(4)(add2)
f(3,4)

res = multiheymon(4)(add2)(4,5)
print (res)TRFYU6H7P0[;-'' \
                        '\]"?:>JMNHGFVaz']

