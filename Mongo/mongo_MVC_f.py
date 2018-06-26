from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	mythings = ['apple','orange','banana','peach']
	return render_template("hello_world_f.html", **{"username":"Data Exploitation", "things":mythings})

app.debug = 'True'
app.run(host='localhost', port=8080)
