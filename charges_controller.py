import json
import helpers
import httplib


class ChargesController(object):

    @staticmethod
    def set_charges(data):
        charges = helpers.get_charges_data()

        if helpers.validate_charge_schema(data):
            new_charge_id = len(charges) + 1
            charges[new_charge_id] = data
            with open('customer_charges.json', 'w') as overwritten_file:
                json.dump(charges, overwritten_file)

            return helpers.get_response('charge with id {} was stored'.format(str(new_charge_id)),
                                        httplib.CREATED)

        else:
            return helpers.get_response('Charge not stored - there are schema errors in your json - check documentation for help',
                                        httplib.BAD_REQUEST)
