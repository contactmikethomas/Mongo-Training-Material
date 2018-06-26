from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/hello/<name>')
def index(name):
	return render_template_string('<b>Hello {{name}}</b>!', name=name)

if __name__ == '__main__':
	app.run(host='localhost', port=8080)
