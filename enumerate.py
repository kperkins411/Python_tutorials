
#enumerate a dictionary
people={'keith':54,'lynn':56,'kate':18,'ben':21}
for name,age in people.items():
    print('%s,%d'%(name,age))

#enumerate a list
dogs = ['barkly','polly','the bad dog','chloe']
for i,name in enumerate(dogs,1):    #start counting from 1 not 0
    print('%d,%s'%(i,name))