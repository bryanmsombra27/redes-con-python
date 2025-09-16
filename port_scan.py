import socket


def portList(ip, ports):

    # ip = "127.0.0.1"
    # ports = [20, 22, 23, 80, 135, 445, 8080,
    #             3000, 4200, 5173, 3001, 3002, 4001]

    for port in ports:
        # PUERTO TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(port, ":", "ABIERTO")
        else:
            print(port, ":", "CERRADO")
        # cerrar la conexion del puerto
        s.close()


portList("www.google.com", [80, 8080, 443, 22, 3000, 4200, 5173, 5432])
