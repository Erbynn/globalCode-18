from flask import Flask
app = Flask(__name__)

@app.route('/') # help runs files associating anotation with url(/) 
def index():
   return 'Hello world, this is my first webserver app'
# type http://127.0.0.1:5000 into the url to print the fxn


# adding another route
@app.route('/whereami')
def whereami():
   return 'Cape Coast !!'
# type http://127.0.0.1:5000/whereami in browser to see changes


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')

# host 0.0.0.0 allow it takes diff host given to it
# http://127.0.0.1:5000 ....difault port number is 5000

