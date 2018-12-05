export FLASK_APP=customer_charges.py
export FLASK_DEBUG=1

install:
	sudo virtualenv env  # create a virtual enviroment to contain your python depedencies
	. env/bin/activate  # activate the environment
	sudo pip install Flask  # install Flask
	sudo pip install cerberus
	pip install requests
	sudo pip install --ignore-installed six
	sudo pip install pytest

run:
	FLASK_APP=customer_charges.py
	flask run

test:
	python test_customer_charges.py
	git checkout customer_charges.json
