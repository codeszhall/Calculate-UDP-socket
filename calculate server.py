import socket

s = socket
IPv4 = s.AF_INET
UDP = s.SOCK_DGRAM
ss = s.socket(IPv4, UDP)

HOST = ""
PORT = 8080
ss.bind((HOST, PORT))

buffer_size = 1024

endecode_data = "ascii"
status_success_response = "OK"

while 1 :
    message, addr = ss.recvfrom(buffer_size)
    client_addr = str(addr[0])
    message = message.decode(endecode_data)
    calculate = eval(message)
    calculate_to_string = str(calculate)
    print("Status:", status_success_response, " From:", client_addr, " Calculate:", message, " Result:", calculate_to_string)
    result_message = "Result = " + calculate_to_string
    message = result_message.encode(endecode_data)
    ss.sendto(message, addr)

ss.close()