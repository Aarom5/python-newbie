#get = input('Enter file name: ')
fhand = open('D:\mbox-short.txt')
for i in fhand:
    i = i.rstrip()
    if not i.startswith('From '):
        continue
    words = i.split()
    #mbprint(words)
    print(words[2])


