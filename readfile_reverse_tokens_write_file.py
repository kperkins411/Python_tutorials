out=[]
outfile = open('/home/keith/Desktop/cap2.txt', "w")
with open('/home/keith/Desktop/cap1.txt', "r") as filestream:
    for line in filestream:
        line = line.strip().replace(u'\ufeff', '')  #get rid of weird characters
        cl = line.split(",")                        #create list from line items
        # cl = currentline[::-1]                      #reverse
        outfile.write("%s , %s %s\n" % (cl[1], cl[0],"CS"))
        # outfile.writeln(','.join(cl) + ' CS')     #convert the list to a line
outfile.close()

pass