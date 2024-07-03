from PIL import Image
import os

def test_image():
    logo_path = os.path.abspath("static/logo.png")
    print(f"Ruta del logo: {logo_path}")  # Imprimir la ruta del logo para depuración
    
    try:
        img = Image.open(logo_path)
        img.show()  # Esto abrirá la imagen usando el visor de imágenes predeterminado
        print("Imagen cargada correctamente.")
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

if __name__ == "__main__":
    test_image()
