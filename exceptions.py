def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('0 divisor') from e
try:
    result = divide(1,0)
except ValueError as e:
    print('ValueError:' + e.args[0])
else:
    print('%.3f' %result)


try:
    result = divide(1,2)
except ValueError as e:
    print('ValueError:' + e.args[0])
else:
    print('Result=%.3f' %result)
