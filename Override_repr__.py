class toy():
    pass

inst= toy()

class inhtoy():
    def __new__(cls,obj):
        def __repr__(self):
            return 'Sucessful'
        import types
        obj.__repr__ = types.MethodType(__repr__,obj)
        return obj

t = inhtoy(inst)

print(t)
print(t.__repr__())
print(repr(t))
print(t.__repr__)

def __repr__(self):
    return "Success"
t.__class__.__repr__=__repr__
print(t)

j = inhtoy(inst)
print(j)
pass