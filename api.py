from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/teste", methods=["GET"])
def teste():
	response = {"resposta":True}
	return jsonify(response)

@app.route("/api/dobro/<int:numero>")
def dobro(numero):
	response = {"dobro":str(numero * 2)}
	return jsonify(response)

@app.route("/api/metodos",methods=["GET","POST"])
def metodos():
	if request.method == "GET":
		return jsonify({"mensagem":"Endpoint teste", "metodo": request.method})

if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)

