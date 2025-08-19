from flask import Flask, render_template
import yfinance as yf

# Create a Flask web server instance
app = Flask(__name__)

# Define the homepage route
@app.route("/")
def index():
    # Define the stock ticker you want to display
    ticker_symbol = "AAPL"
    try:
        # Fetch the current stock data from yfinance
        stock_data = yf.Ticker(ticker_symbol)
        current_price = stock_data.history(period="1d")["Close"].iloc[-1]
        
        # Format the price to two decimal places
        price_formatted = f"{current_price:.2f}"
    except IndexError:
        # Handle cases where data might not be available
        price_formatted = "Data not available"

    # Pass the ticker and price to the HTML template
    return render_template("index.html", ticker=ticker_symbol, price=price_formatted)

# This block ensures the app only runs when you execute the file directly
if __name__ == "__main__":
    app.run(debug=True)
