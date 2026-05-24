import math

# Function to check if number is prime


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to calculate gcd


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate modular inverse


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None


# Step 1: Select Prime Numbers
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

if not (is_prime(p) and is_prime(q)):
    print("Both numbers must be prime.")
    exit()

if p == q:
    print("p and q should not be equal.")
    exit()

# Step 2: Compute n
n = p * q

# Step 3: Compute phi
phi = (p - 1) * (q - 1)

# Step 4: Choose e
for e in range(2, phi):
    if gcd(e, phi) == 1:
        break

# Step 5: Compute d
d = mod_inverse(e, phi)

# Public and Private Keys
print("\nPublic Key:", (e, n))
print("Private Key:", (d, n))

# Encryption
message = input("\nEnter message: ")

encrypted = [pow(ord(char), e, n) for char in message]
print("Encrypted Message:", encrypted)

# Decryption
decrypted = ''.join([chr(pow(char, d, n)) for char in encrypted])
print("Decrypted Message:", decrypted)
