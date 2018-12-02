
import hashlib
def hash_sha256(string):
    m = hashlib.sha256()
    m.update(bytes(string,'utf8'))
    print('SHA256值：')
    print(m.hexdigest())
    print('HASH长度（16进制）：',m.blocksize)
if __name__ == '_main_':
    import sys
    hash_sha256(sys.argv[1])
