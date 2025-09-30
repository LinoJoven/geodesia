# geodesy/transformacion.py
from .elipsoide import get_ellipsoid
import math
import pyproj

def geodetic_to_cartesian(phi, lam, h, ellipsoid_name):
    """Convierte coordenadas geodésicas a cartesianas."""
    params = get_ellipsoid(ellipsoid_name)
    a = params['a']
    f = params['f']
    e2 = 2*f - f**2  # Excentricidad al cuadrado

    # Convertir lat/lon a radianes
    phi_rad = math.radians(phi)
    lam_rad = math.radians(lam)

    # Radio de curvatura en la primera vertical (N)
    N = a / math.sqrt(1 - e2 * math.sin(phi_rad)**2)

    # Calcular coordenadas cartesianas
    X = (N + h) * math.cos(phi_rad) * math.cos(lam_rad)
    Y = (N + h) * math.cos(phi_rad) * math.sin(lam_rad)
    Z = (N * (1 - e2) + h) * math.sin(phi_rad)
    
    return X, Y, Z

def transformar_con_helmert(phi, lam, h, params_helmert, elipsoide_origen, elipsoide_destino):
    """
    Realiza una transformación de Helmert de 7 parámetros.
    (Punto j de la lista)
    """
    # --- 1. Convertir de geodésicas a cartesianas ---
    X, Y, Z = geodetic_to_cartesian(phi, lam, h, elipsoide_origen)

    # --- 2. Aplicar los 7 parámetros de Helmert ---
    # Obtener parámetros
    Tx = params_helmert['tx']  # en metros
    Ty = params_helmert['ty']
    Tz = params_helmert['tz']
    Rx = math.radians(params_helmert['rx'] / 3600)  # de arc-sec a radianes
    Ry = math.radians(params_helmert['ry'] / 3600)
    Rz = math.radians(params_helmert['rz'] / 3600)
    S = params_helmert['s'] / 1_000_000  # de ppm a factor de escala

    # Aplicar la fórmula de transformación (Bursa-Wolf)
    X_destino = X + Tx + S*X - Rz*Y + Ry*Z
    Y_destino = Y + Ty + Rz*X + S*Y - Rx*Z
    Z_destino = Z + Tz - Ry*X + Rx*Y + S*Z

    # --- 3. Convertir de cartesianas de vuelta a geodésicas ---
    # Usaremos pyproj para esta conversión inversa, que es más precisa.
    
    # Definir sistema cartesiano y geodésico de destino
    params_destino = get_ellipsoid(elipsoide_destino)
    crs_cart = pyproj.CRS.from_dict({"proj": "cart", "a": params_destino['a'], "f": params_destino['f']})
    crs_geod = pyproj.CRS.from_dict({"proj": "latlong", "a": params_destino['a'], "f": params_destino['f']})
    
    transformer = pyproj.Transformer.from_crs(crs_cart, crs_geod, always_xy=True)
    
    # pyproj espera (X, Y, Z), devuelve (lon, lat, h)
    lon_destino, lat_destino, h_destino = transformer.transform(X_destino, Y_destino, Z_destino)

    return lat_destino, lon_destino, h_destino