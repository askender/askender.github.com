import os
for i in range(256):
    print i
    os.system('ssh lb@192.168.10.%s' % i)
