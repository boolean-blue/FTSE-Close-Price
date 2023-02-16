# Importing libraries
import yfinance as yf
from flask import Flask, render_template, request
from datetime import datetime, date

# Initialising name of variable for debugging
app = Flask(__name__)

# Decorator functions to create webpages
@app.route('/')  # Default page
def home():
	todayDate = date.today()
	return render_template('inputPage.html', todayDate=todayDate)

@app.route('/result', methods = ['POST'])  # Using POST as method to get the data after the user has inputted their dates
def result():
	startDate = request.form['date']  # The HTML takes care of any minimum and maximum values/bounds
	# Stopping stupid users from doing stupid things
	try:
		x = datetime.strptime(startDate, '%Y-%m-%d')
	except ValueError:
		return render_template('error.html', message='Invalid date format. Please input as YYYY-mm-dd')
	earliestDate = datetime.strptime('1984-01-03', '%Y-%m-%d')
	inputCheck = datetime.strptime(startDate, '%Y-%m-%d')
	if inputCheck < earliestDate:
		return render_template('error.html', message='Date must be later than 3rd January 1984 (1984-01-03)')
# Continuing with the code
	prices = yf.download('^FTSE', start=startDate)['Adj Close']  # Only want the adjusted close price; this will download until the most recent date
	startPrice = prices.iloc[0]
	endPrice = prices.iloc[-1]
	PnL = round(((endPrice/startPrice)-1) * 100, 2)
	return render_template('result.html', startPrice=round(startPrice, 2), PnL=PnL, startDate=startDate)

if __name__ == '__main__':
	app.run() # Only run if initialised name of app equals the running name

