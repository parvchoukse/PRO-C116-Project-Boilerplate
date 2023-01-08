# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "parv" 
    age = "14"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
app.route('/father')

# define the route to mother webpage
app.route('/mother)

# define the route to friends webpage
app.route(/arpan)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
