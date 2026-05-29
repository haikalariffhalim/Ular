# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Find prime numbers between 1 and 250
primes = []

for number in range(1, 251):
    if is_prime(number):
        primes.append(number)

# Display prime numbers
print("Prime numbers between 1 and 250:")

for prime in primes:
    print(prime)

# Store results in a text file
with open("results.txt", "w") as file:
    file.write("Prime numbers between 1 and 250:\n")

    for prime in primes:
        file.write(f"{prime}\n")

print("\nResults have been saved to results.txt")
