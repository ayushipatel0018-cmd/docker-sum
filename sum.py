import sys

if len(sys.argv) != 3:
    print("Error: Two arguments required.")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
except ValueError:
    print("Error: Arguments must be numbers.")
    sys.exit(1)

print(num1 + num2)
