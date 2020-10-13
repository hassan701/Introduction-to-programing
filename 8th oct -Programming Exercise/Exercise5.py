def celsius(F):
    C=(5/9)*(F-32)
    return C
def kelvin(C):
    K = C +273.15
    return K



def convert_temp():
    F= eval(input("Enter a temperature in Fahrenheit:"))
    C= celsius(F)
    K= kelvin(C)
    print("The temperature in Fahrenheit is:", F)
    print("The temperature in Celsius is:",C)
    print("The temperature in Kelvin is:", K)

convert_temp()