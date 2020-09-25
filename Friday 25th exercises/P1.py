print("Enter your height")
a = eval(input("Feet:"))
b = eval(input("Inches:"))
c = (a*12) + b
print("Suggested board length:",(c*2.54*0.88),"cm")