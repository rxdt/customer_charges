from flask import Flask, jsonify
import json
import httplib

app = Flask(__name__)


with open('partners.json') as partners_file:
    PARTNERS_DATA = json.load(partners_file)
with open('customer_charges.json') as charges_file:
    CHARGES_DATA = json.load(charges_file)


@app.route('/health')
def health():
    return 'all is wlll'

# Accepts the charge processing results
@app.route('/v1/set-charges')
def post_charge_processing_results():
    return


# Retrieves a list of charges, each with an 'Approval' or 'Decline' state
@app.route('/v1/get-charges/<partner_name>')
def get_charge_processing_results(partner_name):

    partner_data = PARTNERS_DATA.get(partner_name.lower())
    if not partner_data:
        return 'partner {} does not exist'.format(partner_name)

    partners_customers = partner_data.get('customerIds')
    if not partners_customers:
        return 'partner {} does not have any customers'.format(partner_name)

    partner_id = partner_data['partnerId']
    partners_customer_charges = {}
    for charge_id, values in CHARGES_DATA.iteritems():
        if values['partnerId'] == partner_id:
            partners_customer_charges[charge_id] = values
    if not partners_customer_charges:
        return 'partner {} does not have any charges for its customers'.format(partner_name)

    return jsonify(partners_customer_charges)
