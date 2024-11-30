# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i=i+6
    return True

# Function to find the first n Fibonacci numbers that are prime
def my_n_fib_primes(n):
    fib_primes = []
    a=0
    b=1
    while len(fib_primes) < n:
        a,b=b,a+b
        if is_prime(a):
            fib_primes.append(a)
    return fib_primes


n = input("Enter the number n: ")

# Check if the input is a valid positive integer
if n.isdigit() and int(n) > 0:
    n = int(n)
    print("The first", n, "Fibonacci prime numbers are:", my_n_fib_primes(n))
else:
    print("Please enter a valid positive integer.")