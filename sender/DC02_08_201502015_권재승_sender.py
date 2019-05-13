import socket

IP = "127.0.0.1"
PORT = 9000
BLOCK = 1024

class ClientSocket():
	def __init__(self):	
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.socket.settimeout(0.1)
	
	def socket_sendfile(self, filename):
		# file open and read data
		filedata = open(filename, "rb").read()
		total_size = len(filedata)
		# send total size
		self.socket.sendto(str(total_size).encode(), (IP, PORT))
		
		current_size = 0
		print("File Transmit Start....")
		while current_size < total_size:
			senddata = filedata[current_size:current_size+BLOCK]
			self.socket.sendto(senddata, (IP, PORT))
			current_size+=BLOCK
			
			try:
				msg, addr = self.socket.recvfrom(BLOCK)
			except:
				pass
			persent = (current_size/total_size)*100
			msg = ("current_size / total_size = %d/%d, " % (current_size,total_size)) + str(persent) +"%"
			print(msg)
		print("ok")
		print("file_send_end")

	def main(self):
		# input file name
		filename = input("Input your file name : ")
		
		# send file name & send file
		self.socket.sendto(filename.encode(), (IP, PORT))
		self.socket_sendfile(filename)
		
		
if __name__ == '__main__':
	client_socket = ClientSocket()
	client_socket.main()
