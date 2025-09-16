import socket

ip = "127.0.0.1"
port_list = [20, 22, 23, 80, 135, 445, 8080,
             3000, 4200, 5173, 3001, 3002, 4001]


for port in port_list:
    # PUERTO TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(port, ":", "ABIERTO")
    else:
        print(port, ":", "CERRADO")
    # cerrar la conexion del puerto
    s.close()
