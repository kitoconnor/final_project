from flask import Flask, render_template, request
from googlefinance import getQuotes
app = Flask(__name__)


def get_stock_price(ticker):
	quotes = getQuotes(ticker)
	price = quotes[0]['LastTradePrice']
	return "The price of {} is {}".format(ticker,price)



@app.route('/')
def index(): #this needs to be right under the @app line
	name = request.values.get('name')
	greeting = "HELLO {} you amazaing person!".format(name)
	return render_template('index.html', greeting=greeting)

@app.route('/about')
def about(): #this needs to be right under the @app line
	return render_template('about.html')

@app.route('/results')
def results():
	stock = request.values.get('stock')
	price = get_stock_price(stock)
	return render_template('results.html',price=price)


app.run(debug=True)