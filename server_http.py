import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8080))
s.listen(5)


def manejarSolicitud(request):
    lines = request.splitlines()
    lineRequest = lines[0]
    method, route, version = lineRequest.split()
    if route == b'/':
        bodyResponse = """""
            <html>
             <body> 
             <h1>   Welcome motherFucker</h1>
             </body>
               </html>
        """
        responseState = "HTTP/1.1 200 Ok"
    elif route == b'/hola':
        bodyResponse = """""
            <html>
             <body> 
             <h1>   Hola  motherFucker</h1>
             </body>
               </html>
        """
        responseState = "HTTP/1.1 200 Ok"
    else:
        bodyResponse = """""
            <html>
             <body> 
             <h1>   mamaste   </h1>
             </body>
               </html>
        """
        responseState = "HTTP/1.1 404 Not Found"
    response = f"{responseState}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{bodyResponse}"

    return response.encode("utf-8")


while True:
    print("Esperando conexiones")
    (socketCliente, direccion) = s.accept()
    print("Solicitud http recibida")
    request = socketCliente.recv(1024)
    response = manejarSolicitud(request)
    socketCliente.send(response)
    socketCliente.close()
