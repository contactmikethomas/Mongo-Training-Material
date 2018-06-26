from flask import Flask, render_template, request, redirect, make_response, url_for
app = Flask(__name__)

@app.route('/')
def home_page():
	mythings = ['apple','orange','banana','peach']
	return render_template("hello_world_form_f.html", **{"username":"Data Exploitation", "things":mythings})

@app.route('/favourite_fruit', methods=["POST"])
def favourite_fruit():
	fruit = request.form['fruit']
	if (fruit == None or fruit == ""):
		fruit = "No Fruit Selected"

	response = make_response(redirect(url_for("show_fruit")))
	response.set_cookie("fruit", fruit)
	
	return response

@app.route('/show_fruit')
def show_fruit():
	fruit = request.cookies.get('fruit')

	return render_template('fruit_selection_f.html', **{"fruit":fruit})	

app.debug = "True"
app.run(host='localhost', port=8080)
