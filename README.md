
# Customer Charges

__A small Flask app to get customer charges to partners__
Project goals are detailed in the [exercise description](exercise_description.md) in this repo.

### Development

__Run the following commands to install dependencies and to start the app.__
(A Makefile contains make commands that install dependies and spin up the application.)
```
$ make install
$ make run
```
Check that the application is running and healthy:
```
$ curl http://127.0.0.1:5000/health
all is wlll
```