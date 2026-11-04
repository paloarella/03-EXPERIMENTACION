from pathlib import Path
from PIL import Image
from pix2tex.cli import LatexOCR

# Obtener la ubicación de este archivo
BASE_DIR = Path(__file__).resolve().parent

# Ubicación de la imagen de prueba
RUTA_IMAGEN = BASE_DIR.parent / "imagenes" / "frac_7.png"

# Cargar el modelo
modelo = LatexOCR()

# Abrir la imagen
imagen = Image.open(RUTA_IMAGEN).convert("RGB")

# Reconocer la expresión matemática
latex = modelo(imagen)
print("Expresión reconocida:")
print(latex)