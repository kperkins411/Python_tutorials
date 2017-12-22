def sort_priority(values,group):
    found = False
    def helper(x):
        if x in group:
            nonlocal found
            found = True
            return (0,x)
        return (1,x)
    values.sort(key = helper)

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7,7}
group1 = {2:1,3:1,5:1,7:1,8:1}
print(type(group))
print(type(group1))

sort_priority(numbers,group)
print (numbers)

numbers = [8,3,1,2,5,4,7,6]
class Sorter(object):
    def __init__(self,group):
        self.group=group
        self.Found = False

    def __call__(self,x):
        if x in self.group:
            self.Found = True
            return(0,x)
        return (1,x)
sorter = Sorter(group)
numbers.sort(key=sorter)

print(numbers)
assert sorter.Found is True

