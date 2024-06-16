#user inputs 2 numbers
num1 = int(input("Enter First Number\n"))
num2 = int(input("Enter Second Number\n"))

#multiply numbers
mult = num1 * num2

#make sure num2 is not 0 before dividing
if num2 != 0:
    div = num1 / num2
else:
    div = "undefined"

#output results
print(num1,"*",num2,"is",mult)
print(num1,"/",num2,"is",div)
input("Press Enter to exit.")
