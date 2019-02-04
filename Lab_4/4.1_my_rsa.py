import math

def extended_euclid(a, b) :
    if b == 0 :
        return (1, 0, a)
    x, y, d = extended_euclid(b, a % b)

    return (y, (x - math.floor(a / b) * y), d) 

def modular_inv (b, n) :
    x, y, gcd = extended_euclid(b, n)

    if gcd == 1 :
        return x % n

p = 11
q = 19

N = p * q
phi = (p - 1) * (q - 1)

print 'N =', N
print 'phi =', phi

e = 7
d = modular_inv(e, phi)

d = int(d)

print 'd =', d

def encrypt(m) :
    c = (m ** e) % N
    return c

def decrypt(c) :
    m = (c ** d) % N
    return m

m = 3
print 'M =', m

c = encrypt(m)
print 'C =', c

print 'M =', decrypt(c)