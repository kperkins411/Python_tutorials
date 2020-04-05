# tuples are much like C++ structs
bob = ('Bob', 30, 'male')
print ('Representation:', bob)

jane = ('Jane', 29, 'female')
print ('\nField by index:', jane[0])

print ('\nFields by index:')
for p in [ bob, jane ]:
    print ('%s is a %d year old %s' % p)

# named tuples give fields names, 1st string is name of tuple, next string is fields, a list of parameters
import collections
Person = collections.namedtuple('Person', 'name age gender')

print ('Type of Person:', type(Person))

bob = Person(name='Bob', age=30, gender='male')
print ('\nRepresentation:', bob.name)

jane = Person(name='Jane', age=29, gender='female')
print ('\nField by name:', jane.name)

print ('\nFields by index:')
for p in [ bob, jane ]:
    print ('%s is a %d year old %s' % p)

# you can access the fields of the name tuple via dtted syntax (tup.name
# or by index)

try:
    collections.namedtuple('Person', 'name class age gender')   #class is reserved
except ValueError as err:
    print (err)

try:
    collections.namedtuple('Person', 'name age gender age') # age is repeated
except ValueError as err:
    print (err)

print (Person._fields)