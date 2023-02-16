# FTSE Closing Price Web App
## Overview
This is a Flask app that allows users to input a date in the format yyyy-mm-dd, and returns the closing price of the FTSE 100 index for that day. It also calculates the total PnL for the most recent close price. If the user enters an invalid date, the app redirects them to an error page with instructions on how to input a valid date.

## Requirements
Python 3.6 or later
Flask 2.1.0 or later
yfinance 0.1.62 or later

## Installation
Clone the repository from Github.
Create a virtual environment for the project: python -m venv venv.
Activate the virtual environment: source venv/bin/activate.
Install the required packages: pip install -r requirements.txt.
Run the app: flask run.

## Usage
Open your web browser and go to http://localhost:5000.
Enter a date in the format yyyy-mm-dd and submit the form.
The app will redirect you to a page displaying the closing price of the FTSE 100 index on that day, as well as the total PnL for the most recent close price.
If you entered an invalid date, the app will redirect you to an error page with instructions on how to input a valid date.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Credits
This project was created by Daniel Oakey. I would like to dedicate my first available code to Wesley.
