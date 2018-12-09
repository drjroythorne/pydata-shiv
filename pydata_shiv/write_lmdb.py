import lmdb
import uuid

if __name__=='__main__':
    env = lmdb.open('/tmp/lmdb', map_size=int(1e10))

    with env.begin(write=True) as t:
        for i in range(1000000, int(1e7)):
            t.put(str(i).encode(), uuid.uuid4().hex.encode())
    env.close()
