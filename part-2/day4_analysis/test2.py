filename="input_whole_review_test2.txt"#input file replace by input_whole_review_test2.txt
filename1="each_line_one_sent.txt"
fp1=open(filename1,'w')
fp=open(filename,'r')
line=fp.readline()
while True:
    line=fp.readline()
    if not line:
        break
    token=line.strip().split('.')
    for i in range(0,len(token)):
        fp1.write(str(token[i])+"\n")
fp1.close()
fp.close()