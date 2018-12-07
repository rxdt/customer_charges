
# Customer Charges

__A small Flask app to get customer charges to partners__

Project goals are detailed in the [exercise description](exercise_description.md) in this repo.

## Development

__Run the following commands to install dependencies and to start the app.__

A Makefile contains 'make' commands that install dependencies and spin up the application.
```
$ make install  # sudo may be required
$ make run
```
Check that the application is running and healthy:
```
$ curl http://127.0.0.1:5000/health
all is well
```

__Run tests in the test suite.__
```
make test
```


## API Endpoints

__Retrieve a partner's customer charges with charge IDs as the top level identifiers and in the currency requested__

Each json blob within the response correspondes to a charge ID / a customer's charge and whether their state is 'approved' or 'denied'.
Currency code must be specified as a path parameter. Charge amounts are left with all trailing digits for partner's to round values as they see fit.
Currency code options are: ['MXN', 'JPY', 'USD', 'AUD', 'GBP', 'CAD', 'CHF', 'SGD', 'EUR']

### __Example URI and request__

> GET v1/get-charges/{{partner-name}}/{{currency}}


`$ curl localhost:5000/v1/get-charges/sprint/MXN`

__Response 200 OK__

__Headers__ `Content-Type: application/json`

__Response Body__
```
{
  "10": {		# 10 is the charge ID
    "amount": 3.12,
    "approved": true,
    "customerId": 5,
    "partnerId": 2
  },
  "8": {		# 8 is the charge ID
    "amount": 0.01,
    "approved": false,
    "customerId": 4,
    "partnerId": 2
  }
}
```


__Set a new charge for a customer and get the new charge's ID__
New charge data is accepted as JSON and must contain the following fields:

>customerId: integer  # the ID of the customer to store the charge for

>partnerId: integer  # the ID of the partner whose customer the charge will be stored for

>amount: float  # the amount of this charge record

>approved: boolean  # whether this charge was declined or successfully approved


### __Example URI and request__

> POST v1/set-charges


`$ curl -X POST localhost:5000/v1/set-charges -d '{"customerId":2, "partnerId":2, "amount":2.31, "approved": true}' -H "Accept: application/json"`

__Response 201 CREATED__

__Headers__ `Content-Type: application/json`

__Response__
```
charge with id 12 was stored
```
