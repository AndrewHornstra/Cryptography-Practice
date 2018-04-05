
# Three-letter encryption addition-modulo
length = 3
d = {
"A":"01","B":"02","C":"03","D":"04","E":"05","F":"06","G":"07","H":"08",
"I":"09","J":"10","K":"11","L":"12","M":"13","N":"14","O":"15","P":"16",
"Q":"17","R":"18","S":"19","T":"20","U":"21","V":"22","W":"23","X":"24",
"Y":"25","Z":"26","-":"27"
}
d_inverse = {
1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",
13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",
24:"X",25:"Y",26:"Z",27:"-"
}
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
    for j in range(i,i+length):
        intermediate += d[msg[j]]
    num_msg.append(int(intermediate))
    num_msg_copy.append(str(int(intermediate)))
    cipher.append(str((num_msg[s] + shift)%mod))
    i += 3
    s += 1
# print("NUMERICAL MESSAGE:"," ".join(num_msg_copy))
#
# print("CIPHERTEXT:", " ".join(cipher))


# Encrypt two-letter multiplication-modulo
# Spaces and "-" are treated the same in encoding, then decoded as "-"
length = 2
d = {
"A":"01","B":"02","C":"03","D":"04","E":"05","F":"06","G":"07","H":"08",
"I":"09","J":"10","K":"11","L":"12","M":"13","N":"14","O":"15","P":"16",
"Q":"17","R":"18","S":"19","T":"20","U":"21","V":"22","W":"23","X":"24",
"Y":"25","Z":"26","-":"27", " ":"27"
}

message = "DENY EVERYTHING"
shift = 5
modulo = 2727
num_msg = []
num_msg_copy = []
cipher = []
i = 0
s = 0
while i <len(message):
    intermediate = ""
    for j in range(i, i + length):
        intermediate += d[message[j]]
    num_msg.append(int(intermediate))
    num_msg_copy.append(str(int(intermediate)))
    cipher.append(str((num_msg[s] * shift)%mod))
    i += 3
    s += 1
# print("NUMERICAL MESSAGE:"," ".join(num_msg_copy))
#
# print("CIPHERTEXT:", " ".join(cipher))

# Decrypt two-letter multipication-modulo
# This needs to be made into a function and made to work for n-letter
longest = 4
second_problem = [1859, 2625, 2647, 1621, 727, 1894, 2181, 1151, 1540]
inverse = 1091
num_msg_2 = []
message = []
mod = 2727
for i in second_problem:
    a = i*inverse % mod
    num_msg_2.append(str(a))
    if len(str(a)) == longest-1:
        message.append(d_inverse[int(str(a)[0])] + d_inverse[int(str(a)[1:])])
    else:
        message.append(d_inverse[int(str(a)[0:2])] + d_inverse[int(str(a)[2:])])


# print("NUMERICALLY DECRYPTED:", " ".join(num_msg_2))
# print("MESSAGE:", " ".join(message))
