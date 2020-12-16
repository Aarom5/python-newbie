numlist=list()
while True:
    inp=input('Enter number: ')
    if inp == 'done':
        break
    inp_f=float(inp)
    numlist.append(inp_f)
average=sum(numlist)/len(numlist)
print(average)