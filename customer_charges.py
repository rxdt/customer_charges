from flask import Flask, jsonify, request
import json

from partner_controller import PartnersController
from charges_controller import ChargesController


app = Flask(__name__)


@app.route('/health')
def health():
    return 'all is well'


# Accepts the charge processing results
# Returns HTTP code 201 resource created
@app.route('/v1/set-charges', methods=['POST'])
def post_charge_processing_results():
    return ChargesController.set_charges(json.loads(request.get_data()))


# Retrieves a list of charges, each with an 'Approval' or 'Decline' state
# Returns HTTP code 200 OK
@app.route('/v1/get-charges/<partner_name>/<currency>')
def get_charge_processing_results(partner_name, currency):
    partners_customer_charges = PartnersController.get_partners_customer_charges(partner_name, currency)
    return partners_customer_charges
