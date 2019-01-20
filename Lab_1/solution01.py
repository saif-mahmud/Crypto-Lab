from pycipher import SimpleSubstitution

sub_key = open('sub_key.txt').read()
sub_cipher = open('sub_ciphertext.txt').read()

print 'Substitution Key : ', sub_key
print 'Substitution Cipher : ', sub_cipher

plain_text = SimpleSubstitution(sub_key).decipher(sub_cipher, keep_punct = True)

print 'Plain Text : ', plain_text

output_file = open('solution01.txt', 'w')
output_file.write(plain_text)
output_file.close()