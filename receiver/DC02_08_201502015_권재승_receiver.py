import socket

# md5 file write
BLOCK = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('',9000))

# timeout 3s
server_socket.settimeout(5)

data, addr = server_socket.recvfrom(2000)
print("file recv start from " + addr[0])
print(data.decode())
filename = data.decode()
print("File Name : " + filename)

data, addr = server_socket.recvfrom(2000)
total_size = int(data.decode())
print("File Size : " + str(total_size))

current_size = 0
filedata = bytes()

while current_size < total_size:
	try:
		data = server_socket.recv(BLOCK)
	except:
		break
	filedata += data
	current_size += BLOCK
	persent = (current_size/total_size)*100
	print(("current_size / total_size = %d/%d, " % (current_size,total_size)) + str(persent) +"%")


open(filename, "wb").write(filedata)
