hrs = input("Enter Hours:")
h = float(hrs)
rph=input("Enter rate per hour:")
rph_f= float(rph)
if h<=40:
    grosspay=h*rph_f
    print(grosspay)
elif h>40:
    new_hrs=h-40
    grosspay=(new_hrs*1.5*rph_f) + (40*rph_f)
    print(grosspay)

