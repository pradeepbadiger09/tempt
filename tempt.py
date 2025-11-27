import sys
if len (sys.argv) != 2:
print("Usage: python temp_alert.py ‹temperi
sys.exit()
temp = float(sys.argv[1])
if temp < 15:
print("Cold")
elif 15 <= temp <= 30:
print("Normal")
else:
print("Hot")
