inp=input('Enter file name: ')
fhand=open(inp)
str=inp.strip()
for i in fhand:
    print(i.upper().rstrip())
