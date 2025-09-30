# geodesy/calculos.py
from pyproj import Geod
from .elipsoide import get_ellipsoid 

def calcular_arco_meridiano(phi1, phi2, ellipsoid_name="GRS80"):
    # ... (esta función ya la tienes) ...
    params = get_ellipsoid(ellipsoid_name)
    geod = Geod(a=params['a'], f=params['f'])
    _, _, distancia = geod.inv(lats1=phi1, lons1=0, lats2=phi2, lons2=0)
    return distancia

# ======== AÑADE ESTA NUEVA FUNCIÓN ========
def calcular_arco_paralelo(phi, lambda1, lambda2, ellipsoid_name="GRS80"):
    """
    Calcula la distancia a lo largo de un paralelo entre dos longitudes.
    (Punto i de la lista)
    
    Args:
        phi (float): Latitud del paralelo en grados decimales.
        lambda1 (float): Longitud inicial en grados decimales.
        lambda2 (float): Longitud final en grados decimales.
        ellipsoid_name (str): Nombre del elipsoide (ej. "GRS80").
        
    Returns:
        float: Distancia en metros.
    """
    params = get_ellipsoid(ellipsoid_name)
    geod = Geod(a=params['a'], f=params['f'])
    
    # Calculamos la distancia entre dos puntos en la misma latitud
    _, _, distancia = geod.inv(lats1=phi, lons1=lambda1, lats2=phi, lons2=lambda2)
    
    return distancia
# ============================================