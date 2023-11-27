from flask import Flask
from flask import render_template
from flaskext.mysql import MySql

app = Flask(__name__)
mysql = MySql()


if __name__ == '__main__':
    app.run(debug=True)

