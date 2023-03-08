import urllib
from urllib.request import urlopen
from urllib.error import HTTPError
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib.parse.quote(q)    # Create query URL
        req = urllib.request.Request(target)         # Send HTTP request to server
        try:
            f = urlopen(req)          # Wait for response
        except HTTPError as e:          
            print("We got: %d" % e.code)       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

def xor(a,b):
    return hex(int(a,16) ^ int(b,16))

if __name__ == "__main__":
    po = PaddingOracle()

    targetCipher = "f20bdba6ff29eed7b046d1df9fb70000 58b1ffb4210a580f748b4ac714c001bd 4a61044426fb515dad3f21f18aa577c0 bdf302936266926ff37dbf7035d5eeb4".split(' ')
    cIV = targetCipher[0]
    c0 = targetCipher[1]
    c1 = targetCipher[2]
    c2 = targetCipher[3]

    #Steps:
    #Take the last segment that is c2, xor that with guess byte and 0x01 until True
    #Repeat this for second last byte -> Repeat for all bytes
    #Get decoded c2

    last_byte = ""
    decrypted_msg = ""
        
    for j in range(1,17):
        pad = ""
        to_add=str(hex(j)[2:])
        if len(to_add)==1:
            to_add = '0'+to_add
        for k in range(0,j):
            pad += to_add
        print("pad="+pad)
        for i in range(2,256):  # start from 0, if it doesn't work for last block, start from 2
            print("i="+str(i)+" j="+str(j)+"\n")
            to_add2 = str(hex(i)[2:])
            if len(to_add2)==1:
                to_add2 = '0'+to_add2
            guess_byte = to_add2+decrypted_msg
            print("Guess Byte: "+guess_byte)
            to_xor = xor(pad,guess_byte)[2:]
            # Change the next 2 lines as to
            # guess_c = xor(c0,to_xor)
            # guess_cipher = guess_c + c1
            # to get the decryption for c1, and so on.
            # The code is complete.
            # If this does not work for the last block, try starting the i loop from 1 or 2 instead of 0
            # This happens due to it already having a valid padding and hence showing correct padding.
            # Anyways 00 or 01 won't be there generally in a plaintext, so it doesn't affect other blocks
            guess_c = xor(c1,to_xor)[2:]
            guess_cipher = guess_c + c2
            print("Guess Cipher: "+guess_cipher)
            if po.query(guess_cipher):
                decrypted_msg = guess_byte
                print("Decrypted message:"+decrypted_msg)
                break
    print(decrypted_msg)

# 546865204d6167696320576f72647320 6172652053717565616d697368204f73 73696672616765090909090909090909
# The Magic Words are Squeamish Ossifrage