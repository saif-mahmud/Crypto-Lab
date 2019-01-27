def wha(message) :
    mask = 0x3FFFFFFF
    outHash = 0

    for char in message :
        byte = ord(char)

        intermediate_value = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
        outHash = (outHash & mask) + (intermediate_value & mask)

    return hex(outHash)


def wha_collision(message) :
    wha_hash = wha(message)
    wha_hash = str(wha_hash)

    case_idx = [idx for idx in range(len(message)) if message[idx].isupper()]

    if len(case_idx) >= 2 :
        first_idx = case_idx[0]

        for idx in case_idx[1 : ] :
            if message[first_idx] != message[idx] :

                result = list(message)
                
                #Swap
                temp = result[idx]
                result[idx] = message[first_idx]
                result[first_idx] = temp

                return ''.join(result)

    case_idx = [idx for idx in range(len(message)) if message[idx].islower()]

    if len(case_idx) >= 2 :
        first_idx = case_idx[0]

        for idx in case_idx[1 : ] :
            if message[first_idx] != message[idx] :
                
                result = list(message)
                
                #Swap
                temp = result[idx]
                result[idx] = message[first_idx]
                result[first_idx] = temp

                return ''.join(result)

    return message[: : -1]



#print wha('Hello world!')
#print wha('I am Groot.')

message = open('3.2_input_string.txt').read()
print 'Message : ', message
print 'Message Hash : ', wha(message)

print 'Collsion Message : ', wha_collision(message)
print 'Collision Hash : ', wha(wha_collision(message))

output_file = open('solution32.txt', 'w')
output_file.write(wha_collision(message))
output_file.close()