import socket
dominio = input("Ingresa el dominio: ")
try:
    ip = socket.gethostbyname(dominio)
    print("IP:", ip, "n")
    print("Host:", socket.gethostbyaddr(str(ip)), "n")
    print("Nombre cualificado:", socket.getfqdn(dominio))
except socket.error as error:
    print(str(error))
    print("Error de conexion")
