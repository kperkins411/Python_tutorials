from time import time
def factorize(number):
    for i in range(1,number+1):
        if number % i == 0:
            yield i

numbers = [2139079, 1214759,1516637,1852285]

start =time()
j=None
for number in numbers:
    list(factorize(number))
end = time()
print("Took %.3f seconds"%(end-start))

########################################

from threading import Thread

class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))

start =time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
end = time()
print("Took %.3f seconds"%(end-start))