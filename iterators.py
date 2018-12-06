#!/usr/bin/python3.1
from torch.utils.data import Dataset, DataLoader
import itertools

def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'
for char in my_generator():
    print(char)

class A:
    def __getitem__(self, index):
        if index >= 10:
            raise IndexError
        return index * 111

print(list(A()))

b= list(range(11))
bb = iter(b)
for _ in range(11):
    print(next(bb))


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

q='abcde'
z = Reverse(q)
print(list((iter(z))))

def reverse(a):
    for index in range(len(a)-1,-1,-1):   #start,stop,step
        yield a[index]
for char in reverse('golf'):
    print(char)
print(next(reverse(q)))
print(next(reverse(q)))
print(next(reverse(q)))


def cycle(iterable):
    while True:
        for x in iterable:
            yield x
def nocycle(iterable):
    for x in iterable:
        yield x


q = 'abcde'
# batch_iterator = itertools.cycle(nocycle(q))
batch_iterator = itertools.cycle(q)

for a in batch_iterator:            # handles the stopiteration exception thrown whenever
    print(a)
for a in batch_iterator:  # handles the stopiteration exception thrown whenever
    print(a)


        # class TestDataset(Dataset):
#     def __init__(self, num):
#         self.nums = list(range(num))
#         self.cur = 0
#
#     def __len__(self):
#         return len(self.nums)
#
#     def __getitem__(self, index):
#         return self.nums[self.cur +=1 ]