import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import codecs

key = open('aes_key.hex').read()
print key

iv = open('aes_iv.hex').read()
cipher = open('aes_ciphertext.hex').read()

key = codecs.decode(key, 'hex')
print key

iv = codecs.decode(iv, 'hex')
cipher = codecs.decode(cipher, 'hex')

decryption_suite = AES.new(key, AES.MODE_CBC, iv)
plain_text = decryption_suite.decrypt(cipher)

print plain_text

output_file = open('solution02.txt', 'w')
output_file.write(plain_text)
output_file.close()
