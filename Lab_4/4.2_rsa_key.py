from Crypto.PublicKey import RSA

rsa_private_key = open('rsa_key').read()
rsa_public_key = open('rsa_key.pub').read()

rsa_private_key = RSA.importKey(rsa_private_key)
rsa_public_key = RSA.importKey(rsa_public_key)

m = 'hello world'
print 'Plain Text :', m

c = rsa_public_key.encrypt(m, '')
print 'Encryption :', c

m = rsa_private_key.decrypt(c)
print 'Decrypted Text :', m