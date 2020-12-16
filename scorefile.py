score = input("Enter Score: ")
try:
    score_f=float(score)
except:
    print("Error")
    quit()
if score_f>=0.9:
    print("A")
elif score_f>=0.8:
    print("B")
elif score_f >= 0.7:
    print("C")
elif score_f >= 0.6:
    print("D")
elif score_f < 0.6:
    print("F")