import os

def test_logo_path():
    logo_path = os.path.abspath("static/logo.png")
    print(f"Ruta absoluta del logo: {logo_path}")
    if os.path.exists(logo_path):
        print("El archivo del logo existe.")
    else:
        print("El archivo del logo NO existe.")

if __name__ == "__main__":
    test_logo_path()
