from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yfinance as yf
import time
import pandas as pd




# GLOBAL VARIBLES 
acc_username = "NJ_21_ZZ1125"
acc_password = "EXCZ4300" 
total_capital = 100000


def buy_stock(driver, ticker, number_of_shares):
    """
    Buys a stock using the provided Selenium WebDriver.

    Parameters:
    - driver: The Selenium WebDriver instance.
    - ticker: The stock ticker symbol.
    - number_of_shares: The number of shares to buy.
    """
    
    # Select the "buy" radio button
    buy_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'rbBuy'))
    )
    buy_radio_button.click()

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

    print(f"[BUY]: {ticker} {number_of_shares}")

# Example usage:
# driver = webdriver.Chrome()
# driver.get('YOUR_WEBSITE_URL_HERE')
# buy_stock(driver, "AAPL", 5)

def sell_stock(driver, ticker, number_of_shares):
    """
    Buys a stock using the provided Selenium WebDriver.

    Parameters:
    - driver: The Selenium WebDriver instance.
    - ticker: The stock ticker symbol.
    - number_of_shares: The number of shares to buy.
    """
    
    # Select the "sell" radio button
    sell_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'rbSell'))
    )
    sell_radio_button.click()

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
    print(f"[SELL]: {ticker} {number_of_shares}")

# Example usage:
# driver = webdriver.Chrome()
# driver.get('YOUR_WEBSITE_URL_HERE')
# buy_stock(driver, "AAPL", 5)


def short_stock(driver, ticker, number_of_shares):
    """
    Buys a stock using the provided Selenium WebDriver.

    Parameters:
    - driver: The Selenium WebDriver instance.
    - ticker: The stock ticker symbol.
    - number_of_shares: The number of shares to buy.
    """
    
    # Select the "short" radio button
    short_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'rbShortCell'))
    )
    short_radio_button.click()

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

    print(f"[SHORT]: {ticker} {number_of_shares}")

# Example usage:
# driver = webdriver.Chrome()
# driver.get('YOUR_WEBSITE_URL_HERE')
# buy_stock(driver, "AAPL", 5)

def shortcover_stock(driver, ticker, number_of_shares):
    """
    Buys a stock using the provided Selenium WebDriver.

    Parameters:
    - driver: The Selenium WebDriver instance.
    - ticker: The stock ticker symbol.
    - number_of_shares: The number of shares to buy.
    """
    
    # Select the "shortcover" radio button
    shortcover_radio_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'rbShortcover'))
    )
    shortcover_radio_button.click()

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

    print(f"[SHORT-COVER]: {ticker} {number_of_shares}")

# Example usage:
# driver = webdriver.Chrome()
# driver.get('YOUR_WEBSITE_URL_HERE')
# buy_stock(driver, "AAPL", 5)

def trade_stocks(action, ticker, number_of_shares):
    """
    Automates stock trading actions using Selenium WebDriver.

    Parameters:
    - action: The trading action to perform. Can be 'buy', 'sell', 'short', or 'shortcover'.
    - ticker: The stock ticker symbol.
    - number_of_shares: The number of shares to trade.
    - acc_username: Account username for login.
    - acc_password: Account password for login.
    """

    
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

    # Trading actions
    if action == "buy":
        buy_stock(driver, ticker, number_of_shares)
    elif action == "sell":
        sell_stock(driver, ticker, number_of_shares)
    elif action == "short":
        short_stock(driver, ticker, number_of_shares)
    elif action == "shortcover":
        shortcover_stock(driver, ticker, number_of_shares)
    else:
        print("Invalid action provided!")

    # Close the driver after completing the action
    driver.close()


    # Example usage:
    # trade_stocks('buy', 'AAPL', 5, 'your_username', 'your_password')



# -------------------------------------------   TRADING STRATEGY   ---------------------------------------------

# List of stocks to monitor
stocks_to_monitor = ["META", "AAPL", "AMZN", "CVNA", "PTON", "TSLA", "UPST", "BROS", "C", "DIS"]

def fetch_data(ticker_symbol):
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)
    # Fetch historical data for 15-minute intervals
    hist_data = ticker.history(period="1d", interval="15m")
    return hist_data

def calculate_shares_to_buy(entry_price, stop_loss_price, total_capital, risk_percentage=0.01):
    risk_per_trade = total_capital * risk_percentage
    risk_per_share = abs(entry_price - stop_loss_price)
    
    # Calculate the number of shares
    num_shares = int(risk_per_trade / risk_per_share)
    
    # Ensure you don't spend more than your capital
    total_cost = num_shares * entry_price
    if total_cost > total_capital:
        num_shares = int(total_capital / entry_price)
    
    return num_shares

