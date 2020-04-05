import IPython
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)

x = 5

def outer():
    global x
    x = "local"

    def inner():
        global x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
print("global x:", x)

def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x)


def foo():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


foo()
print("x in main : ", x)

# print system information (but not packages)
print(IPython.sys_info())


import subprocess
from subprocess import Popen, PIPE


with open("frozen-requirements.txt","wb") as out, open("stderr.txt","wb") as err:
    # subprocess.run("pip freeze",stdout=out,stderr=err)
    subprocess.call(["pip", "freeze"], stdout=out)
# # get module information
# from subprocess import call
# call(["pip", "freeze", " >"," frozen-requirements.txt"])

# !pip freeze > frozen-requirements.txt

# append system information to file
with open("frozen-requirements.txt", "a") as file:
    file.write(IPython.sys_info())


def func():
    global g
    g=3


func()

c=g
