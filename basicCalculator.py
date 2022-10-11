#Question of the DAY!
##complete the code challenge




ch1 = "Y"
while(ch1 == "Y" or ch1 == "y"):

    print("1. Addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")

    opt = int(input("Enter your selection: "))

    if opt == 1:
        num1= float(input("enter 1st number: "))
        num2= float(input("enter 2nd number: "))
        sum = num1 + num2

        print(f"sum of {num1} and {num2} is: ",sum )

    elif opt == 2:
        num1= float(input("enter 1st number: "))
        num2= float(input("enter 2nd number: "))
        sub = num1 - num2

        print(f"difference of {num1} and {num2} is: ",sub )

    elif opt == 3:
        num1= float(input("enter 1st number: "))
        num2= float(input("enter 2nd number: "))
        into = num1 * num2

        print(f"{num1} times {num2} is: ",into )

    elif opt == 4:
        num1= float(input("enter 1st number: "))
        num2= float(input("enter 2nd number: "))
        sub = num1 / num2

        print(f"{num1} divided by {num2} is: ",sub )

    else:
        print("Enter a valid option")


    ch1 = input("Do yo want to continue?(Y/N): ")
