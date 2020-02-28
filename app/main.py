from flask import Flask,request, jsonify
from flask_mysqldb import MySQL
import random

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'main'

mysql = MySQL(app)


@app.route('/echo', methods = ['GET','POST'])
def msg():
	try:
		message = request.get_json()
		ident = message["id"]
		name = message["name"]
		cur = mysql.connection.cursor()
		cur.execute(f"INSERT INTO employees VALUES (\'{ident}\', \'{name}\')")
		mysql.connection.commit()
		cur.close()
		return jsonify({"status": "ok"}, {"msg":f'{message}'})
	except:
		return jsonify({"status": "error"})
		

@app.route("/random", methods = ['GET'])
def rand():
	ran_num = random.randint(0,100)
	return jsonify({"status": "ok"}, {"number":f'{ran_num}'})


@app.route('/list', methods = ['GET'])
def table():
	cur = mysql.connection.cursor()
	cur.execute('SELECT * FROM employees')
	fetchdata = jsonify(cur.fetchall())
	cur.close()
	return fetchdata


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=False)
