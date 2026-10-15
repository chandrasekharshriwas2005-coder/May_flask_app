#importing the flusk module in the code
from flask import Flask

#creating an object of the Flask class
app = Flask(__name__)

#using decorator for creating a route for the home page
@app.route('/')
def home():
    return "Welcome to the Home Page! this is pw class"

#calling the main 
if __name__ == '__main__':
    app.run(debug=True)
    
