from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return 'all is wlll'

# Accepts the charge processing results
@app.route('/set-charges')
def post_charge_processing_results():
    return
