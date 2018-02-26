n = int(input())
text = input()

for i in range(len(text)):
	flag = ord(text[i]) - n;
	if flag < 97 and text[i] != ' ':
		print(chr(26 + flag), end="")
	elif text[i] != ' ':
		print(chr(flag),end="")
	else:
		print(text[i],end="")

print()
