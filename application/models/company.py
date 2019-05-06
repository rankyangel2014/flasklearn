from database import db
from marshmallow import Schema, fields, ValidationError


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Company %r>' % self.name


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class CompanySchema(Schema):
    id = fields.Int(dumpy_only=True)
    name = fields.Str(required=True, validate=must_not_be_blank)
    age = fields.Int(required=True, validate=must_not_be_blank)
    address = fields.Str(required=True, validate=must_not_be_blank)
