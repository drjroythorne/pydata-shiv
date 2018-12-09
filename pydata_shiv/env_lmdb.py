import lmdb
import uuid
import random
import time
import pickle

if __name__=='__main__':
    with lmdb.open('/tmp/lmdb', map_size=int(1e10), readonly=True) as env:
        with open('/home/dan/lmdb_env', 'w') as f:
            pickle.dump(env, f)

        while True:
            time.sleep(1)
#        with env.begin() as t:
#            val = t.get(str(random.randint(1, int(1e7))).encode(), default=None)
#            print(val.decode())
