from flask import Flask

app = Flask(__name__)

@app.get("/test") 

def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()
