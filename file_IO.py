fn = "test.txt"
fn2="test1.txt"

with open(fn,'wt') as f:
    i=5
    while (i>0):
        f.write("line"+ str(i))
        i += -1

try:
    with open(fn2, 'rt') as f:
        for line in f:
            print(line)
except FileNotFoundError as e:
    print (e)
    import sys
    # raise type(e)(str(e) + ' happens at %s' % fn2).with_traceback(sys.exc_info()[2])
