# Define two variables for arithmetic operations
num1 = 20
num2 = 10

# Arithmetic Operators
print("**************Arithmetic Operators:***********************")
# Addition
print(f"{num1}+{num2}={num1 + num2}")
# Subtraction
print(f"{num1}-{num2}={num1 - num2}")
# Multiplication
print(f"{num1}*{num2}={num1 * num2}")
# Division (Floating point)
print(f"{num1}/{num2}={num1 / num2}")
# Integer Division (Floor division)
print(f"{num1}//{num2}={num1 // num2}")
# Modulus (Remainder)
print(f"{num1}%{num2}={num1 % num2}")
# Exponentiation (Power)
print(f"{num1}**{num2}={num1 ** num2}")
print()  # Line break for readability

# Define two values for comparison operations
value1 = 2000
value2 = 500

# Comparison Operators
print("**********************Comparision Operators:**************************")
# Check equality
print(f"{value1}=={value2}->{value1 == value2}")
# Check inequality
print(f"{value1}!={value2}->{value1 != value2}")
# Greater than
print(f"{value1}>{value2}->{value1 > value2}")
# Less than
print(f"{value1}<{value2}->{value1 < value2}")
# Greater than or equal to
print(f"{value1}>={value2}->{value1 >= value2}")
# Less than or equal to
print(f"{value1}<={value2}->{value1 <= value2}")
# Repeated comparison for illustration (Note: This line compares in reverse order by mistake)
print(f"{value1}>={value2}->{value1 <= value2}")  # This should be comparison: value1 >= value2
print()  # Line break for readability

# Define two boolean flags for logical operations
flag1 = True
flag2 = False

# Logical Operators
print("*********************Logical Operator:***********************")
# AND operation
print(f"{flag1} and {flag2}->{flag1 and flag2}")
# OR operation
print(f"{flag1} or {flag2}->{flag1 or flag2}")
# NOT operation (inverts flag2)
print(f" not {flag2}->{not flag2}")
print()  # Line break for readability

# Define two numbers for bitwise operations
bitwise_num1 = 9
bitwise_num2 = 8

# Bitwise Operators
print("**********************BitWise Operator:****************************")
# Bitwise AND
print(f"{bitwise_num1} & {bitwise_num2}->{bitwise_num1 & bitwise_num2}")
# Bitwise OR
print(f"{bitwise_num1} | {bitwise_num1}->{bitwise_num1 | bitwise_num2}")
# Bitwise XOR
print(f"{bitwise_num1} ^ {bitwise_num2}->{bitwise_num1 ^ bitwise_num2}")
# Bitwise NOT (Unary)
print(f"~{bitwise_num1} ->{~bitwise_num1}")
# Left shift (shift bits to the left)
print(f"{bitwise_num1} << 1 ->{bitwise_num1 << 1}")
# Right shift (shift bits to the right)
print(f"{bitwise_num1} >> 1 ->{bitwise_num1 >> 1}")
