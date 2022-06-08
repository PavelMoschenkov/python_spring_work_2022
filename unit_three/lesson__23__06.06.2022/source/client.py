# Echo client program
import socket
import base64

HOST = '127.0.0.1'    # The remote host
PORT = 50008          # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'GET car.jpg')
    data = s.recv(1024)
    data_dec = data.decode(encoding="ansi")
    f = open('client_car.jpg', 'w')
    f.write(data_dec)
    f.close()
    # f_data = f.read(udata)
# s.send(f_data)
print('Received', repr(data))