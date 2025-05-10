import base64

# hex string format
input = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# output in base 64
output = base64.b64encode(bytes.fromhex(input))

print(output)
# decoded output
print(output.decode())
