from app import app
from flask import Flask
from flask import render_template

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Hello, World"
    return render_template('index.html', message=message)

# run the application
if __name__ == "__main__":
    app.run(debug=True)