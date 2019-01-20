from collections import Counter
from pycipher import Caesar

def chi2(plain_text) :
    
    #print 'Length of Plain Text : ', len(plain_text)

    english_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    english_freq = [i * len(plain_text) for i in english_freq]
    
    plain_text = plain_text.upper()

    counts = Counter(plain_text)
    #print 'Character Frequency : ', counts

    cnt_freq = [0] * 26

    for key, value in counts.iteritems():
        cnt_freq[ord(key) - 65] = value
    
    chi_square = [0] * 26

    for i in range(26) :
        chi_square[i] = ((cnt_freq[i] - english_freq[i]) ** 2) / english_freq[i]    

    return sum(chi_square)



cipher_text = open('caesar_cipher.txt').read()

data = []

for i in range(26):
    plain_text = Caesar(i).decipher(cipher_text)
    print "%2d" % i ," | ", plain_text, " | Chi-Square : ", chi2(plain_text)
    data.append(tuple((i, chi2(plain_text))))
    
x = min(data, key = lambda tup: tup[1])
decipher_text = Caesar(x[0]).decipher(cipher_text, keep_punct = True)

print '\nShift : ', x[0], ', Chi-Square : ', x[1]
print 'Deciphered Text : ', decipher_text