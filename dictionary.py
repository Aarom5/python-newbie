classmates={'Tony':' cool but smells','Zack':' Sits at the front','Lucy': ' Weird'} # creates a set with key and values
print(classmates)
print(classmates['Zack']) # info about specific object

for k,v in classmates.items():# iterates through every item
    print(k+v)
