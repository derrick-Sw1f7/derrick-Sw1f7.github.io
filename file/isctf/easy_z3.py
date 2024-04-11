print("Please input flag:")
flag = input()
if len(flag)!=42:
	print("Check your length!")
	exit()

l=[]
for i in range(6):
	s=""
	for j in flag[i*7:i*7+7]:
		s+=hex(ord(j))[2:]
	l.append(int(s,16))
if (
(593*l[5] + 997*l[0] + 811*l[1] + 258*l[2] + 829*l[3] + 532*l[4])== 0x54eb02012bed42c08 and \
(605*l[4] + 686*l[5] + 328*l[0] + 602*l[1] + 695*l[2] + 576*l[3])== 0x4f039a9f601affc3a and \
(373*l[3] + 512*l[4] + 449*l[5] + 756*l[0] + 448*l[1] + 580*l[2])== 0x442b62c4ad653e7d9 and \
(560*l[2] + 635*l[3] + 422*l[4] + 971*l[5] + 855*l[0] + 597*l[1])== 0x588aabb6a4cb26838 and \
(717*l[1] + 507*l[2] + 388*l[3] + 925*l[4] + 324*l[5] + 524*l[0])== 0x48f8e42ac70c9af91 and \
(312*l[0] + 368*l[1] + 884*l[2] + 518*l[3] + 495*l[4] + 414*l[5])== 0x4656c19578a6b1170):
	print("Good job!")
else:
	print("Wrong\nTry again!!!")
	exit()