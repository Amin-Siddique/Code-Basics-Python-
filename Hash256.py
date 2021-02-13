#This code will convert a string to a hash value

import hashlib

str = 'AMIN'

result = hashlib.sha256(str.encode())

print(result.hexdigest())


########### OUTPUT ###########
c596ce513490691676cec7361db64062bdfd5b25da7a61bff3209ac71c588aea
