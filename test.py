import re
fopen=open('regex_sum_1095234.txt')
total=[0]
s=0
for word in fopen:
    word=word.rstrip()
    if len(word) == 0:
        continue
    num=re.findall('[0-9]+',word)

    #num_f=float(num)
    #print(num)
    total= num + total
    #print(total)
    res = [int(i) for i in total]
    for dig in total:
        dig=int(dig)
        s=s + dig
        #print(s) # Checking which numbers are skipped and which are not, seems '7' is skipped everytime can,t understand why

#print(total)
print(sum(res))
#print(s)# Could you please have a look as to why this line doesn't give right output