num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the limit: "))

m = [i for i in range(num3) if i % num1 == 0 or i % num2 == 0]
sum = sum(m)

print (f"The sum of multiples of {num1} or {num2} up to 10 is {sum}.")