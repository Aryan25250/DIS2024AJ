from flask import Flask # Import flask

app = Flask(__name__) # New flask instance

@app.route('/') # Tells flask what URL should trigger the function

def hello_form():
    return "<h1><b>Hello, this is a form!<b></h1>" # Message to display in browser

if __name__ == '__main__':
    app.run(debug=True)