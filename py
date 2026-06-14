num1 = input("first number: ")
Operation = input("Operation (+,-,*,/) :")
num2 = input("second number: ")
if Operation == "+":
  result = int(num1) + int(num2)
elif Operation == "*":
  result = int(num1) * int(num2)
elif Operation == "-":
  result = int(num1) - int(num2)
elif Operation == "/":
  result = int(num1) / int(num2)
else:
  result = "Operation not invaild"
print(result)
