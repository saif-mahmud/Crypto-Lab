import sys 
from Crypto.Hash import SHA256
import codecs 


string1 = open('3.1_input_string.txt').read()

string2 = open('3.1_perturbed_string.txt').read()

hex1 = int(SHA256.new(string1).hexdigest(), 16)
hex2 = int(SHA256.new(string2).hexdigest(), 16)
	
hamming = hex(bin(hex1 ^ hex2)[2:].count('1'))[2:]
print 'Hamming Distance : ', hamming

hamming = codecs.encode(hamming, 'hex')

output_file = open('solution31.hex', 'w')
output_file.write(hamming)
output_file.close()