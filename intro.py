# intro.py
import sock

print("Welcome to Offensive Python!")
print("This is your first Python script.")

#Basic Data Types
#Numeric Types
#Int
n = 2_147_483_648          # underscores improve readability
print(n.bit_length())      # bits needed: 31
print(hex(n))              # '0x80000000'
print(n.to_bytes(4, 'big'))  # b'\x80\x00\x00\x00'

from math import isclose
isclose(0.1 + 0.2, 0.3, rel_tol=1e-09)

from decimal import Decimal    # fixed-point, user-defined precision
from fractions import Fraction # rational numbers

#TextData
raw = sock.recv(1024)        # bytes
text = raw.decode('utf-8', errors='replace')




