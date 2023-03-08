from Crypto.Util import Counter
from Crypto.Cipher import AES

def encrypt(key, msg, iv=b'0123456789abcdef'):   #takes inputs in bytes. Give string as b'text in string'
    cipher = AES.new(key,AES.MODE_CBC,iv=b'0123456789abcdef')
    ciphertext = cipher.encrypt(msg)
    return ciphertext #returns bytes. Convert to hex using ciphertext.hex()

def decrypt(key, ciphertext, iv=b'4ca00ff4c898d61e1edbf1800618fb28'):  #takes inputs in bytes. Give string as b'text in string'
    ctr = Counter.new(128, initial_value=iv) #for ctr modes
    cipher = AES.new(key,AES.MODE_CTR, counter=ctr)
    msg = cipher.decrypt(ciphertext)
    return msg   #gives output as string bytes. Convert to string using msg.decode('utf-8')

key = bytearray.fromhex('36f18357be4dbd77f050515c73fcf9f2')
ciphertext = bytearray.fromhex('e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451')

msg = decrypt(key, ciphertext, iv=0x770b80259ec33beb2561358a9f2dc617)
print(msg.decode('utf-8'))