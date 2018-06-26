import bottle

# this is the handler for the default path of the web server

@bottle.route('/')
def home_page():
    return "<html><title></title><body>Hello World\n</body></html>"

@bottle.route('/testpage')
def test_page():
    return "<html><title></title><body>this is a test page</body></html>"

bottle.debug(True)
bottle.run(host='localhost', port=8080)
