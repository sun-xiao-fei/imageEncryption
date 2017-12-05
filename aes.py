from Crypto.Cipher import AES
data = 2**128-1
password=2**128-1

obj = AES.new(password.to_bytes(16,'big'), AES.MODE_CBC, b'This is an IV456')
ciphertext = obj.encrypt(data.to_bytes(16,'big'))
obj2 = AES.new(password.to_bytes(16,'big'), AES.MODE_CBC, b'This is an IV456')
data_get=obj2.decrypt(ciphertext)
int.from_bytes(ciphertext,'big')

