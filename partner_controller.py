import helpers
import httplib


class PartnersController(object):

    @staticmethod
    def get_partners_customer_charges(partner_name, currency):
        partner_data = helpers.get_partners_data(partner_name)
        if not partner_data:
            return helpers.get_response('partner {} does not exist'.format(partner_name),
                                        httplib.NOT_FOUND)

        partners_customers = partner_data.get('customerIds')
        if partners_customers == []:
            return helpers.get_response('partner {} does not have any customers'.format(partner_name),
                                        httplib.NO_CONTENT)

        currency = currency.upper()
        if currency not in helpers.ALLOWED_CURRENCIES:
            return helpers.get_response('{} is not an applicable currency. Options are: {}'.format(currency, helpers.ALLOWED_CURRENCIES),
                                        httplib.NOT_FOUND)

        currency_multiplier = helpers.get_currency_multiplier(currency)

        partner_id = partner_data['partnerId']
        partners_customer_charges = {}
        for charge_id, values in helpers.get_charges_data().iteritems():
            if values['partnerId'] == partner_id:
                partners_customer_charges[charge_id] = values
                # currency calculation is not rounded so partners can round themselves, according to their stadards
                partners_customer_charges[charge_id]['amount'] = values['amount'] * currency_multiplier

        if not partners_customer_charges:
            return helpers.get_response('partner {} does not have any charges for its customers'.format(partner_name))

        return helpers.get_response(partners_customer_charges)
