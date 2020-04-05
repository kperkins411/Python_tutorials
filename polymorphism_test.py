import os
class base(object):
    def read(self,config):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

class Derived(base):
    def __init__(self,path):
        self.path = path

    def read(self,config):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        print("Derived")
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir,name))
class Derived2(base):
    def __init__(self,path):
        self.path = path

    def read(self,config):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        print("Derived2")
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir,name))




from tempfile import TemporaryDirectory
def write_test_files(tmpdir):
    for i in range(100):
        with open(os.path.join(tmpdir,str(i)),"w") as file:
            file.write("tmp1\ntmp2\n")
            file.write("tmp1\ntmp2\n")

def getList(input_class, config):
    lst=[]
    for input_data in input_class.generate_inputs(config):
        lst.append(input_data)
    return lst


if __name__=='__main__':
    with TemporaryDirectory() as tmpdir:
        write_test_files(tmpdir)
        config = {'data_dir': tmpdir}
        lst = getList(Derived2, config)

