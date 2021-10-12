num1 = float(input("Enters Numbers : "))
operator = input("""Choose math operation:
+\t: Addition
-\t: Subtraction
x\t: Multipication
/\t: Division
...""")

while operator != "=":
    num2 = float(input("Enters Numbers : "))
    if operator == "+":
        result = num1+num2
    elif operator == "-":
        result = num1-num2
    elif operator == "x":
        result = num1*num2
    elif operator == "/":
        result = num1/num2
    else:
        print("You Input Wrong")
    print(result)
    operator = input("""Choose math operation:
+\t: Addition
-\t: Subtraction
x\t: Multipication
/\t: Division
=\t: Final Result
...""")
    num1 = result

print(f"The final result of the calculation is {result:.2f}")
