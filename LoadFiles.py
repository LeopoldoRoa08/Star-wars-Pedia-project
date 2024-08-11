import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def cargar_info(url):
        # Crear una solicitud con encabezados personalizados
        req = Request(url, headers={'User-Agent': 'Windows NT 10.0; Win64; x64'})
        response = urlopen(req)
        data_json = json.loads(response.read())
        return data_json
  

# Ejemplo de uso
url = "https://www.swapi.tech/api/"
datos = cargar_info(url)

if datos:
    print(datos)
else:
    print("No se pudieron cargar los datos.")
