from geoip2 import database
import socket
lector = database.Reader("GeoLite2-City.mmdb")
ip = socket.gethostbyname("www.google.com")
respuestaGeoIP = lector.city(ip)
print(respuestaGeoIP)
