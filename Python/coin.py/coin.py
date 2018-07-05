import hashlib as hashlib

tohash = "hello world"

hash = hashlib.sha256(tohash.encode('utf-8')).hexdigest()

nonce = 0
while hash[0] !="0":
    nonce = nonce + 1
    tohash = tohash + str(nonce)
    hash = hashlib.sha256(tohash.encode("utf-8")).hexdigest()

print(hash)
