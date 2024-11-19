from flask import Flask
app = Flask(__name__)
@app.get("/test") 
def test(): 
	return {"msg": "Hello World!"}

#i still error