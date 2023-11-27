from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/empleados'
db = SQLAlchemy(app)

class Empleados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    foto = db.Column(db.String(255))

@app.route('/')
def index():

    nuevo_empleado = Empleados(nombre='Juan', correo='juan@email.com', foto='fotodejuan.jpg')
    db.session.add(nuevo_empleado)
    db.session.commit()

    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run(debug=True)