# Imports

from aux_pro import Process
from flask import Flask
from flask import jsonify
from flask import render_template
from database import Database
from models import Muestras
import datetime

app = Flask(__name__)
db = Database()
pro = Process()

@app.route('/')
def index():
	if not pro.is_running():
		id=pro.start_process()
	return render_template("index.html")



@app.route('/_get_data/', methods=['POST'])
def _get_data():
	pasos=0
	distancia=0
	calorias=0
	velocidad=0
	last = db.get_last()
	pasos=last.pasos
	distancia=last.distancia
	calorias=last.calorias
	velocidad=last.velocidad
		#last_ten = db.get_last_ten()
	#return render_template('index.html',l=last,t=last_ten,id=idd
	result = {"pasos":pasos,"distancia":distancia,"calorias":calorias,"velocidad":velocidad}
	return jsonify({'data': render_template('response.html', myList=result)})

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8888)
