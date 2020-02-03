import os
from threading import Thread

#item 24 in Effective Python
class InputData(object):
    '''base class'''
    def read(self):
        raise NotImplementedError

class InputDataPath(InputData):
    def __init__(self,path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

#-------------------------------------
class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self,other):
        raise NotImplementedError

class WorkerLineCount(Worker):
    #no init?

    def map(self):
        data=self.input_data.read()
        self.result=data.count('\n')

    def reduce(self, other):
        self.result += other.result

#-------------------------------------
def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield InputDataPath(os.path.join(data_dir,name))

def create_workers(input_list):
    workers=[]
    for input_data in input_list:
        workers.append(WorkerLineCount(input_data))
    return workers

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]

    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0],workers[1:]
    for worker in rest:
        first.reduce(worker)

    return first.result

def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

#-------------------------------------
from tempfile import TemporaryDirectory
def write_test_files(tmpdir):
    for i in range(100):
        with open(os.path.join(tmpdir,str(i)),"w") as file:
            file.write("tmp1\ntmp2\n")
            file.write("tmp1\ntmp2\n")

with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    result = mapreduce(tmpdir)

print(f"There are {result} lines in {tmpdir}")