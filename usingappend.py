#Thank You Coursera
fget = input('Please enter file name:')
f_handle = open(fget)
text = list()
for line in f_handle:
	line = line.rstrip()
	line = line.split()
	for i in line:
		if i in text:
			continue
		else:
			text.append(i)
text.sort()
print(text)