def computepay(h,r):
    if h<=40:
        grosspay=h*r
        return grosspay
    elif h>40:
        h_new=h-40
        grosspay=(h_new*1.5*r) + (40*r)
        return grosspay

hrs = input("Enter Hours:")
rph=input("Enter rate per hour:")
hrs_f=float(hrs)
rph_f=float(rph)
p = computepay(hrs_f,rph_f)
print("Pay",p)







