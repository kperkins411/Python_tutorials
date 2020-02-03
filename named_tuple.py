# these things are like sttructs without methods, except  you cannot change their values once created

from collections import namedtuple

Car = namedtuple('car', 'color mileage')
car = Car('red', 1000)
print(f"{car.color}  {car[0]}")

#cant do the following cause immutable
car.color='red'
car.mileage=7777
car.mileage=8888
pass