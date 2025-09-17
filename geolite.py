from geolite2 import geolite2
import socket

ip = socket.gethostbyname("www.google.com")
lector = geolite2.reader()
respuesta = lector.get(ip)
print(respuesta)
