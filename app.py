from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formularionotas', methods=['GET', 'POST'])
def formulario1():
    resultado = None
    promedio = None
    if request.method == 'POST':
        try:
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            if not (10 <= nota1 <= 70):
                flash('Nota 1 debe estar entre 10 y 70')
            elif not (10 <= nota2 <= 70):
                flash('Nota 2 debe estar entre 10 y 70')
            elif not (10 <= nota3 <= 70):
                flash('Nota 3 debe estar entre 10 y 70')
            elif not (0 <= asistencia <= 100):
                flash('Asistencia debe estar entre 0 y 100')
            else:
                promedio = (nota1 + nota2 + nota3) / 3
                if promedio >= 40 and asistencia >= 75:
                    resultado = 'APROBADO'
                else:
                    resultado = 'REPROBADO'
        except ValueError:
            flash('Por favor, ingrese valores numéricos válidos')

    return render_template('formularionotas.html', promedio=promedio, resultado=resultado)

@app.route('/formularionombres', methods=['GET', 'POST'])
def formulario2():
    nombre_mayor = None
    longitud_mayor = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        longitud_mayor = len(nombre_mayor)

    return render_template('formularionombres.html', nombre_mayor=nombre_mayor, longitud_mayor=longitud_mayor)

if __name__ == '__main__':
    app.run(debug=True)
