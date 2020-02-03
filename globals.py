import IPython

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
