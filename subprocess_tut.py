'''
Implements Item 36 in Effective Python
'''
import os
import functools
import subprocess
import  time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def fun_KP():
   # redirect output to file
    out = open("tmp.txt", "w")

    # cmds = "cd ~/eclipse-workspace/Proj3_Library_Vector_SOLUTION ./Debug/Proj3_Library_Vector_SOLUTION;pwd"
    cmds = "cd ~/eclipse-workspace/util_outstring;./Debug/util_outstring"
    process = subprocess.Popen(cmds, shell=True, stdout=out, stderr=out)
    process.wait()


@timer
def fun_EP1():
    proc = subprocess.Popen(['echo','hello from child'],stdout=subprocess.PIPE)
    out,err = proc.communicate()
    print(out.decode('utf-8'))

@timer
def fun_EP2():
    proc = subprocess.Popen(['sleep','0.3'])
    while (proc.poll() is None):
        print("working")
    print("Done!")

def fun_EP2_launchAndWaitForManyProcesses():
    def run_sleep(period):
        proc = subprocess.Popen(['sleep', str(period)])
        return proc

    start = time.time()
    procs = []
    for _ in range(10):
        procs.append(run_sleep(0.3))

    for proc in procs:
        proc.communicate()
    end=time.time()

    print("finished fun_EP2_launchAndWaitForManyProcesses, launched %d in %.3f seconds"%(10,(end-start)))

def run_openssl(data):
    env = os.environ.copy()
    env['password']=b'\xe24U\n\xd0Q136\x11'
    proc = subprocess.Popen(['openssl','enc', '-des3','-pass','env:password'],
                            env=env,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

def run_md5(std_in):
    proc=subprocess.Popen([])
def doSign():
    procs = []
    for _ in range(3):
        data=os.urandom(10)
        proc = run_openssl(data)
        procs.append(proc)

    for proc in procs:
        out,err = proc.communicate()
        print(out[-10:])


if (__name__=="__main__"):

    # fun_KP()
    # fun_EP1()
    # fun_EP2()
    # fun_EP2_launchAndWaitForManyProcesses()
    doSign()
