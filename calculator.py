def calc():
    def add(a,b):
        return (a+b)
    def sub(a,b):
        return (a-b)
    def mul(a,b):
        return (a*b)
    def div(a,b):
        if (b!=0):
            return (a/b)
        else:
            return"Zero cannot be used to divide"

    print("Enter the numbers need to solved: ")
    x=float(input("1 st number: "))
    y=float(input("2 st number: "))
    print("""Select the operation need to taken place by Entering the coressponding number: 
    1.addition
    2.substraction
    3.multiplication
    4.division""")

    a=int(input("select your choice: "))
    if a==1:
        print("the sum is",add(x,y))
    elif a==2:
        print("the difference is",sub(x,y))
    elif a==3:
        print("the product is",mul(x,y))
    elif a==4:
        print("the value is",div(x,y))
    else:
        print("Out of choice")
    a=str(input(" yes to Calculate again\n no to end the calculator: "))
    a.lower()
    if a=="yes":
        print("\n")
        calc()
calc()
