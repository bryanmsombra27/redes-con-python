import requests

ip = "8.8.8.8"
print("RESPUESTA HACKERTARGET")
respuesta1 = requests.get(f"https://api.hackertarget.com/geoip/?q={ip}")

lineas = respuesta1.text.split("\n")
for linea in lineas:
    print(linea)

print("-" * 20)

respuesta2 = requests.get(f"https://api.ipbase.com/v1/json/{ip}").json()

for clave, valor in respuesta2.items():
    print(clave, "--->", valor)

print("-" * 20)