def trade_strategy(ticker_symbol):
    data = fetch_data(ticker_symbol)
    
    # Calculate MACD and Signal line
    data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    # Calculate RSI
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # Buy and Sell signals
    buy_signals = []
    sell_signals = []
    
    for i in range(1, len(data)):
        # Buy Entry
        if data['MACD'].iloc[i] > data['Signal_Line'].iloc[i] and data['RSI'].iloc[i] > 30:
            buy_signals.append(data['Close'].iloc[i])
            sell_signals.append(float('nan'))
        # Sell Entry
        elif data['MACD'].iloc[i] < data['Signal_Line'].iloc[i] and data['RSI'].iloc[i] < 70:
            sell_signals.append(data['Close'].iloc[i])
            buy_signals.append(float('nan'))
        else:
            buy_signals.append(float('nan'))
            sell_signals.append(float('nan'))
    
    data['Buy_Signal'] = buy_signals
    data['Sell_Signal'] = sell_signals
    
     # Execute trades based on signals
    for i in range(1, len(data)):
        if not pd.isna(data['Buy_Signal'].iloc[i]):
            # Calculate the number of shares to buy
            shares_to_buy = calculate_shares_to_buy(data['Close'].iloc[i], data['Close'].iloc[i-1], total_capital)
            trade_stocks('buy', ticker_symbol, shares_to_buy)
        elif not pd.isna(data['Sell_Signal'].iloc[i]):
            # Calculate the number of shares to sell
            shares_to_sell = calculate_shares_to_buy(data['Close'].iloc[i], data['Close'].iloc[i-1], total_capital)
            trade_stocks('sell', ticker_symbol, shares_to_sell)




# --------------------------  Execute Code  -------------------------------



# Monitor the stocks
while True:
    for stock in stocks_to_monitor:
        trade_strategy(stock)
    time.sleep(300) 








































# Day Trading Strategy Using RSI and MACD:
# Setup:

# Chart Timeframe: 15-minute or 30-minute charts are recommended for day trading.
# RSI Settings: Standard settings (14 periods with overbought level at 70 and oversold level at 30).
# MACD Settings: Standard settings (12, 26, 9) - which represent the fast EMA, slow EMA, and the signal line respectively.
# Entry Rules:

# Buy Entry:

# MACD: Wait for the MACD line to cross above the signal line, indicating bullish momentum.
# RSI: Look for the RSI to move above 30, moving out of the oversold territory. This suggests that the recent downward momentum is slowing down, and a potential upward move could be coming.
# Combined Signal: A buy signal is generated when the MACD line crosses above the signal line, and the RSI moves above 30 almost simultaneously or within a few bars of each other.
# Sell/Short Entry:

# MACD: Wait for the MACD line to cross below the signal line, indicating bearish momentum.
# RSI: Look for the RSI to move below 70, moving out of the overbought territory. This suggests that the recent upward momentum is slowing down, and a potential downward move could be coming.
# Combined Signal: A sell/short signal is generated when the MACD line crosses below the signal line, and the RSI moves below 70 almost simultaneously or within a few bars of each other.
# Exit Rules:

# Buy Trades: Exit the trade when the MACD line crosses below the signal line or when the RSI moves into the overbought territory (above 70), indicating potential overextension.
# Sell/Short Trades: Exit the trade when the MACD line crosses above the signal line or when the RSI moves into the oversold territory (below 30), suggesting potential overextension.
# Stop-Loss:

# For buy trades, set a stop-loss below the recent swing low.
# For sell/short trades, set a stop-loss above the recent swing high.
# Risk Management:

# Never risk more than 1-2% of your trading capital on a single trade.
# Ensure that your potential reward is at least twice the amount you're risking (2:1 reward-to-risk ratio).
# Final Thoughts:
# This strategy combines the momentum detection capabilities of both the RSI and MACD. While the MACD identifies the general momentum direction, the RSI helps to pinpoint overbought or oversold conditions, providing a more refined entry or exit point.

# However, like all trading strategies, this combination is not foolproof. It's essential to backtest the strategy on historical data and practice in a demo environment before going live. Additionally, always be aware of major news events or market conditions that might affect the asset you're trading, as these can influence the effectiveness of technical indicators.



# TRADE THIS ________________________
# Meta Platforms Inc. (META) - Source
# Apple Inc. (AAPL) - Source
# Amazon.com Inc. (AMZN) - Source
# Carvana Co. (CVNA) - Source
# Peloton Interactive (PTON) - Source
# Tesla Inc. (TSLA) - Source
# Upstart Holdings Inc (UPST) - Source
# Dutch Bros Inc. (BROS) - Source
# Citigroup Inc. (C) - Source
# Walt Disney Co. (DIS) - Source











# --------------------------  Execute Code Test -------------------------------

# trade_stocks('buy', 'AAPL', 15)