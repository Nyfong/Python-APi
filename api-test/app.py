from flask import Flask , request
from companies import your_small_companies
app = Flask(__name__)

@app.get("/test") 
def home():
    return "Hello, Flask!"

#display all companies
@app.get("/companies") 
def test():
	return {"companies": your_small_companies}


#creating a company
@app.post("/company")
def create_company():
    new_company = {"name": "KESA", "items":[{"name": "pen","price": 15.99}, {"name": "notebook","price": 20}]}
    your_small_companies.append(new_company)
    return new_company, 201

#get company by name
@app.get("/company/<string:name>")
def get_com(name):
    for company in your_small_companies:
        if company["name"] == name:
            return company
    return {"msg": "Company not found"}, 404


#post the item in the company
@app.post("/company/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for company in your_small_companies:
        if company["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            company["items"].append(new_item)
            return new_item, 201
    return {"msg": "Company not found"}, 404


