import socket

host = "127.0.0.1"
port = 8080
socket.setdefaulttimeout(5)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(bytes("Encender iluminacion", "utf-8"))
    data = s.recv(1024)
    print("DATOS RECIBIDOS CLIENTE: ", data.decode())

except socket.errno as err:
    print("socket eror", err)
finally:
    s.close()
