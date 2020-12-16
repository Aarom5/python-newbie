import re
#x='My 2 favourite numbers are 19 and 55'
#y=re.findall('[0-9]+',x)
#print(y)
x='From: Using the:'
y=re.findall('^F.+:',x)  #Greedymatching, will give maximum output,-^(starts with),-.(any character)
z=re.findall('^F.+?:',x)  #Not greedy matching,shortest output
print(y)
print(z)
r='From stephen@uct.mg.ic 12/12/20'
s=re.findall('^From (\S+@\S+)',r)#/S-non blank character,+-one or more,()-Extraction start and end
print(s)
#Python Regular Expression Quick Guide
'''
^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
'''