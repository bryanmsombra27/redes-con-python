import socket

# GLOBAL PARA TODOS LOS SOCKETS
# socket.setdefaulttimeout(10)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)  # tiempo en segundos
hostObjetivo = "www.example.com"
portObjetivo = 8080


try:
    s.connect((hostObjetivo, portObjetivo))
    request = f"GET / HTTP 1.1\r\nHost: {hostObjetivo}\r\n\r\n"
    s.send(request.encode())
    data = s.recv(5000)
    print(data, "DATOS QUESO")
except socket.timeout:
    print("Operacion de red supero el tiempo limite de espera")
except socket.gaierror as e:
    print(f"Error en la resolucion del nombre del host: {e}")
except socket.error as e:
    print(f"Error en el socket: {e}")
finally:
    s.close()
