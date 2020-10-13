def calc_new_height():
    cw=eval(input("Enter the current width:"))
    ch=eval(input("Enter the current height:"))
    dw=eval(input("Enter the desired width:"))
    dh=(dw*ch)/cw
    return print("The corresponding height is:",dh)

calc_new_height()