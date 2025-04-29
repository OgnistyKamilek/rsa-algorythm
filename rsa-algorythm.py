from sympy import randprime

#powers definition
power_1 = 1023
power_2 = 1024

#p and q definition
p = randprime(2**power_1, 2**power_2)
q = randprime(2**power_1, 2**power_2)

if p == q:
    raise ValueError("p and q cannot be the same!")

if abs(p-q) < 2*100:
    raise ValueError("p and q are too close!")

#GDC definition
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Obliczenie n i phi
n = p * q
phi = (p - 1) * (q - 1)


#e definition and check
e = 65537
if gcd(e, phi) != 1:
    raise ValueError("e is not relatively prime with phi")
else:
    print("e is relatively prime with phi")

#d calculations
d = pow(e, -1, phi)

#Display public and private key
print(f"Public key: {e}, {n}")
print(f"Private key: {d}, {n}")

while True:
    try:
        plaintext = int(input("Enter plaintext: "))
        break
    except ValueError:
        print("Plaintext must be an integer!")

if plaintext >= n:
    raise ValueError("Plaintext is too large for encryption.")

encrypted = pow(plaintext, e, n)
decrypted = pow(encrypted, d, n)

print("Plaintext: ", plaintext)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)