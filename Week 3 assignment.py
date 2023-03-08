import hashlib

def computeHash(byte):
    h = hashlib.sha256(byte)
    hexDigest = h.hexdigest()
    return hexDigest
byte_array = []
with open("C:\\Users\\shahn\\Desktop\\Raj\\Coursera\\Cryptography\\6.1.intro.mp4_download",mode="rb") \
    as my_file:
    my_file.seek(0)
    byte = my_file.read(1024)
    while byte:
        byte_array.append(byte)
        byte = my_file.read(1024)

byte_array.reverse()

h = computeHash(byte_array[0])
hBytes = bytearray.fromhex(h)
l = len(byte_array)
for i in range(1,l) :
    hBytes = bytearray.fromhex(computeHash(byte_array[i]+hBytes))
print(hBytes.hex())
