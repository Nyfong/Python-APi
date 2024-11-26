from flask import Flask

app = Flask(__name__)

@app.get("/test") 
def home():
    return "Hello, Flask!"

#display all companies
@app.get("/companies") 
def test():
	return {"companies": companies}


#creating a company
@app.post("/company")
def create_company():
    new_company = {"name": "KESA", "items":[{"name": "pen","price": 15.99}, {"name": "notebook","price": 20}]}
    companies.append(new_company)
    return new_company, 201

#get company by name
@app.get("/company/<string:name>")
def get_com(name):
    for company in companies:
        if company["name"] == name:
            return company
    return {"msg": "Company not found"}, 404

companies = [
    {
        "name": "ABSARA",
        "items": [
            {
                "name": "pen",
                "price": 15.99
            },
            {
                "name": "book",
                "price": 11
            }
        ]
    }
]
