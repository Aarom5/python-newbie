# Use the file name mbox-short.txt as the file name
countx = 0
countline = 0
fname = input("open file name: ")
try:
   fhand = open(fname)
except:
   print ("file not found, ", fname)
   quit()
for line in fhand:
   line = line.rstrip()
   if line.startswith ("X-DSPAM-Confidence"):
      line=line.rstrip()
      #stripped = line.strip("X-DSPAM-Confidence: ")
      fn=line.find('0')
      pos=line[fn:]
      #countx = countx + float(stripped)
      countline = countline + 1
      f_pos=float(pos)
      countx=countx + f_pos
print ("Average spam confidence:", countx / countline)

#desired output:
#Average spam confidence: 0.750718518519