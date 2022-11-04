

Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

Generated_OTP = []

f = open('vault.txt','r')
for i in f:
    Generated_OTP.append(i[0:8])
    print(i)

print(Generated_OTP)

