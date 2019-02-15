from fractions import Fraction
from decimal import *
import math
import sys

sys.setrecursionlimit(1500)

def bigmod(m, e, n):
    if e == 0:
        return 1
    elif e == 1:
        return m
    elif m == 0 or n == 1:
        return 0
    
    ans = bigmod(m, (e//2), n) % n
    ans = (ans*ans) % n
    
    if e % 2 == 1:
        ans = (ans*m) % n
    
    return ans



ciphertext = open("4.3_ciphertext.hex", "r").read()
print 'Ciphertext (from File):', ciphertext, '\n'

e = open("4.4_public_key.hex", "r").read()
print 'e (from File)=', e, '\n'

n = open("4.5_modulo.hex", "r").read()
print 'n (from File)=', n, '\n'

ciphertext = int(ciphertext, 16)
print 'Ciphertext :', ciphertext, '\n'

e = int(e, 16)
print 'e =', e, '\n'

n = int(n, 16)
print 'n =', n, '\n'

d = 1
fractional_parts = []


def getContinuedFractionSum(lst):
    a = Fraction(0)

    for i in lst:
        b = Fraction(1, 1)
        a = b._div(a._add(i))
    
    return a


def euclidContinuedFraction(n, e):
    global fractional_parts

    if e == 0:
        return n
    
    fractional_parts.append(n//e)
    
    if is_upto_this_approximation_valid(fractional_parts) == True:
        return
    
    euclidContinuedFraction(e, n % e)


def is_upto_this_approximation_valid(fractional_parts):
    global e, n, ciphertext, d

    reversed_fractional_partlst = list(reversed(fractional_parts))
    
    rational_approximation = getContinuedFractionSum(reversed_fractional_partlst)
    
    k = rational_approximation.numerator
    d = rational_approximation.denominator
    
    if (d % 2 == 0) or ((e*d-1) % k != 0):
        return False
    
    phi = (e*d-1)/k

    b = -(n-phi+1)
    discriminant = (b**2)-(4*n) # b^2 - 4ac

    if discriminant < 0:
        return False
    if ((-b+math.sqrt(Decimal(discriminant)))/2) % 1 != 0 or ((-b-math.sqrt(Decimal(discriminant)))/2) % 1 != 0:
        return False

    #print bigmod(ciphertext, d, n)
    
    return True

euclidContinuedFraction(n, e)


print 'Wiener\'s Attack : \n'

print 'd =', d, '\n'

deciphered_text = bigmod(ciphertext, d, n)
print 'Deciphered Text :', deciphered_text, '\n'

print 'Verification : '

test_plaintext = 10101010103
print 'Test Plaintext :', test_plaintext, '\n'

test_cipher = bigmod(test_plaintext, e, n)
print 'Encryption :', test_cipher, '\n'

deciphered_verification = bigmod(test_cipher, d, n)
print 'Decryption :', deciphered_verification, '\n'