

d = {
"A":"01","B":"02","C":"03","D":"04","E":"05","F":"06","G":"07","H":"08",
"I":"09","J":"10","K":"11","L":"12","M":"13","N":"14","O":"15","P":"16",
"Q":"17","R":"18","S":"19","T":"20","U":"21","V":"22","W":"23","X":"24",
"Y":"25","Z":"26","-":"27"}
msg = "THE-FUTURE-WILL-BE-BETTER-TOMORROW--"
i = 0
s = 0
num_msg = []
cipher = []
num_msg_copy = []
shift = 123456
mod = 279999
while i < len(msg):
    intermediate = ""
    for j in range(i,i+3):
        intermediate += d[msg[j]]
    num_msg.append(int(intermediate))
    num_msg_copy.append(str(int(intermediate)))
    cipher.append(str((num_msg[s] + shift)%mod))
    i += 3
    s += 1
print("NUMERICAL MESSAGE:"," ".join(num_msg_copy))

print("CIPHERTEXT:", " ".join(cipher))
