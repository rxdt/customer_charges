from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return 'all is wlll'

# Accepts the charge processing results
@app.route('v1/set-charges')
def post_charge_processing_results():
    return


# Retrieves a list of charges, each with an 'Approval' or 'Decline' state
@app.route('/v1/get-charges/<partner_name>')
def get_charge_processing_results(partner_name):
    return
