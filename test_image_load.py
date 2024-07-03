from PIL import Image
import os

def test_image_load():
    logo_path = os.path.abspath("static/logo.png")
    print(f"Ruta del logo: {logo_path}")

    try:
        img = Image.open(logo_path)
        img.verify()  # Verificar que la imagen es válida
        print("La imagen se ha cargado y verificado correctamente.")
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

if __name__ == "__main__":
    test_image_load()
