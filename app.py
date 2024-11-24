from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario1', methods=['GET', 'POST'])
def formulario1():
    nombre = None
    total_sin_descuento = 0
    total_con_descuento = 0

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

    return render_template('formulario1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento)

@app.route('/formulario2', methods=['GET', 'POST'])
def formulario2():
    mensaje = None
    usuarios = {
        'juan': 'admin',
        'pepe': 'user'
    }

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == 'juan':
                mensaje = "Bienvenido administrador juan"
            elif usuario == 'pepe':
                mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrecta"

    return render_template('formulario2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
