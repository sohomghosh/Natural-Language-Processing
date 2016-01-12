filename="modify2.txt"
filename1="modifyne_line1.txt"
f=open(filename,'r')
f1=open(filename1,'w')
_list=[]
while True:
    line = f.readline()
    if not line:
        break
    _list.append(line)
f.close()
#print >> f1, _list
_list1=[]
i=0
while True:
    if i==len(_list):
        break
    a=str(_list[i])
    a=a[0:len(a)-1]
    _list1.append(a)
    #print a
    #print >> f1, a+" "
    i=i+1
i=0
print >>f1, _list1
f1.close()