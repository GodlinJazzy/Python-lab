# Electricity Bill Generator

name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")

previous = float(input("Enter Previous Meter Reading (kWh): "))
current = float(input("Enter Current Meter Reading (kWh): "))
cost_per_unit = float(input("Enter Cost per Unit (₹): "))

# Calculations
units = current - previous
energy_charge = units * cost_per_unit
duty = 0.05 * energy_charge
fixed_charge = 100
net_bill = energy_charge + duty + fixed_charge

# Display Bill
print("\n" + "=" * 45)
print("          ELECTRICITY BILL")
print("=" * 45)

print(f"Consumer Name       : {name}")
print(f"Consumer ID         : {consumer_id}")
print(f"Previous Reading    : {previous:.2f} kWh")
print(f"Current Reading     : {current:.2f} kWh")
print(f"Units Consumed      : {units:.2f} kWh")
print(f"Cost per Unit       : ₹{cost_per_unit:.2f}")

print("-" * 45)

print(f"Energy Charge       : ₹{energy_charge:.2f}")
print(f"Electricity Duty    : ₹{duty:.2f}")
print(f"Fixed Meter Charge  : ₹{fixed_charge:.2f}")

print("-" * 45)

print(f"NET BILL AMOUNT     : ₹{net_bill:.2f}")

print("=" * 45)
