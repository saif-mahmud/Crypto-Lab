import os

i = 1

while(True):
    os.system("./md5_collision.sh")

    x = os.system("ghostscript collisions/file_1.ps")

    print(i)
    i += 1

    if x == 0:
        break
