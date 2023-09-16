from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import yfinance as yf
import time
import pandas as pd
# GLOBAL VARIBLES 
acc_username = "NJ_21_ZZ1125"
acc_password = "EXCZ4300" 
total_capital = 40000
stocks_to_monitor = ["CVNA"]

class InsufficientCapitalError(Exception):
    pass





def fetch_current_price(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        # Fetch the latest day's data
        today_data = stock.history(period="1d")
        # Return the Close price of the stock for the latest day
        return today_data['Close'][0]
    except Exception as e:
        print(f"An error occurred while fetching the current price for {ticker_symbol}: {str(e)}")
        return None
    


def fetch_data(ticker_symbol):
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)
    # Fetch historical data for 15-minute intervals
    hist_data = ticker.history(period="1d", interval="15m")
    return hist_data
    



def trade_stock(ticker, number_of_shares, action):
    """
    Trades a stock using the provided Selenium WebDriver based on the action.

    Parameters:
    - driver: The Selenium WebDriver instance.
    - ticker: The stock ticker symbol.
    - number_of_shares: The number of shares to trade.
    - action: The trade action ("buy", "sell", "short", "short-cover").
    """
    global total_capital, acc_username, acc_password

    current_price = fetch_current_price(ticker)

    # Set up the driver (assuming you're using Chrome; you can use others like Firefox too)
    driver = webdriver.Chrome()

    # Navigate to the website and login
    driver.get('https://www.stockmarketgame.org/login.html')
    account_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'ACCOUNTNO')))
    account_input.send_keys(acc_username)
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'USER_PIN')))
    password_input.send_keys(acc_password)
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Log In"][contains(@class, "button primary")]')))
    login_button.click()

    # Once logged in, navigate to the provided website
    driver.get('https://www.stockmarketgame.org/pa.html')
    driver.get('https://www.stockmarketgame.org/eat.html')
    stock_trade_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'aStockTrade')))
    stock_trade_button.click()



    if action == "buy":
        if current_price * number_of_shares > total_capital:
            raise InsufficientCapitalError("Not enough capital to buy the shares.")
        total_capital -= current_price * number_of_shares
        radio_button_id = 'rbBuy'
    elif action == "sell":
        total_capital += current_price * number_of_shares
        radio_button_id = 'rbSell'
    elif action == "short":
        radio_button_id = 'rbShortCell'
    elif action == "short-cover":
        radio_button_id = 'rbShortcover'
    else:
        raise ValueError(f"Invalid action: {action}")

    # Select the radio button based on action
    radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, radio_button_id))
    )
    radio_button.click()

    # Input the ticker symbol into the appropriate field
    ticker_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'SymbolName'))
    )
    ticker_input.send_keys(ticker)

    # Input the number of shares into the appropriate field
    shares_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'BuySellAmt'))
    )
    shares_input.send_keys(str(number_of_shares))

    # Click the "Preview Trade" button
    preview_trade_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'btnSend'))
    )
    preview_trade_button.click()

    # Input the account password into the specified input field
    trade_password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'TradePassword'))
    )
    trade_password_input.send_keys(acc_password)

    # Click the "Confirm Trade" button
    confirm_trade_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'btnConfirmTrade'))
    )
    confirm_trade_button.click()

    print(f"[{action.upper()}]: {ticker} {number_of_shares} shares")

# Example usage:
# driver = webdriver.Chrome()
# driver.get('YOUR_WEBSITE_URL_HERE')
# trade_stock("AAPL", 5, "buy")





def strategy_RSI_MACD(ticker):
    """
    Day Trading Strategy Using RSI and MACD.

    Parameters:
    - ticker: The stock ticker symbol.
    """

    global total_capital

    # Constants
    RISK_PERCENTAGE = 0.02
    REWARD_TO_RISK_RATIO = 2.0
    MIN_SHARES = 10
    MAX_SHARES = 500

    try:
        # Fetch the data for the given ticker
        data = fetch_data(ticker)

        for i in range(1, len(data)):
            # Buy Entry Conditions
            if (data['MACD'].iloc[i] > data['Signal'].iloc[i] and data['MACD'].iloc[i - 1] <= data['Signal'].iloc[i - 1]) and \
               (data['RSI'].iloc[i] > 30 and data['RSI'].iloc[i - 1] <= 30):
                # Calculate the amount to invest
                amount_to_invest = total_capital * RISK_PERCENTAGE
                if amount_to_invest > total_capital:
                    amount_to_invest = total_capital

                # Calculate the number of shares to buy
                num_shares = amount_to_invest // data['Close'].iloc[i]
                num_shares = max(MIN_SHARES, min(num_shares, MAX_SHARES))

                # Check if there's enough capital to buy the shares
                if num_shares * data['Close'].iloc[i] <= total_capital:
                    # Execute the buy trade
                    trade_stock(ticker, num_shares, "buy")
                    total_capital -= num_shares * data['Close'].iloc[i]

            # Sell Entry Conditions
            elif (data['MACD'].iloc[i] < data['Signal'].iloc[i] and data['MACD'].iloc[i - 1] >= data['Signal'].iloc[i - 1]) and \
                 (data['RSI'].iloc[i] < 70 and data['RSI'].iloc[i - 1] >= 70):
                # Calculate the number of shares to sell
                num_shares = max(MIN_SHARES, min(num_shares, MAX_SHARES))

                # Execute the sell trade
                trade_stock(ticker, num_shares, "sell")
                total_capital += num_shares * data['Close'].iloc[i]

            # Exit Conditions for Buy Trades
            if (data['MACD'].iloc[i] < data['Signal'].iloc[i] or data['RSI'].iloc[i] > 70):
                # Calculate the number of shares to sell
                num_shares = max(MIN_SHARES, min(num_shares, MAX_SHARES))

                # Execute the sell trade
                trade_stock(ticker, num_shares, "sell")
                total_capital += num_shares * data['Close'].iloc[i]

            # Exit Conditions for Sell Trades
            if (data['MACD'].iloc[i] > data['Signal'].iloc[i] or data['RSI'].iloc[i] < 30):
                # Calculate the amount to invest
                amount_to_invest = total_capital * RISK_PERCENTAGE
                if amount_to_invest > total_capital:
                    amount_to_invest = total_capital

                # Calculate the number of shares to buy
                num_shares = amount_to_invest // data['Close'].iloc[i]
                num_shares = max(MIN_SHARES, min(num_shares, MAX_SHARES))

                # Check if there's enough capital to buy the shares
                if num_shares * data['Close'].iloc[i] <= total_capital:
                    # Execute the buy trade
                    trade_stock(ticker, num_shares, "buy")
                    total_capital -= num_shares * data['Close'].iloc[i]

    except Exception as e:
        print(f"An error occurred while executing the strategy for {ticker}: {str(e)}")



def start_trading():
    """
    Monitors the stocks in the stocks_to_monitor list and executes the RSI_MACD strategy for each stock.
    Cycles every minute.
    """
    global stocks_to_monitor

    try:
        while True:
            for ticker in stocks_to_monitor:
                print(f"Executing:  {ticker}...")
                strategy_RSI_MACD(ticker)
                print(f"Complete: {ticker} ")
            
            # Wait for 1 minute (60 seconds) before the next cycle
            time.sleep(30)

    except KeyboardInterrupt:
        print("Trading stopped by user.")
    except Exception as e:
        print(f"An error occurred while trading stocks: {str(e)}")







# ----------------------- To start trading, call the function -----------------------
start_trading()



