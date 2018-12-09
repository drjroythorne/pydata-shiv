import lmdb
import uuid
import random
import time

if __name__=='__main__':
    env = lmdb.open('/tmp/lmdb', map_size=int(1e10), readonly=True)
    i = 0
    with env.begin() as t:
        while(True):
        #for i in range(int(1e2)):
            val = t.get(str(random.randint(1, int(1e7))).encode(), default=None)
            time.sleep(0.001)
#            print(val.decode())
            i += 1
            if (i % 1000) == 0:
                print(env.stat())
    env.close()
