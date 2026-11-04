from pathlib import Path
from pix2text import Pix2Text

# Obtener la ruta de la imagen
BASE_DIR = Path(__file__).resolve().parent
RUTA_IMAGEN = BASE_DIR.parent / "imagenes" / "frac_6.png"

# Comprobar la imagen seleccionada
print("Imagen seleccionada:", RUTA_IMAGEN)
print("¿Existe el archivo?:", RUTA_IMAGEN.exists())
print("Tamaño del archivo:", RUTA_IMAGEN.stat().st_size, "bytes")

# Inicializar el modelo
print("Inicializando Pix2Text...")
modelo = Pix2Text()

# Procesar la imagen
print("Procesando imagen...")
resultado = modelo.recognize_text_formula(
    str(RUTA_IMAGEN),
    return_text=True
)

# Mostrar el resultado
print("Resultado del reconocimiento:")
print(resultado)