from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario1')
def formulario1():
    return render_template('formulario1.html')

@app.route('/formulario2')
def formulario2():
    return render_template('formulario2.html')

if __name__ == '__main__':
    app.run(debug=True)
