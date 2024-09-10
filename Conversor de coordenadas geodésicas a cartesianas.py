import pandas as pd
from pyproj import Proj, transform

def geodetic_to_utm(latitude, longitude):
    # Definir el sistema de coordenadas geodésicas
    geodetic_proj = Proj(proj='latlong', datum='WGS84')

    # Definir el sistema de coordenadas UTM
    utm_proj = Proj(proj='utm', zone=utm_zone(longitude), datum='WGS84')

    # Convertir coordenadas geodésicas a UTM
    easting, northing = transform(geodetic_proj, utm_proj, longitude, latitude)

    return easting, northing

def utm_zone(longitude):
    # Calcular la zona UTM según la longitud
    zone = int((longitude + 180) / 6) + 1
    return zone

# Cargar datos desde el archivo CSV
file_path = 'Coordenadas geodésicas de MUNICIPIOS Y ALMACÉN DE SEPH.csv'  # Reemplaza con la ruta de tu archivo CSV
df = pd.read_csv(file_path)

# Crear nuevas columnas en el DataFrame para latitud y longitud en UTM
df['Abcisa X'], df['Ordenada Y'] = zip(*df.apply(lambda row: geodetic_to_utm(row['Latitud'], row['Longitud']), axis=1))

# Mostrar la tabla con las columnas de latitud y longitud en UTM
print("Tabla con coordenadas UTM:")
print(df[['Latitud', 'Longitud', 'Abcisa X', 'Ordenada Y']])

# Guardar el DataFrame actualizado en un nuevo archivo CSV
output_file_path = 'Coordenadas cartesianas de MUNICIPIOS Y ALMACÉN DE SEPH.csv'  # Reemplaza con la ruta deseada para el archivo de salida
df.to_csv(output_file_path, index=False)

print(f'\nLos resultados se han guardado en: {output_file_path}')