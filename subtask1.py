# Subtask 8.1
def largest_square(n):
    q = 0
    while (q + 1) ** 2 <= n:
        q += 1
    return q ** 2


n = int(input("Enter a natural number (n): "))
result = largest_square(n)
print(f"The largest square number less than or equal to {n} is {result}.")
