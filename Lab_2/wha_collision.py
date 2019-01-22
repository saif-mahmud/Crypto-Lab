def wha(msg) :
    mask = 0x3FFFFFFF
    outHash = 0

    for char in msg :
        byte = ord(char)

        intermediate_value = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
        outHash = (outHash & mask) + (intermediate_value & mask)

    return hex(outHash)


def wha_collision(msg) :
    wha_hash = wha(msg)
    wha_hash = str(wha_hash)

    case_idx = [idx for idx in range(len(msg)) if msg[idx].isupper()]

    if len(case_idx) >= 2 :
        first_idx = case_idx[0]

        for idx in case_idx[1 : ] :
            if msg[first_idx] != msg[idx] :
                result = list(msg)
                temp = result[idx]
                result[idx] = msg[first_idx]
                result[first_idx] = temp

                return ''.join(result)

    case_idx = [idx for idx in range(len(msg)) if msg[idx].islower()]

    if len(case_idx) >= 2 :
        first_idx = case_idx[0]

        for idx in case_idx[1 : ] :
            if msg[first_idx] != msg[idx] :
                result = list(msg)
                temp = result[idx]
                result[idx] = msg[first_idx]
                result[first_idx] = temp

                return ''.join(result)

    return msg[: : -1]





#print wha('Hello world!')
#print wha('I am Groot.')

msg = open('3.2_input_string.txt').read()
print 'Message : ', msg
print 'Message Hash : ', wha(msg)

print 'Collsion Message : ', wha_collision(msg)
print 'Collision Hash : ', wha(wha_collision(msg))