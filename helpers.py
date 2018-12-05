from flask import jsonify
from cerberus.validator import Validator

import json


SCHEMA = {
    'customerId': {'required': True, 'type': 'integer'},
    'partnerId': {'required': True, 'type': 'integer'},
    'amount': {'required': True, 'type': 'float'},
    'approved': {'required': True, 'type': 'boolean'}
}


CURRENCY_MULTIPLIERS = {
    'USD': 1.00,
    'EUR': 0.881547,
    'MXN': 20.573060,
    'GBP': 1.272358,
    'CAD': 0.746450,
    'JPY': 0.008876,
    'AUD': 0.722337,
    'SGD': 0.729559,
    'CHF': 1.003640
}


ALLOWED_CURRENCIES = CURRENCY_MULTIPLIERS.keys()


def get_currency_multiplier(currency):
    return CURRENCY_MULTIPLIERS.get(currency)


def get_partners_data(partner_name):
    with open('partners.json') as partners_file:
        return json.load(partners_file).get(partner_name.lower())


# values are stored in USD and converted according to currency requested by partner
def get_charges_data():
    with open('customer_charges.json') as charges_file:
        return json.load(charges_file)


def validate_charge_schema(data):
    validator = Validator(SCHEMA)
    return validator.validate(data)


def get_response(message, code=200):
    response = jsonify(message or partners_customer_charges)
    response.status_code = code
    return response
