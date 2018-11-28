

install:
	virtualenv env  # create a virtual enviroment to contain your python depedencies
	. env/bin/activate  # activate the environment
	pip install Flask  # install Flask

run:
	export FLASK_APP=customer_charges.py
	flask run
