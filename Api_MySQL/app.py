from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Terms , GeneralLedgerArccounts
#Create an instance of the Flask application
app = Flask(__name__)

#Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] \
='mysql+pymysql://root:fongfong@localhost:3306/ap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize the SQLAlchemy extension with the Flask app
db.init_app(app)

@app.get('/terms')
def get_terms():
    t = db.session.query(Terms)\
        .with_entities(Terms.terms_id, Terms.terms_description, Terms.terms_due_days)

    ls=[]
    for v in t:
        te = {
            "id" : v.terms_id,
            "description" : v.terms_description,
            "due_days" : v.terms_due_days
        }
        ls.append(te)
    return ls
#get general ledger account
@app.get('/generalaccounts')
def get_generalaccount():
    t = db.session.query(GeneralLedgerArccounts)\
        .with_entities(GeneralLedgerArccounts.account_number, GeneralLedgerArccounts.account_description).all()

    ls = []
    for v in t:
        # `v` is a tuple, where v[0] is account_number and v[1] is account_description
        te = {
            "account_number": v[0],  # Access the actual value from the tuple
            "description": v[1]      # Access the actual value from the tuple
        }
        ls.append(te)

    # Return the list of dictionaries as a response
    return ls

#Run the Flask app
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000)