from flask import Flask
app = Flask(__name__)

# this is the handler for the default path of the web server

@app.route('/')
def home_page():
    return "Hello World\n"

@app.route('/testpage')
def test_page():
    return "this is a test page"

if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost', port=8080)


