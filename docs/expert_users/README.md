# Water Carrier Setup Documentation
This document provides step-by-step instructions for setting up the Water Carrier web app.

### Set Up Your Environment:

* Make sure you have Python installed on your system. You can download it from python.org.
* Setup virtual environment `python3 -m venv venv`
* Install Flask in virtual environment `pip install flask`
* Clone the WaterCarrier repository from Github.

### Run Your Flask Application:

* Open virtual environment `source venv/bin/activate`
* Navigate to the dev directory of WaterCarrier in your terminal.
* Install project dependencies `pip install -r requirements.txt`
* Initialize the database `python3 application/init_db.py`
* Run `flask run`
* Navigate to `http://127.0.0.1:5000` to view the progress of Water Carrier.
