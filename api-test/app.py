from flask import Flask

app = Flask(__name__)

@app.get("/test") 
def home():
    return "Hello, Flask!"

@app.get("/aaa") 
def test(): 
	return {"msg": "Hello World!"}

