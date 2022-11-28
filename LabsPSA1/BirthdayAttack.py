import hashlib
import os
import binascii


def ranstr():
    return str(binascii.b2a_hex(os.urandom(16))).removeprefix("b'").removesuffix("'")


hashdict = {}
colnr = 0

while colnr < 10:
    samplestr=ranstr()
    hashstr = hashlib.md5(samplestr.encode()).hexdigest()
    slicehash = hashstr[:10]
    if slicehash in hashdict:
        print("Found Collision!", slicehash)
        print("Randomly generated string:", samplestr, "Hash:", hashstr)
        print("Original string:", hashdict[slicehash])
        colnr += 1
        print("Collisions:", colnr)
    else:
        hashdict.update({slicehash: samplestr})
