from flask import Blueprint, jsonify
from application.models.company import Company, CompanySchema


first = Blueprint('first', __name__, url_prefix='/first')

company_schema = CompanySchema()
companys_schema = CompanySchema(many=True)


@first.route('/')
def getCompanyList():
    list = Company.query.all()
    result = companys_schema.dump(list)
    return jsonify(result)


@first.route('/<int:id>')
def getCompanyById(id):
    company = Company.query.get(id)
    result = company_schema.dump(company)
    return jsonify(result)
