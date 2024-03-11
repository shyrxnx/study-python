# Sum of digits

number = int(input("Enter the number: "))

sum_num = 0

while number != 0:
    digits = int(number % 10)
    sum_num += digits
    number /= 10

print(f"The sum of the digits is {sum_num}")
