class C(object):
    def __init__(self):
        self._name = "nameless"

    @property
    def name(self):
        """I'm the 'name' property."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

c = C()
c.name="toast"
pass