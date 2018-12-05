export FLASK_APP=customer_charges.py
export FLASK_DEBUG=1

install:
	virtualenv env  # create a virtual enviroment to contain your python depedencies
	. env/bin/activate  # activate the environment
	pip install Flask  # install Flask
	pip install requests

run:
	FLASK_APP=customer_charges.py
	flask run
