# see https://discuss.pytorch.org/t/in-what-condition-the-dataloader-would-raise-stopiteration/17483/2
class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
# c = Counter(5,10)
# for i in c:
#     print(i, end=' ')

class cycler(object):
    def __init__(self, iterable, num_epochs):
        self.iterable = iterable
        self.iter1 = None
        # self.iter1= iter(self.iterable)
        self.num_epochs = num_epochs

    def __iter__(self):
        return self

    def __next__(self):
        while(True):
            if (self.iter1 == None):
                print(f"starting epoch #" + str(self.num_epochs))
                self.iter1 = iter(self.iterable)
            try:
                return next(self.iter1)
            except StopIteration as e:
                self.num_epochs -= 1
                if( self.num_epochs == 0):
                    raise StopIteration
                # print(f"starting epoch #" + str(self.num_epochs))
                self.iter1 = None


# def cycle(iterable):
#     while True:
#         print ("Starting anew")
#         for x in iterable:
#             yield x


a=[0,1,2,3,4,5]
# for x in a:
#     print(x)

y=cycler(a,5)
for x in y:
    print(x)


# for x in cycle(a):
#     print(x)

#
# for x in cycle(a):
#     print(x)

