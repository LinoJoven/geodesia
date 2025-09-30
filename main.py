# main.py

# Imports de nuestras funciones geodésicas
from geodesy.calculos import calcular_arco_meridiano, calcular_arco_paralelo
from geodesy.transformacion import transformar_con_helmert

# Constantes (parámetros para la transformación)
PARAMETROS_BOGOTA_A_MAGNA = {
    "tx": 307.0, "ty": 304.0, "tz": -318.0, # Traslaciones en metros
    "rx": -0.8, "ry": -1.3, "rz": -1.0,    # Rotaciones en arc-segundos
    "s": 5.7                            # Factor de escala en ppm (partes por millón)
}

def main_menu():
    """Muestra el menú principal y maneja la lógica del programa."""
    while True:
        print("\n--- CALCULADORA GEODÉSICA PROFESIONAL ---")
        print("1. Calcular longitud de arco de meridiano (GRS80)")
        print("2. Calcular longitud de arco de paralelo (SIRGAS/GRS80)")
        print("3. Transformación de Helmert (Bogotá a MAGNA-SIRGAS)")
        print("4. Salir")
        
        choice = input("Selecciona una opción: ")
        
        if choice == '1':
            try:
                print("\n--- Cálculo de Arco de Meridiano ---")
                lat1 = float(input("Ingresa la latitud inicial (grados): "))
                lat2 = float(input("Ingresa la latitud final (grados): "))

                # --- Validación de entradas ---
                if not (-90 <= lat1 <= 90 and -90 <= lat2 <= 90):
                    print("❌ Error: La latitud debe estar entre -90 y 90 grados.")
                    continue # Vuelve al inicio del menú

                distancia = calcular_arco_meridiano(lat1, lat2)
                print(f"\n✅ La distancia es: {distancia:,.3f} metros")
            except ValueError:
                print("❌ Error: Debes ingresar un número válido.")
            except Exception as e:
                print(f"❌ Ocurrió un error inesperado: {e}")

        elif choice == '2':
            try:
                print("\n--- Cálculo de Arco de Paralelo ---")
                lat = float(input("Ingresa la latitud del paralelo (grados): "))
                lon1 = float(input("Ingresa la longitud inicial (grados): "))
                lon2 = float(input("Ingresa la longitud final (grados): "))

                # --- Validación de entradas ---
                if not (-90 <= lat <= 90):
                    print("❌ Error: La latitud debe estar entre -90 y 90 grados.")
                    continue
                if not (-180 <= lon1 <= 180 and -180 <= lon2 <= 180):
                    print("❌ Error: La longitud debe estar entre -180 y 180 grados.")
                    continue

                distancia = calcular_arco_paralelo(lat, lon1, lon2)
                print(f"\n✅ La distancia es: {distancia:,.3f} metros")
            except ValueError:
                print("❌ Error: Debes ingresar un número válido.")
            except Exception as e:
                print(f"❌ Ocurrió un error inesperado: {e}")
        
        elif choice == '3':
            try:
                print("\n--- Transformación de Helmert (Datum Bogotá -> MAGNA-SIRGAS) ---")
                print("Introduce las coordenadas en el sistema antiguo (Datum Bogotá, Elipsoide Bessel).")
                lat = float(input("Ingresa la latitud (grados): "))
                lon = float(input("Ingresa la longitud (grados): "))
                h = float(input("Ingresa la altura elipsoidal (metros): "))

                # --- Validación de entradas ---
                if not (-90 <= lat <= 90):
                    print("❌ Error: La latitud debe estar entre -90 y 90 grados.")
                    continue
                if not (-180 <= lon <= 180):
                    print("❌ Error: La longitud debe estar entre -180 y 180 grados.")
                    continue

                lat_nueva, lon_nueva, h_nueva = transformar_con_helmert(
                    lat, lon, h, 
                    PARAMETROS_BOGOTA_A_MAGNA, 
                    "BESSEL_1841", 
                    "GRS80"
                )
                
                print("\n✅ Coordenadas transformadas a MAGNA-SIRGAS (GRS80):")
                print(f"   Nueva Latitud: {lat_nueva:.8f}")
                print(f"   Nueva Longitud: {lon_nueva:.8f}")
                print(f"   Nueva Altura: {h_nueva:.3f} metros")
            except ValueError:
                print("❌ Error: Debes ingresar un número válido.")
            except Exception as e:
                print(f"❌ Ocurrió un error inesperado: {e}")

        elif choice == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("❌ Error: Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main_menu()
