def day(h,m,s):
    days= (h/24)+(m/(60*24))+(s/(3600*24))
    return round(days,4)



def convert_to_days():
    h= eval(input("Enter number of hours:"))
    m= eval(input("Enter number of minutes:"))
    s= eval(input("Enter number of seconds:"))
    return print("The number of days is: ",day(h,m,s))

convert_to_days()
