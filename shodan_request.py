import requests
import socket

ipHost = input("Introduce el nombre del host o su IP: ")
apikey = "nYEaxsYKpk4XGTGS0HarM8CQWGzSR8Xk"


def shodanInfo(ip):
    try:
        result = requests.get(
            f"https://api.shodan.io/shodan/host/{socket.gethostbyname(ip)}?key={apikey}").json()
    except Exception as error:
        result = {"error": "No esta disponible la informacion"}
    return result


def extraerServicios(result):
    servicios = []
    for servicio in result.get("data", []):
        port = servicio.get("port")
        protocol = servicio.get("transport")
        banner = servicio.get("data", "").strip()
        servicios.append({
            "puerto": port,
            "protocolo": protocol,
            "banner": banner,
        })
    return servicios


resultados = shodanInfo(ipHost)
servicios = extraerServicios(resultados)


print("SERVICIOS: ", servicios)
