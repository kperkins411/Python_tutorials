dogs = ['barkly','polly','the bad dog','chloe']
len_names=[len(name) for name in dogs]

longest_name=None
max_cnt=0

def func():
    global max_cnt
    for name,cnt in zip(dogs,len_names):
        if cnt >max_cnt:
            longest_name = name
            max_cnt = cnt
func()
print ('%s:%d'%(longest_name,max_cnt))

for name, cnt in zip(dogs, len_names):  #notice I dont need global here
    if cnt > max_cnt:
        longest_name = name
        max_cnt = cnt
print ('%s:%d'%(longest_name,max_cnt))

