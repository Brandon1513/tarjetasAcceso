from flask import Flask, request, render_template, send_file
from generate_pdf import create_pdf
import io

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf_route():
    name = request.form['name']
    puesto = request.form['puesto']
    departamento = request.form['departamento']
    plastico = request.form['plastico']
    referencia = request.form['referencia']
    fecha = request.form['fecha']
    
    pdf_buffer = create_pdf(name,puesto, departamento, plastico, referencia, fecha)
    
    return send_file(
        io.BytesIO(pdf_buffer.getvalue()), 
        as_attachment=True, 
        download_name='formulario.pdf', 
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
