import urllib
from pymd5 import md5, padding

query = open('3.3_query.txt').read()
command3 = open('3.3_command3.txt').read()

print 'Query : ', query

token = query.split('=')[1].split('&')[0]
print 'Token : ', token

parameters = query.split('&')
print 'Parameters : ', parameters

message = parameters[1] + '&' + parameters[2] + '&' + parameters[3]
print 'Message (without 8-char password) : ', message

length =  len(message) + 8 # message + 8-character password (1 char = 1 Byte)
print 'Length of Message (with 8-char password) : ', (length * 8)
print 'Length of Padding : ', (len(padding(length * 8)) * 8)

bits = (length + len(padding(length * 8))) * 8
print 'Total # of Bits : ', bits

h = md5(state = token.decode('hex'), count = bits)
h.update(command3)

modified_token = h.hexdigest()
print 'Modified Token : ', modified_token

updated_query = query.split('=')[0] + '=' + modified_token + '&' + message + urllib.quote(padding(length * 8)) + command3
print 'Updated Query : ', updated_query

output_file = open('solution33.txt', 'w')
output_file.write(updated_query)
output_file.close()

print '\nVerification Step : '
password = input('Insert 8-character Password : ')
print 'Valid User Pass : ', password
message = str(password) + message
print 'Message (with 8-char Pass) : ', message
verification_query = message + padding(len(message) * 8) + command3
print 'Verification Query : ', verification_query
verification_token = md5(verification_query).hexdigest()
print 'Verification Token : ', verification_token

print 'Verification : ', token == verification_token 