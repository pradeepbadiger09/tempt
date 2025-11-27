import sys

# Check if argument count is correct
if len(sys.argv) != 2:
    print("Usage: python temp_alert.py <temperature>")
    sys.exit()

# Convert input to float
temp = float(sys.argv[1])

# Temperature conditions
if temp < 15:
    print("Cold")
elif 15 <= temp <= 30:
    print("Normal")
else:
    print("Hot")
