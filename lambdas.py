d1 = {"red": 1, "blue": 2}
d2 = {"green": 3, "blue": 17, "orange": 4}

d3=[("green", 3),( "blue", 17),( "orange", 4)]
d4=[1, 5, 4, 6, 8, 11, 3, 12]
l2=list(d2)
print("test1")
# map(lambda x: print("test"), d4)
# map(lambda x: print( "("+x[0]+":"+x[1]+ ")"), d3)
pass

xx=[1,2,3,4,5,-6,7,-8]
# xxx = xx.reshape(2,2,2)
yy=list(filter(lambda x: x if x%2==0 else None,xx))
y=list(filter(lambda x: (x%2==0), xx))
zz= list(map(lambda x:0 if x<0 else x))
print (y)
pass