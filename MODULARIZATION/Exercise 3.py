import calendar

def main():
    x = eval(input("What Year:"))
    y = eval(input("What month in numbers(April = 4):"))
    print (calendar.month(x,y, w=0, l=0))

main()