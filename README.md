# RSA Cryptography Project

## Principles and Practices of Cryptography

This project demonstrates the implementation of the RSA Algorithm using Python programming language.

The project simulates secure communication between two parties, Alice and Bob, using public key cryptography.

---

# Features

- RSA Key Generation
- Public and Private Key Creation
- Encryption using Public Key
- Decryption using Private Key
- Secure Communication Simulation
- User Input Support
- ASCII Conversion
- Test Cases and Outputs

---

# Technologies Used

- Python 3
- VS Code

---

# RSA Algorithm Steps

1. Select two prime numbers
2. Generate modulus (n)
3. Compute Euler’s Totient Function
4. Generate public key
5. Generate private key
6. Encrypt plaintext
7. Decrypt ciphertext

---



# How To Run

## Step 1

Install Python:
https://www.python.org/downloads/

---

## Step 2

Clone the repository:

```bash
git clone https://github.com/kripamehta/rsa_cryptography.git
```

---

## Step 3

Open terminal inside project folder.

Run:

```bash
python rsa.py
```

---

# Sample Input

```text
Enter prime number p: 61
Enter prime number q: 53
Enter message: HELLO
```

---

# Sample Output

```text
Public Key: (7, 3233)
Private Key: (1783, 3233)

Encrypted Message:
[1087, 155, 83, 83, 913]

Decrypted Message:
HELLO
```

---

# Applications of RSA

- Secure Communication
- Digital Signatures
- SSL/TLS Security
- Banking Security
- VPN Authentication

---

# Author

Name: Kripa Sameer Mehta  
Course: Principles and Practices of Cryptography  
University: Ramaiah University of Applied Sciences

---

# License

This project is developed for educational purposes.