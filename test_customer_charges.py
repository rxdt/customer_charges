import httplib
import json
import unittest

from customer_charges import app


class TestEndpointsLogic(unittest.TestCase):

    def test_health_endpoint_returns_ok(self):
        with app.test_client() as tc:
            response = tc.get('/health')
            self.assertEqual(response.data, 'all is well')
            self.assertEqual(response.status_code, httplib.OK)

    def test_get_charges_returns_not_found_when_partner_does_not_exist(self):
        with app.test_client() as tc:
            response = tc.get('/v1/get-charges/bob/mxn')
            self.assertEqual(response.data, '"partner bob does not exist"\n')
            self.assertEqual(response.status_code, httplib.NOT_FOUND)

    def test_get_charges_returns_not_found_when_nonexistent_currency_requested(self):
        with app.test_client() as tc:
            response = tc.get('/v1/get-charges/sprint/mx')
            self.assertEqual(response.data, '"MX is not an applicable currency. Options are: [\'MXN\', \'JPY\', \'USD\', \'AUD\', \'GBP\', \'CAD\', \'CHF\', \'SGD\', \'EUR\']"\n')
            self.assertEqual(response.status_code, httplib.NOT_FOUND)

    def test_get_charges_returns_no_content_when_partner_has_no_customers(self):
        with app.test_client() as tc:
            response = tc.get('/v1/get-charges/comcast/mxn')
            self.assertEqual(response.status_code, httplib.NO_CONTENT)

    def test_get_charges_returns_correct_partners_customer_charges(self):
        with app.test_client() as tc:
            response = tc.get('/v1/get-charges/sprint/mxn')
            self.assertEqual(response.data.replace('\n', '').replace(' ', ''), '{"4":{"amount":187.62630719999999,"approved":true,"customerId":4,"partnerId":2},"5":{"amount":64.18794720000001,"approved":true,"customerId":5,"partnerId":2}}')

    def test_set_charges_does_not_store_empty_payloads(self):
        with app.test_client() as tc:
            response = tc.post('/v1/set-charges', data='{}', content_type='application/json')
            self.assertEqual(response.data, '"Charge not stored - there are schema errors in your json - check documentation for help"\n')
            self.assertEqual(response.status_code, httplib.BAD_REQUEST)

    def test_set_charges_stores_correct_payloads_for_new_charges(self):
        with app.test_client() as tc:
            response = tc.post('/v1/set-charges', data=json.dumps({"customerId":2, "partnerId":2, "amount":2.31, "approved": True}), content_type='application/json')
            self.assertEqual(response.status_code, httplib.CREATED)
            self.assertEqual(response.data, '"charge with id 12 was stored"\n')


if __name__ == '__main__':
    unittest.main()
