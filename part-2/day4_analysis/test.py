fp=open("pos_neg_word_replace_by_value.txt",'r')
fp1=open("value_change.txt",'w')
while True:
    line=fp.readline()
    if not line:
        break;
    token=line.strip().split(';')
    #count=0
    for i in range(0,len(token)-1):
        _token1=str(token[i]).split(',')
        _token2=str(token[i+1]).split(',')
"""        if(len(_token1)>=1)and(len(_token2)>=1):

        if (int(_token2[1])- int(_token1[1]))<=3:
                i=i+1
                if _token1[0]=='-1' and _token2[0]=='+1':
                    fp1.write("-1,")#count=count-1
                if _token1[0]=='-1' and _token2[0]=='-1':
                    fp1.write("+1,")#count=count+1
                if _token1[0]=='+1' and _token2[0]=='+1':
                    fp1.write("+1,")#count=count+1
                if _token1[0]=='+1' and _token2[0]=='-1':
                    fp1.write("-1,")#count=count-1
            else:
                if _token1[0]==-1:
                    fp1.write("-1,")#count=count-1
                if _token1[0]==+1:
                    fp1.write("+1,")#count=count+1
                if i==(len(token)-1):
                    if _token2[0]==-1:
                        fp1.write("-1,")#count=count-1
                    if _token2[0]==+1:
                        fp1.write("+1,")#count=count+1
            #print count
            #fp1.write(str(count))
    fp1.write("\n")
        #if (token2[2]- _token1[2])<=3:
        #print _token1[1]
       # if _token1[1]=='-1' and _token2[1]=='+1':
        #    count=count-1
        """

