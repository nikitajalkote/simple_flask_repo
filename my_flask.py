# import add
# Inmporting Flask
from flask import Flask
# Create the server
app=Flask(__name__)
####
@app.route("/")
def hello():
    return "Hello World"
if (__name__ == "__main__"):
   app.run(host='3.138.137.23', port=5000, debug=True)
