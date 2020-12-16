def computepay(h,r):
    if h>40:
        gpay=(h-40)*r*1.5 + 40*r
    else:
        gpay=h*r
    return gpay
hours1=input('Enter hours:')
rph1=input('Enter rate per hour:')
hours=float(hours1)
rph=float(rph1)
pay=computepay(hours,rph)
print('Pay',pay)
