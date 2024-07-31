while True:
    weight = float(input("Enter Your Weight: \n"))
    unit = input("Enter the unit kg or p: \n").lower()
    if unit == 'kg':
        print(str(2.204 * weight) + " is your weight in pounds")
    elif unit == 'p':
        print(str(0.453592 * weight) + " is your weight in kg")