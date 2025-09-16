import socket
from threading import *


def escanear(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((host, port))
        print(f"tcp: ABIERTO {port}")
    except Exception as error:
        print(error)
        print(f"tcp: CERRADO {port}")
    finally:
        s.close()


def portScan(host, ports):
    try:
        ip = socket.gethostbyname(host)
    except:
        print(f"No fue posible obtener datos de host: {host}")
        return
    try:
        name = socket.gethostbyaddr(ip)
        print(f"\n Resultados para host {name[0]}: ")

    except:
        print(f"No fue posible obtener datos de host: {host}")
    for port in ports:
        t = Thread(target=escanear, args=(ip, int(port)))
        t.start()


def main(host, ports):
    ports = ports.split(",")
    if host == None or ports == None:
        exit(0)
    else:
        portScan(host, ports)


if __name__ == "__main__":
    host = input("Escribe el dominio o direccion ip: ")
    ports = input("Escribe los puertos separados por coma: ")
    main(host, ports)
