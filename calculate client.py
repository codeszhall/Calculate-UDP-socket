import socket

s = socket
IPv4 = s.AF_INET
UDP = s.SOCK_DGRAM
ss = s.socket(IPv4, UDP)

HOST_CONNECT = "127.0.0.1"
PORT_CONNECT = 8080
SERVER_ADDR = (HOST_CONNECT, PORT_CONNECT)

endecode_data = "ascii"
buffer_size_udp = 65536

ss.connect(SERVER_ADDR)

print("Calculate your number")
message = input("Enter [number, operand, number]: ")

message = message.encode(endecode_data)
ss.sendto(message, SERVER_ADDR)

message = ss.recv(65536)
message = message.decode(endecode_data)

print(message)
ss.close()
