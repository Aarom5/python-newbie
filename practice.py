n=input('Enter a number: ')
fact=1
try:
    n_f=float(n)
except:
    n=-1
    quit()
while n_f > 0:
    fact=n_f*fact
    n_f=n_f - 1
    #sum=n_f*fact
print(fact)