# main.py

# 👇 1. Importa la nueva función junto a la anterior
from geodesy.calculos import calcular_arco_meridiano, calcular_arco_paralelo

def main_menu():
    while True:
        # 👇 2. Añade la nueva opción al menú
        print("\n--- CALCULADORA GEODÉSICA PROFESIONAL ---")
        print("1. Calcular longitud de arco de meridiano (GRS80)")
        print("2. Calcular longitud de arco de paralelo (SIRGAS/GRS80)")
        print("3. Salir")
        
        choice = input("Selecciona una opción: ")
        
        if choice == '1':
            try:
                print("\n--- Cálculo de Arco de Meridiano ---")
                lat1 = float(input("Ingresa la latitud inicial (grados): "))
                lat2 = float(input("Ingresa la latitud final (grados): "))
                distancia = calcular_arco_meridiano(lat1, lat2, "GRS80")
                print(f"\n✅ La distancia es: {distancia:,.3f} metros")
            except ValueError:
                print("❌ Error: Debes ingresar un número válido.")
            except Exception as e:
                print(f"❌ Ocurrió un error inesperado: {e}")

        # 👇 3. Añade el bloque de lógica para la opción 2
        elif choice == '2':
            try:
                print("\n--- Cálculo de Arco de Paralelo ---")
                lat = float(input("Ingresa la latitud del paralelo (grados): "))
                lon1 = float(input("Ingresa la longitud inicial (grados): "))
                lon2 = float(input("Ingresa la longitud final (grados): "))
                distancia = calcular_arco_paralelo(lat, lon1, lon2, "GRS80")
                print(f"\n✅ La distancia es: {distancia:,.3f} metros")
            except ValueError:
                print("❌ Error: Debes ingresar un número válido.")
            except Exception as e:
                print(f"❌ Ocurrió un error inesperado: {e}")
            
        elif choice == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
            
        else:
            print("❌ Error: Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main_menu()