largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
            num_f = float(num)
    except:
            print("Invalid Input")
            continue
    if smallest is None:
        smallest = num_f
    elif smallest > num_f:
        smallest = num_f
    if largest is None:
        largest = num_f
    elif largest < num_f:
        largest = num_f
print("Maximum is", int(largest))
print("Minimum is",int(smallest))