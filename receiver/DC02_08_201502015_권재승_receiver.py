import socket

BLOCK = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('',9000))

# timeout 10s
server_socket.settimeout(10)

# recv server_addr & filename
data, addr = server_socket.recvfrom(2000)
print("file recv start from " + addr[0])
print(data.decode())
filename = data.decode()
print("File Name : " + filename)

# recv filesize
data, addr = server_socket.recvfrom(2000)
total_size = int(data.decode())
print("File Size : " + str(total_size))

# empty bytes array
current_size = 0
filedata = bytes()

# recv file
while current_size < total_size:
	try:
		data = server_socket.recv(BLOCK)
	except:
		break
	filedata += data
	current_size += len(data)
	if(current_size > total_size):
		current_size = total_size
	
	persent = (current_size/total_size)*100
	
	msg = ("current_size / total_size = %d/%d, " % (current_size,total_size)) + str(persent) +"%"
	print(msg)
	server_socket.sendto(msg.encode(), addr)

# write file
open(filename, "wb").write(filedata)
