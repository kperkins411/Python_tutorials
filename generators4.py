class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

class NoReverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return iter(self.data)


def epoch_iter(*,data,numb_epochs = 5):
    '''
    A function that allows you to iterate through all data in data, numb_epochs times
    :param data: an iterable
    :param numb_epochs: number of times to go through above iterable
    :return:
    '''
    epoch_num = 1
    print(f"starting epoch number {epoch_num}")
    iterable = iter(data)

    while(True):
        try:
            yield next(iterable)
        except StopIteration:
            epoch_num +=1
            if (epoch_num > numb_epochs):
                break
            print(f"starting epoch number {epoch_num}")
            iterable = iter(data)



a="fish"










for q in epoch_iter(data = a):
    print(q)

b = NoReverse(a)
# c= Reverse(a)
# for q in b:
#     print(q)
#
# for q in c:
#     print(q)


# import functools
# def set_epochs(func):
#     "A simple decorator for limiting the number of epochs"
#
#     @functools.wraps(func)
#     def wrapper(*args):
#         iter=next(args[0])
#         yield from func(data = iter)
#
#     return wrapper

# @set_epochs
# def get_data(data =a):
#     for

a="chips"
epochs =5
for k in range(epochs):
    print(f"starting epoch {k}")
    iterator= iter(a)
    while(True):
        try:
            print(str(next(iterator)))
        except StopIteration:
            break

