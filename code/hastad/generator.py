from Crypto.Util.number import getPrime, bytes_to_long
import os

e = 17
m = bytes_to_long(open("flag.txt", "rb").read())

with open("output.txt", "w") as f:
    for i in range(e):
        p = getPrime(1024)
        q = getPrime(1024)
        N = p * q
        C = pow(m, e, N)
        f.write(f"e = {e}\n")
        f.write(f"N = {N}\n")
        f.write(f"C = {C}\n\n")

print("Generated output.txt successfully")