def sort_priority(values,group):
    def helper(x):  #closure (inner function) refers to values and group
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key = helper)

numbers=[8,7,4,5,6,3,1,1,1,4]
group =[1,3,5]

sort_priority(numbers,group)
print (numbers)


class sorter(object):
    def __init__(self,group):
        self.group = group

    def __call__(self, x):
        if x in self.group:
            return (0,x)
        return (1,x)

numbers=[8,7,4,5,6,3,1,1,1,4]
group =[2,3,7]
s = sorter(group)
numbers.sort(key = s)
print (numbers)
