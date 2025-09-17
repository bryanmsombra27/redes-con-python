import socket

host = "127.0.0.1"
port = 8080
socket.setdefaulttimeout(100)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)


def encenderLed():
    print("Led encendido")


def apagarLed():
    print("Led apagado")


while True:
    try:
        client, address = s.accept()
        print("Conexion desde: ", address)
        data = client.recv(1024)
        print("Datos recibidos", data.decode())

        if data == b"Encender iluminacion":
            client.send(bytes("Encendiendo iluminacion\n", "utf-8"))
            encenderLed()
        elif data == b"Apagar iluminacion":
            client.send(bytes("Apagando iluminacion\n", "utf-8"))
            apagarLed()
        client.close()

    except socket.timeout:
        print("La operacion de red supero el tiempo de espera")
