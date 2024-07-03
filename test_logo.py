from reportlab.pdfgen import canvas
import os
import io

def test_logo():
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    width, height = 595.27, 841.89  # A4 size in points

    # Obtener la ruta absoluta del logo
    logo_path = os.path.abspath("static/logo.png")
    print(f"Ruta del logo: {logo_path}")  # Imprimir la ruta del logo para depuración
    
    if os.path.exists(logo_path):
        try:
            # Intentar dibujar la imagen en el PDF
            p.drawImage(logo_path, 40, height - 60, width=120, preserveAspectRatio=True, mask='auto')
            print("Logo cargado correctamente.")
        except Exception as e:
            print(f"Error al cargar el logo: {e}")
            p.drawString(40, height - 60, f"Error al cargar el logo: {e}")
    else:
        print("Logo no encontrado.")
        p.drawString(40, height - 60, "Logo no encontrado.")
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    with open("test_logo_output.pdf", "wb") as f:
        f.write(buffer.getbuffer())
    print("PDF generado con éxito.")

if __name__ == "__main__":
    test_logo()
