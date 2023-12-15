# Subtask 8.2
n = 0
s = 0
m = float('inf')  
a = 0

x = int(input("Enter a natural number (or -1 to terminate): "))

while x != -1:
    n += 1
    s += x
    
    if x < m:
        m = x
    
    a = s / n
    
    x = int(input("Enter the next natural number (or -1 to terminate): "))

if n == 0:
    m = a = -1

print(f"Count (n): {n}")
print(f"Sum (s): {s}")
print(f"Minimum (m): {m}")
print(f"Mean (a): {a}")
