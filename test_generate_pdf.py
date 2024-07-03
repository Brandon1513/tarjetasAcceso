from generate_pdf import create_pdf

# Datos de prueba
name = "John Doe"
email = "john.doe@example.com"
message = "This is a test message."

# Generar el PDF
pdf_buffer = create_pdf(name, email, message)

# Guardar el PDF en un archivo para verificar
with open("test_output.pdf", "wb") as f:
    f.write(pdf_buffer.getbuffer())

print("PDF generado con éxito.")
