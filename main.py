import csv
# -----------------------------------------------

def sin_tildes(texto):
    reemplazos = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    texto_mod = texto.lower()
    for a, b in reemplazos:
        texto_mod = texto_mod.replace(a, b)
    return texto_mod

def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                fila['poblacion'] = int(fila['poblacion'])
                fila['superficie'] = int(fila['superficie'])
                paises.append(fila)
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'.")
    except ValueError:
        print("Hay un problema con los carácteres de los números en el CSV.")
    return paises

def guardar_paises(paises, nombre_archivo):
    try:
        with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
    except Exception as e:
        print(f"Error al guardar los datos en el archivo: {e}")

# --- Funciones interactivas ---

def agregar_pais(paises, archivo_datos):
    print("\n--- Agregar Nuevo País ---")

    while True:
        nombre = input("Nombre (o 0 para cancelar): ").strip().title()
        if nombre == '0':
            return
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
        elif not nombre.replace(" ", "").isalpha():
            print("Error: El nombre solo puede contener letras.")
        else:
            break
    while True:
        continente = input("Continente: ").strip().title()
        if not continente:
            print("Error: El continente no puede estar vacío.")
        elif not continente.replace(" ", "").isalpha():
            print("Error: El continente solo puede contener letras.")
        else:
            break
    while True:
        try:
            poblacion = int(input("Población: "))
            superficie = int(input("Superficie: "))
            if poblacion <= 0 or superficie <= 0:
                print("Error: La población y la superficie no pueden ser números negativos.")
            else:
                break
        except ValueError:
            print("Error: La población y la superficie deben ser números enteros positivos.")

    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    paises.append(nuevo_pais)
    guardar_paises(paises, archivo_datos)
    print(f"Éxito al añadir {nombre} al sistema.")

def actualizar_pais(paises, archivo_datos):
    print("\n--- Actualizar Datos de un País ---")
    busqueda = sin_tildes(input("Ingrese el nombre del país que desea actualizar (o 0 para Cancelar): ").strip())

    if busqueda == '0':
        return

    for pais in paises:
        if sin_tildes(pais['nombre']) == busqueda:
            print(f"País encontrado: {pais['nombre']} | Continente: {pais['continente']} | Población actual: {pais['poblacion']} | Superficie: {pais['superficie']}")

            while True:
                try:
                    nueva_pob = int(input("Nueva población: "))
                    nueva_sup = int(input("Nueva superficie en km2: "))
                    if nueva_pob <= 0 or nueva_sup <= 0:
                        print("Error: Los valores actualizados no pueden ser negativos ni 0.")
                    else:
                        pais['poblacion'] = nueva_pob
                        pais['superficie'] = nueva_sup
                        guardar_paises(paises, archivo_datos)
                        print("Datos actualizados correctamente.")
                        return
                except ValueError:
                    print("Error: Debe ingresar números enteros positivos.")
    print("Error: País no encontrado. Asegurese de escribir el nombre completo.")

def buscar_pais(paises):
    print("\n--- Buscar País ---")
    busqueda = sin_tildes(input("Ingrese el nombre del país: ").strip())
    resultados = [p for p in paises if busqueda in sin_tildes(p['nombre'])]
    if resultados:
        print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
        for p in resultados:
            print(f"- {p['nombre']} -> {p['continente']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km2")
    else:
        print("No se encontraron países que coincidan con la búsqueda.")

def filtrar_paises(paises):
    print("\n--- Filtrar Países ---")
    print("1- Por continente")
    print("2- Por rango de población")
    print("3- Por rango de superficie")
    while True:
        opcion = input("Seleccione un criterio de filtro [1-3] (o 0 para Cancelar): ")
        if opcion in ['0', '1', '2', '3']:
            break
        print("Opción inválida. Intente de nuevo.")

    if opcion == '0':
        return
    
    resultados = []

    if opcion == "1":
        cont = sin_tildes(input("Ingrese el continente: ").strip())
        resultados = [p for p in paises if sin_tildes(p['continente']) == cont]
    elif opcion == "2":
        while True:
            try:
                min_pob = int(input("Población mínima: "))
                max_pob = int(input("Población máxima: "))
                if min_pob < 0 or max_pob < 0:
                    print("Error: Los límites no pueden ser negativos.")
                elif max_pob < min_pob:
                    print("Error: La población máxima no puede ser menor que la mínima.")
                else:
                    resultados = [p for p in paises if min_pob <= p['poblacion'] <= max_pob]
                    break
            except ValueError:
                print("Error: Los límites deben ser numéricos.")
    elif opcion == "3":
        while True:
            try:
                min_sup = int(input("Superficie mínima: "))
                max_sup = int(input("Superficie máxima: "))
                if min_sup < 0 or max_sup < 0:
                    print("Error: Los límites no pueden ser negativos.")
                elif max_sup < min_sup:
                    print("Error: La superficie máxima no puede ser menor que la mínima.")
                else:
                    resultados = [p for p in paises if min_sup <= p['superficie'] <= max_sup]
                    break
            except ValueError:
                print("Error: Los límites deben ser numéricos.")
    else:
        print("Opción inválida.")
        return

    if resultados:
        print(f"\nResultados del filtro ({len(resultados)} países): ")
        for p in resultados:
            print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km2")
    else:
        print("Ningún país coincide con los filtros aplicados.")

def ordenar_paises(paises):
    print("\n--- Ordenar Lista de Países ---")
    print("1- Por nombre")
    print("2- Por población")
    print("3- Por superficie")
    while True:
        criterio = input("Elija el criterio del órden [1-3] (o 0 para Cancelar): ")
        if criterio in ['0', '1', '2', '3']:
            break
        print("Opción inválida.")

    if criterio == '0':
        return

    while True:
        orden = input("Ingrese una opción [A] Orden Ascendente | [D] Orden Descendente: ").strip().lower()
        if orden in ['a', 'd']:
            break
        print("Error: Opción Inválida. Debe ingresar 'A' o 'D'.")

    reversa = True if orden == "d" else False

    if criterio == "1":
        paises.sort(key=lambda x: x['nombre'], reverse=reversa)
    elif criterio == "2":
        paises.sort(key=lambda x: x['poblacion'], reverse=reversa)
    elif criterio == "3":
        paises.sort(key=lambda x: x['superficie'], reverse=reversa)

    print("\nLista ordenada exitosamente. Vista previa de los primeros países ordenados: ")
    for p in paises[:5]:
        print(f"- {p['nombre']} | Poblacion: {p['poblacion']} | Superficie: {p['superficie']}")

def mostrar_estadisticas(paises):
    if not paises:
        print("Error: No hay datos cargados para calcular sus estadísticas.")
        return

    print("\n--- Estadísticas Generales ---")

    # MAYOR Y MENOR POBLACIÓN
    mayor_pob = max(paises, key=lambda x: x['poblacion'])
    menor_pob = min(paises, key=lambda x: x['poblacion'])
    print(f"País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']} Habitantes.)")
    print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']} Habitantes.)")

    # PROMEDIOS
    total_paises = len(paises)
    total_pob = sum(p['poblacion'] for p in paises)
    total_sup = sum(p['superficie'] for p in paises)
    print(f"Promedio de población: {total_pob / total_paises:,.0f} Habitantes.")
    print(f"Promedio de superficie: {total_sup / total_paises:,.0f} km2")

    # CANTIDAD POR CONTINENTE
    conteos_continentes = {}
    for p in paises:
        cont = p['continente']
        conteos_continentes[cont] = conteos_continentes.get(cont, 0) + 1

    print("Cantidad de países por continente:")
    for continente, cantidad in conteos_continentes.items():
        print(f" - {continente}: {cantidad}")

# --- MENÚ ---

def menu():
    archivo_datos = 'paises.csv'
    paises = cargar_paises(archivo_datos)

    if not paises:
        print("Se iniciará el programa sin datos en la lista de países.")

    while True:
        print("\n--- GESTIÓN DE DATOS DE PAÍSES ---")
        print("1- Agregar un país")
        print("2- Actualizar población y superficie")
        print("3- Buscar un país por nombre")
        print("4- Filtrar países por Continente - Población - Superficie")
        print("5- Ordenar países por Nombre - Población - Superficie")
        print("6- Mostrar estadísticas")
        print("7- Salir")

        opcion = input("Seleccione una opción [1-7]: ")

        if opcion == "1":
            agregar_pais(paises, archivo_datos)
        elif opcion == "2":
            actualizar_pais(paises, archivo_datos)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 7.")

# Ejecución

if __name__ == "__main__":
    menu()
