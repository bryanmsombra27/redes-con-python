import socket

# SOCKET TIPO TCP
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# SOCKET TIPO UDP
# s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# obtener la direccion ip de un nombre de dominio
dirIPv4 = socket.gethostbyname("www.google.com")

# obtener todas las direcciones asociadas al dominio
info = socket.gethostbyname_ex("www.google.com")


info2 = socket.getfqdn("www.google.com")

info3 = socket.gethostbyaddr("142.251.218.132")

print(dirIPv4)
print(info)
print(info2)
print(info3)

# INFORMACIOND E LOS PUERTOS
# obtiene el puerto de acuerdo al nombre que se le pasa
info4 = socket.getservbyname("http")
print(info4)

# obtiene el nombre del servicio de cuerdo al puerto que se le pasa
info5 = socket.getservbyport(80)
print(info5)
