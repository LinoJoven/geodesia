# geodesy/elipsoide.py

ELLIPSOIDS = {
    "GRS80": {"a": 6378137.0, "f": 1 / 298.257222101},
    "WGS84": {"a": 6378137.0, "f": 1 / 298.257223563},
    "BESSEL_1841": {"a": 6377397.155, "f": 1 / 299.1528128}
}

def get_ellipsoid(name="WGS84"):
    if name.upper() in ELLIPSOIDS:
        return ELLIPSOIDS[name.upper()]
    else:
        raise ValueError(f"Elipsoide '{name}' no se encuentra definido.")