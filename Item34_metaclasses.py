import json

a=[1,2,'fish']
c=''
for v in a:
    c=str(v)


# b=','.join(a)
z=''.join([str(ele) for ele in a])
# z=list(map(str,a))

class Serializable(object):
    def __init__(self,*args):
        self.args=args
    def serialize(self):
        return json.dumps({'args':self.args})

class Point2D(Serializable):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.x=x
        self.y=y
    def __repr__(self):
        return 'Point2D(%d,%d)'%(self.x,self.y)

class DeSerializeable(Serializable):
    @classmethod
    def deserialize(cls,json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

class BetterPoint2D(DeSerializeable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D(%d,%d)' % (self.x, self.y)

point = BetterPoint2D(5,3)
print('Before   ',point)
data = point.serialize()
print('Serialized ',data)
after=point.deserialize(data)
print('AFter   ',after)
print(point.__module__)


class BetterSerializable(object):
    def __init__(self,*args):
        self.args=args

    def serialize(self):
        return json.dumps({'class':self.__class__.__name__,
                            'args':self.args})

    def __repr__(self):
        return self.serialize()

a = BetterSerializable()
a = BetterSerializable(1)
a = BetterSerializable(1,2)
a = BetterSerializable(1,2,'fish')

# BetterSerializable:*args=1,2,fish
out = a.serialize()

registry = {}
def register_class(target_class):
    registry[target_class.__name__]=target_class

def deserialize(data):
    params = json.loads(data)
    name=params['class']
    target_class=registry[name]
    return target_class(*params['args'])

class EvenBetterPoint2D(BetterSerializable):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.x=x
        self.y=y


register_class(EvenBetterPoint2D)

point = EvenBetterPoint2D(5,3)
print('Before',point)
data=point.serialize()
print('Serialized',data)
after = deserialize(data)
print('after ',after)
pass








# point = Point2D(5,3)
# print('Object:    ',point)
# print('Serialized:', point.serialize())