import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import codecs

cipher = open('aes_weak_ciphertext.hex').read()
print (cipher)

cipher = codecs.decode(cipher, 'hex')
print (cipher)

iv = ''
for i in range(16) :
    iv += chr(0)
    
print (iv)

test_root = ''

for i in range(0, 31) :
    test_root += chr(0)

for i in range(32) :
    test_key = (chr(i))
    #print (test_key + test)
    
    decryption_suite = AES.new(test_root + test_key, AES.MODE_CBC, iv)
    plain_text = decryption_suite.decrypt(cipher)

    print i, ' : ', plain_text

ans = test_root + chr(30)
ans = codecs.encode(ans, 'hex')

print 'Key : ', ans

output_file = open('solution03.hex', 'w')
output_file.write(ans)
output_file.close()