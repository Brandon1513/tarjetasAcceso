from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import os

def create_pdf(name, puesto, departamento, plastico, referencia, fecha):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    logo_path = os.path.abspath("static/Logotipo.png")
    print(f"Ruta del logo: {logo_path}")

    if os.path.exists(logo_path):
        print("El archivo del logo existe.")
        try:
            p.drawImage(logo_path, 40, height - 250, width=90, preserveAspectRatio=True, mask='auto')
            print("Logo cargado correctamente.")
        except Exception as e:
            print(f"Error al cargar el logo: {e}")
            p.drawString(40, height - 60, f"Error al cargar el logo: {e}")
    else:
        print("Logo no encontrado.")
        p.drawString(40, height - 60, "Logo no encontrado.")
    
    p.setFont("Helvetica-Bold", 16)
    p.drawString(240, height - 50, "Tarjetas de Acceso")

    p.setFont("Helvetica", 12)
    p.drawString(370, height - 90 ,f"Guadalajara, jalisco a {fecha}")
    p.drawString(40, height - 160, "Por medio de la presente declaro que me fue entregada por parte de Sistemas la tarjeta de control")
    p.drawString(40, height - 180, "de acceso con los siguientes datos:")        
    p.drawString(40,height - 200, f"Número de plástico: {plastico}")
    p.drawString(40, height - 220, f"Número de referencia: {referencia}")

    p.drawString(40, height - 260, "Así mismo estoy consciente que el uso que le dé a mi tarjeta es totalmente responsabilidad propia y ")
    p.drawString(40, height - 280, "deslindo de cualquier problema legal a Dasavena Gourmet S.A. de C.V. en caso de darle un uso")
    p.drawString(40, height - 300, "no permitido o con algún fin ilegal.")
    p.drawString(40, height - 340, "Así mismo, estoy enterado(a) que, para darle un mejor uso a mi tarjeta, es recomendable que la porte")
    p.drawString(40, height-360,"junto con mi gafe de la empresa, en caso de pérdida o extravío, el costo generado por la reposición")
    p.drawString(40, height -380, "de la tarjeta es de $500 y se descontará directamente de nómina.")
    p.drawString(40,height -420, "También estoy enterado que una vez terminada mi relación laboral con Dasavena Gourmet S.A. ")
    p.drawString(40, height -440, "de C.V., es mi responsabilidad entregar dicha tarjeta al departamento de Sistemas, para realizar su ")
    p.drawString(40,height -460, "baja inmediata.")

    

    # Línea para la firma
    p.line(150, height - 600, 450, height - 600)
    p.drawString(220, height - 620, f"{name}")
    p.drawString(220, height - 640, f"{puesto} // {departamento}")

    p.drawString(210, height- 765, "DASAVENA GOURMET S.A. DE C.V. LAT.")
    p.drawString(100, height -780, "PERIFERICO NORTE #253 INT 15 COL. EL VIGIA C.P. 45140, ZAPOPAN, JAL." )
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer

