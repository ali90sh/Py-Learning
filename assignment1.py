def count_prime_divisors(n):

    n = abs(n)
    count = 0
    # Checking 2 
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n //= 2
    # Odd primes
    i = 3
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 2
    # If residual is greater than 1
    if n > 1:
        count += 1
    return count

# input 10 numbers
numbers = []
for _ in range(10):
    x = int(input())
    numbers.append(x)

# Finding number with more prime divisor
best_num = None
best_count = -1

for num in numbers:
    c = count_prime_divisors(num)
    # Choose biggest if primes count is equal
    if c > best_count or (c == best_count and num > best_num):
        best_count = c
        best_num = num

print(f"{best_num} {best_count}")