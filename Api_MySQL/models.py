from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Terms(db.Model):
    __tablename__ = "terms"
    terms_id = db.Column(db.Integer, primary_key=True)
    terms_description = db.Column(db.String(50), nullable=False)
    terms_due_days = db.Column(db.Integer, nullable=False)


class Invoices (db.Model):
    tablename = "invoices"

    invoice_id = db.Column(db.Integer, primary_key=True)
    # vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.vendor_id'), nullable=False)
    invoice_number = db.Column(db.Integer, nullable=False)
    invoice_date = db.Column(db.DateTime, nullable=False)
    invoice_total = db.Column(db.Float, nullable=False)
    payment_total = db.Column(db.Float, nullable=False, default=0.00)
    credit_total  = db.Column(db.Float, nullable=False, default=0.00)
    terms_id = db.Column(db.Integer, db.ForeignKey('terms.term_id'), nullable=False)
    invoice_due_date = db.Column(db.DateTime, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False, default=None)

class Vendors(db.Model):
    tablename = "vendors"
    #logic here

class VendorContacts(db.Model):
    tablename = "vendor_contacts"
    #logic here

class InvoiceArchive(db.Model):
    tablename = "invoice_archive"
    #logic here

class GeneralLedgerArchive(db.Model):
    tablename = "general_ledger_archive"
    #logic here
    