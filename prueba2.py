import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "4mDiNy2sj3smSFacOf4ECKb7Wlf0Gjnu"

while True:
    # Pedir datos al usuario
    orig = input("\nIngrese la ciudad de origen (o 'q' para salir): ")
    if orig.lower() == "q":
        print("Saliendo del programa.")
        break

    dest = input("Ingrese la ciudad de destino (o 'q' para salir): ")
    if dest.lower() == "q":
        print("Saliendo del programa.")
        break

    # Agregar país para mejorar precisión
    orig += ", Argentina"
    dest += ", Argentina"

    # Construir URL
    url = main_api + urllib.parse.urlencode({
        "key": key,
        "from": orig,
        "to": dest
    })

    # Obtener respuesta
    response = requests.get(url)
    json_data = response.json()

    # Validar y procesar
    if json_data["info"]["statuscode"] == 0:
        distance_miles = json_data["route"]["distance"]
        distance_km = distance_miles * 1.60934
        tiempo_formateado = json_data["route"]["formattedTime"]
        combustible_estimado = distance_km / 13

        print(f"\nDistancia desde {orig} hasta {dest}: {distance_km:.2f} km")
        print(f"Duración aproximada del viaje: {tiempo_formateado} (horas:minutos:segundos)")
        print(f"Combustible estimado (13 km por litro): {combustible_estimado:.2f} litros")

        # Imprimir narrativa del viaje
        print("\nNarrativa del viaje:")
        for paso in json_data["route"]["legs"][0]["maneuvers"]:
            print(" -", paso["narrative"])
    else:
        print("\nError en la solicitud:")
        print(json_data["info"]["messages"])