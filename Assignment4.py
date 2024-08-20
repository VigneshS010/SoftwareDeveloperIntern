# Temperature Convertor

def f_to_c(temp):
    return (5/9)*(temp-32)
def c_to_f(temp):
    return (9/5)*temp+32

def main():
    print("Temperature Convertor")
    print("1 - Fahrenheit to Celsius")
    print("2 - Celsius to Fahrenheit")
    print()
    oper = int(input("Choose the Option: "))

    if oper == 1:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = f_to_c(f)
        print(c,"°C")
    elif oper == 2:
        c = float(input("Enter temperature in Celsius: "))
        f = c_to_f(c)
        print(f,"°F")
    else:
        print("Invalid Option")
if __name__ == "__main__":
    main()

