import os
from threading import Thread

#item 24 in Effective Python
class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls,config):
        raise NotImplementedError

class InputDataPath(GenericInputData):
    def __init__(self,path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls,config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

class InputDataPath2(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

#-------------------------------------
class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self,other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls,input_class,config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers

class GenericWorkerLineCount(GenericWorker):
    #no init?

    def map(self):
        data=self.input_data.read()
        self.result=data.count('\n')

    def reduce(self, other):
        self.result += other.result

#-------------------------------------

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]

    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0],workers[1:]
    for worker in rest:
        first.reduce(worker)

    return first.result

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
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
    config={'data_dir':tmpdir}
    result = mapreduce(GenericWorkerLineCount, InputDataPath2, config)

print(f"There are {result} lines in {tmpdir}")