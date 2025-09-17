import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostObjetivo = "www.example.com"
portObjetivo = 80
s.connect((hostObjetivo, portObjetivo))
request = f"GET / HTTP 1.1\r\nHost: {hostObjetivo}\r\n\r\n"
s.send(request.encode())

data = s.recv(5000)
response = data.decode("utf-8").splitlines()

print("HEADERS")

print("\n".join(response[:response.index("")]))
print("\n".join(response[response.index("") + 1:]))

s.close()
