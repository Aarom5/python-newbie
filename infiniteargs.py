def add_numbers(*args): #*args tells the program any no. of arguments can be given
    total=0
    for a in args:
        total += a
    print(total)
add_numbers(3)
add_numbers(43,53,29)
add_numbers(12231,12322,43432)

