import socket
import time
import threading


class Servidor(object):

    def __init__(self):
        self.host = "192.168.100.9"
        self.port = 8080
        self.socket = None
        self.clients = []

    def createServer(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
            print("Server iniciado")
            return True
        except socket.error as error:
            print("No se ha podido crear el socket", error)
            time.sleep(5)
            self.createServer()

    def iniciarServidor(self):
        while True:
            try:
                print("Servidor: Esperando nueva conexion")
                socketCliente, direccion = self.socket.accept()

                nombreCliente = socketCliente.recv(1024).decode('utf-8')
                print('{} {} conectado '.format(nombreCliente, direccion))
                direccionCliente = direccion + (nombreCliente,)
                self.clientes.append((socketCliente, direccionCliente))

            except socket.error as e:
                print("Error aceptando la conexion " + str(e))

    def enviarComandos(self, cliente):
        cmd = 'iniciar'
        while True:
            cliente.send(cmd.encode())
            if cmd == 'terminar':
                break
            respuesta = str(cliente.recv(1024), "utf-8")
            print(respuesta, end="")
            cmd = input()

    def iniciarServidor(servidor):
        servidor.createServer()
        servidor.iniciarServidor()

    def procesarClientes(servidor):
        while True:
            if not servidor.clientes:
                print('.', end="")
                time.sleep(1)
                continue
            print()
            for i, infoCliente in enumerate(servidor.clientes):
                print(i, infoCliente[1])
            cmd = input('Selecciona el cliente : ')
            if cmd == 'r':
                continue
            infoCliente = servidor.clientes[int(cmd)]
            servidor.enviarComandos(infoCliente[0])
