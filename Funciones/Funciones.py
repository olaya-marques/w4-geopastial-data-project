def isnull(x):
    """ 
    Esta función muestra la suma de todos los NaNs ordenados de mayor a menor
    """
    return x.isnull().sum().sort_values(ascending = False)

def comprobacion_duplicados (x):
     """ 
     Esta función muestra el número de datos repetidos
     """
    repetidos = list(unique_everseen(duplicates(x)))
    return len(repetidos)

def geocode(direccion): 
    """
    Saca las coordenadas de una dirección
    """
    data = requests.get(f"https://geocode.xyz/{direccion}?json=1").json()
    try:
        return {
            "type":"Point",
            "coordinates":  [float(data["latt"]), float(data["longt"])]
        }
    except:
        return data

def distancia(lat1, lon1, lat2, lon2):
    """
    Calcula mediante la fórmula de Harvesine la distancia entre dos puntos, dándole la latitud y la longitud de ambos.
    """
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia