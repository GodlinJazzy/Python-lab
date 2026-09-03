# Student Information and Academic Summary

name = input("Enter Student Name: ")
usn = input("Enter USN: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculations
total = mark1 + mark2 + mark3
average = total / 3

# Formatted output
print("\n" + "=" * 40)
print("       STUDENT ACADEMIC SUMMARY")
print("=" * 40)

print(f"Student Name : {name}")
print(f"USN          : {usn}")
print(f"Branch       : {branch}")
print(f"Semester     : {semester}")
print(f"Subject 1    : {mark1}")
print(f"Subject 2    : {mark2}")
print(f"Subject 3    : {mark3}")
print(f"Total Marks  : {total}")
print(f"Average Marks: {average:.2f}")

print("=" * 40)
