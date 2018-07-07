from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') 
def index():
   return render_template('index.html')
   


# adding another route
#@app.route('/whereami')
#def whereami():
#   return 'Cape Coast !!'
# type http://127.0.0.1:5000/whereami in browser to see change

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')

