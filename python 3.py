import math

num = float(input("Enter a floating-point number: "))

print("\n--- Mathematical Calculator ---")

print(f"Square          : {num ** 2}")
print(f"Cube            : {num ** 3}")

if num >= 0:
    print(f"Square Root     : {math.sqrt(num)}")
else:
    print("Square Root     : Not possible for negative number")

print(f"Ceiling Value   : {math.ceil(num)}")
print(f"Floor Value     : {math.floor(num)}")
print(f"Absolute Value  : {abs(num)}")
print(f"Type of Variable: {type(num)}")
print(f"Memory Address  : {id(num)}")
