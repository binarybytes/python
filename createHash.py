# simple program to generate the SHA-256 hash of file

import hashlib
print("." * 40)
print("Generating Hashes for multiple files")
print("." * 40)
myString = "Python forensics"
md5hash = hashlib.md5(str(myString).encode('utf-8'))
sha256hash = hashlib.sha256(str(myString).encode('utf-8'))

hexmd5 = md5hash.hexdigest()
hexsha256 = sha256hash.hexdigest()
# print out the result and utilize the upper method
# to convert all the hex characters to upper case
print("SHA256: " + hexsha256.upper())
print("MD5: " + hexmd5.upper())
print("FileName: " + myString)
print("." * 40)
print("Processing completed.")
print("." * 40)

