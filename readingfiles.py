# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for read in fh:
    read=read.upper()
    read=read.strip()
    print(read)

