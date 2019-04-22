import socket
from word2number import w2n

TCP_IP = '206.189.224.72'
TCP_PORT = 5123
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)

data = s.recv(BUFFER_SIZE)
#if not data: break
print data
#s.close()
data2 = data[0: 10: 1]
data2 = data2[:-3]

print data2
result = str(eval(data2))
s.send(result + "\n")
print result

wordnum = False

count = 0

i = 0

while 1:
	data = s.recv(BUFFER_SIZE)
	try:
		newdata = data.split(' ')
		num1 = newdata[0] + " " + newdata[1]
		int_num1 = w2n.word_to_num(num1)
		wordnum = True
	except ValueError:
		wordnum = False
		# do normal things
		pass

	newdata = data.split(" ")

	if (len(newdata[1]) < 2):
		
		if not data: break
		print(data)
		#s.close()
		data2 = data[0: 10: 1]
		data2 = data2[:-3]
		
		print(data2)
		result = str(eval(data2))
		s.send(result + "\n")
		print result
		print i
		i += 1
	elif ((len(newdata[1]) > 2) and (wordnum == False)):
		if not data: break
		print(data)
		newdata = data.split(' ')
		if newdata[1] == 'plus':
			result = int(newdata[0]) + int(newdata[2])
			print result
		elif newdata[1] == 'minus':
			result = int(newdata[0]) - int(newdata[2])
			print result
		elif newdata[1] == 'mod':
			result = int(newdata[0]) % int(newdata[2])
			print result
		elif newdata[1] == 'times':
			result = int(newdata[0]) * int(newdata[2])
			print result
		elif newdata[1] == 'divided':
			result = int(newdata[0]) / int(newdata[3])
			print result
		s.send(str(result) + '\n')
		i += 1
		print i

	elif (wordnum == True):
		if not data: break
		print(data)
		newdata = data.split(' ')
		num1 = newdata[0] + " " + newdata[1]
		op = newdata[2]
		num2 = newdata[3] + " " + newdata[4]

		print("num1: " + str(num1))
		print("num2: " + str(num2))

		int_num1 = w2n.word_to_num(num1)
		int_num2 = w2n.word_to_num(num2)

		print("int_num1: " + str(int_num1))
		print("int_num2: " + str(int_num2))

		if op == 'plus':
			result = int(int_num1) + int(int_num2)
			print result
		elif op == 'minus':
			result = int(int_num1) - int(int_num2)
			print result
		elif op == 'mod':
			result = int(int_num1) % int(int_num2)
			print result
		elif op == 'times':
			result = int(int_num1) * int(int_num2)
			print result
		elif op == 'divided':
			result = int(int_num1) / int(int_num2)
			print result
		s.send(str(result) + '\n')
		print(result)

